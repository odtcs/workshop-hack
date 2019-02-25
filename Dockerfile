FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN apk --update add --no-cache build-base

RUN mkdir /workshop-hack
WORKDIR /workshop-hack
RUN adduser -S -u 1000 workshop-hack
RUN mkdir /run/nginx

## Install dependencies
## RUN apk --update add --no-cache nginx supervisor python3-dev supervisor postgresql-dev
RUN apk --update add --no-cache nginx supervisor python3-dev supervisor

## Install webserver
RUN pip install gunicorn
ADD ./supervisor.ini /etc/supervisor.d/supervisor.ini

ADD ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
ENTRYPOINT ["./entrypoint.sh"]
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]

ADD ./workshop-hack/requirements.txt .

## Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN rm -rf /var/cache/apk/*

ADD ./workshop-hack/ .
RUN chmod +x ./entrypoint.sh
