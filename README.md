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
pip install -r requirements/local.txt
```

Create the database inside postgres. Type `psql` to enter postgres, then enter:
```
CREATE DATABASE vis WITH ENCODING 'UTF-8';
\c vis
createuser postgres
create extension pgcrypto;
```

Sync and migrate the database:
```
./manage.py migrate
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
