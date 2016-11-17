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

RUN gem update rdoc
RUN gem install compass
RUN npm install -g bower
RUN npm install -g gulp

COPY ./conf/uwsgi/*.ini /app


ADD ./conf/supervisor /etc/supervisor
ADD ./requirements  /app/requirements
ADD ./requirements.txt /app/requirements.txt

RUN gem update rdoc compass
RUN npm install -g bower gulp
RUN bower install --allow-root
RUN npm install
RUN gulp build:prod

EXPOSE 8000
RUN chmod +x ./run.sh
ENTRYPOINT ["./run.sh"]
