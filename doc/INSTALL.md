# INSTALL

## Back End Dependencies

### Virtualenv and Pyenv

We strongly recommend you to create a virtual environment :

```bash
pyenv install 2.7
pyenv virtualenv 2.7 python27
```

```bash
git clone https://github.com/demain-supermarche/odoo-production.git
cd odoo-production/
echo "python27" > .python-version # replace "python27" by your virtualenv's name
pip install -r odoo/requirements.txt
```
### For Ubuntu users

You may have to install the following packages :

```bash
sudo apt-get install libxml2-dev libxslt1-dev python-dev libxslt libldap2-dev libsasl2-dev libssl-dev
```

## Front End Dependencies

```bash
npm install
```

### For Ubuntu users

You may have to install the following package :

```bash
sudo apt install npm
```

## Database
```bash
# Please replace " odoo_user" and "odoo_prod" with the value you want
sudo -u postgres createuser -P odoo_user
sudo -u postgres createdb odoo_prod
sudo -u postgres psql
# On SQL prompt
grant all privileges on database odoo_prod to odoo_user
\q
# Some config are needed
sudo cp /etc/postgresql/9.5/main/pg_hba.conf /etc/postgresql/9.5/main/pg_hba.conf.bk
sudo gedit /etc/postgresql/9.5/main/pg_hba.conf # or whatever text editor you like
# Then replace every "peer" by "md5"
sudo service postgresql restart # Restart the service
# Finally this command should works :
psql -U odoo_user -W odoo_prod
# On SQL prompt
odoo_prod=> \dt;
No relations found.
odoo_prod=> \q
```

### For Ubuntu users

You may have to install the following package :

```bash
sudo apt install postgresql
```
## Launch the app

```bash
python odoo/odoo.py -w odoo_user -r odoo_passwd --addons-path=odoo/addons/,louve_addons,intercoop_addons
# To not forget to replace odoo_user by your user and odoo_passwd by its password
```

Open your favorite browser and go to [127.0.0.1:8069](http://127.0.0.1:8069)
