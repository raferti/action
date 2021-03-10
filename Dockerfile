FROM python:3.8-alpine

COPY . /app
WORKDIR /app
RUN apk update
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt --no-cache-dir

RUN python manage.py flush --no-input
RUN python manage.py migrate

EXPOSE 8000