#!/bin/sh

if [$# -ne 2]; then
    echo "usage: proc-text.sh <input-file> <output-directory>"
    exit 1
fi

# run malt and frame extractor in parallel
mkfifo $2/conll
/semafor-master/bin/runMalt.sh $1 $2 &
cat $2/conll | nc -w 15 ${FRAMEPARSER_HOST} ${FRAMEPARSER_PORT} > $2/output
rm -f $2/conll
