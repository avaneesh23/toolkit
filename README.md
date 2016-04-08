# toolkit
Django app providing handsontable interface for the contents of the database

Devbox Setup
-------------

Starting from a fresh EC2 instance running Ubuntu 14.04.1 LTS

#### Initial Setup

Install initial dependencies:

```
sudo apt-get install git nginx gunicorn libmysqlclient-dev python-mysqldb mysql-server
```

Clone the main github repo:

```
mkdir git
cd git
git clone https://github.com/avaneesh23/toolkit
```


# Install the rest of the python dependencies:

```
# NOTE: the default python-pip ubuntu package has a bug at time of writing, that's
# why we're using the get-pip.py script for now
# https://bugs.launchpad.net/ubuntu/+source/python-pip/+bug/1306991
# http://stackoverflow.com/questions/27341064/how-do-i-fix-importerror-cannot-import-name-incompleteread
cd ~
wget https://bootstrap.pypa.io/get-pip.py
sudo python ./get-pip.py
cd ~/git/toolkit
sudo -H pip install --upgrade -r ~/git/toolkit/requirements.txt
```


# Set environment variables:

To have env variables always set on login

```
echo "source ~/git/toolkit/config/devbox-env" >> ~/.bashrc
```


# For generating django secret key:

```python
import string, random; ''.join([random.SystemRandom().choice("{}{}{}".format(string.ascii_letters, string.digits, string.punctuation)) for i in range(50)]).replace('\'','"')
```


#### Django Deployment

Django is deployed using nginx, gunicorn, and upstart. We register a service
with upstart that runs gunicorn, which will instantiate django on
port 8000. This is proxied by nginx to port 80. The scripts and configuration
files needed to set all this up are in ~/git/toolkit/nginx.

First, create the log directory that will aggregate logs from all services:

```
sudo mkdir -p /var/log/euprime
sudo chown www-data:www-data /var/log/euprime
```

Next, the SSL certificate and key need to be installed to enable HTTPS.

```
cd ~/git/toolkit/nginx
sudo cp star_euprime_com.key /etc/ssl/
sudo cp star_euprime_com.pem /etc/ssl/
sudo chmod 600 /etc/ssl/star_euprime_com.*
```

Set up nginx:

```
sudo apt-get install nginx
sudo cp ~/git/toolkit/nginx/nginx_site_django /etc/nginx/sites-available/euprime-django
sudo ln -s /etc/nginx/sites-available/euprime-django /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart
```

Set up upstart:

```
sudo cp ~/git/toolkit/config/upstart/startup_script_django /etc/init/euprime_django.conf # install the script
sudo ln -fs /lib/init/upstart-job /etc/init.d/euprime_django # add as system service
sudo update-rc.d euprime_django defaults # have it start at boot
sudo service euprime_django start # start it now
```


#### Django Setup

The Django project is named 'handsontable' and is located at 
~/git/toolkit/handsontable, and the project settings files are in
~/git/toolkit/handsontable/handsontable. All other subfolders of
~/git/toolkit/handsontable are different django applications.
We have several django applications such as userinfo, website.
A new application can be created by running manage.py startapp <appname>
Each of the applications tackle different roles on the backend. 
The 'website' application holds templates and static files. 
The static files of all the django apps get collected and stored 
in project directory after running manage.py collectstatic --noinput

The apps that will be run by django are configured in
~/git/toolkit/handsontable/handsontable/settings.py,

To enable any given django application the name simply needs to be included in the 
INSTALLED_APPS variable, and then the database for that application gets created 
by running manage.py migrate.

```
sudo -E ~/git/toolkit/config/setup_db.sh
```

That creates the databases for all apps on the local machine and sets usernames
and passwords. The mysql password needs to be entered here to modify the mysql
database. Once complete, the standard django mechanisms can be used to setup the
database tables:

```
sudo -E python ~/git/toolkit/handsontable/manage.py migrate
```

Next we need to create the django superuser used for API access. Just run it 
once even if it seems to fail because it always creates the user in the db

```
echo "from django.contrib.auth.models import User; User.objects.create_user('$EUPRIME_TOOLKIT_USERNAME', '', '$EUPRIME_TOOLKIT_PASSWORD')" | python ~/git/toolkit/handsontable/manage.py shell
```

Finally, static files need to be collected from all applications so nginx can
host them in one place:

```
python ~/git/toolkit/handsontable/manage.py collectstatic --noinput
```


