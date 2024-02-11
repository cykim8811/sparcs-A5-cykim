from pyx2 import createElement, current

from watcher import watch

from . import header, body, nav

class Main:
    def __init__(self):
        self.header = header.Header()
        self.body = body.Body()
        self.nav = nav.Nav(self.body)
        watch(header, self.header)
        watch(body, self.body)
        watch(nav, self.nav)

    def __render__(self):
        return createElement("div", {
            'style': {
                'width': '100vw',
                'height': '100vh',
                'display': 'flex',
                'flexDirection': 'column',
            }
        },
            self.header,
            self.body,
            self.nav,
        )


root = Main()
