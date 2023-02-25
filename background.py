import pygame
from pygame.locals import*

def backgroundMethod():

    pygame.init()
    screen = pygame.display.set_mode((150,10))
    pygame.display.set_caption('Game')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))

    screen.blit(background,(0,0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        screen.blit(background,(0,0))
        pygame.display.flip()

if __name__ == '__main__': backgroundMethod()