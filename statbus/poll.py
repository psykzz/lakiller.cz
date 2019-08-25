from statbus.app import cache
from .database import Poll_question, Poll_option, Poll_vote, Poll_textreply


@cache.memoize(timeout=60)
def get_valid_polls(self, offset):
    if not offset:
        offset = 0

    data = (
        Poll_question.select(
            Poll_question.id,
            Poll_question.question,
            Poll_question.adminonly,
            Poll_question.dontshow,
        )
        .limit(50)
        .offset(offset)
    )

    html = "<ul>"

    for poll in data:
        if poll.is_hidden():
            continue
        html += poll.basic_link()

    html += "</ul>"

    return html


@cache.memoize(timeout=60)
def handle_polltype(self, pollid):
    data = Poll_question.select().where(Poll_question.id == pollid).first()

    if data.polltype == "OPTION":
        return poll_option(data)

    elif data.polltype == "TEXT":
        return poll_text(data)

    elif data.polltype == "NUMVAL":
        return poll_numval(data)

    elif data.polltype == "MULTICHOICE":
        return poll_multichoice(data)

    elif data.polltype == "IRV":
        return poll_irv(data)


@cache.memoize(timeout=60)
def poll_option(self, data):
    pollid = data.pollid

    html = "<p><b>Options:</b></p>"

    onedesc = (
        Poll_option.select(Poll_option.text).where(Poll_option.pollid == pollid).first()
    )
    twodesc = (
        Poll_option.select(Poll_option.text)
        .where(Poll_option.pollid == pollid)
        .second()
    )

    onevotes = (
        Poll_vote.select()
        .where(Poll_vote.pollid == pollid and Poll_vote.optionid == 1)
        .count()
        .first()
    )
    twovotes = (
        Poll_vote.select()
        .where(Poll_vote.pollid == pollid and Poll_vote.optionid == 2)
        .count()
        .first()
    )

    html += f"<p>1. {onedesc}: {onevotes}</p>"
    html += f"<p>2. {twodesc}: {twovotes}</p>"

    return html


@cache.memoize(timeout=60)
def poll_text(self, data):
    pollid = data.pollid

    replies = (
        Poll_textreply.select(Poll_textreply.replytext)
        .where(Poll_textreply.pollid == pollid)
        .get()
    )

    html = "<p><b>Replies:</b></p>"
    for z in range(len(replies)):
        dat += f"<p><b>{z}:</b> {replies[z][0]}</p>"

    return dat


def poll_numval(self, data):
    pollid = data.pollid

    numval = Poll_option.select().where(Poll_option.pollid == pollid).first()

    html = ""


"""
<p><b>Options:</b></p>
<p>Poll description: {result[0][2]}</p>
<p>Minimum rating description: {result[0][5]}</p>
<p>Middle rating description: {result[0][6]}</p>
<p>Maximum rating description: {result[0][7]}</p>
<p>Minimum rating: {result[0][3]}</p>
<p>Maximum rating: {result[0][4]}</p>
<p><b>Votes:</b></p>

	for x in range(result[0][4] + 1):
		self.cursor.execute('SELECT COUNT(*) FROM poll_vote WHERE pollid = ' + pollid + ' AND rating = ' + str(x))
		result = self.cursor.fetchall()
		dat += f"<p>Rating {x}: {result[0][0]}</p>"

	return dat
"""


def poll_multichoice(self, data):
    return "<p>This type of poll is currently not implemented.</p>"


def poll_irv(self, data):
    return "<p>This type of poll is currently not implemented.</p>"
