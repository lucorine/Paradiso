# don't forget to comment y'all

import webapp2
#import jinja2
import os
import json
from google.appengine.api import urlfetch
import urllib2
from random import randint
# from rejectedid import rejectedID
from data_type import Movie

# jinja_environment = jinja2.Environment(
#   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))# this little bit sets jinja's relative directory to match the directory name(dirname) of the current __file__, in this case, helloworld.py
# env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

# this is to link to the html file
# make sure to change 'search_template' to something relevant
# search_template = jinja_env.get_template('search.html')
# self.response.out.write(search_template.render())

class MainHandler(webapp2.RequestHandler):
    def get(self):

        for i in range(1,500):
            r = str(i)
            full_url = "http://www.omdbapi.com/?i=tt" + r.zfill(7)
            data_source = urlfetch.fetch(full_url)
            results = json.loads(data_source.content)
            if(results['Type'] == 'movie'):
                movie = Movie(title= results['Title'], genre= results['Genre'], imdbid= r.zfill(7))
                movie.put()

# class RandomHandler(webapp2.RequestHandler):
#     def get(self):
#
#         # r creates a random imdb id from 0 to 2000000 which is entered into the
#         # url for the api
#         # function returns the full url with the random id
#         randomInt = str(randint(0,2000000))
#         full_url = "http://www.omdbapi.com/?i=tt" + randomInt.zfill(7)
#
#         data_source = urlfetch.fetch(full_url)
#         results = json.loads(data_source.content)
#
#         # refreshes page if not a movie or and Adult movie
#         if not results['Type'] == 'movie' or results['Genre'] == 'Adult':
#             x = rejectedID(id=randomInt)
#             x.put()
#
#             self.redirect("/random")
#
#         # prints movie information
#         self.response.write(results['Title'] + '<br>')
#         self.response.write(results['Year'] + ' - ' + results['Genre'] + '<br>')
#         if results['Plot'] != "N/A":
#             self.response.write(results['Plot'])



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    # ('/random', RandomHandler)
], debug=True)
