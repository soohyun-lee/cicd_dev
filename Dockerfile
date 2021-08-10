FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN mkdir /logs

RUN pip install -r requirements.txt