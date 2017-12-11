# INSTALL
## Table of Contents
1. [Get the source](#source)
2. [Back End Dependencies](#back-end)
3. [Front End Dependencies](#front-end)
4. [Database](#database)
5. [Launch the app](#launch)

## Get the source <a name="source"></a>

```bash
git clone https://github.com/demain-supermarche/odoo-production.git && cd odoo-production/
```

## Back End Dependencies <a name="back-end"></a>
### Virtualenv and Pyenv

We **strongly** recommend you to create a virtual environment, For example using [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).

Once these two softwares are installed you can create a python environment under version 2.7 like this :


```bash
pyenv install 2.7
pyenv virtualenv 2.7 python27
echo "python27" > .python-version # replace "python27" by your virtualenv's name in order to automatically source it
```
### pip

When you're virtual environment is set up, install back-end dependencies with pip :

```bash
pip install -r odoo/requirements.txt
```
### For Ubuntu users

You may have to install the following packages :

```bash
sudo apt-get install libxml2-dev libxslt1-dev python-dev libldap2-dev libsasl2-dev libssl-dev
```

## Front End Dependencies <a name="front-end">

```bash
npm install -g less && npm install
```

### For Ubuntu users

You may have to install the following package :

```bash
sudo apt install npm node-less nodejs-legacy
```

## Database <a name="database"></a>

Create a postgres user.

```bash
# Please replace " odoo_user" with the value you want
sudo -u postgres createuser -P odoo_user
sudo -u postgres psql
```
Allow user to create a database : Open an SQL prompt by tipping **sudo -u postgres psql**

```SQL
ALTER USER odoo_user CREATEDB; \q
```

Configure postgres

```bash
sudo cp /etc/postgresql/9.5/main/pg_hba.conf /etc/postgresql/9.5/main/pg_hba.conf.bk
sudo gedit /etc/postgresql/9.5/main/pg_hba.conf # or whatever text editor you like
# Then replace every "peer" by "md5" EXCEPT FOR THE LINE REGARDING POSTGRES USER
# local   all             postgres                                peer
sudo service postgresql restart # Restart the service
```

### For Ubuntu users

You may have to install the following package :

```bash
sudo apt install postgresql
```
## Launch the app <a name="launch"></a>

```bash
python odoo/odoo.py -r odoo_user -w odoo_passwd --addons-path=odoo/addons/,louve_addons,intercoop_addons
# To not forget to replace odoo_user by your user and odoo_passwd by its password
```

Open your favorite browser and go to [127.0.0.1:8069](http://127.0.0.1:8069)
