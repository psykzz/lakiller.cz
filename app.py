from flask import Flask, render_template, request, abort
import src.base
import src.poll

app = Flask(__name__)
statbus = src.base.Statbus()

@app.route("/")
def index():
	 return render_template('index.tpl', cursor = statbus.cursor)


@app.route("/poll")
def poll():
	if not statbus.is_connected():
		abort(500)
	offset = request.args.get('offset', '')
	return render_template('poll.tpl', cursor = statbus.cursor, offset = offset, poll = src.poll)


@app.route("/poll/<int:pollid>")
def pollid(pollid = None):
	if not statbus.is_connected():
		abort(500)
	return render_template('pollid.tpl', cursor = statbus.cursor, pollid = pollid, poll = src.poll)


@app.errorhandler(500)
def internal_error(error):
	statbus.try_reconnect()
	return render_template('error.tpl'), 500


if __name__ == "__main__":
	app.run()