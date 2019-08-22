from playhouse.mysql_ext import MySQLConnectorDatabase
from playhouse.flask_utils import FlaskDB
from dotenv import load_dotenv
from os import getenv
from peewee import *


class Database():
	app = None
	db = None
	wrapper = FlaskDB()


	def __init__(self, app):
		load_dotenv()
		self.app = app


	def connect(self):
		dbusername = getenv("STATBUS_DBUSERNAME")
		dbpassword = getenv("STATBUS_DBPASSWORD")
		dbhost = getenv("STATBUS_DBHOST")
		dbport = getenv("STATBUS_DBPORT")
		dbname = getenv("STATBUS_DBNAME")

		try:
			self.db = MySQLConnectorDatabase(database = dbname, host = dbhost, port = dbport, user = dbusername, passwd = dbpassword)
			self.wrapper = FlaskDB(self.app, self.db)
		except Exception as e:
			self.db = None
			self.wrapper = None
			return e

		return True


	def disconnect(self):
		if self.db:
			self.db.close()

		self.db = None
		self.wrapper = None


class DatabaseError(Exception):
	pass


class Poll_option(Database.wrapper.Model):
	id = IntegerField(unique = True)
	pollid = IntegerField()
	text = CharField()
	minval = IntegerField(null = True)
	maxval = IntegerField(null = True)
	descmin = CharField(null = True)
	descmid = CharField(null = True)
	descmax = CharField(null = True)
	default_percentage_calc = IntegerField(default = 1)


class Poll_question(Database.wrapper.Model):
	id = IntegerField(unique = True)
	polltype = CharField()
	starttime = DateTimeField()
	endtime = DateTimeField()
	question = CharField()
	adminonly = IntegerField()
	multiplechoiceoptions = IntegerField(null = True)
	createdby_ckey = CharField(max_length = 32, null = True)
	createdby_ip = IntegerField()
	dontshow = IntegerField()


class Poll_textreply(Database.wrapper.Model):
	id = IntegerField(unique = True)
	datetime = DateTimeField()
	pollid = IntegerField()
	ckey = CharField(max_length = 32)
	ip = IntegerField()
	replytext = CharField(max_length = 2048)
	adminrank = CharField(max_length = 32, default = "Player")


class Poll_vote(Database.wrapper.Model):
	id = IntegerField(unique = True)
	datetime = DateTimeField()
	pollid = IntegerField()
	optionid = IntegerField()
	ckey = CharField(max_length = 32)
	ip = IntegerField()
	adminrank = CharField(max_length = 32, default = "Player")
	rating = IntegerField(null = True)