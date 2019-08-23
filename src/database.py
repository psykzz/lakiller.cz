from dotenv import load_dotenv
load_dotenv()

from os import getenv

from playhouse.mysql_ext import MySQLConnectorDatabase
from playhouse.flask_utils import FlaskDB

from peewee import *

dbusername = getenv("STATBUS_DBUSERNAME")
dbpassword = getenv("STATBUS_DBPASSWORD")
dbhost = getenv("STATBUS_DBHOST")
dbport = getenv("STATBUS_DBPORT")
dbname = getenv("STATBUS_DBNAME")

db = MySQLConnectorDatabase(database = dbname, host = dbhost, port = dbport, user = dbusername, passwd = dbpassword)
db_wrapper = FlaskDB(None, db)


class DBModel(db_wrapper.Model):
	class Meta:
		database = db


class Poll_option(DBModel):
	id = IntegerField(unique = True)
	pollid = IntegerField()
	text = CharField()
	minval = IntegerField(null = True)
	maxval = IntegerField(null = True)
	descmin = CharField(null = True)
	descmid = CharField(null = True)
	descmax = CharField(null = True)
	default_percentage_calc = IntegerField(default = 1)


class Poll_question(DBModel):
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


class Poll_textreply(DBModel):
	id = IntegerField(unique = True)
	datetime = DateTimeField()
	pollid = IntegerField()
	ckey = CharField(max_length = 32)
	ip = IntegerField()
	replytext = CharField(max_length = 2048)
	adminrank = CharField(max_length = 32, default = "Player")


class Poll_vote(DBModel):
	id = IntegerField(unique = True)
	datetime = DateTimeField()
	pollid = IntegerField()
	optionid = IntegerField()
	ckey = CharField(max_length = 32)
	ip = IntegerField()
	adminrank = CharField(max_length = 32, default = "Player")
	rating = IntegerField(null = True)
