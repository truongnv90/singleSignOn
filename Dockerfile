FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get -q install -y build-essential

RUN pip3 install -r ./requirements.txt --no-cache-dir

COPY . .