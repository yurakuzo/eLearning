# Stage 1: Generate SSL certificates
#FROM alpine/openssl AS certs
#
#WORKDIR /certs
#RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
#    -keyout ssl_certificate_key \
#    -out ssl_certificate \
#    -subj "/C=US/ST=CA/L=San Francisco/O=My Company/OU=Org/CN=mydomain.com"

# Stage 2: Build the main Docker image
FROM python:3.11-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt

RUN python -m pip install --upgrade pip

COPY . /app

#CMD ["python", "app/main.py"]
