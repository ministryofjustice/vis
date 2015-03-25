from fabric.api import task, cd, sudo


@task
def update_maintenance_page(url):
    """
    Update maintenance server with page from production site

    Path to SSH identify file and host params will also be required:

    fab update_maintenance_page:http://host/foo/ -i key.pem -H user@host
    """
    with cd('/usr/share/nginx/html'):
        sudo('rm -rf ./*')
        sudo('wget -EHkpnd --user-agent="" -e robots=off %s' % url)
        sudo("echo 'User-agent: *\nDisallow: /' > robots.txt")
