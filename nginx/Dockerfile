FROM nginxinc/nginx-unprivileged:1-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

USER root

RUN mkdir -p /var/cache/nginx
RUN chmod 755 /var/cache/nginx

USER nginx