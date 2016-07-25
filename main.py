# don't forget to comment y'all

import webapp2
import jinja2
import os
import json
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

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
