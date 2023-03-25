# syntax=docker/dockerfile:1

FROM python:3.12.0a6-slim-bullseye


RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV PORT=8888
EXPOSE 8888

#use "" not ''
CMD [ "python3", "tornadotest.py"]  

# build image: 
# docker build -t tornado-app:1.0 .
# run container:
# docker run -p 8888:8888 tornado-app:1.0
# docker run -d -p 8888:8888 tornado-app:1.0
# -d is detached, free's up terminal
# learned: don't name your python file tornado.py = the same as the import package = errors