FROM python:2.7-onbuild

RUN echo "Europe/London" > /etc/timezone  &&  dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update && \
    apt-get install -y software-properties-common python-software-properties \
        build-essential git python python-dev python-setuptools python-pip \
        sudo curl libpq-dev ntp ruby ruby-dev gdal-bin uwsgi-core uwsgi-plugin-python

RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get install -y nodejs && pip install --upgrade -r requirements.txt

WORKDIR /app

COPY . /app

# I'm not certainly sure if following gems ( except of bundler are required )
RUN gem install rdoc compass bundler
RUN npm install -g bower gulp
RUN bower install --allow-root
RUN npm install && bundle install
RUN gulp build:prod
RUN sass --update vis/assets-src:vis/assets

RUN chmod +x ./run.sh
ENTRYPOINT ["./run.sh"]
