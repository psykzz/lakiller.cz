from bottle import default_app, run, route, template, static_file, request
import src.base

database = None
cursor = None

@route("/")
def index(cursor = cursor):
	 return src.base.generate_template(template('template/index', cursor = cursor))


@route("/poll", method = "GET")
def poll():
	global cursor

	if not src.base.handle_connection():
		return src.base.connection_error()

	offset = request.query.offset

	return src.base.generate_template(template('template/poll', cursor = cursor, offset = offset))


@route("/poll/<pollid:int>")
def pollid(pollid = None):
	global cursor

	if not src.base.handle_connection():
		return src.base.connection_error()

	return src.base.generate_template(template('template/pollid', cursor = cursor, pollid = pollid))


@route('/static/<filename:path>')
def send_static(filename):
	return static_file(filename, root = 'static/')


src.base.try_connect()


database = src.base.database
cursor = src.base.cursor


if __name__ == "__main__":
	run(host = 'localhost', port = 8080)

else:
	application = default_app()