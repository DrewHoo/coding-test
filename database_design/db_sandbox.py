from peewee import *
from datetime import datetime

from models.blogpost import BlogPost
from models.comment import Comment
from models.user import User

db = MySQLDatabase('blog', user='root', password='', host='localhost')
db.connect()
db.drop_tables([User, Comment, BlogPost])
db.create_tables([User, Comment, BlogPost])
drew = User(display_name='DrewHoo', email_address='drewhoover@gmail.com')
drew.save()

post = BlogPost(author=drew, text='lorem ipsum', date_posted=datetime.now())
post.save()
comment = Comment(author=drew, text='wow great post Drew', date_posted=datetime.now(), blog_post=post)
comment.save()
scout = User(display_name='Scout', email_address='scout@example.com')
scout.save()
post2 = BlogPost(author=scout, text='ruff ruff', date_posted=datetime.now())
post2.save()
comment2 = Comment(author=scout, 
  text='it is time to feed me', 
  date_posted=datetime.now(), 
  blog_post=post, 
  parent=comment)
comment2.save()

db.close()