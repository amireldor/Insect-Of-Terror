import util

class Model(object):
    def update(self, dt):
        pass

class Actor(Model):
    """An actor is someone on the screen that can move and rotate"""

    def __init__(self):
        self.position = [0, 0]
        self.rotation = 0

    def set_position(self, new_pos):
        for i in xrange(len(new_pos)):
            if new_pos[i] is not None:
                self.position[i] = new_pos[i]

    def get_position(self):
        return self.position

    def set_rotation(self, new_rot):
        self.rotation = util.restrict_0_360(new_rot)

    def get_rotation(self):
        return self.rotation
