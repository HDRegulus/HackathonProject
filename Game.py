import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")

PURPLE = (216,191,216)
FPS = 60

PLAYER1_IMG = pygame.image.load(os.path.join('ASSETS', 'sPlayerIdle_strip4.png'))
#PLAYER2_IMG = pygame.image.load(os.path.join('ASSETS', 'sEnemy_strip7.png'))

def draw_window():
    WIN.fill(PURPLE)
    WIN.blit(PLAYER1_IMG, (100, 100))
    WIN.blit(PLAYER2_IMG, (100, 300))
    # update the display
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        # control the frame rate
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    # shut down Pygame
    pygame.quit()

if __name__ == "__main__":
    main()