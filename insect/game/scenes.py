import collections
from game.models import Model

class SceneStack(list):
    """A list of scenes. Includes some helper methods."""

    def head(self):
        return self[0]

    def next(self):
        return self.pop(0)

    def update_head(self, dt):
        self.head().update(dt)

class Scene(Model):
    """Base class for a Scene. A scene is that you see on the screen at a time such as Main Menu, Game, etc..."""

    def __init__(self, stack=None):
        Model.__init__(self)

        self.models = []
        self.stack = stack

    def append_model(self, model):
        if isinstance(model, collections.Iterable):
            self.models += model
        else:
            self.models.append(model)

    def get_models(self):
        return self.models

    def update(self, dt):
        pass
