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

database = mysql.connector.connect(user = dbusername, password = dbpassword, host = dbhost, port = dbport, database = dbname)

cursor = database.cursor(buffered = True)


@route("/")
def index(cursor = cursor):
	 return template('template/index', cursor = cursor)


@route("/poll", method = "GET")
def poll(cursor = cursor):
	offset = request.query.offset
	try:
		offset = int(offset)
		return template('template/poll', cursor = cursor, offset = offset)
	except:
		return template('template/poll', cursor = cursor, offset = 0)

@route("/poll/<pollid:int>")
def pollid(cursor = cursor, pollid = None):
	return template('template/pollid', cursor = cursor, pollid = pollid)


@route('/static/<filename:path>')
def send_static(filename):
	return static_file(filename, root='static/')


if __name__ == "__main__":
	run(host = 'localhost', port = 8080)

else:
	application = default_app()