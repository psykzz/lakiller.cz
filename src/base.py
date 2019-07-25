from mysql.connector import connect, cursor
from configparser import ConfigParser
from bottle import template
from os import path

class Statbus():
	database = None
	cursor = None


	def __init__(self):
		self.try_connect()


	def try_connect(self):
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
			self.database = connect(user = dbusername, password = dbpassword, host = dbhost, port = dbport, database = dbname)
			self.cursor = self.database.cursor(buffered = True)
			return True
		except:
			return False

      
	def handle_connection(self):
		if self.database is None:
			self.try_connect()

		if self.database is None:
			return False

		status = self.database.is_connected()
		if status:
			return True
		else:
			try_connect()

		status = self.database.is_connected()
		if status:
			return True
		else:
			return False
 

	def connection_error(self):
		return self.generate_template(template('template/error'))


	def generate_template(self, templ):
		return template('template/header') + templ + template('template/footer')