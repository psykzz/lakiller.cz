from bottle import default_app, run, route, template, static_file, request
import src.base

statbus = src.base.Statbus()

@route("/")
def index():
	 return statbus.generate_template(template('template/index', cursor = statbus.cursor))


@route("/poll", method = "GET")
def poll():
	if not statbus.handle_connection():
		return statbus.connection_error()

	offset = request.query.offset

	return statbus.generate_template(template('template/poll', cursor = statbus.cursor, offset = offset))


@route("/poll/<pollid:int>")
def pollid(pollid = None):
	if not statbus.handle_connection():
		return statbus.connection_error()

	return statbus.generate_template(template('template/pollid', cursor = statbus.cursor, pollid = pollid))


@route('/static/<filename:path>')
def send_static(filename):
	return static_file(filename, root = 'static/')


if __name__ == "__main__":
	run(host = 'localhost', port = 8080)

else:
	application = default_app()