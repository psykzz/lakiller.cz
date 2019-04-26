from bottle import route, run, request, static_file, template, default_app
import configparser
import mysql.connector
from os import path

config = configparser.ConfigParser()

if path.isfile('production.ini'):
	config.read('production.ini')
else:
	config.read('config.ini')

dbconfig = config['Database']

dbusername = dbconfig['dbusername']
dbpassword = dbconfig['dbpassword']
dbhost = dbconfig['dbhost']
dbport = dbconfig['dbport']
dbname = dbconfig['dbname']

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

	try:
		database = mysql.connector.connect(user = dbusername, password = dbpassword, host = dbhost, port = dbport, database = dbname)
		cursor = database.cursor(buffered = True)
	
	except:
		pass


def connection_error():
	return template('template/error')



@route("/")
def index(cursor = cursor):
	 return template('template/index', cursor = cursor)


@route("/poll", method = "GET")
def poll():
	global cursor

	if not handle_connection():
		return connection_error()

	offset = request.query.offset

	try:
		offset = int(offset)
		return template('template/poll', cursor = cursor, offset = offset)
	except:
		return template('template/poll', cursor = cursor, offset = 0)


@route("/poll/<pollid:int>")
def pollid(pollid = None):
	global cursor

	if not handle_connection():
		return connection_error()

	return template('template/pollid', cursor = cursor, pollid = pollid)


@route('/static/<filename:path>')
def send_static(filename):
	return static_file(filename, root='static/')


try_connect()


if __name__ == "__main__":
	run(host = 'localhost', port = 8080)

else:
	application = default_app()