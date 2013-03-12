import unittest

from game.views import CoordConversion

class TestConversions(unittest.TestCase):

    def setUp(self):
        self.coord_conversion = CoordConversion( (800, 600), (10, 10) )

    def test_to_real(self):
        coord = (5, 5)

        result = self.coord_conversion.to_real(coord)

        self.assertAlmostEqual(result[0], 400)
        self.assertAlmostEqual(result[1], 300)

    def test_to_world(self):
        coord = (400, 300)

        result = self.coord_conversion.to_world(coord)

        self.assertAlmostEqual(result[0], 5) 
        self.assertAlmostEqual(result[1], 5)
