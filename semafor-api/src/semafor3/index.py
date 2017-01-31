from flask import Flask, request, jsonify, abort
import sys
import logging
import json
import subprocess
import tempfile
import time
import os
import re

from nltk.tokenize import sent_tokenize

from logstash.formatter import LogstashFormatterVersion1
from logging.handlers import RotatingFileHandler

#### LOGGING SETUP ####

class LogstashFormatter(LogstashFormatterVersion1):
    @classmethod
    def serialize(cls,message):
        return json.dumps(message)

log_level = os.getenv("LOG_LEVEL","INFO")
try:
    numeric_level = getattr(logging, log_level)
except:
    print("Invalid log level: {0}".format(log_level))
    numeric_level = logging.INFO

root = logging.getLogger()

root.setLevel(numeric_level)

handler = RotatingFileHandler(os.getenv("PYTHON_LOG_FILE","/var/log/mexusage.log"),
                              mode='ab',
                              maxBytes=1000000,
                              backupCount=2)
handler.setFormatter(LogstashFormatter(tags=['python']))
root.addHandler(handler)



#------------------------------------------------------------------------
# App maintenance -- APP IS STARTED AT THE END OF THE FILE
#------------------------------------------------------------------------

# App instance
application = Flask(__name__)

LOGGER = logging.getLogger(__name__)



def proc_input(d):
    resp_list = []
    tstart = time.time()
    with tempfile.TemporaryDirectory() as tmpdirname:
        f_in = os.path.join(tmpdirname,'input')
        lines = re.split('[\\r\\n]*',d)
        with open(f_in,'w') as in_f:
            for l in lines:
                l = l.strip().replace('\t',' ')
                if len(l)>0:
                    # split sentences
                    for sentence in sent_tokenize(l):
                        in_f.write(sentence+'\n')
        LOGGER.info("Calling proc-text {0} {1}".format(f_in,tmpdirname))
        subprocess.run(["/proc-text.sh",
                        f_in,
                        tmpdirname],
                       check=True)
        with open(os.path.join(tmpdirname,'output'),'r') as out_f:
            while True:
                line = out_f.readline()
                if len(line)==0:
                    break
                resp_list.append(json.loads(line))
    LOGGER.info("Input length = {0}, processing time = {1:.3f}".format(len(d),time.time()-tstart))
    return resp_list

        
@application.route("/parse-frames",methods=['POST','GET'])
def parse_frames():
    if request.method == 'GET':
        # parse from text parameter
        d = request.args.get('t')
        if d == None:
            abort(400)
    else:
        d = request.get_data(as_text=True)
    tstart = time.time()
    try:
        r = proc_input(d)
    except:
        LOGGER.exception("Error processing input")
        abort(500)
    return jsonify(r)
        
@application.route("/keepalive",methods=['GET'])
def keepalive():
    return "OK"


if __name__ == '__main__':
    application.run(debug=True)

