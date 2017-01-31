FROM reutersmedia/semafor-base:latest

VOLUME /var/log/docker

RUN apk --update add supervisor curl python3 uwsgi uwsgi-python3 jq bash nginx && \
    python3 -m ensurepip && \
    pip3 install python-logstash flask nltk && \
    python3 -m nltk.downloader -d /usr/share/nltk_data punkt
    

COPY conf /tmp/conf
COPY src /tmp/src
COPY config.sh /semafor-master/bin/config.sh
COPY proc-text.sh /proc-text.sh

ENV ENVIRONMENT=dev \
    APPLICATION=semaforsvr \
    NUM_PYTHON_PROCESSES=1 \
    NUM_UWSGI_THREADS=1 \
    LOG_LEVEL=INFO \
    FRAMEPARSER_HOST=localhost \
    FRAMEPARSER_PORT=8085

RUN mkdir /run/nginx && \
    cd /tmp/src && \
    python3 setup.py install --root / && \
    cp /tmp/conf/uwsgi.ini /root/uwsgi.ini && \
    cp /tmp/conf/supervisord.conf /etc/supervisord.conf && \
    cp /tmp/conf/run.sh /root/run.sh && \
    cp /tmp/conf/nginx.conf /etc/nginx/nginx.conf && \
    cp /tmp/conf/uwsgi_params /root/uwsgi_params && \
    rm -rf /tmp/conf && \
    rm -rf /tmp/src 

EXPOSE 80

CMD ["/root/run.sh"]

