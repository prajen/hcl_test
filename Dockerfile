FROM centos:7

RUN mkdir -p /usr/src/app

COPY mac_info_fetcher.py /usr/src/app/

WORKDIR /usr/src/app/
