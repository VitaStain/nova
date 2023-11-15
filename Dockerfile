FROM python:3.10-slim

RUN mkdir /nova

WORKDIR /nova

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python manage.py migrate

CMD python manage.py runserver