from playhouse.mysql_ext import MySQLConnectorDatabase
from playhouse.flask_utils import FlaskDB
from dotenv import load_dotenv
from os import getenv
from peewee import *


load_dotenv()
dbusername = getenv("STATBUS_DBUSERNAME")
dbpassword = getenv("STATBUS_DBPASSWORD")
dbhost = getenv("STATBUS_DBHOST")
dbport = getenv("STATBUS_DBPORT")
dbname = getenv("STATBUS_DBNAME")

try:
	db = MySQLConnectorDatabase(database = dbname, host = dbhost, port = dbport, user = dbusername, passwd = dbpassword)
except:
	pass


db_wrapper = FlaskDB(None, db)


class Poll_option(db_wrapper.Model):
	id = IntegerField(unique = True)
	pollid = IntegerField()
	text = CharField()
	minval = IntegerField(null = True)
	maxval = IntegerField(null = True)
	descmin = CharField(null = True)
	descmid = CharField(null = True)
	descmax = CharField(null = True)
	default_percentage_calc = IntegerField(default = 1)


class Poll_question(db_wrapper.Model):
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

	def is_shown(self):
		return adminonly or dontshow

	def basic_link(self):
		return f"<li>Poll {self.id} {self.question} | <a href='/poll/{self.pollid}'>View</a></li>"


class Poll_textreply(db_wrapper.Model):
	id = IntegerField(unique = True)
	datetime = DateTimeField()
	pollid = IntegerField()
	ckey = CharField(max_length = 32)
	ip = IntegerField()
	replytext = CharField(max_length = 2048)
	adminrank = CharField(max_length = 32, default = "Player")


class Poll_vote(db_wrapper.Model):
	id = IntegerField(unique = True)
	datetime = DateTimeField()
	pollid = IntegerField()
	optionid = IntegerField()
	ckey = CharField(max_length = 32)
	ip = IntegerField()
	adminrank = CharField(max_length = 32, default = "Player")
	rating = IntegerField(null = True)