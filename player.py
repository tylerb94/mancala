import pygame
from mancala import Space, Home
import time

display = pygame.display.set_mode((1000, 500))

TOP = 1
BOTTOM = 0

WOOD_YELLOW = (245, 227, 157)
WOOD_YELLOW_SHADE_LIGHT = (207, 192, 132)

class Player:

    def __init__(self, name, position):

        self.name = name
        self.position = position
        self.hand = []
        self.finished = False
        self.index = 0

    def take_turn(self, _spaces, index):

        spaces = _spaces
        self.index = index

        self.hand.clear()

        for piece in spaces[index].pieces:
            self.hand.append(piece)
        spaces[self.index].pieces.clear()

        self.index += 1

        while len(self.hand) > 0:

            if self.index == 13 and self.position == TOP:

                self.index = 0

            elif self.index == 6 and self.position == BOTTOM:

                self.index += 1

            else:

                if self.index > 13: self.index = 0

                p = self.hand[-1]
                spaces[self.index].add_piece(p)
                self.hand.pop()

                ## DRAW
                #pygame.draw.rect(display, WOOD_YELLOW, [100, 106, 800, 288], 0)

                #for space in spaces:
                #    space.draw()
                #    display.blit(space.image, [space.location[0] + 100, space.location[1] + 106])

                #for space in spaces:
                #    space.draw()
                #    display.blit(space.image, [space.location[0] + 100, space.location[1] + 106])

                #pygame.display.update()
                #time.sleep(.1)
                ## END DRAW

                if len(self.hand) == 0:
                    self.finished = True

                    if self.index == 6 and self.position == TOP or self.index == 13 and self.position == BOTTOM:
                        self.finished = False

                self.index += 1

        return spaces
