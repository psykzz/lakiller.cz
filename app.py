from flask import Flask, render_template, request, abort, redirect
import src.base
import src.poll

app = Flask(__name__)
statbus = src.base.Statbus()
poll = src.poll.Poll()

@app.route("/")
def index():
	return render_template('index.tpl')


@app.route("/poll")
def pollmain():
	if not statbus.is_connected():
		raise src.base.DatabaseError
	offset = request.args.get('offset', '')
	return render_template('poll.tpl', offset = offset, poll = poll)


@app.route("/poll/<int:pollid>")
def pollid(pollid = None):
	if not statbus.is_connected():
		raise src.base.DatabaseError
	return render_template('pollid.tpl', pollid = pollid, poll = poll)


@app.errorhandler(src.base.DatabaseError)
def dberror(error):
	result = statbus.try_reconnect()
	return render_template('dberror.tpl', message = result), 500


@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
def internal_error(e):
    return render_template('error.tpl', error = e), 404


if __name__ == "__main__":
	app.run()