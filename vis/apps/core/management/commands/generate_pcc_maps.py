import os
import glob
import json
import urllib
import shutil
from collections import defaultdict
from decimal import Decimal

from django_docopt_command import DocOptCommand
import requests
from .lib import ogr2ogr, minify_json


# set default geometry simplification value, and individual simplification
# values for particularly complex geometries
simplifications = defaultdict(lambda: "0.01")
simplifications['cumbria'] = "0.04"
simplifications['devon-and-cornwall'] = "0.015"
simplifications['dyfed-powys'] = "0.015"
simplifications['north-wales'] = "0.015"
simplifications['north-yorkshire'] = "0.015"
simplifications['west-mercia'] = "0.015"


MAPBOX_URL = ("http://api.tiles.mapbox.com/v4/{map_id}/geojson({geojson})/"
              "{lon},{lat},6/{png_width}x{png_height}{format}"
              "?access_token={api_key}")


def simplify_coords(coords):
    """
    Reduce coord decimal places to 4 and remove z/elevation value.
    """
    return map(lambda x: float(Decimal("%.4f" % x)), coords[:2])


class Command(DocOptCommand):
    docs = """
    Usage:
        generate_pcc_maps <mapbox_api_key> <mapbox_map_id> <png_width> <png_height> <kml_input_directory> <png_output_directory> [--stroke-width=<width>] [--stroke-color=<color>] [--stroke-opacity=<opacity>] [--fill-color=<color>] [--fill-opacity=<opacity>]

    Options:
        -h --help                   Show this screen.
        --stroke-width=<width>      float [default: 1.0]
        --stroke-color=<color>      hex [default: #000]
        --stroke-opacity=<opacity>  float [default: 1.0]
        --fill-color=<color>        hex [default: #fff]
        --fill-opacity=<opacity>    float [default: 1.0]
    """

    def handle_docopt(self, args):
        print args
        input_dir = args['<kml_input_directory>']
        output_dir = args['<png_output_directory>']

        for f in glob.glob("%s/%s" % (input_dir, "*.kml")):
            basename = f.split('/')[-1].replace('.kml', '')
            geojson_path = os.path.join(output_dir, "%s.geojson" % basename)

            # print basename, simplifications[basename]

            ogr2ogr.main([
                "",
                "-f", "GeoJSON",
                "-simplify", simplifications[basename],
                geojson_path,
                f,
            ])

            with open(geojson_path, 'r') as gj:
                geojson = json.loads(gj.read())['features'][0]
            os.remove(geojson_path)

            # convert MultiPolys to Polys (ie. remove islands), by including
            # only the geometry with the most points
            if geojson['geometry']['type'] == 'MultiPolygon':
                geojson['geometry']['type'] = 'Polygon'
                polys = sorted(geojson['geometry']['coordinates'][0])
                geojson['geometry']['coordinates'] = [polys[-1]]

            # simplify all coords
            geojson['geometry']['coordinates'][0] = map(
                simplify_coords,
                geojson['geometry']['coordinates'][0]
            )

            geojson['properties'] = {
                "stroke-width": float(args['--stroke-width']),
                "stroke": args['--stroke-color'],
                "stroke-opacity": float(args['--stroke-opacity']),
                "fill": args['--fill-color'],
                "fill-opacity": float(args['--fill-opacity'])
            }

            lon = geojson['geometry']['coordinates'][0][0][0]
            lat = geojson['geometry']['coordinates'][0][0][1]

            # minify geoJSON as mapbox URLs can be 4096 chars max
            url_geojson = minify_json.json_minify(json.dumps(geojson))

            for fmt in ('.png', '@2x.png'):
                png_url = MAPBOX_URL.format(**{
                    "map_id": args['<mapbox_map_id>'],
                    "geojson": urllib.quote(url_geojson),
                    "png_width": args['<png_width>'],
                    "png_height": args['<png_height>'],
                    "api_key": args['<mapbox_api_key>'],
                    "lon": lon,
                    "lat": lat,
                    "format": fmt
                })

                png_path = os.path.join(output_dir, "%s%s" % (basename, fmt))
                print "Saving %s..." % png_path

                response = requests.get(png_url, stream=True)
                with open(png_path, 'wb') as out:
                    shutil.copyfileobj(response.raw, out)
