from datetime import datetime
from src.base import Statbus

class Poll():
	statbus = None
	cursor = None


	def __init__(self):
		self.statbus = Statbus()
		self.cursor = self.statbus.cursor


	def get_valid_polls(self, offset):
		try: 
			offset = int(offset)
		except:
			offset = 0
		self.cursor.execute("SELECT id, question, adminonly, dontshow FROM poll_question LIMIT 50 OFFSET " + str(offset))
		result = self.cursor.fetchall()
		dat = "<ul class='left'>"
		for pollid, question, adminonly, dontshow in result:
			if adminonly == 1 or dontshow == 1:
				continue
			dat += f"<li>Poll {pollid} {question} | <a href='/poll/{pollid}'>View</a></li>"
		dat += "</ul>"

		return dat


	def handle_polltype(self, pollid):
		pollid = str(pollid)
		self.cursor.execute('SELECT * FROM poll_question WHERE id = ' + pollid)
		result = self.cursor.fetchall()
		x = result[0]

		if x[5] == 1 or x[9] == 1:
			return "<p>Access Denied</p>"

		dat = f"""
	<p>Question: {x[4]}</p>
	<p>Type: {x[1]}</p>
	<p>Start time: {x[2].strftime('%d %B %Y - %H:%M:%S')}</p>
	<p>End time: {x[3].strftime('%d %B %Y - %H:%M:%S')}</p>
		"""

		if x[1] == "OPTION":
			dat += poll_option(pollid)
		elif x[1] == "TEXT":
			dat += poll_text(pollid)
		elif x[1] == "NUMVAL":
			dat += poll_numval(pollid)
		elif x[1] == "MULTICHOICE":
			dat += poll_multichoice(pollid)
		elif x[1] == "IRV":
			dat += poll_irv(pollid)

		return dat


	def poll_option(self, pollid):
		dat = "<p><b>Options:</b></p>"
		self.cursor.execute('SELECT text FROM poll_option WHERE pollid = ' + pollid)
		result = self.cursor.fetchall()
		self.cursor.execute('SELECT COUNT(*) FROM poll_vote WHERE pollid = ' + pollid + ' AND optionid = 1')
		first = self.cursor.fetchall()
		self.cursor.execute('SELECT COUNT(*) FROM poll_vote WHERE pollid = ' + pollid + ' AND optionid = 2')
		second = self.cursor.fetchall()
		dat += f"<p>1. {result[0][0]}: {first[0][0]}</p>"
		dat += f"<p>2. {result[1][0]}: {second[0][0]}</p>"

		return dat


	def poll_text(self, pollid):
		self.cursor.execute('SELECT replytext FROM poll_textreply WHERE pollid = ' + pollid)
		result = self.cursor.fetchall()
		dat = "<p><b>Replies:</b></p>"
		for z in range(len(result)):
			dat += f"<p><b>{z}:</b> {result[z][0]}</p>"

		return dat


	def poll_numval(self, pollid):
		self.cursor.execute('SELECT * FROM poll_option WHERE pollid = ' + pollid)
		result = self.cursor.fetchall()
		dat = f"""
	<p><b>Options:</b></p>
	<p>Poll description: {result[0][2]}</p>
	<p>Minimum rating description: {result[0][5]}</p>
	<p>Middle rating description: {result[0][6]}</p>
	<p>Maximum rating description: {result[0][7]}</p>
	<p>Minimum rating: {result[0][3]}</p>
	<p>Maximum rating: {result[0][4]}</p>
	<p><b>Votes:</b></p>
	"""
		for x in range(result[0][4] + 1):
			self.cursor.execute('SELECT COUNT(*) FROM poll_vote WHERE pollid = ' + pollid + ' AND rating = ' + str(x))
			result = self.cursor.fetchall()
			dat += f"<p>Rating {x}: {result[0][0]}</p>"

		return dat


	def poll_multichoice(self, pollid):
		return "<p>This type of poll is currently not implemented.</p>"


	def poll_irv(self, pollid):
		return "<p>This type of poll is currently not implemented.</p>"