from peewee import *

from .user import User
from .blogpost import BlogPost

db = MySQLDatabase('blog', user='root', password='', host='localhost')

class Comment(Model):
  text = TextField()
  date_posted = DateTimeField()
  parent = ForeignKeyField('self', null=True, backref='children')
  author = ForeignKeyField(User)
  blog_post = ForeignKeyField(BlogPost)


  class Meta:
    database = db