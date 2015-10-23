import os
from tornado import web, ioloop

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": True,
    "autoreload": True
}

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")

application = web.Application([
    (r'/', IndexHandler),
    (r'/index', IndexHandler),
], **settings)

port = 8080

if __name__ == '__main__':
    application.listen(port)
    ioloop.IOLoop.instance().start()
