"""
DB 접근을 총괄하는 클래스
"""
import sqlite3
from datetime import datetime

DB_PATH = "./data.db"

class Database:

	def __init__(self):
		"""객체가 생성될 때, 실행"""
		self.conn = sqlite3.connect(DB_PATH, isolation_level=None)

	def get_posts(self, page=1):
		"""해당 페이지의 포스트 리스트 반환"""
		cur = self.conn.cursor()
		cur.execute(
			'''
			SELECT * FROM post
			ORDER BY updated_at DESC
			LIMIT ?, ?
			''', 
			((page - 1) * 10, 10)
		)
		return cur.fetchall()

	def insert_post(self, name, title, content):
		"""포스트 등록"""
		cur = self.conn.cursor()
		now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		cur.execute(
			"""
			INSERT INTO post (name, title, content, updated_at) 
			VALUES (?, ?, ?, ?)
			""",
			(name, title, content, now_date)
		)
		self.conn.commit()

	def __del__(self):
		"""객체가 소멸할 때, 실행"""
		self.conn.close()


def initialize_db():
	"""DB 초기화 함수, 웹 서버 실행전에 확인"""
	conn = sqlite3.connect(DB_PATH, isolation_level=None)
	cur = conn.cursor()
	cur.execute('''
		CREATE TABLE IF NOT EXISTS post
		(
			id INTEGER PRIMARY KEY AUTOINCREMENT, 
			name TEXT, 
			title TEXT, 
			content TEXT, 
			updated_at TEXT
		)
	''')
	# cur.execute(
	# 	"INSERT INTO post (name, title, content, updated_at) VALUES ('BUY','RHAT','RHAT', 'RHAT')")
	conn.close()


