from tornado.web import RequestHandler, HTTPError
import os


class NotFoundHandler(RequestHandler):
    def prepare(self):
        raise HTTPError(
            status_code=404,
            reason="Invalid resource path.<br/>Please use this endpoints:<br/><b><br/>/greetings<br/>/square/[0-9]+</b>"
        )

class GreetingsHandler(RequestHandler):
    def get(self):
        payload = {"message": "Hello world from: {}".format(os.uname()[1])}
        self.write(payload)

class SquareHandler(RequestHandler):
    def get(self, number=0):
        aux_number = int(number)
        payload = {"message": {"number": aux_number, "square": aux_number ** 2}}
        self.write(payload)

