FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN mkdir /logs

RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
    
RUN pip install -r requirements.txt

RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential
