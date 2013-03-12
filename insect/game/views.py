import pygame

class CoordConversion(object):
    def __init__( self, real = (800, 600), world = (100, 100) ):
        self.real = real # real screen coordinate system, i.e. window size or resolution
        self.world = world # our world's coordinate system

    def to_real(self, coord):
        x = coord[0]
        y = coord[1]

        x = (float(x) / self.world[0]) * self.real[0]
        y = (float(y) / self.world[1]) * self.real[1]

        return (x, y)

    def to_world(self, coord):
        x = coord[0]
        y = coord[1]

        x = (float(x) / self.real[0]) * self.world[0]
        y = (float(y) / self.real[1]) * self.world[1]

        return (x, y)

class View(object):

    coord_conversion = CoordConversion()

    def render(self, model, screen):
        """Draw `model` on `screen`"""
        pass

class OneImageView(View):
    def __init__(self, path):
        View.__init__(self)

        self.image = pygame.image.load(path)

    def render(self, model, screen):
        pos = model.position
        pos = View.coord_conversion.to_real(pos)
        screen.blit(self.image, pos)
        pass
