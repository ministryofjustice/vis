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
./manage.py loaddata glossary helplines police test_pages
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
gulp build
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

It will automatically run `gulp build` and then create a [browsersync](http://www.browsersync.io/) server which will run at [http://localhost:3000](http://localhost:3000). By default it will proxy the django app from [http://localhost:8000](http://localhost:8000). To change the port add a `port` argument to the `watch` command, eg:
```
gulp watch --port=8001
```

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
$ fig run django python manage.py loaddata vis/fixtures/test_users glossary helplines police vis/fixtures/test_pages
```

Start it up:

```
$ fig up
```

The site should now be viewable in your browser at [http://192.168.59.103:8000/](http://192.168.59.103:8000/) (or [http://boot2docker:8000/](http://boot2docker:8000/) if you've added an `/etc/hosts` entry).

### Deploy to Heroku
Just press the button:
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
