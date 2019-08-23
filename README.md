# lakiller.cz
This is an open source statbus for the [/tg/station](https://github.com/tgstation/tgstation/) database code Space Station 13 server. It was created to provide a python alternative.

# Requirements
The following packages are required:
* Flask (and it's requirements)
* mysql-connector-python
* peewee
* uwsgi
* python-dotenv

You can install the requirements from the requirements.txt file.

# Setting up
Make sure you have a read-only database account and that you have whitelisted just the server you will be hosting this on for security reasons. Either set the environment variables yourself or head into the src folder and create a new file called .env, using the following variable names:

```
STATBUS_DBUSERNAME="username" //The username for your database account.
STATBUS_DBPASSWORD="password" //The password for your database account.
STATBUS_DBHOST="127.0.0.1"    //The IP address of your database server. If you're running both on one machine, leave it be.
STATBUS_DBPORT="3306"         //The port of your database server.
STATBUS_DBNAME="feedback"     //This is the name of the database, you likely won't need to change it.
```

# Contributing
Any help is welcome, your best bet is reaching out to me first on [this](https://discord.gg/2dFpfNE) Discord to talk about the feature you want to implement or to provide details about a bug.