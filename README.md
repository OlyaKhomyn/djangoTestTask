
## Description
This is the source code of the test task in Django.

## Technologies
* Python (3.7.3)
* PostgreSQL (11.4)
* Django (3.0.9)

## Install
Run following commands: 
```
pip install Django
pip install djangorestframework
pip install psycopg2
```
### Create PostgreSQL database on your local machine:
```
'NAME': 'django_db',
'USER': 'postgres',
'PASSWORD': 'postgres',
'HOST': 'localhost',
'PORT': '5432'
```
Apply migrations:
```
python manage.py migrate
```
### Create superuser
```
python manage.py createsuperuser
```
Enter your desired username and press enter.
```
Username: admin
```
You will then be prompted for your desired email address:
```
Email address: admin@example.com
```
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
```
Password: **********
Password (again): *********
Superuser created successfully.
```
### Start server
```
python manage.py runserver
```
### Get users API
All users:
```
http://localhost:8000/users
```
Filtered by registration date
```
http://localhost:8000/users?registration=2018-05-09
```
### Admin interface
Go to:
```
http://127.0.0.1:8000/admin
```
Enter username and password created before

#### Import of users
Go to:
```
http://127.0.0.1:8000/admin/users/user/
```
Click on "Choose file" button
Select csv file with users' information
Click on "Upload" button.
