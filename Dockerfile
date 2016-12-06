FROM python:2.7

RUN echo "Europe/London" > /etc/timezone  &&  dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update && \
    apt-get install -y software-properties-common python-software-properties \
        build-essential git python python-dev python-setuptools python-pip \
        sudo curl libpq-dev ntp ruby ruby-dev gdal-bin uwsgi-core uwsgi-plugin-python && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && apt-get install nodejs

WORKDIR /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

RUN rm -rf /app/node_modules

# fix docker aufs / npm install issue "Error: EXDEV: cross-device link not permitted"
RUN cd $(npm root -g)/npm  && npm install fs-extra && sed -i -e s/graceful-fs/fs-extra/ -e s/fs\.rename/fs.move/ ./lib/utils/rename.js

RUN npm update -g && npm install -g bower gulp && npm install
RUN gem install bundler
RUN bower install --allow-root && bundle install

RUN gulp build:prod

RUN chmod +x ./run.sh
CMD ["./run.sh"]

# Enforce "OK" exit code even if following command fails
#RUN sass --force --update vis/assets-src:vis/assets || :
