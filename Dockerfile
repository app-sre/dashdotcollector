FROM        centos:7

WORKDIR     /dashdotcollector

COPY        . ./

RUN         yum install -y epel-release
RUN         yum install -y centos-release-openshift-origin
RUN         yum install -y python36 origin-clients
RUN         pip3 install .

WORKDIR     /tmp
ENTRYPOINT  ["celery", "--app=dashdotcollector", "--loglevel=info"]
