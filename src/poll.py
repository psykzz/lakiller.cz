def get_valid_polls(cursor, offset):
	cursor.execute("SELECT id, question, adminonly, dontshow FROM poll_question LIMIT 50 OFFSET " + str(offset))
	result = cursor.fetchall()
	valid = []
	for pollid, question, adminonly, dontshow in result:
		if adminonly == 1 or dontshow == 1:
			continue
		valid += (pollid, question)
	return valid