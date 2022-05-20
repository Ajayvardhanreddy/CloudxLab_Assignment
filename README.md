<div align="center">
<h1>CloudxLab Assignment</h1>
<br/></div><br/>


## Getting Started 

If you are trying to use this project for the first time, you can get up and running by following these steps. 

## Assignment Images:


  <img src="https://github.com/Ajayvardhanreddy/CloudxLab_Assignment/blob/main/static/images/form.png" width="800" />
  <img src="https://github.com/Ajayvardhanreddy/CloudxLab_Assignment/blob/main/static/images/form_success.png" width="800" /> 
  <img src="https://github.com/Ajayvardhanreddy/CloudxLab_Assignment/blob/main/static/images/form-invalid-mail.png" width="800" />
  



## Requirements 

|                          Technology                          |      Version       |
| :----------------------------------------------------------: | :----------------: |
|           [**Python**](https://docs.python.org/3/)           |      **3.x**       |
|           [**pip**](https://pypi.org/project/pip/)           | **latest version** |
|     [**Django**](https://docs.djangoproject.com/en/3.2/)     |      **4.0.4** |
|      [**gunicorn**](https://pypi.org/project/gunicorn/)      |     **20.1.0** |
|      [**psycopg2**](https://pypi.org/project/psycopg2/)      |     **2.9.3** |
|      [**asgiref**](https://pypi.org/project/asgiref/)      |     **3.5.2** |
|      [**sqlparse**](https://pypi.org/project/sqlparse/)      |     **0.4.2**  |
|      [**tzdata**](https://pypi.org/project/tzdata/)      |     **2022.1** 

## Install and Run

Make sure you have **Python 3.x** installed and **the latest version of pip** *installed* before running these steps.
.

Clone the repository using the following command

```bash
git clone https://github.com/Ajayvardhanreddy/CloudxLab_Assignment.git
# After cloning, move into the directory having the project files using the change directory command
cd cloudxlab_assignment
```
Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python -m venv env
```
Activate the virtual environment

```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```
Install all the project Requirements
```bash
pip install -r requirements.txt
```
## Create Project

We can now start a Django project within our `cloudxlab_assignment` directory. This will create a child directory of the same name to hold the code itself, and will create a management script within the current directory. Make sure to add the dot at the end of the command so that this is set up correctly:
```bash
django-admin startproject cloudxlab_assignment .
```
> **NOTE:** Dot (.) at the end of the above command makes the current directory as Project directory.

##  Configure the Django Database Settings:

Now that we have a project, we need to configure it to use the database we created. Open the main Django project settings file located within the child project directory:
``` bash
nano ~/cloudxlab_assignment/cloudxlab_assignment/settings.py
```
Towards the bottom of the file, you will see a `DATABASES` section that looks like this:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
This is currently configured to use `SQLite` as a database. We need to change this so that our `PostgreSQL` database is used instead of default `SQLite. `

```bash

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<db_name>',
        'USER': '<db_username>',
        'PASSWORD': '<password>',
        'HOST': '<db_hostname_or_ip>',
        'PORT': '<db_port>',
    }
}

```
## Migrate the Database
Now that the Django settings are configured, we can migrate our data structures to our database and test out the server.

```bash
cd ~/cloudxlab_assignment

# apply migrations

python manage.py makemigrations
python manage.py sqlmigrate formData 0001
python manage.py migrate
```

 Create a superuser with the following command:

```bash
python manage.py createsuperuser
```

Run the development server

```bash
# run django development server
python manage.py runserver
```


## Explore admin panel for model data or instances

Open http://127.0.0.1:8000/admin or http://localhost:8000/admin, enter the superuser credentials (only superuser can access /admin page)

## Success:
If everything is good and has been done successfully, your **Django Project** should be hosted on port 8000 i.e http://127.0.0.1:8000/ or http://localhost:8000/ to serve you.




