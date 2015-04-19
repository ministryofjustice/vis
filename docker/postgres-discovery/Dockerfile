FROM ubuntu:trusty

RUN echo "Europe/London" > /etc/timezone  &&  dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update
RUN apt-get install -y curl postgresql-client

# install etcdctl
RUN curl -L https://github.com/coreos/etcd/releases/download/v2.0.9/etcd-v2.0.9-linux-amd64.tar.gz \
    -o etcd-v2.0.9-linux-amd64.tar.gz
RUN tar xzf etcd-v2.0.9-linux-amd64.tar.gz
RUN mv etcd-v2.0.9-linux-amd64/etcdctl /usr/local/bin/etcdctl
RUN rm -rf etcd-v2.0.9-linux-amd64

ADD monitor.sh /monitor.sh
RUN chmod +x /monitor.sh

CMD ["/bin/bash", "-c", "/monitor.sh"]
