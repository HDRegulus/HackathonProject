import pygame
import os

WIDTH, HEIGHT = 1100, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")

PURPLE = (216,191,216)
FPS = 60
VEL = 5

CHAR_WIDTH, CHAR_HEIGHT = 70, 70

charizard_Image = pygame.image.load(os.path.join('ASSETS', 'charizard.png'))
charizard = pygame.transform.scale(charizard_Image, (CHAR_WIDTH, CHAR_HEIGHT))
sonic_Image = pygame.image.load(os.path.join('ASSETS', 'sonic.png'))
sonic = pygame.transform.scale(sonic_Image, (CHAR_WIDTH, CHAR_HEIGHT))
grass_Image = pygame.image.load(os.path.join('ASSETS', 'grass.png'))
grass = pygame.transform.scale(grass_Image, (WIDTH, HEIGHT))
ZOMBIE_IMAGE = pygame.image.load(
    os.path.join('Assets', 'sEnemyDead.png'))
ZOMBIE = pygame.transform.scale(ZOMBIE_IMAGE, (30, 30))

def draw_window(player1, player2, zombie):
    WIN.fill(PURPLE)
    WIN.blit(grass, (0, 0))
    WIN.blit(charizard, (player1.x, player1.y))
    WIN.blit(sonic, (player2.x, player2.y))
    WIN.blit(ZOMBIE, (zombie.x, zombie.y))
    # update the display
    pygame.display.update()

def player1_movement(keys_pressed, player1):
        if keys_pressed[pygame.K_w]: # UP
            player1.y -= VEL
        if keys_pressed[pygame.K_a]: # LEFT
            player1.x -= VEL
        if keys_pressed[pygame.K_s]: # DOWN
            player1.y += VEL
        if keys_pressed[pygame.K_d]: # RIGHT
            player1.x += VEL

def player2_movement(keys_pressed, player2):
        if keys_pressed[pygame.K_UP]: # UP
            player2.y -= VEL
        if keys_pressed[pygame.K_LEFT]: # LEFT
            player2.x -= VEL
        if keys_pressed[pygame.K_DOWN]: # DOWN
            player2.y += VEL
        if keys_pressed[pygame.K_RIGHT]: # RIGHT
            player2.x += VEL

def zombie_movement(zombie, player1, player2):

    distPlayer1 = (abs(player1.x - zombie.x) ** 2 + abs(player1.y - zombie.y) ** 2) ** (1/2)
    distPlayer2 = (abs(player2.x - zombie.x) ** 2 + abs(player2.y - zombie.y) ** 2) ** (1/2)
    chasePlayer = player1
    if distPlayer1 > distPlayer2:
        chasePlayer = player2

    if zombie.x < chasePlayer.x:
        zombie.x += 1
    if zombie.x > chasePlayer.x:
        zombie.x -= 1
    if zombie.y < chasePlayer.y:
        zombie.y += 1
    if zombie.y > chasePlayer.y:
        zombie.y -= 1

def main():
    player1 = pygame.Rect(200, 200, CHAR_WIDTH, CHAR_HEIGHT)
    player2 = pygame.Rect(700, 200, CHAR_WIDTH, CHAR_HEIGHT)
    zombie = pygame.Rect(50, 50, 30, 30)
    clock = pygame.time.Clock()
    run = True
    while run:
        # control the frame rate
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        player1_movement(keys_pressed, player1)
        player2_movement(keys_pressed, player2)
        zombie_movement(zombie, player1, player2)
        draw_window(player1, player2, zombie)

    # shut down Pygame
    pygame.quit()

if __name__ == "__main__":
    main()