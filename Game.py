import pygame
import os

WIDTH, HEIGHT = 900, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")

PURPLE = (216,191,216)
FPS = 60

CHAR_IMG = pygame.image.load(os.path.join('ASSETS', 'characters.png'))

def draw_window():
    WIN.fill(PURPLE)
    WIN.blit(CHAR_IMG, (0, 0))
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