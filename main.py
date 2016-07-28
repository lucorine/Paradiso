# don't forget to comment y'all

import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch
import urllib2
from random import randint
from datatype import Movie
import logging

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

class RelatedHandler(webapp2.RequestHandler):
    def get(self):
        similarPageTemplate = jinja_env.get_template('RelatedMovies.html')

        user_query = self.request.get('user_query')
        user_query = user_query.replace(" ", "%20")

        if len(user_query) > 0:
            self.give_results(user_query)
        else:
            self.response.out.write(similarPageTemplate.render())

    def give_results(self, user_query):

        firstUrlPart = 'https://api.themoviedb.org/3/search/movie?query='

        apiKey = '&api_key=7f2e8836857048a3c77885647f9c0f47'
        full_url = firstUrlPart + user_query + apiKey
        data_source = urlfetch.fetch(full_url)
        movies = json.loads(data_source.content)

        search_id = movies['results'][0]['id']

        id_url = 'https://api.themoviedb.org/3/movie/' + str(search_id) + '/similar?api_key=7f2e8836857048a3c77885647f9c0f47'
        similar_results = urlfetch.fetch(id_url)
        similar_movies = json.loads(similar_results.content)

        titles = []
        years = []
        plots = []
        ratings = []
        popularity = []

        for i in range(0,5):
            titles.append(similar_movies['results'][i]['title'])
            years.append(similar_movies['results'][i]['release_date'])
            plots.append(similar_movies['results'][i]['overview'])
            ratings.append(similar_movies['results'][i]['vote_average'])
            popularity.append(similar_movies['results'][i]['popularity'])

        variables = {
        'titles': titles,
        'years': years,
        'popularity': popularity,
        'ratings': ratings,
        'plots': plots
        }
        similarResultsTemplate = jinja_env.get_template('SimilarResults.html')
        self.response.write(similarResultsTemplate.render(variables))


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
        action = GenreHandler(28, 'ACTION')
        variables = action.get()
        self.response.write(variables)

class ComedyHandler(webapp2.RequestHandler):
    def get(self):
        comedy = GenreHandler(35, 'COMEDY')
        variables = comedy.get()
        self.response.write(variables)

class HorrorHandler(webapp2.RequestHandler):
    def get(self):
        horror = GenreHandler(27, 'HORROR')
        variables = horror.get()
        self.response.write(variables)

class FamilyHandler(webapp2.RequestHandler):
    def get(self):
        family = GenreHandler(10751, 'FAMILY')
        variables = family.get()
        self.response.write(variables)

class DramaHandler(webapp2.RequestHandler):
    def get(self):
        drama = GenreHandler(18, 'DRAMA')
        variables = drama.get()
        self.response.write(variables)

class CrimeHandler(webapp2.RequestHandler):
    def get(self):
        crime = GenreHandler(80, 'CRIME')
        variables = crime.get()
        self.response.write(variables)

class AdventureHandler(webapp2.RequestHandler):
    def get(self):
        adventure = GenreHandler(12, 'ADVENTURE')
        variables = adventure.get()
        self.response.write(variables)

class AnimationHandler(webapp2.RequestHandler):
    def get(self):
        animation = GenreHandler(16, 'ANIMATION')
        variables = animation.get()
        self.response.write(variables)

class DocumentaryHandler(webapp2.RequestHandler):
    def get(self):
        documentary = GenreHandler(99, 'DOCUMENTARY')
        variables = documentary.get()
        self.response.write(variables)

class FantasyHandler(webapp2.RequestHandler):
    def get(self):
        fantasy = GenreHandler(14, 'FANTASY')
        variables = fantasy.get()
        self.response.write(variables)

class ForeignHandler(webapp2.RequestHandler):
    def get(self):
        foreign = GenreHandler(10769, 'FOREIGN')
        variables = foreign.get()
        self.response.write(variables)

class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        history = GenreHandler(36, 'HISTORY')
        variables = history.get()
        self.response.write(variables)

class MusicHandler(webapp2.RequestHandler):
    def get(self):
        music = GenreHandler(10402, 'MUSIC')
        variables = music.get()
        self.response.write(variables)

class MysteryHandler(webapp2.RequestHandler):
    def get(self):
        mystery = GenreHandler(9648, 'MYSTERY')
        variables = mystery.get()
        self.response.write(variables)

class RomanceHandler(webapp2.RequestHandler):
    def get(self):
        romance = GenreHandler(10749, 'ROMANCE')
        variables = romance.get()
        self.response.write(variables)

class ScifiHandler(webapp2.RequestHandler):
    def get(self):
        scifi = GenreHandler(878, 'SCI-FI')
        variables = scifi.get()
        self.response.write(variables)

class ThrillerHandler(webapp2.RequestHandler):
    def get(self):
        thriller = GenreHandler(53, 'THRILLER')
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
    ('/thriller', ThrillerHandler),
    ('/related', RelatedHandler)
], debug=True)
