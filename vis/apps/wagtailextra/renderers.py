from django_medusa.renderers import StaticSiteRenderer
from wagtail.wagtailcore.models import Site


class PageRenderer(StaticSiteRenderer):
    def get_paths(self):
        # Get site
        # TODO: Find way to get this to work with other sites
        site = Site.objects.filter(is_default_site=True).first()
        if site is None:
            return []

        # Return list of paths
        return site.root_page.get_static_site_paths()


renderers = [PageRenderer]
