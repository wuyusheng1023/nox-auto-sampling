FROM python:3.9.1-alpine 

ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . .

RUN \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps

ENTRYPOINT ["sh", "entrypoint.sh"]
