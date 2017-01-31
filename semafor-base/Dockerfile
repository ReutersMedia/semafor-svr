FROM alpine:3.5
MAINTAINER kenneth.ellis@thomsonreuters.com

RUN apk --update add openjdk8 && \
    apk add --virtual build-dependencies maven curl && \
    cd / && \
    curl -L https://github.com/Noahs-ARK/semafor/archive/master.tar.gz | tar xz -C / && \
    cd /semafor-master && \
    export JAVA_HOME=/usr/lib/jvm/default-jvm && \
    mvn package && \
    rm -rf /var/cache/apk/* && \
    mkdir /models && \
    curl -L http://www.ark.cs.cmu.edu/SEMAFOR/semafor_malt_model_20121129.tar.gz | tar xzv -C /models && \
    apk del build-dependencies 

