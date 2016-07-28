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
        # url for the api
        # function returns the full url with the random id
        pageNumber = str(randint(1,1000))
        firstUrlPart = 'https://api.themoviedb.org/3/discover/movie?'
        page = 'page='
        apiKey = '&api_key=7f2e8836857048a3c77885647f9c0f47'
        full_url = firstUrlPart + page + pageNumber + apiKey

        image_url = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2'

        data_source = urlfetch.fetch(full_url)
        movies = json.loads(data_source.content)

        # prints movie information
        indexNumber = randint(1,19)
        randomPageTemplate = jinja_env.get_template('RandomPage.html')

        variables = {
        'title': movies['results'][indexNumber]['title'],
        'dates': movies['results'][indexNumber]['release_date'],
        'popularity': str(movies['results'][indexNumber]['popularity']),
        'rating': str(movies['results'][indexNumber]['vote_average']),
        'plot': movies['results'][indexNumber]['overview'],
        'poster': image_url + movies['results'][indexNumber]['poster_path']
        }

        self.response.out.write(randomPageTemplate.render(variables))

class ActionHandler(webapp2.RequestHandler):
    def get(self):
        action = GenreHandler(28, 'Action')
        variables = action.get()
        self.response.write(variables)

class ComedyHandler(webapp2.RequestHandler):
    def get(self):
        comedy = GenreHandler(35, 'Comedy')
        variables = comedy.get()
        self.response.write(variables)

class HorrorHandler(webapp2.RequestHandler):
    def get(self):
        horror = GenreHandler(27, 'Horror')
        variables = horror.get()
        self.response.write(variables)

class FamilyHandler(webapp2.RequestHandler):
    def get(self):
        family = GenreHandler(10751, 'Family')
        variables = family.get()
        self.response.write(variables)

class DramaHandler(webapp2.RequestHandler):
    def get(self):
        drama = GenreHandler(18, 'Drama')
        variables = drama.get()
        self.response.write(variables)

class CrimeHandler(webapp2.RequestHandler):
    def get(self):
        crime = GenreHandler(80, 'Crime')
        variables = crime.get()
        self.response.write(variables)

class AdventureHandler(webapp2.RequestHandler):
    def get(self):
        adventure = GenreHandler(12, 'Adventure')
        variables = adventure.get()
        self.response.write(variables)

class AnimationHandler(webapp2.RequestHandler):
    def get(self):
        animation = GenreHandler(16, 'Animation')
        variables = animation.get()
        self.response.write(variables)

class DocumentaryHandler(webapp2.RequestHandler):
    def get(self):
        documentary = GenreHandler(99, 'Documentary')
        variables = documentary.get()
        self.response.write(variables)

class FantasyHandler(webapp2.RequestHandler):
    def get(self):
        fantasy = GenreHandler(14, 'Fantasy')
        variables = fantasy.get()
        self.response.write(variables)

class ForeignHandler(webapp2.RequestHandler):
    def get(self):
        foreign = GenreHandler(10769, 'Foreign')
        variables = foreign.get()
        self.response.write(variables)

class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        history = GenreHandler(36, 'History')
        variables = history.get()
        self.response.write(variables)

class MusicHandler(webapp2.RequestHandler):
    def get(self):
        music = GenreHandler(10402, 'Music')
        variables = music.get()
        self.response.write(variables)

class MysteryHandler(webapp2.RequestHandler):
    def get(self):
        mystery = GenreHandler(9648, 'Mystery')
        variables = mystery.get()
        self.response.write(variables)

class RomanceHandler(webapp2.RequestHandler):
    def get(self):
        romance = GenreHandler(10749, 'Romance')
        variables = romance.get()
        self.response.write(variables)

class ScifiHandler(webapp2.RequestHandler):
    def get(self):
        scifi = GenreHandler(878, 'Sci-Fi')
        variables = scifi.get()
        self.response.write(variables)

class ThrillerHandler(webapp2.RequestHandler):
    def get(self):
        thriller = GenreHandler(53, 'Thriller')
        variables = thriller.get()
        self.response.write(variables)

class GenreHandler(webapp2.RequestHandler):
    def __init__(self, search_id, genre):
        self.search_id = search_id
        self.genre = genre

    def get(self):
        #titles is a list of movie titles, years is a list of movie years, and
        #plots is a list of movie plots. The values are assigned in the for loop
        template = jinja_env.get_template('GenrePage.html')

        image_url = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2'

        titles = []
        years = []
        plots = []
        ratings = []
        popularity = []
        poster = []

        for i in range(0,5):
            rand_page = randint(0, 101)
            movies = self.fetch_movies(rand_page)
            rand_movie = randint(0,19)
            titles.append(movies['results'][rand_movie]['title'])
            years.append(movies['results'][rand_movie]['release_date'])
            plots.append(movies['results'][rand_movie]['overview'])
            ratings.append(movies['results'][rand_movie]['vote_average'])
            popularity.append(movies['results'][rand_movie]['popularity'])
            poster.append(image_url + movies['results'][rand_movie]['poster_path'])

        variables = {
            'titles': titles,
            'years': years,
            'plots': plots,
            'ratings': ratings,
            'specific_genre': self.genre,
            'popularity': popularity,
            'poster2': poster
        }

        return template.render(variables)
        # self.response.write(template.render(variables))
    def fetch_movies(self, random_page):
        data_source = urlfetch.fetch(self.movie_search(random_page))
        results = json.loads(data_source.content)
        return(results)

    def movie_search(self, random_page):
        base_url = "https://api.themoviedb.org/3/discover/movie?with_genres="
        searchid = str(self.search_id)
        page = '&page='+str(random_page)
        final_url = "&api_key=7f2e8836857048a3c77885647f9c0f47"
        full_url = base_url + searchid + final_url
        return full_url

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about', AboutHandler),
    ('/random', RandomHandler),
    ('/action', ActionHandler),
    ('/comedy', ComedyHandler),
    ('/drama', DramaHandler),
    ('/family', FamilyHandler),
    ('/horror', HorrorHandler),
    ('/crime', CrimeHandler),
    ('/adventure', AdventureHandler),
    ('/animation', AnimationHandler),
    ('/documentary', DocumentaryHandler),
    ('/fantasy', FantasyHandler),
    ('/foreign', ForeignHandler),
    ('/history', HistoryHandler),
    ('/music', MusicHandler),
    ('/mystery', MysteryHandler),
    ('/romance', RomanceHandler),
    ('/scifi', ScifiHandler),
    ('/thriller', ThrillerHandler)
], debug=True)
