from mysql.connector import connect, cursor
from configparser import ConfigParser
from bottle import template
from os import path

database = None
cursor = None

def handle_connection():
	global database
	global cursor

	if database is None:
		try_connect()

	if database is None:
		return False

	status = database.is_connected()
	if status:
		return True
	else:
		try_connect()

	status = database.is_connected()
	if status:
		return True
	else:
		return False
 

def try_connect():
	global database
	global cursor

	config = ConfigParser()

	if path.isfile('config/production.ini'):
		config.read('config/production.ini')
	else:
		config.read('config/config.ini')

	dbconfig = config['Database']

	dbusername = dbconfig['dbusername']
	dbpassword = dbconfig['dbpassword']
	dbhost = dbconfig['dbhost']
	dbport = dbconfig['dbport']
	dbname = dbconfig['dbname']

	try:
		database = connect(user = dbusername, password = dbpassword, host = dbhost, port = dbport, database = dbname)
		cursor = database.cursor(buffered = True)
	
	except:
		pass


def connection_error():
	return generate_template(template('template/error'))


def generate_template(templ):
	return template('template/header') + templ + template('template/footer')