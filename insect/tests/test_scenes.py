import unittest
from game.scenes import Scene, SceneStack
from game.models import Model

class SceneWithNumber(Scene):
    """
    A scene base class for this module's test scenes.
    It, counts a number. Each update it's self.number += 1
    """
    def __init__(self):
        Scene.__init__(self)
        self.number = 0

    def update(self, dt):
        Scene.update(self, dt)
        self.number += 1

    def get_number(self):
        return self.number

class SceneA(SceneWithNumber):
    def __init__(self):
        SceneWithNumber.__init__(self)

class SceneB(SceneWithNumber):
    def __init__(self):
        SceneWithNumber.__init__(self)
        self.number = 10

# TODO: I don't check the styack.next() properly, it should use the `has_ended()` and `end_scene()` Scene methods
class SceneStackTests(unittest.TestCase):

    def setUp(self):
        self.stack = SceneStack()
        self.stack.append( SceneA() )
        self.stack.append( SceneB() )
        self.stack.append( SceneA() )

    def test_stack_sequence(self):
        self.assertEqual(self.stack.head().get_number(), 0) # First Scene A
        self.stack.next()

        self.assertEqual(self.stack.head().get_number(), 10) # Scene B
        self.stack.next()

        self.assertEqual(self.stack.head().get_number(), 0) # Second Scene A
        self.stack.next()

    def test_update(self):
        dt = 1 # meaningless `dt` value

        self.stack.head().update(dt)
        self.assertEqual(self.stack.head().get_number(), 1)
        self.stack.next()

        self.stack.head().update(dt)
        self.assertEqual(self.stack.head().get_number(), 11) # Scene B

class SceneTests(unittest.TestCase):

    def setUp(self):
        self.scene = SceneWithNumber()

    def test_scene(self):
        self.assertEqual(self.scene.get_number(), 0)
        self.scene.update(1) # meaningless `dt` value
        self.assertEqual(self.scene.get_number(), 1)
        
    def test_models(self):
        self.scene.append_model(Model())
        self.assertEqual(len(self.scene.get_models()), 1)

        self.scene.append_model( [ Model(), Model()] )
        self.assertEqual(len(self.scene.get_models()), 3)
