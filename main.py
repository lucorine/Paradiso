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

        data_source = urlfetch.fetch(full_url)
        movies = json.loads(data_source.content)

        # prints movie information
        indexNumber = randint(1,19)
        randomPageTemplate = jinja_env.get_template('RandomPage.html')
        self.response.out.write(randomPageTemplate.render())
        self.response.write(movies['results'][indexNumber]['title'] + '<br><br>')
        self.response.write('Release Date: ' + movies['results'][indexNumber]['release_date'] + '<br>')
        self.response.write('Popularity: ' + str(movies['results'][indexNumber]['popularity']) + '<br>')
        self.response.write('Rating: ' + str(movies['results'][indexNumber]['vote_average']) + '<br><br>')
        self.response.write(movies['results'][indexNumber]['overview'] + '<br>')

class ActionHandler(webapp2.RequestHandler):
    def get(self):

        #titles is a list of movie titles, years is a list of movie years, and
        #plots is a list of movie plots. The values are assigned in the for loop

        titles = []
        years = []
        plots = []

        for i in range(0,5):
            rand_page = randint(0, 101)
            movies = self.fetch_movies(rand_page)
            rand_movie = randint(0,19)
            titles.append(movies['results'][rand_movie]['title'])
            years.append(movies['results'][rand_movie]['release_date'])
            plots.append(movies['results'][rand_movie]['overview'])

        self.response.write(titles)
        self.response.write(years)
        self.response.write(plots)

    def fetch_movies(self, random_page):
        data_source = urlfetch.fetch(self.movie_search(random_page))
        results = json.loads(data_source.content)
        return(results)

    def movie_search(self, random_page):
        base_url = "https://api.themoviedb.org/3/discover/movie?with_genres="
        # search_id = self.fetch_genre() - This could be used to use just one handler for all genres
        search_id = '28&'
        page = 'page='+str(random_page)
        final_url = "&api_key=7f2e8836857048a3c77885647f9c0f47"
        full_url = base_url + search_id + final_url

        return full_url

class ComedyHandler(webapp2.RequestHandler):
    def get(self):

        #titles is a list of movie titles, years is a list of movie years, and
        #plots is a list of movie plots. The values are assigned in the for loop

        titles = []
        years = []
        plots = []

        for i in range(0,5):
            rand_page = randint(0, 101)
            movies = self.fetch_movies(rand_page)
            rand_movie = randint(0,19)
            titles.append(movies['results'][rand_movie]['title'])
            years.append(movies['results'][rand_movie]['release_date'])
            plots.append(movies['results'][rand_movie]['overview'])

        self.response.write(titles)
        self.response.write(years)
        self.response.write(plots)

    def fetch_movies(self, random_page):
        data_source = urlfetch.fetch(self.movie_search(random_page))
        results = json.loads(data_source.content)
        return(results)

    def movie_search(self, random_page):
        base_url = "https://api.themoviedb.org/3/discover/movie?with_genres="
        # search_id = self.fetch_genre() - This could be used to use just one handler for all genres
        search_id = '35&'
        page = 'page='+str(random_page)
        final_url = "&api_key=7f2e8836857048a3c77885647f9c0f47"
        full_url = base_url + search_id + final_url

        return full_url


class DramaHandler(webapp2.RequestHandler):
    def get(self):

        #titles is a list of movie titles, years is a list of movie years, and
        #plots is a list of movie plots. The values are assigned in the for loop

        titles = []
        years = []
        plots = []

        for i in range(0,5):
            rand_page = randint(0, 101)
            movies = self.fetch_movies(rand_page)
            rand_movie = randint(0,19)
            titles.append(movies['results'][rand_movie]['title'])
            years.append(movies['results'][rand_movie]['release_date'])
            plots.append(movies['results'][rand_movie]['overview'])

        self.response.write(titles)
        self.response.write(years)
        self.response.write(plots)

    def fetch_movies(self, random_page):
        data_source = urlfetch.fetch(self.movie_search(random_page))
        results = json.loads(data_source.content)
        return(results)

    def movie_search(self, random_page):
        base_url = "https://api.themoviedb.org/3/discover/movie?with_genres="
        # search_id = self.fetch_genre() - This could be used to use just one handler for all genres
        search_id = '18&'
        page = 'page='+str(random_page)
        final_url = "&api_key=7f2e8836857048a3c77885647f9c0f47"
        full_url = base_url + search_id + final_url

        return full_url


class FamilyHandler(webapp2.RequestHandler):
    def get(self):

        #titles is a list of movie titles, years is a list of movie years, and
        #plots is a list of movie plots. The values are assigned in the for loop

        titles = []
        years = []
        plots = []

        for i in range(0,5):
            rand_page = randint(0, 101)
            movies = self.fetch_movies(rand_page)
            rand_movie = randint(0,19)
            titles.append(movies['results'][rand_movie]['title'])
            years.append(movies['results'][rand_movie]['release_date'])
            plots.append(movies['results'][rand_movie]['overview'])

        self.response.write(titles)
        self.response.write(years)
        self.response.write(plots)

    def fetch_movies(self, random_page):
        data_source = urlfetch.fetch(self.movie_search(random_page))
        results = json.loads(data_source.content)
        return(results)

    def movie_search(self, random_page):
        base_url = "https://api.themoviedb.org/3/discover/movie?with_genres="
        # search_id = self.fetch_genre() - This could be used to use just one handler for all genres
        search_id = '10751&'
        page = 'page='+str(random_page)
        final_url = "&api_key=7f2e8836857048a3c77885647f9c0f47"
        full_url = base_url + search_id + final_url

        return full_url


class HorrorHandler(webapp2.RequestHandler):
    def get(self):

        #titles is a list of movie titles, years is a list of movie years, and
        #plots is a list of movie plots. The values are assigned in the for loop

        titles = []
        years = []
        plots = []

        for i in range(0,5):
            rand_page = randint(0, 101)
            movies = self.fetch_movies(rand_page)
            rand_movie = randint(0,19)
            titles.append(movies['results'][rand_movie]['title'])
            years.append(movies['results'][rand_movie]['release_date'])
            plots.append(movies['results'][rand_movie]['overview'])

        self.response.write(titles)
        self.response.write(years)
        self.response.write(plots)

    def fetch_movies(self, random_page):
        data_source = urlfetch.fetch(self.movie_search(random_page))
        results = json.loads(data_source.content)
        return(results)

    def movie_search(self, random_page):
        base_url = "https://api.themoviedb.org/3/discover/movie?with_genres="
        # search_id = self.fetch_genre() - This could be used to use just one handler for all genres
        search_id = '27&'
        page = 'page='+str(random_page)
        final_url = "&api_key=7f2e8836857048a3c77885647f9c0f47"
        full_url = base_url + search_id + final_url

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about', AboutHandler),
    ('/random', RandomHandler),
    ('/action', ActionHandler),
    ('/comedy', ComedyHandler),
    ('/drama', DramaHandler),
    ('/family', FamilyHandler),
    ('/horror', HorrorHandler)
], debug=True)
