from urls import urls
from handlers import NotFoundHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
import os


def make_app():
    return Application(urls, default_handler_class=NotFoundHandler)

if __name__ == '__main__':
    app = make_app()
    app.listen(os.getenv("APP_PORT",3000))
    IOLoop.instance().start()

