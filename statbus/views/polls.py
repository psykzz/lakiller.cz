from flask import Blueprint, render_template, request
from statbus.database import Poll_question, Poll_option, Poll_vote, Poll_textreply
from peewee import fn, JOIN

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
		.where(Poll_question.adminonly == False and Poll_question.dontshow == False)
		.limit(50)
		.offset(offset)
	)
	
	return render_template("polls/polls.html", offset = offset, polls = polls)


@bp.route("/poll/<int:poll_id>")
def pollid(poll_id):
	poll = Poll_question.select().where(Poll_question.id == poll_id).first()
	if not poll or not poll_id or poll.is_hidden():
		abort(404)

	if poll.polltype == "OPTION":
		votes = (
				Poll_option.select(
					Poll_option.text,
					fn.Count(Poll_vote.id).alias("votes")
				)
				.join(Poll_vote, JOIN.LEFT_OUTER, on = (Poll_option.id == Poll_vote.optionid))
				.group_by(Poll_option.text)
				.order_by(Poll_vote.optionid)
			)

		total = sum([x.votes for x in votes])
		percentages = [(int(x.votes) / total) * 100 for x in votes]
		
		return render_template("polls/detail_option.html", poll = poll, votes = votes, percentages = percentages)

	elif poll.polltype == "TEXT":
		return render_template("polls/detail_text.html", poll = poll)
	
	elif poll.polltype == "NUMVAL":
		return render_template("polls/detail_numval.html", poll = poll)
	
	elif poll.polltype == "MULTICHOICE":
		return render_template("polls/detail_multichoice.html", poll = poll)
	
	elif poll.polltype == "IRV":
		return render_template("polls/detail_irv.html", poll = poll)

	return abort(404)