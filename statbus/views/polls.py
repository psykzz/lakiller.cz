from flask import Blueprint, render_template, request
from flask_caching import Cache
from playhouse.flask_utils import FlaskDB

from statbus.database import db_wrapper
from statbus import poll


bp = Blueprint("polls", __name__)


@bp.route("/poll")
def pollmain():
	offset = request.args.get('offset', '', int)
	valid_polls = poll.get_valid_polls(offset)
	return render_template('polls/polls.html', offset=offset, valid_polls=valid_polls)


@bp.route("/poll/<int:poll_id>")
def pollid(poll_id = 0):
	poll = Poll_question.select().where(Poll_question.id == pollid).first()
	if not poll or poll.is_hidden():
		abort(404)

	if poll.polltype == "OPTION":	
		options = Poll_option.select(Poll_option.text).where(Poll_option.pollid == pollid)
		votes_by_option = Poll_vote.select(
				Poll_vote.optionid,
				fn.Count(Poll_vote.id).alias('votes'),
			).where(
				Poll_vote.pollid == pollid, 
				Poll_vote.optionid._in([1, 2])
			).group_by(Poll_vote.optionid).dicts()

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
