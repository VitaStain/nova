FROM python:3.10-slim

RUN mkdir /nova

WORKDIR /nova

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python manage.py migrate

CMD gunicorn -w 2 -t 600 catena.wsgi:application --bind 0.0.0.0:8000