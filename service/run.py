from pyx2 import PyX, current, createElement

import app.main as main

import asyncio
import importlib


class WatcherComponent:
    def __init__(self):
        self.component = main.root
        self.rerender_target = []
        self.initialized = False

    async def init(self):
        self.initialized = True
        current.app.rerender(self)
        while True:
            for module, component in self.rerender_target:
                importlib.reload(module)
                component.__class__ = module.__dict__[component.__class__.__name__]
                current.app.rerender(component)
            self.rerender_target = []
            await asyncio.sleep(0.5)

    def __render__(self):
        if not self.initialized:
            return createElement(
                "div",
                {
                    "onMouseMove": self.init,
                    "style": {
                        "width": "100vw",
                        "height": "100vh",
                    },
                },
                "Loading...",
            )
        return self.component


watcher_component = WatcherComponent()

import watcher

watcher.watcher.runner = watcher_component
watcher.watcher.target.append((main, main.root))

app = PyX(watcher_component)

import uvicorn

uvicorn.run(app, host="0.0.0.0", port=7004)
