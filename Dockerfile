FROM python:2.7-onbuild

RUN echo "Europe/London" > /etc/timezone  &&  dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update && \
    apt-get install -y software-properties-common python-software-properties

RUN apt-get update && \
    apt-get install -y \
        build-essential git python python-dev python-setuptools python-pip \
        sudo supervisor curl libpq-dev ntp ruby ruby-dev gdal-bin

RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get install -y nodejs

RUN pip install -r requirements.txt

WORKDIR /app

ADD . /app

RUN gem update rdoc
RUN gem install compass
RUN npm install -g bower
RUN npm install -g gulp

ADD ./conf/uwsgi /etc/uwsgi

ADD ./conf/supervisor /etc/supervisor

RUN bower install --allow-root

RUN npm install 

RUN gulp build:prod

EXPOSE 8000
CMD ["/usr/bin/supervisord"]

CMD ["supervisord", "-n"]
