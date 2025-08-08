# E-Learniverse Flexbox & Other Learning Backend
A Django Backend application for E-Learniverse. This is a Self-Learning Project to document all my Personal leanrings in Django Framework.

## Installation guide
You do need to install Python-3.8 first. After that run following commands:

```shell script
  pip install virtualenv
  virtualenv e_learniverse_env
  source ./e_learniverse_env/bin/activate
  which python
```

Then install the requirements from "requirements.txt"
```shell script
  pip install -r requirements.txt 
```

if "pip" gives you version error run the following command:
```shell script
  pip install "pip<24"
```

Please follow standard **Django** installation guide.

To start **Django** development server:
```shell script
  python manage.py runserver
```

To start **Django** development server in a Particular PORT (example: Port 9999):
```shell script
  python manage.py runserver 0.0.0.0:9999
```

### Docker guide
Please follow [this docker guide](docker/docker-guide.md) to run tallykhata backend with docker. 
First Install Docker & Docker-Compose in your System. Then run following command-

`DockerFile` Build & Run Command
```shell script
sudo docker build --tag django-project-docker-image .
sudo docker run --publish 8002:9998 --name my-django-web-container django-project-docker-image
sudo docker exec -it my-django-web-container /bin/bash
```

`Docker-Compose` Command to run all service
```shell script
sudo docker-compose up --build
sudo docker-compose run django_web_app python manage.py migrate
```

### Celery guide
Run the following command after installing Celery in Django Project
```shell script
celery -A django_docker_project worker --loglevel=info
```

`Custom Queue` Command of Celery Worker in Django Project
```shell script
celery -A django_docker_project worker -Q e_learniverse_default_queue,custom_queue --loglevel=info
```

Start `Celery-BEAT` in Django Project
```shell script
celery -A django_docker_project beat --loglevel=info
```

### Run Test Cases
Run the following command for Unit Testing
```shell script
python manage.py test
```

### Production Setup with Gunicorn
Run the following command for Gunicorn Command:
```shell script
gunicorn -w 4 --bind 0.0.0.0:9999 django_docker_project.wsgi
```
The `-w 4` flag tells Gunicorn to spawn 4 worker processes. These are not threads, but separate processes that can handle requests concurrently.
Gunicorn documentation suggests to have:
Gunicorn documentation suggests:

`workers = 2 × (CPU cores) + 1`

Now To have:
- **4 worker processes**
- **Each process with 2 threads**
- **Total of 8 threads handling requests**

```shell script
gunicorn -w 4 --threads 2 --bind 0.0.0.0:9999 django_docker_project.wsgi
```