from .database import Poll_question, Poll_option, Poll_vote, Poll_textreply

class Poll():
	def get_valid_polls(self, offset):
		if not offset:
			offset = 0

		data = Poll_question.select(
			Poll_question.id,
			Poll_question.question,
			Poll_question.adminonly,
			Poll_question.dontshow
		).limit(50).offset(offset)

		html = "<ul>"

		for poll in data:
			if poll.is_hidden():
				continue
			html += poll.basic_link()

		html += "</ul>"

		return html


	def handle_polltype(self, pollid):
		data = Poll_question.select().where(Poll_question.id == pollid).first()

		if not data:
			return "<p>Poll not found.</p>"

		if data.is_hidden():
			return "<p>Access denied.</p>"

		if data.polltype == "OPTION":
			return self.poll_option(data)

		elif data.polltype == "TEXT":
			return self.poll_text(data)

		elif data.polltype == "NUMVAL":
			return self.poll_numval(data)

		elif data.polltype == "MULTICHOICE":
			return self.poll_multichoice(data)

		elif data.polltype == "IRV":
			return self.poll_irv(data)


	def poll_option(self, data):
		pollid = data.pollid

		html = "<p><b>Options:</b></p>"

		onedesc = Poll_option.select(Poll_option.text).where(Poll_option.pollid == pollid).first()
		twodesc = Poll_option.select(Poll_option.text).where(Poll_option.pollid == pollid).second()

		onevotes = Poll_vote.select().where(Poll_vote.pollid == pollid and Poll_vote.optionid == 1).count().first()
		twovotes = Poll_vote.select().where(Poll_vote.pollid == pollid and Poll_vote.optionid == 2).count().first()

		html += f"<p>1. {result[0][0]}: {onevotes}</p>"
		html += f"<p>2. {result[1][0]}: {twovotes}</p>"

		return html


	def poll_text(self, data):
		pollid = data.pollid

		replies = Poll_textreply.select(Poll_textreply.replytext).where(Poll_textreply.pollid == pollid).get()
		
		html = "<p><b>Replies:</b></p>"
		for z in range(len(replies)):
			dat += f"<p><b>{z}:</b> {replies[z][0]}</p>"

		return dat


	def poll_numval(self, data):
		pollid = data.pollid

		numval = Poll_option.select().where(Poll_option.pollid == pollid).first()

		html = ""
	"""
	<p><b>Options:</b></p>
	<p>Poll description: {result[0][2]}</p>
	<p>Minimum rating description: {result[0][5]}</p>
	<p>Middle rating description: {result[0][6]}</p>
	<p>Maximum rating description: {result[0][7]}</p>
	<p>Minimum rating: {result[0][3]}</p>
	<p>Maximum rating: {result[0][4]}</p>
	<p><b>Votes:</b></p>
	
		for x in range(result[0][4] + 1):
			self.cursor.execute('SELECT COUNT(*) FROM poll_vote WHERE pollid = ' + pollid + ' AND rating = ' + str(x))
			result = self.cursor.fetchall()
			dat += f"<p>Rating {x}: {result[0][0]}</p>"

		return dat
	"""


	def poll_multichoice(self, data):
		return "<p>This type of poll is currently not implemented.</p>"


	def poll_irv(self, data):
		return "<p>This type of poll is currently not implemented.</p>"