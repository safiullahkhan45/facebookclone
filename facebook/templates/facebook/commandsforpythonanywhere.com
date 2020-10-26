git clone https://github.com/safiullahkhan45/facebookclone

mkvirtualenv --python=/usr/bin/python3.8 myenv

add virtualenv in web tab
update wsgi configuration file

cd facebookclone

pwd and update the wsgi path with the pwd result

update settings as well and add the project name that you used while using startproject command.

update the allowed hosts inside settings.py with ['domain_name']

add static root to settings.py file
STATIC_ROOT = '/home/loginfacebook/facebookclone/static'

python manage.py collectstatic