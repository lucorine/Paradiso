from google.appengine.ext import ndb

class Movie(ndb.Model):
  title = ndb.StringProperty(required=True)
  genre = ndb.StringProperty(required=True)
  imdbid = ndb.StringProperty(required=True)
