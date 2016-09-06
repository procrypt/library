FROM centos:7
MAINTAINER Abhishek Pratap Singh asingh@redhat.com

RUN yum install -y wget \
    tar \
    epel-release \
    gnupg \
    python34 \
    openssl \
    java-1.8.0-openjdk-headless \
    javapackages-tools \
    lksctp-tools \
    python-javapackages \
    python-lxml \
    tzdata-java \


RUN gpg --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" \
    && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64.asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm -f /usr/local/bin/gosu.asc \
    && rm -rf /root/.gnupg/ \
    && chmod +x /usr/local/bin/gosu

RUN groupadd crate && useradd crate -g crate -d /home/crate -s /bin/bash -p 'crate'

USER crate 

RUN  wget https://cdn.crate.io/downloads/tmp/crate-0.55.4.tar.gz \
     && wget https://cdn.crate.io/downloads/releases/crate-0.55.4.tar.gz.asc \
     && export GNUPGHOME="$(mktemp -d)" \
     && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 90C23FC6585BC0717F8FBFC37FAAE51A06F6EAEB \
     && gpg --batch --verify crate-0.55.4.tar.gz.asc crate-0.55.4.tar.gz \
     && rm -r "$GNUPGHOME" crate-0.55.4.tar.gz.asc \
     && mkdir /crate \
     && tar -zvxf crate-0.55.4.tar.gz -C /crate --strip-components=1 \
     && chown -R crate /crate

ENV PATH /crate/bin:$PATH

VOLUME ["/data"]

ADD files/crate.yml /crate/config/crate.yml
ADD files/logging.yml /crate/config/logging.yml    
COPY docker-entrypoint.sh /

WORKDIR /data    

EXPOSE 4200 4300

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["crate"]
