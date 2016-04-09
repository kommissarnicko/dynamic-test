import webapp2
from datetime import datetime

class DynamicTestHandler(webapp2.RequestHandler):
	def get(self):
		thetime = datetime.now().time()
		greeting = "Nick Williams Site, time now is " + str(thetime)
		self.response.write(str(greeting))
		
app = webapp2.WSGIApplication([
	('/', DynamicTestHandler), 
], debug = True)

"""
@app.route('/')
def hello():
    Dynamic greeting
	thetime = datetime.now().time()
	greeting = "Nick Williams Site, time now is " + str(thetime)
    return greeting


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
"""