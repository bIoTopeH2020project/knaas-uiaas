FROM frolvlad/alpine-oraclejdk8:slim

# replace this with the latest oorcs jar
ADD oorcs-0.0.1-SNAPSHOT.jar oorcs.jar

ADD run.sh run.sh

RUN sh -c 'touch /oorcs.jar'
RUN sh -c 'chmod +x /run.sh'

ENTRYPOINT ["/run.sh"]
