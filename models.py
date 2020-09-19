from sqlalchemy import Column, String, create_engine,Integer
from flask_sqlalchemy import SQLAlchemy
import json
import os
from flask_migrate import Migrate

database_name = "capstone1"
database_path = "postgres://laruynydptixbq:0691c6bb2a9c3d378d238e6a678185f252dd3b2c7245b0f7a242fc32a7ff3842@ec2-3-214-4-151.compute-1.amazonaws.com:5432/deuhak7u65lpbd"
#database_path = "postgres://{}:{}@{}/{}".format('postgres','Pranita123','localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    migrate = Migrate(app,db)
    db.app = app
    db.init_app(app)
    #db.create_all()

'''
Commands
'''
class Commands(db.Model):
    __tablename__ = 'commands'

    id = Column(Integer, primary_key=True)
    command = Column(String)
    category = Column(Integer)
    explanation = Column(String)

    def __init__(self, command, category,explanation):
        self.command = command
        self.category = category
        self.explanation = explanation

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'command': self.command,
        'category': self.category,
        'explanation':self.explanation
        }

    
class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category = Column(String)

    def __init__(self,category):
        self.category = category

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'category': self.category
        }

class Suggestion(db.Model):
    __tablename__ = 'suggestion'

    id = Column(Integer, primary_key=True)
    suggestion = Column(String)
    category = Column(Integer)

    def __init__(self,suggestion,category):
        self.suggestion = suggestion
        self.category = category

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'suggestion' : self.suggestion,
        'category': self.category
        }
