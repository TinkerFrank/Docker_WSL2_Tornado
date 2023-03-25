
import tornado.ioloop  #main event loop
import tornado.web # to map the http requests to the defined handlers
import sqlite3
import asyncio

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello,Tornado🌪!')

class PostHandler(tornado.web.RequestHandler):
    def get(self):
        #write a view html page != rendering an existing real one
        self.write('<h1>This is Post 1 🔥') 

class WeatherHandler (tornado.web.RequestHandler):
    def get(self):
        degree = int(self.get_argument("degree"))  # user input e.g.  /weather?degree=19 
        output = 'Hot 🌞!' if degree > 20 else 'cold ⛄'
        drink = 'Have some beer 🍻' if degree > 20 else 'you need a hot beverage☕'
        self.render('/weather.html',output=output, drink=drink)

class JSONrequestHandler (tornado.web.RequestHandler):
    def get(self):
        self.write({'message':'hello world', 'Cars':'["BMW", "Mercedes"]'})
        
# we need a routing system (app) to route (entered in the browser) 
# the different request to the right handlers
async def make_app():
    application = tornado.web.Application([
        (r'/',HelloHandler),
        (r'/post',PostHandler),
        (r'/weather',WeatherHandler),
        (r'/api/data', JSONrequestHandler),
    ])
    application.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(make_app())

