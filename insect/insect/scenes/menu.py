"""
Menu screen scene
"""

import pygame
from random import random

from insect.conf import conf

from game.scenes import Scene
from insect.models.roach import Roach

from game.views import OneImageView

class Menu(Scene):

    def __init__(self):
        Scene.__init__(self)

        self.roaches = []
        for x in xrange(conf.menu.roaches):
            new_roach = Roach()

            #new_roach.set_position( [random() * conf.world.dimensions[0], random() * conf.world.dimensions[1]] )
            new_roach.set_position( [random() * conf.world.dimensions[0], 500] )
            new_roach.set_rotation( random() * 360 )

            self.roaches.append(new_roach)

        self.append_model(self.roaches)

        self.roach_view = OneImageView(conf.images.test)

    def process_event(self, event):
        Scene.process_event(self, event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.end_scene()

    def update(self, dt):
        Scene.update(self, dt)

        for roach in self.roaches:
            roach.set_rotation(roach.get_rotation() + 280 * dt)

    def render(self, screen):
        Scene.render(self, screen)
        screen.fill( (0, 128, 255) )

        for roach in self.roaches:
            self.roach_view.render(roach, screen)
