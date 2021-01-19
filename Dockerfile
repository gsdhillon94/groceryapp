FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /groceryapp

ADD . /groceryapp

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /groceryapp