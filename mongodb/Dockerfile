FROM fedora
#MAINTAINER scollier

RUN yum -y update
RUN yum -y install mongodb-server
RUN mkdir -p /data/db
RUN sed -i 's/dbpath =\/var\/lib\/mongodb/dbpath =\/data\/db/' /etc/mongodb.conf

VOLUME ["/data/db"]

EXPOSE 27017
ENTRYPOINT ["/usr/bin/mongod"]
