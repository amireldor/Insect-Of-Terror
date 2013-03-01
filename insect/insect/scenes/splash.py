"""
Splash screen scene
"""

from random import random

from insect.conf import conf

from game.scenes import Scene
from insect.models.roach import Roach

class Splash(Scene):

    def __init__(self, stack):
        Scene.__init__(self, stack)

        self.roaches = []
        for x in xrange(conf.splash.roaches):
            new_roach = Roach()

            new_roach.set_position( [random() * conf.world.dimensions[0], random() * conf.world.dimensions[1]] )
            new_roach.set_rotation( random() * 360 )

            self.roaches.append(new_roach)

        self.append_model(self.roaches)

        # TEMP CODE TODO REMOVE
        self.life = 10

    def update(self, dt):
        print dt, [ (r.get_position(), r.get_rotation()) for r in self.roaches ]

        for roach in self.roaches:
            roach.set_rotation(roach.get_rotation() + 280 * dt)

        # TEMP CODE TODO REMOVE
        self.life -= 1
        if self.life <= 0:
            self.stack.next()
