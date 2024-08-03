FROM python:3.12.2-slim-bullseye

RUN apt-get update && apt-get install -y git && apt-get clean

RUN mkdir /hapy

VOLUME /hapy
VOLUME /root/.ssh

RUN mkdir /hapy/user
RUN mkdir /hapy/src

WORKDIR /hapy/src
COPY hapy hapy
COPY requirements.txt requirements.txt
COPY setup.py setup.py
RUN pip install --no-cache-dir .

WORKDIR /hapy/user

CMD ["hapy-run"]
