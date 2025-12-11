FROM python:3.14-alpine

RUN mkdir /app
WORKDIR /app

ADD flask-app /app/

RUN pip install -e .

RUN flask --app flaskr init-db

EXPOSE 5000
CMD ["flask", "--app", "flaskr", "run", "--host=0.0.0.0", "--port=5000"]
