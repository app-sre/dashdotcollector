FROM        centos:8

WORKDIR     /dashdotcollector

COPY        . ./
COPY        oc /usr/bin

RUN         dnf -y install python36
RUN         pip3 install .

WORKDIR     /tmp
ENTRYPOINT  ["celery", "--app=dashdotcollector", "--loglevel=info"]
