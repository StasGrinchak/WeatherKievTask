FROM python:3.9.6-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip3 install --upgrade pip
RUN apk update && apk add postgresql-dev gcc libc-dev libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev musl-dev
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

WORKDIR /app
COPY req.txt /app/
RUN pip install -r req.txt
COPY . /app/