from flask import Flask, render_template, request, abort
from playhouse.flask_utils import FlaskDB
from .database import db_wrapper
from .poll import Poll


app = Flask(__name__)
db_wrapper.init_app(app)
poll = Poll()


@app.route("/")
def index():
	return render_template('index.tpl')


@app.route("/poll")
def pollmain():
	offset = request.args.get('offset', '', int)
	return render_template('poll.tpl', offset = offset, poll = poll)


@app.route("/poll/<int:pollid>")
def pollid(pollid = 0):
	return render_template('pollid.tpl', pollid = pollid, poll = poll)


@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
def internal_error(e):
	return render_template('error.tpl', error = e), e.code