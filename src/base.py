from mysql.connector import connect, cursor, errorcode, Error
from configparser import ConfigParser
from os import path

class DatabaseError(Exception):
    pass

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
		except Error as e:
			self.database = None
			self.cursor = None
			return e

	  
	def try_reconnect(self):
		if self.database:
			self.database.close()
			self.database = None
			self.cursor = None

		return self.try_connect()


	def is_connected(self):
		if self.database is None:
			return False

		return self.database.is_connected()