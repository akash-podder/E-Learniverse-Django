FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /web_app

COPY requirements.txt /web_app/

RUN pip3 install -r requirements.txt

COPY . /web_app/
COPY django_docker_project/.env_docker /web_app/django_docker_project/.env

EXPOSE 9998

# as the WORKDIR is `/web_app/` folder... so the CMD, RUN & Other Commands are Run on that specific Folder
CMD ["python", "manage.py", "runserver", "0.0.0.0:9998"]