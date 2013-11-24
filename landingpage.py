# import os
# import urllib

# from google.appengine.api import users
# from google.appengine.ext import ndb

# import jinja2
# import webapp2


# JINJA_ENVIRONMENT = jinja2.Environment(
#     loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
#     extensions=['jinja2.ext.autoescape'],
#     autoescape=True)



# # class Greeting(ndb.Model):
# #     """Models an individual Guestbook entry with author, content, and date."""
# #     author = ndb.UserProperty()
# #     content = ndb.StringProperty(indexed=False)
# #     date = ndb.DateTimeProperty(auto_now_add=True)


# class MainPage(webapp2.RequestHandler):

#     def get(self):
        

#         template = JINJA_ENVIRONMENT.get_template('index.html')
#         self.response.write(template)


#     application = webapp2.WSGIApplication([
#     ('/', MainPage),
#     ('/sign', Guestbook),
# ], debug=True)

import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import webapp2
import jinja2

#from user import *

template_dir = "templates"
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

class Participant(ndb.Model):
	phone_number = ndb.StringProperty(required = True)
	date = ndb.DateTimeProperty(auto_now_add=True)




class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    @staticmethod
    def render_str(template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainHandler(Handler):
    def get(self):
        self.render("index.html")

    def post(self):
        phone_number = self.request.get('participate')
        participant = Participant(phone_number = phone_number)
        participant.put()
        self.render("success.html")

        # self.redirect("/")

class TestHandler(Handler):
	def get(self):
		self.write("I was redirected here")


application = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/test', TestHandler)
], debug=True)