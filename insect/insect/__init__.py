from game.views import View, CoordConversion

from insect.conf import conf

# set the main coordinate system conversion stuff according to what's configured for the game 'insect'
View.coord_conversion = CoordConversion( conf.window.dimensions, conf.world.dimensions )
