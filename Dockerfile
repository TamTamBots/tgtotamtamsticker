FROM python:3.10.7-slim-bullseye
RUN apt-get install -y wget curl bash sudo
RUN sudo apt-get install -y apt-utils build-essential python3-dev
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -U -r requirements.txt
ADD . /app
RUN python setup.py sdist
RUN pip3 install dist/*
EXPOSE 19999
ENTRYPOINT [ "tg-to-tt-bot" ]
