from flask import Blueprint, render_template, request
from statbus.database import Poll_question, Poll_option, Poll_vote, Poll_textreply

bp = Blueprint("polls", __name__)


@bp.route("/poll")
def pollmain():
	offset = request.args.get("offset", 0, int)
	
	polls = (
		Poll_question.select(
			Poll_question.id,
			Poll_question.question,
			Poll_question.adminonly,
			Poll_question.dontshow,
		)
		.limit(50)
		.offset(offset)
	)

	valid_polls = [poll for poll in polls if poll.id_hidden()]
	return render_template("polls/polls.html", offset = offset, polls = valid_polls)


@bp.route("/poll/<int:poll_id>")
def view_poll(poll_id):
	poll = Poll_question.select().where(Poll_question.id == poll_id).first()
	if not poll or poll.is_hidden():
		abort(404)

	if poll.polltype == "OPTION":
		options = Poll_option.select(Poll_option.text).where(
			Poll_option.pollid == pollid
		)
		votes_by_option = (
			Poll_vote.select(Poll_vote.optionid, fn.Count(Poll_vote.id).alias("votes"))
			.where(Poll_vote.pollid == pollid, Poll_vote.optionid._in([1, 2]))
			.group_by(Poll_vote.optionid)
			.dicts()
		)

		return render_template("polls/detail_option.html", options = options, votes = votes_by_option)

	elif poll.polltype == "TEXT":
		return render_template("polls/detail_text.html", poll = poll)
	
	elif poll.polltype == "NUMVAL":
		return render_template("polls/detail_numval.html", poll = poll)
	
	elif poll.polltype == "MULTICHOICE":
		return render_template("polls/detail_multichoice.html", poll = poll)
	
	elif poll.polltype == "IRV":
		return render_template("polls/detail_irv.html", poll = poll)

	return abort(404)