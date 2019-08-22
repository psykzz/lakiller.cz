from flask import Flask, render_template, request, abort
import src.base
import src.poll


app = Flask(__name__)
database = src.base.Database(app)
poll = src.poll.Poll()


@app.route("/")
def index():
	return render_template('index.tpl')


@app.route("/poll")
def pollmain():
	offset = request.args.get('offset', '')
	return render_template('poll.tpl', offset = offset, poll = poll)


@app.route("/poll/<int:pollid>")
def pollid(pollid = None):
	return render_template('pollid.tpl', pollid = pollid, poll = poll)


@app.before_request
def before_request_func():
	if database.connect() != True:
		raise src.base.DatabaseError


@app.after_request
def after_request_func(response):
	database.disconnect()
	return response


@app.errorhandler(src.base.DatabaseError)
def dberror(error):
	result = database.connect()
	return render_template('dberror.tpl', message = result), 500


@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
def internal_error(e):
	return render_template('error.tpl', error = e), e.code


if __name__ == "__main__":
	app.run()