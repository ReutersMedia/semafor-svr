#!/bin/sh

# make sure only numbers
N_PROC=$(echo $NUM_PYTHON_PROCESSES | sed 's/[^0-9]//g')
sed -i -e "s/__NUM_PYTHON_PROCESSES__/$N_PROC/g" /root/uwsgi.ini 


LOG_PATH=/var/log/docker/$HOSTNAME/$ENVIRONMENT/$APPLICATION
mkdir -p $LOG_PATH/python
mkdir -p $LOG_PATH/httpd
mkdir -p $LOG_PATH/text/uwsgi

# for file-based cache (dev only)
mkdir -p /var/cache/nginx
chown nginx /var/cache/nginx
chgrp -R nginx $LOG_PATH

chmod -R 775 /var/log/docker/$HOSTNAME

LOG_PATH_ENC=$(echo $LOG_PATH | sed -e 's/[\/&]/\\&/g')

sed -i -e "s/__LOG_PATH__/$LOG_PATH_ENC/g" /etc/supervisord.conf

PYTHON_LOG_FILE=$LOG_PATH/python/whr-scorer.log
export PYTHON_LOG_FILE

/usr/bin/supervisord -c /etc/supervisord.conf -n
