FROM python:3.9.1-slim-buster

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]
