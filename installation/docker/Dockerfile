FROM debian:buster-slim

RUN /usr/bin/apt-get update -q && \
    /usr/bin/apt-get install -qqy python3-pip gunicorn3 libmariadbclient-dev && \
    /usr/bin/apt-get clean && \
    /bin/rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY /requirements.txt /opt/ps/
COPY /patchserver /opt/ps/patchserver
COPY /installation/docker/wsgi.py /opt/ps/
COPY /installation/docker/config.py /opt/ps/

RUN pip3 install -r /opt/ps/requirements.txt && \
    pip3 install futures

ENV DATABASE_DIR=/var/lib/patchserver

WORKDIR /opt/ps

EXPOSE 5000

CMD ["/usr/bin/gunicorn3", "--config", "/opt/ps/config.py", "wsgi", "--preload"]
