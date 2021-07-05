from flask import Blueprint, render_template
from model import Database

bp = Blueprint('index', __name__)


@bp.route("/")
def index_page():
	db = Database()
	data = db.get_posts(1)
	print(data)
	return render_template('index.html')