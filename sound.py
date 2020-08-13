#coding:utf-8     

import os
import tornado.ioloop
import tornado.web

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": True,
}


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        items = [u"for Sleep && Study", u"Study"]
        self.render("index.html", title="Listen the Sound", name=items[0])

# route
application = tornado.web.Application([
    (r"/", IndexHandler),
], **settings
)

if __name__ == "__main__":
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()
