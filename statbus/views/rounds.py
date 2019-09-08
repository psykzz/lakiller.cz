from flask import Blueprint, render_template, request, abort
from playhouse.flask_utils import PaginatedQuery
from statbus.database import Round


bp = Blueprint("rounds", __name__)


@bp.route("/round")
def roundmain():	
	rounds = (
		Round.select(
			Round.id,
			Round.game_mode,
			Round.game_mode_result,
			Round.map_name,
		)
		.order_by(Round.id.desc())
	)

	pages = PaginatedQuery(rounds, 30, "page")
	
	return render_template("rounds/rounds.html", pages = pages)


@bp.route("/round/<int:round_id>")
def roundid(round_id):
	round_info = Round.select().where(Round.id == round_id).first()
	if not round_info:
		abort(404)

	return render_template("rounds/round_info.html", round_info = round_info)