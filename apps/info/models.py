from datetime import datetime
from apps.app import db
from sqlalchemy import Column, Integer, String, Date

class Fish(db.Model):
  __tablename__='fish'

  id = db.Column(db.Integer, primary_key=True)
  fishname = db.Column(db.String, index=True)
  season = db.Column(db.Integer, index=True)
  etc = db.Column(db.String, index=True)
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate= datetime.now)
