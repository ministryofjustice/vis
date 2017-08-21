FROM python:2.7

RUN echo "Europe/London" > /etc/timezone  &&  dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update && \
    apt-get install -y software-properties-common python-software-properties \
        build-essential git python python-dev python-setuptools python-pip \
        sudo curl libpq-dev ntp ruby ruby-dev gdal-bin uwsgi-core uwsgi-plugin-python && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && apt-get install nodejs

RUN mkdir -p /app
WORKDIR /app

COPY ./requirements.txt ./requirements.txt
COPY ./requirements ./requirements/
RUN pip install -r requirements.txt

# fix docker aufs / npm install issue "Error: EXDEV: cross-device link not permitted"
RUN cd $(npm root -g)/npm && npm install fs-extra && sed -i -e s/graceful-fs/fs-extra/ -e s/fs\.rename/fs.move/ ./lib/utils/rename.js

COPY ./package.json ./package.json
COPY ./Gemfile ./Gemfile
COPY ./Gemfile.lock ./Gemfile.lock
RUN npm install \
  && gem install bundler && bundle install

COPY . .
RUN mkdir -p ./vis/assets && mkdir -p ./assets
RUN node_modules/.bin/bower install --allow-root \
  && node_modules/.bin/gulp build:prod \
  && ./manage.py collectstatic --noinput

CMD ["./run.sh"]

