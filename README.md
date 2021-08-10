<h1 align="center"> Welcome to facturaxion! </h1>



## Introduction :notebook:

This repository contains all the work done for the facturaxion database and the platform services. It is written in Python/Django, Docker, and other tools / languages.

## Table of Contents :open_file_folder:

* [About](#about)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)


## About
You are on your way to getting to know the backend of the Sisben virtual office! These are some things you will want to see.

1. **python/django installation:** :black_nib:
* How to install django
* How to run a virtual environment
* How to install third party packages
* How to run current packages
* How to handle django commands


## Requirements

* Ubuntu 20.04 LTS | WSL 2 on Windows | MacOS 10.15.7
* python 3.9.1
* Django 3.1.6
* Docker 20.10.5
* @vue/cli 4.5.13
* node 12.21.0
* pip 21.0.1
* All programs were run on a Vagrant(ubuntu/trusty64) (Virtualbox) environment

## Installation backend

![drf](https://i2.wp.com/codethief.io/wp-content/uploads/2019/03/a6a2d-image-3.png?resize=516%2C293)

In your terminal, git clone the directory with the following command:

```sh
git clone https://github.com/estebanmorad/facturaxion/
```
#### docker-compose installation

if you want install docker at 

* [Windows](https://docs.docker.com/docker-for-windows/install/)
* [MacOS](https://docs.docker.com/docker-for-mac/install/)
* [Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)

After only run command to used  instance in the directory  :

```bash
docker-compose --version
```

#### Installation steps

1. Ensure you have python3 installed

2. Clone the repository
3. create a virtual environment using `virtualenv env`
4. Activate the virtual environment by running `source env/bin/activate`

- On Windows use `env\Scripts\activate`

5. Install the dependencies using `pip install -r requirements.txt`

* Also you can only use `source env/bin/activate`

6. Run docker to postgres-db, nginx, django`docker-compose up --build`
* To database `docker-compose run backend python backend/manage.py makemigrations`
* To migrate database `docker-compose run backend python backend/manage.py migrate`
* To load templates `docker-compose run backend python backend/manage.py collectstatic`

* To stop use `docker-compose stop`

7. Migrate existing db tables by running `python manage.py migrate`

8. Run the django collectstatic `python manage.py collectstatic`

9. Run the django development server using `python manage.py runserver`

## Usage

If you want you can use the automated or manual scripts with the above indications

```sh
docker-compose up --build
```

## Information to admin django
```python
python manage.py createsuperuser
docker-compose run backend python backend/manage.py createsuperuser
```
| user | password | Description |
| ----- | ----- | ------ |
| admin | esteban123 | Admin |


## Installation frontend

![vue](https://res.cloudinary.com/practicaldev/image/fetch/s--zAemwa8F--/c_imagga_scale,f_auto,fl_progressive,h_500,q_auto,w_1000/https://thepracticaldev.s3.amazonaws.com/i/sob3zk1d6hms4klfzftw.jpg)

In your terminal:

```sh
git clone https://github.com/estebanmorad/facturaxion/
```


Enter into frontend and run docker-compose --build if you have it installed:

```bash
/rama-principal/development ❯ cd frontend
/frontend/development ❯ docker-compose --build
```

#### Installation steps

1. Ensure you have vue installed


2. Run `docker-compose up --build`
3. Start - Local:  ` http://localhost:8081/ `

* To stop use `docker-compose stop`



# django-vue.js
# django-vue.js
