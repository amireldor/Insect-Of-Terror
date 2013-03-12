"""
Splash screen scene
"""

import pygame
from random import random

from insect.conf import conf

from game.scenes import Scene
from insect.models.roach import Roach

class Splash(Scene):

    def __init__(self):
        Scene.__init__(self)
        self.ticks = pygame.time.get_ticks()

    def process_event(self, event):
        Scene.process_event(self, event)

        if event.type == pygame.KEYDOWN:
            self.end_scene()

    def update(self, dt):
        Scene.update(self, dt)

    def render(self, screen):
        Scene.render(self, screen)
        screen.fill( (255, 255, 255) )
