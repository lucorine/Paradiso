# creates a datastore to cache rejected IMDb ID's
from google.appengine.ext import ndb

class rejectedID(ndb.Model):
  id = ndb.StringProperty(required=True)
