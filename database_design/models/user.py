from peewee import *

db = MySQLDatabase('blog', user='root', password='', host='localhost')

class User(Model):
  display_name = CharField(unique=True)
  email_address = CharField(unique=True)
  profile_pic = BlobField(null=True)
  # assuming use of 3rd party for Authentication/Authorization


  class Meta:
    database = db