FROM python:3.6.4

MAINTAINER Eduardo Junio

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

#CMD python manage.py runserver 0.0.0.0:$PORT

ADD . /code
