from flask import Blueprint, render_template, request
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
	)

	pages = PaginatedQuery(rounds, 30, "page")
	
	return render_template("rounds/rounds.html", pages = pages)