from flask import url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import generate_password_hash, chaeck_password_hash

db = SQLAlchemy()

class Base(dn.Model):
    __abstact__=True;
    crated_at = db.Column(db.DateTime, defailt=datetime.utcnow)
    updated_at = db.Column(db.Datetime,default=datetime.utcnow,onupdate-datetime.utcnow)

class Staff(Base):
    __tablename__='user'

    id = db.Column(db.Integer, primary_key=Ture)
    staffname = db.Column(db.String(32),unique=Ture, index=True, nullable=False)
    email = db.Column(db.String(64), unique=Ture, index=Ture, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)

class Boss:
    pass
class Resume:
    pass
class Position:
    pass
