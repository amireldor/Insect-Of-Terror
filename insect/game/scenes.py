import collections
from game.models import Model

class SceneStack(list):
    """A list of scenes. Includes some helper methods."""

    def head(self):
        return self[0]

    def next(self):
        return self.pop(0)

class Scene(Model):
    """
    Base class for a Scene. A scene is that you see on the screen at a time such as Main Menu, Game, etc...
    """
    # TODO: tell more stories in the doc

    def __init__(self):
        Model.__init__(self)

        self.models = []
        self.ended = False # did scene end?

    def append_model(self, model):
        if isinstance(model, collections.Iterable):
            self.models += model
        else:
            self.models.append(model)

    def get_models(self):
        return self.models

    def process_event(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        pass

    def end_scene(self):
        self.ended = True

    def has_ended(self):
        return self.ended
