from fabric.api import task, cd, sudo


@task
def update_maintenance_page(url):
    with cd('/usr/share/nginx/html'):
        sudo('rm -rf ./*')
        sudo('wget -EHkpnd --user-agent="" -e robots=off %s' % url)
