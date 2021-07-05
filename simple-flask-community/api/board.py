from flask import Blueprint, render_template

bp = Blueprint('board', __name__)

@bp.route("/board")
@bp.route("/board/<int:page>")
def board_page(page=1):
	return render_template('board.html')
