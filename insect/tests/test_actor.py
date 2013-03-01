import unittest
from game.models import Actor

class TestActor(unittest.TestCase):

    def test_actor_position(self):
        actor = Actor()

        actor.set_position([100, 200])
        self.assertEqual(actor.get_position(), [100, 200])

        actor.set_position([200, None])
        self.assertEqual(actor.get_position(), [200, 200])

        actor.set_position([None, 300])
        self.assertEqual(actor.get_position(), [200, 300])

    def test_rotation(self):
        actor = Actor()

        actor.set_rotation(150)
        self.assertEquals(actor.get_rotation(), 150)

        actor.set_rotation(-10)
        self.assertEquals(actor.get_rotation(), 350)

        actor.set_rotation(370)
        self.assertEquals(actor.get_rotation(), 10)
