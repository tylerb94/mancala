import pygame
import player
import mancala

window_size = (1000, 500)

display = pygame.display.set_mode(window_size)

def main():

    board = mancala.Board()

    board.position[0] = window_size[0]/2 - board.size[0]/2
    board.position[1] = window_size[1]/2 - board.size[1]/2

    while True:

        board.update()

        board.draw()

        pygame.Surface.blit(display, board.image, board.position)

        pygame.display.update()


main()