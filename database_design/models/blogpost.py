from peewee import *

from .user import User

db = MySQLDatabase('blog', user='root', password='', host='localhost')

class BlogPost(Model):
  text = TextField()
  date_posted = DateTimeField()
  author = ForeignKeyField(User)


  class Meta:
    database = db