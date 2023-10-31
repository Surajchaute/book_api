from bkconfig import *

class Bookstore(db.Model):
    id = db.Column('book_id',db.Integer(),primary_key=True)
    title = db.Column('book_title', db.String(100))
    author = db.Column('book_author', db.String(30))
    published_date = db.Column('book_published_date', db.Date())
    price = db.Column('book_price', db.Integer())



with app.app_context():
    db.create_all()
    print('Tables are created into database -- bookdb')

