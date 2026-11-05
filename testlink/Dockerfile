FROM php:7.4-apache

# Debian 11 (bullseye) ya es EOL: sus paquetes viven en archive.debian.org
RUN sed -i -e '/bullseye-updates/d' \
           -e 's|deb.debian.org|archive.debian.org|g' \
           -e 's|security.debian.org|archive.debian.org|g' /etc/apt/sources.list \
 && echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99archive \
 && apt-get update && apt-get install -y --no-install-recommends \
      libpng-dev libjpeg-dev libfreetype6-dev curl ca-certificates \
 && docker-php-ext-configure gd --with-freetype --with-jpeg \
 && docker-php-ext-install -j"$(nproc)" gd mysqli \
 && rm -rf /var/lib/apt/lists/*

RUN cp "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini" \
 && sed -i 's/^max_execution_time.*/max_execution_time = 120/' "$PHP_INI_DIR/php.ini" \
 && sed -i 's/^memory_limit.*/memory_limit = 256M/' "$PHP_INI_DIR/php.ini" \
 && sed -i 's/^;date.timezone.*/date.timezone = America\/Lima/' "$PHP_INI_DIR/php.ini"

ARG TESTLINK_TAG=1.9.20
RUN curl -fsSL "https://github.com/TestLinkOpenSourceTRMS/testlink-code/archive/refs/tags/${TESTLINK_TAG}.tar.gz" \
    | tar xz --strip-components=1 -C /var/www/html \
 && mkdir -p /var/testlink/logs /var/testlink/upload_area \
 && chown -R www-data:www-data /var/www/html /var/testlink
