from handlers import GreetingsHandler, SquareHandler


urls = [("/greetings", GreetingsHandler),
            ("/square/([0-9]+)", SquareHandler),
        ]

