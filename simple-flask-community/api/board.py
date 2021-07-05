from flask import Blueprint, render_template, request, redirect
from model import Database

bp = Blueprint('board', __name__)


@bp.route("/board")
@bp.route("/board/<int:page>")
def board_page(page=1):
	db = Database()
	posts = db.get_posts(page)
	return render_template('board.html', posts=posts)


@bp.route('/form', methods=['GET', 'POST'])
def form_page():
	
	if request.method == 'GET':
		return render_template('form.html')
	
	name = request.form['name']
	title = request.form['title']
	content = request.form['content']

	db = Database()
	db.insert_post(name, title, content)

	return redirect('/board')
