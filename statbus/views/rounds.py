from flask import Blueprint, render_template, request
from statbus.database import Round


bp = Blueprint("rounds", __name__)


@bp.route("/round")
def roundmain():
    offset = request.args.get("offset", 0, int)

    rounds = (
        Round.select(Round.id, Round.game_mode, Round.game_mode_result, Round.map_name)
        .limit(25)
        .offset(offset)
    )

    return render_template("rounds/rounds.html", offset=offset, rounds=rounds)
