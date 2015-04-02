Victims' Information Service
----------------------------

## Dependencies

- [Virtualenv](http://www.virtualenv.org/en/latest/)
- [Python 2.7](http://www.python.org/) (Can be installed using `brew`)
- [Postgres 9.3+](http://www.postgresql.org/)
- [nodejs.org](http://nodejs.org/)
- [Sass](http://sass-lang.com/) (Ruby version - minimum v3.4)
- [gulp.js](http://gulpjs.com/) (Installed globally using `npm install -g gulp`)
- [Bower](http://bower.io/) (Installed globally using `npm install -g bower`)

## Installation

**The project can also be run with Docker for local development - see _Docker Installation_**

Clone the repository:
```
git clone git@github.com:ministryofjustice/vis.git
```

Next, create the environment and start it up:
```
cd vis
virtualenv env --prompt=\(vis\)

source env/bin/activate
```

Update pip to the latest version:
```
pip install -U pip
```

If you want to install GDAL run:
```
brew install gdal
```

However, it might take a long time to install and it's optional.

In case you want to skip that, just open requirements/dev.txt and comment out `GDAL==1.11.2`

Install python dependencies:
```
pip install -r requirements/dev.txt
```

Create the database inside postgres. Type `psql` to enter postgres, then enter:
```
CREATE DATABASE vis WITH ENCODING 'UTF-8';
\c vis
createuser postgres
```

Sync and migrate the database:
```
./manage.py migrate
```

Create superuser
```
./manage.py createsuperuser --username=admin
```

Load test fixtures
```
./manage.py loaddata glossary helplines police test_pages vis/fixtures/test_users.json
```

Fix PCC Page Permissions such that each PPC Page is owned by the corresponding user:
```
./manage.py fixpccpermissions
```

Install Frontend dependencies libraries:
```
npm install -g bower gulp
```

Install frontend packages:
```
npm install && bower install
```

Compile assets:

```
gulp build:dev  # gulp build:prod in production
```

In the main tab, start the runserver:
```
./manage.py runserver 8000
```

## Frontend Development

Frontend assets are located in the `vis/assets-src/` folder and are compiled using [gulp](http://gulpjs.com/).

Gulp tasks are split into individual task files in `tasks/`.

To watch assets and rebuild them after every change use this command:

```
gulp watch
```

It will automatically run `gulp build:dev` and then create a [browsersync](http://www.browsersync.io/) server which will run at [http://localhost:3000](http://localhost:3000). By default it will proxy the django app from [http://localhost:8000](http://localhost:8000). To change the port add a `port` argument to the `watch` command, eg:
```
gulp watch --port=8001
```

### Police area maps

The maps used on the police pages are generated using [Mapbox](https://www.mapbox.com/). The images are currently kept in `vis/assets-src/images/pcc-maps/`. 

#### Generate maps

Make sure you have [GDAL](http://www.gdal.org/) installed (if brew: `brew install gdal`).

Download the latest police area KML data from the [police data downloads site](http://data.police.uk/data/kmls/).

Run the following command, replacing the items in brackets:

```
./manage.py generate_pcc_maps <mapbox_api_key> <mapbox_map_id> <png_width> <png_height> <kml_input_directory> <png_output_directory> --stroke-width=1.5 --stroke-color="#0E1010" --fill-color="#BCDBDC"
```

### Url2png

The code uses [url2png](https://www.url2png.com/) to take screenshots of `pages.PCCPage.service_website_url`s.

Check `settings.base.py` for settings.


### Scheduling commands

There are two jobs that should/could be run in production.

1. `./manage.py publish_scheduled_pages` (every 10 mins). It uppdates the db when a page is published/unpublished

2. `./manage.py generatestatic` which is optional. It downloads the whole website, zips it and sends it to the email addresses specified in the env variable `EXPORT_RECIPIENTS`.


### Zendesk

Zendesk integration for content feedback is supported.

Check `settings.base.py` for settings.


## Docker Installation

### Install

* Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* Install [boot2docker](http://boot2docker.io)
* Install [Fig](http://www.fig.sh)

### Setup

Create boot2docker VM:

```
$ boot2docker init
```

Start VM:

```
$ boot2docker start
```

Set up environment variables:

```
$ $(boot2docker shellinit)
```

Build the Docker images with Fig:

```
$ fig build
```

If you get the error: 

```
SSL error: hostname '192.168.59.103' doesn't match 'boot2docker'
```

Then add `192.168.59.103 boot2docker` to `/etc/hosts` and run `export DOCKER_HOST=tcp://boot2docker:2376` (and add it to your .bashrc file).

### Start

Bower frontend components and Django fixtures require setup on the **first run only**:

```
$ fig run django bower install --allow-root
$ fig run django python manage.py loaddata vis/fixtures/test_users glossary helplines police test_pages vis/fixtures/test_users
```

Start it up:

```
$ fig up
```

The site should now be viewable in your browser at [http://192.168.59.103:8000/](http://192.168.59.103:8000/) (or [http://boot2docker:8000/](http://boot2docker:8000/) if you've added an `/etc/hosts` entry).

### Deploy to Heroku
Just press the button:
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
