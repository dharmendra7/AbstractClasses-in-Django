# AbstractClasses-in-Django

## Index

- [Index](#index)
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup using docker](#setup-using-docker)

### Introduction

- Supports latest version of Python i.e. Python 3.11.1  along with Django 4.2.5 :zap:
- In models.py file of my application I have two classes Post and Comment.
- Both of the classes share the same fields (tile, body, author, created_at)
- The only diffrence is the Comment class has the foreign key relationship to the post.
- So here is the solution for above.
- We can create an abstract class from which the Post class and the Comment class will inherit.

### Prerequisites

| Plugin | *Version*|
| ------ | ------ |
|  pip   | 22.3.1 |
| Python | 3.11  |
| Django | 4.2.5 |

### Installation

> ##### 1. Clone repository

```bash
git clone 
```

> ##### 2. Create virtual environment and activate

```bash
python -m venev yourr-venv-name
```

> ##### 3. Setup The Project

```bash
pip install -r requirements.txt
```

> ##### 6. Create tables by Django migration

```bash
python manage.py migrate
```

> ##### 7. Start the development server

```bash
python manage.py runserver
```



### Setup using docker
- [Docker](https://docs.docker.com/engine/install/)

> #### Setup
Start the dev server for local development:
```bash
docker-compose up -d
```

<br />

![image](https://github.com/dharmendra7/AbstractClasses-in-Django/assets/85740691/371267ad-0095-4c8f-b01e-9e0c59444db8)

