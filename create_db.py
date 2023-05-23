#  initialize your database.
from server import db, app

with app.app_context():
    db.create_all()
