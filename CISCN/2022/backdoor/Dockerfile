FROM php:7.4-apache

COPY html /var/www/html

COPY flag /flag
COPY readflag/readflag /readflag

RUN sed -i 's#http://deb.debian.org#http://mirrors.aliyun.com#g' /etc/apt/sources.list &&\
    apt-get update && apt-get install -y libmagickwand-dev --no-install-recommends

RUN pecl install imagick && docker-php-ext-enable imagick &&\
    chmod -R 555 /var/www/html &&\
    chmod 400 /flag &&\
    chmod 111 /readflag && chmod u+s /readflag

EXPOSE 80
