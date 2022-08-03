FROM python:3.10.2-alpine3.15

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ARG BUILD_DEPENDENCIES=""
ARG RUNTIME_DEPENDENCIES=""

RUN apk add --no-cache bash nano build-base postgresql-dev gcc python3-dev musl-dev libffi-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

ENTRYPOINT ["/start"]


