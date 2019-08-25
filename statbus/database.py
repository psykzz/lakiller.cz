from playhouse.mysql_ext import MySQLConnectorDatabase
from playhouse.flask_utils import FlaskDB
from peewee import *

# Setup the mysql connection and flaskdb wrapper.
db_wrapper = FlaskDB()


# Meta model all models should parent from
class DBModel(db_wrapper.Model):
	pass


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

	def is_hidden(self):
		return self.adminonly or self.dontshow


class Poll_textreply(DBModel):
	id = IntegerField(unique = True)
	datetime = DateTimeField()
	pollid = IntegerField()
	ckey = CharField(max_length = 32)
	ip = IntegerField()
	replytext = CharField(max_length = 2048)
	adminrank = CharField(max_length = 32, default ="Player")


class Poll_vote(DBModel):
	id = IntegerField(unique = True)
	datetime = DateTimeField()
	pollid = IntegerField()
	optionid = IntegerField()
	ckey = CharField(max_length = 32)
	ip = IntegerField()
	adminrank = CharField(max_length = 32, default = "Player")
	rating = IntegerField(null = True)


class Round(DBModel):
	id = IntegerField(unique = True)
	initialize_datetime = DateTimeField()
	start_datetime = DateTimeField(null = True)
	shutdown_datetime = DateTimeField(null = True)
	end_datetime = DateTimeField(null = True)
	server_ip = IntegerField()
	server_port = SmallIntegerField()
	commit_hash = CharField(max_length = 40, null = True)
	game_mode = CharField(max_length = 32, null = True)
	game_mode_result = CharField(max_length = 64, null = True)
	end_state = CharField(max_length = 64, null = True)
	map_name = CharField(max_length = 32, null = True)