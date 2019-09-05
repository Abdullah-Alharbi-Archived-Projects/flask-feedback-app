from init import db

class Feedback(db.Model):
  __tabelname__ = 'feedback'
  id = db.Column(db.Integer, primary_key=True)
  customer_name = db.Column(db.String(60))
  comments = db.Column(db.Text)
  rating = db.Column(db.Integer)

  def __init__(self, customer_name, comments, rating):
    self.customer_name = customer_name
    self.comments = comments
    self.rating = rating

  def save(self):
    db.session.add(self)
    db.session.commit()

db.create_all()
