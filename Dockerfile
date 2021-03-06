FROM python:3.8.7-slim-buster
LABEL MAINTAINER="Mahdi Namaki | https://mavenium.github.io"

ENV PYTHONUNBUFFERED 1

RUN mkdir /library_management
WORKDIR /library_management
COPY . /library_management

# Installing requirements
ADD requirements.txt /library_management
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
