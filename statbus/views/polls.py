from flask import Blueprint, render_template, request, abort
from playhouse.flask_utils import PaginatedQuery
from statbus.database import Poll_question, Poll_option, Poll_vote, Poll_textreply
from peewee import fn, JOIN
from datetime import datetime

bp = Blueprint("polls", __name__)


@bp.route("/poll")
def pollmain():	
	polls = (
		Poll_question.select(
			Poll_question.id,
			Poll_question.question,
			Poll_question.adminonly,
			Poll_question.dontshow,
		)
		.where(Poll_question.adminonly == False, Poll_question.dontshow == False)
	)

	pages = PaginatedQuery(polls, 25, "page")
	
	return render_template("polls/polls.html", pages = pages)


@bp.route("/poll/<int:poll_id>")
def pollid(poll_id):
	poll = Poll_question.select().where(Poll_question.id == poll_id).first()
	if not poll or poll.is_hidden():
		abort(404)

	if poll.polltype == "OPTION":
		votes = (
				Poll_option.select(
					Poll_option.text,
					fn.Count(Poll_vote.id).alias("votes")
				)
				.join(Poll_vote, JOIN.LEFT_OUTER, on = (Poll_option.id == Poll_vote.optionid))
				.where(Poll_vote.pollid == poll_id)
				.group_by(Poll_option.text)
				.order_by(Poll_vote.optionid)
			)

		total = sum([x.votes for x in votes])
		percentages = ["{0:.2f}".format((int(x.votes) / total) * 100) for x in votes]
		
		return render_template("polls/detail_option.html", poll = poll, votes = votes, percentages = percentages, datetime = datetime)

	elif poll.polltype == "TEXT":
		return render_template("polls/detail_text.html", poll = poll)
	
	elif poll.polltype == "NUMVAL":
		return render_template("polls/detail_numval.html", poll = poll)
	
	elif poll.polltype == "MULTICHOICE":
		return render_template("polls/detail_multichoice.html", poll = poll)
	
	elif poll.polltype == "IRV":
		return render_template("polls/detail_irv.html", poll = poll)

	return abort(404)