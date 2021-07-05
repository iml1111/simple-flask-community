"""
DB 접근을 총괄하는 클래스
"""
import sqlite3

DB_PATH = "./data.db"

class Database:

	def __init__(self):
		"""객체가 생성될 때, 실행"""
		self.conn = sqlite3.connect(DB_PATH)

	def get_all_posts(self):
		"""모든 포스트 리스트 반환"""
		cur = self.conn.cursor()
		cur.execute('SELECT * FROM posts')
		result = cur.fetchall()
		return result


	def __del__(self):
		"""객체가 소멸할 때, 실행"""
		self.conn.close()


