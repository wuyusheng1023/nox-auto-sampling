FROM python:3.9.1-alpine

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]