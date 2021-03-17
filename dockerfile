#FROM python:3.7.4-alpine3.10
FROM python:3.8.8-slim-buster
#FROM python:3
ENV PYTHONUNBUFFERED 1
#RUN apt-get update
#RUN apt-get install -y python3-dev python-dev default-libmysqlclient-dev
#RUN apt-get  install -y gcc
RUN mkdir /code
COPY . /code/
WORKDIR /code/delivery/
RUN pip install -r ../requirements.txt
RUN pip install gunicorn
RUN echo "Collect static files..."
RUN python manage.py collectstatic --noinput