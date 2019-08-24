from flask import Flask, render_template, request
from flask_caching import Cache
from playhouse.flask_utils import FlaskDB
from .database import db_wrapper
from . import poll



'''
App Setup
'''
app = Flask(__name__)
cache = Cache(app)
db_wrapper.init_app(app)



'''
Frontpage routes
'''
@app.route("/")
@cache.cached(timeout = 50)
def index():
	return render_template('index.html')



'''
Poll routes
'''
@app.route("/poll")
def pollmain():
	offset = request.args.get('offset', '', int)
	valid_polls = poll.get_valid_polls(offset)
	return render_template('polls/polls.html', offset=offset, valid_polls=valid_polls)


@app.route("/poll/<int:poll_id>")
def pollid(poll_id = 0):
	poll = Poll_question.select().where(Poll_question.id == pollid).first()
	if not poll or poll.is_hidden():
		abort(404)

	if poll.polltype == "OPTION":	
		options = Poll_option.select(Poll_option.text).where(Poll_option.pollid == pollid)
		votes_by_option = Poll_vote
			.select(
				Poll_vote.optionid,
				fn.Count(Poll_vote.id).alias('votes'),
			).where(
				Poll_vote.pollid == pollid, 
				Poll_vote.optionid._in([1, 2])
			).group_by(Poll_vote.optionid)
			.dicts()

		return render_template('polls/detail_option.html', options=options, votes=votes_by_option)


	elif poll.polltype == "TEXT":
		return render_template('polls/detail_text.html', poll=poll)
	elif poll.polltype == "NUMVAL":
		return render_template('polls/detail_numval.html', poll=poll)
	elif poll.polltype == "MULTICHOICE":
		return render_template('polls/detail_multichoice.html', poll=poll)
	elif poll.polltype == "IRV":
		return render_template('polls/detail_irv.html', poll=poll)

	return abort(404)



'''
Error handlers
'''
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
def internal_error(e):
	return render_template('error.html', error = e), e.code