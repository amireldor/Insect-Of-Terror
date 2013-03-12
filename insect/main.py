#!/usr/bin/env python

import pygame

from insect.conf import conf

from game.scenes import SceneStack
from insect.scenes import splash, menu

def main():
    print "Hello, World!"

    pygame.init()
    screen = pygame.display.set_mode( conf.window.dimensions )

    stack = SceneStack()
    #stack += [ splash.Splash(), menu.Menu() ]
    stack.append( menu.Menu() )

    run = True
    while (len(stack)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            stack.head().process_event(event)

        if not run: # are we still running?
            break

        stack.head().update(1)
        try:
            screen.fill( conf.clear_color )
            stack.head().render(screen)

            pygame.display.flip()

        except IndexError:
            pass # no head, so I guess no more scenes on stack

        pygame.time.delay(10)

        if stack.head().has_ended() is True:
            stack.next()

    print "Goodbye!"

if __name__ == "__main__":
    main()
