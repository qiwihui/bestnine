FROM python:3.7-slim

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip \
  && python -m pip install -r requirements.txt \
  && mkdir -p /code

WORKDIR /code