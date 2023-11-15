FROM python:3.10-slim

#WORKDIR /usr/src/app

#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

#RUN apt-get update -y \
#    && apt-get install -y build-essential libpq-dev # Для postgres auth

RUN mkdir /nova

WORKDIR /nova

#RUN pip install --upgrade pip
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN #mkdir -p /home/app

#ENV HOME=/home/app
#ENV APP_HOME=/home/app/web
#RUN mkdir $APP_HOME
#RUN mkdir $APP_HOME/static
#RUN mkdir $APP_HOME/media

RUN python manage.py migrate



#COPY ./entrypoint.sh .
#COPY . $APP_HOME


#ENTRYPOINT ["/home/app/web/entrypoint.sh"]



#CMD gunicorn -w 2 -t 600 catena.wsgi:application --bind 0.0.0.0:8000
CMD python manage.py runserver