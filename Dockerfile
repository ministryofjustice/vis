FROM ubuntu:trusty

RUN echo "Europe/London" > /etc/timezone  &&  dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update && \
    apt-get install -y software-properties-common python-software-properties

RUN add-apt-repository -y ppa:nginx/stable
RUN add-apt-repository -y ppa:chris-lea/node.js 

RUN apt-get update && \
    apt-get install -y \
        build-essential git python python-dev python-setuptools python-pip \
        curl nginx libpq-dev ntp ruby ruby-dev nodejs
RUN service nginx stop && rm /etc/init.d/nginx

# fix for broken pip package in ubuntu 14
RUN easy_install -U pip

# install confd
RUN curl -L -o /usr/local/bin/confd \
    https://github.com/kelseyhightower/confd/releases/download/v0.9.0/confd-0.9.0-linux-amd64
RUN chmod +x /usr/local/bin/confd

WORKDIR /app

RUN gem update rdoc
RUN gem install compass
RUN npm install -g bower

ADD ./conf/uwsgi /etc/uwsgi

ADD ./conf/nginx/nginx.conf /etc/nginx/nginx.conf
ADD ./conf/nginx/sites-enabled /etc/nginx/sites-enabled
ADD ./conf/supervisor /etc/supervisor
ADD ./conf/confd /etc/confd

ADD ./requirements  /app/requirements
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install uWSGI==2.0.10
RUN pip install supervisor==3.1.3

RUN mkdir -p /var/log/supervisor /var/log/wsgi

ADD . /app
RUN bower install --allow-root

EXPOSE 80
EXPOSE 443
CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
# supervisord -n -c /etc/supervisor/supervisord.conf
#CMD ["/bin/bash"]
