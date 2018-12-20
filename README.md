
# recruit

This recruit micro Project has one jon application form where anonymous user can apply for a job.

In admin section there will be list of job that have been listed. 

Admin can able to accept or reject the application.

By default the application status would be in pending.

clone the application into your system.

use https://github.com/sbhuvanas/recruit this to clone

git clone https://github.com/sbhuvanas/recruit

create and start a virtual env

virtualenv env --no-site-packages

source env/bin/activate

Install the project dependencies:
pip install -r requirements.txt

In settings.py modify the db name according to your mysql

Migrate your db 
python manage.py make migrations
python manage.py migrate

Create admin account
python manage.py createsuperuser

to start the development server
python manage.py runserver

Open localhost:8000 to see the home page