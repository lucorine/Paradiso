# don't forget to comment y'all

import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch
import urllib2
from random import randint
from datatype import Movie

jinja_environment = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

# this is to link to the html file
# make sure to change 'search_template' to something relevant
# search_template = jinja_env.get_template('search.html')
# self.response.out.write(search_template.render())

class MainHandler(webapp2.RequestHandler):
    def get(self):
        mainPageTemplate = jinja_env.get_template('paradisomain.html')
        self.response.out.write(mainPageTemplate.render())

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        mainPageTemplate = jinja_env.get_template('AboutPage.html')
        self.response.out.write(mainPageTemplate.render())

class RandomHandler(webapp2.RequestHandler):
    def get(self):

        # r creates a random imdb id from 0 to 2000000 which is entered into the
        # url for the api
        # function returns the full url with the random id
        pageNumber = str(randint(1,1000))
        firstUrlPart = 'https://api.themoviedb.org/3/discover/movie?'
        page = 'page='
        apiKey = '&api_key=7f2e8836857048a3c77885647f9c0f47'
        full_url = firstUrlPart + page + pageNumber + apiKey

        data_source = urlfetch.fetch(full_url)
        movies = json.loads(data_source.content)

        # refreshes page if not a movie or and Adult movie
        #if results['movie_results']['adult'] == false:
        #    self.redirect("/random")

        #movieQuery = Movie.query()
        #movie = movieQuery.fetch()

        # prints movie information
        indexNumber = randint(1,19)
        self.response.write(movies['results'][indexNumber]['title'] + '<br>')
        self.response.write('Release Date: ' + movies['results'][indexNumber]['release_date'] + '<br>')
        self.response.write('Popularity: ' + str(movies['results'][indexNumber]['popularity']) + '<br>')
        self.response.write('Rating: ' + str(movies['results'][indexNumber]['vote_average']) + '<br>')
        self.response.write(movies['results'][indexNumber]['overview'] + '<br>')



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about', AboutHandler),
    ('/random', RandomHandler)
], debug=True)
