#!/usr/bin/env python

from game.scenes import SceneStack
from insect.scenes.splash import Splash

def main():
    print "Hello, World!"

    stack = SceneStack()
    stack.append( Splash(stack) )

    while (len(stack)):
        stack.update_head(1)

    print "Goodbye!"

if __name__ == "__main__":
    main()
