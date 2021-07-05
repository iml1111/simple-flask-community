from flask import Blueprint, render_template

bp = Blueprint('index', __name__)


@bp.route("/")
def index_page():
	return render_template('index.html')