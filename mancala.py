import pygame
import player
import random
import time

TOP = 1
BOTTOM = 0

WOOD_YELLOW = (245, 227, 157)
WOOD_YELLOW_SHADE_LIGHT = (207, 192, 132)

colors = [
    (204, 0, 0), # Red
    (0, 0, 255), # Blue
    (0, 153, 0), # Green
    (255, 255, 0), # Yellow
    (153, 0, 200), # Purple
    (255, 255, 255), # White
    (0, 0, 0), # Black


]


class Piece:

    def __init__(self):

        self.location = [0, 0]
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        self.color = (r, g, b)
        self.width = 15



class Home:

    def __init__(self, loc):


        self.width = 64
        self.pieces = []
        self.location = loc
        self.image = pygame.Surface((self.width, self.width * 3.5))
        self.type = 'home'

    def add_piece(self, piece):

        piece.location[0] = random.randint(int(piece.width / 2), int(self.width - piece.width / 2))
        piece.location[1] = random.randint(int(piece.width / 2), int(self.width * 3.5 - piece.width / 2))

        self.pieces.append(piece)

    def draw(self):

        pygame.draw.rect(self.image, WOOD_YELLOW_SHADE_LIGHT, [0, 0, self.width, self.width * 3.5], 0)
        pygame.draw.rect(self.image, (0, 0, 0), [0, 0, self.width, self.width * 3.5], 1)
        for piece in self.pieces:

            pygame.draw.circle(self.image, piece.color, piece.location, int(piece.width / 2), 0)
            pygame.draw.circle(self.image, (0, 0, 0), piece.location, int(piece.width / 2), 1)


class Space:

    def __init__(self, loc):

        self.width = 64
        self.pieces = []
        self.location = loc
        self.image = pygame.Surface((self.width, self.width))
        self.type = 'field'

    def add_piece(self, piece):

        piece.location[0] = random.randint(int(piece.width / 2), int(self.width - piece.width / 2))
        piece.location[1] = random.randint(int(piece.width / 2), int(self.width - piece.width / 2))

        self.pieces.append(piece)

    def draw(self):
        pygame.draw.rect(self.image, WOOD_YELLOW_SHADE_LIGHT, [0, 0, self.width, self.width], 0)
        pygame.draw.rect(self.image, (0, 0, 0), [0, 0, self.width, self.width], 1)
        for piece in self.pieces:

            pygame.draw.circle(self.image, piece.color, piece.location, int(piece.width / 2), 0)
            pygame.draw.circle(self.image, (0, 0, 0), piece.location, int(piece.width / 2), 1)




class Board:

    def __init__(self):
        self.size = (800, 288)
        self.position = [0, 0]
        self.image = pygame.Surface(self.size)

        self.player_1 = player.Player(input('Player 1 name: '), TOP)
        self.player_2 = player.Player(input('Player 2 name: '), BOTTOM)

        self.current_player = self.player_1
        self.idle_player = self.player_2
        self.side = self.current_player.position

        self.spaces = [
            Space([608, 32]),
            Space([512, 32]),
            Space([416, 32]),
            Space([320, 32]),
            Space([224, 32]),
            Space([128, 32]),
            Home((32, 32)),
            Space([128, 192]),
            Space([224, 192]),
            Space([320, 192]),
            Space([416, 192]),
            Space([512, 192]),
            Space([608, 192]),
            Home((704, 32))
        ]

        for index in range(0, 13):

            # Don't put pebbles in the home spaces
            if not index == 6 and not index == 13:
                self.spaces[index].add_piece(Piece())
                self.spaces[index].add_piece(Piece())
                self.spaces[index].add_piece(Piece())
                self.spaces[index].add_piece(Piece())

    def win(self):
        pass

    def win_tie(self):
        pass

    def update(self):

        # When the player's hand becomes empty
        if self.current_player.finished:
            self.current_player.finished = False


            s = self.spaces



            # If the idle player has pieces on their side
            if self.idle_player == self.player_1:
                if len(s[0].pieces) + len(s[1].pieces) + len(s[2].pieces) + len(s[3].pieces) + len(s[4].pieces) + len(s[5].pieces) > 0:

                    # Switch current player and idle player
                    self.current_player, self.idle_player = self.idle_player, self.current_player

            elif self.idle_player == self.player_2:

                if len(s[7].pieces) + len(s[8].pieces) + len(s[9].pieces) + len(s[10] .pieces)+ len(s[11].pieces) + len(s[12].pieces) > 0:

                    # Switch current player and idle player
                    self.current_player, self.idle_player = self.idle_player, self.current_player

        # Get events
        for event in pygame.event.get():

            # If event is left click
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

                # Look at each space
                for index in range(len(self.spaces)):

                    space = self.spaces[index]     # Get space's location
                    m = pygame.mouse.get_pos()              # Get mouse's location
                    mouse_x = m[0] - self.position[0]       # Adjust the mouse for the board
                    mouse_y = m[1] - self.position[0]       # ...

                    # If the mouse is over a space
                    if space.location[0] <= mouse_x <= space.location[0] + space.width:
                        if space.location[1] <= mouse_y <= space.location[1] + space.width:

                            # If the space is a home
                            if index == 6 or index == 13:
                                pass

                            # If it is player 1's turn
                            elif self.current_player == self.player_1:

                                # If the space is player 1's space
                                if index in [0, 1, 2, 3, 4, 5]:
                                    # Take a turn with current space/player
                                    self.spaces = self.current_player.take_turn(self.spaces, index)

                            # If it is player 1's turn
                            elif self.current_player == self.player_2:

                                # If the space is player 1's space
                                if index in [7, 8, 9, 10, 11, 12]:
                                    # Take a turn with current space/player
                                    self.spaces = self.current_player.take_turn(self.spaces, index)







    def draw(self):

        # Draw background of board
        pygame.draw.rect(self.image, WOOD_YELLOW, [0, 0, self.size[0], self.size[1]], 0)


        # Draw player 1 (top) spaces
        for space in self.spaces:
            space.draw()
            self.image.blit(space.image, space.location)


        # Draw player 2 (bottom) spaces
        for space in self.spaces:
            space.draw()
            self.image.blit(space.image, space.location)
