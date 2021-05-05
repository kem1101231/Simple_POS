FROM python:3-buster

RUN apt-get update 
RUN apt-get install -y git
RUN mkdir /opt/app/
RUN pip3 install django

COPY . /opt/app/

RUN python3 /opt/app/manage.py makemigrations
RUN python3 /opt/app/manage.py migrate

CMD ["python3 /opt/app/manage.py runserver 0.0.0.0:8000"]
