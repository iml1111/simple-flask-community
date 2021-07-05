from flask import Blueprint, render_template
from model import Database

bp = Blueprint('index', __name__)


@bp.route("/")
def index_page():
	db = Database()
	posts = db.get_posts(1)[:3]
	return render_template('index.html', posts=posts)