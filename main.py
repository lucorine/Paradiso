# don't forget to comment y'all

import webapp2
#import jinja2
#import os
import json
from google.appengine.api import urlfetch
import urllib2
from random import randint
# from 'file name' import 'class'
# from 'api' import 'class'

# jinja_environment = jinja2.Environment(
#   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))# this little bit sets jinja's relative directory to match the directory name(dirname) of the current __file__, in this case, helloworld.py
# env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

# this is to link to the html file
# make sure to change 'search_template' to something relevant
#search_template = jinja_env.get_template('search.html')
#self.response.out.write(search_template.render())

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class RandomHandler(webapp2.RequestHandler):
    def get(self):
        data_source = urlfetch.fetch(self.movie_search())
        results = json.loads(data_source.content)

        genre = results['Genre']

        self.response.write(genre)

    def movie_search(self):
        #please find a way to make the random functional (adding leading zeros)
        #r creates a random imdb id from 0 to 2000000 which is entered into the
        #url for the api
        #movie_search returns the full url with the random id
        r = randint(0,2000000)
        full_url = "http://www.omdbapi.com/?i=tt" + str(r)

        return full_url



app = webapp2.WSGIApplication([
    ('/', RandomHandler)
], debug=True)
