FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /web_app

COPY requirements.txt /web_app/

# "--no-cache-dir" otherwise "PIP" first pulls the Dependency file & after installing the file it keeps those cache file... (Think Windows ee kisu install korar somoy amra jemon ".zip" namai then install kori then, Downloads folder theke oi ".zip" file Remove kore dei)
RUN pip install --no-cache-dir -r requirements.txt

COPY . /web_app/
COPY django_docker_project/.env_docker /web_app/django_docker_project/.env

EXPOSE 9998

# as the WORKDIR is `/web_app/` folder... so the CMD, RUN & Other Commands are Run on that specific Folder
CMD ["python", "manage.py", "runserver", "0.0.0.0:9998"]