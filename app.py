from bottle import default_app, run, route, template, static_file
import src.base
import src.poll

cursor = src.base.cursor

@route("/")
def index(cursor = cursor):
	 return template('template/index', cursor = cursor)


@route("/poll", method = "GET")
def poll():
	global cursor

	if not src.base.handle_connection():
		return src.base.connection_error()

	offset = request.query.offset

	try:
		offset = int(offset)
		return template('template/poll', cursor = cursor, offset = offset)
	except:
		return template('template/poll', cursor = cursor, offset = 0)


@route("/poll/<pollid:int>")
def pollid(pollid = None):
	global cursor

	if not src.base.handle_connection():
		return src.base.connection_error()

	return template('template/pollid', cursor = cursor, pollid = pollid)


@route('/static/<filename:path>')
def send_static(filename):
	return static_file(filename, root = 'static/')


src.base.try_connect()


if __name__ == "__main__":
	run(host = 'localhost', port = 8080)

else:
	application = default_app()