import pygame
import os

WIDTH, HEIGHT = 1100, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")

PURPLE = (216, 191, 216)
FPS = 60
VEL = 5
CHAR_WIDTH, CHAR_HEIGHT = 70, 70

player1Alive = True
player2Alive = True

grass_Image = pygame.image.load(os.path.join('ASSETS', 'grass.png'))
grass = pygame.transform.scale(grass_Image, (WIDTH, HEIGHT))
charizard_Image = pygame.image.load(os.path.join('ASSETS', 'charizard.png'))
charizard = pygame.transform.scale(charizard_Image, (CHAR_WIDTH, CHAR_HEIGHT))
sonic_Image = pygame.image.load(os.path.join('ASSETS', 'sonic.png'))
sonic = pygame.transform.scale(sonic_Image, (CHAR_WIDTH, CHAR_HEIGHT))
enemy1_Image = pygame.image.load(os.path.join('ASSETS', 'enemy1.png'))
enemy1 = pygame.transform.scale(enemy1_Image, (CHAR_WIDTH, CHAR_HEIGHT))
enemy2_Image = pygame.image.load(os.path.join('ASSETS', 'enemy2.png'))
enemy2 = pygame.transform.scale(enemy2_Image, (CHAR_WIDTH, CHAR_HEIGHT))
rick_Image = pygame.image.load(os.path.join('ASSETS', 'rick.png'))
rick = pygame.transform.scale(rick_Image, (CHAR_WIDTH, CHAR_HEIGHT))


def draw_window(player1, player2, bad1, bad2, bad3):
    WIN.fill(PURPLE)
    WIN.blit(grass, (0, 0))
    if player1Alive == True:
        WIN.blit(charizard, (player1.x, player1.y))
    if player2Alive == True:
        WIN.blit(sonic, (player2.x, player2.y))
    WIN.blit(enemy1, (bad1.x, bad1.y))
    WIN.blit(enemy2, (bad2.x, bad2.y))
    WIN.blit(rick, (bad3.x, bad3.y))
    # update the display
    pygame.display.update()


def player1_movement(keys_pressed, player1):
    if keys_pressed[pygame.K_w] and player1.y - VEL > 0:  # UP
        player1.y -= VEL
    if keys_pressed[pygame.K_a] and player1.x - VEL > 0:  # LEFT
        player1.x -= VEL
    if keys_pressed[pygame.K_s] and player1.y + VEL + player1.height < HEIGHT:  # DOWN
        player1.y += VEL
    if keys_pressed[pygame.K_d] and player1.x + VEL + player1.width < WIDTH:  # RIGHT
        player1.x += VEL


def player2_movement(keys_pressed, player2):
    if keys_pressed[pygame.K_UP] and player2.y - VEL > 0:  # UP
        player2.y -= VEL
    if keys_pressed[pygame.K_LEFT] and player2.x - VEL > 0:  # LEFT
        player2.x -= VEL
    if keys_pressed[pygame.K_DOWN] and player2.y + VEL + player2.height < HEIGHT:  # DOWN
        player2.y += VEL
    if keys_pressed[pygame.K_RIGHT] and player2.x + VEL + player2.width < WIDTH:  # RIGHT
        player2.x += VEL


def chasePlayer(player1, player2, bad):
    distPlayer1 = (abs(player1.x - bad.x) ** 2 + abs(player1.y - bad.y) ** 2) ** (1 / 2)
    distPlayer2 = (abs(player2.x - bad.x) ** 2 + abs(player2.y - bad.y) ** 2) ** (1 / 2)

    if player1Alive == True:
        chasePlayer = player1
    else:
        chasePlayer = player2

    if distPlayer1 > distPlayer2:
        if player2Alive == True:
            chasePlayer = player2
    if bad.x < chasePlayer.x:
        bad.x += 1
    if bad.x > chasePlayer.x:
        bad.x -= 1
    if bad.y < chasePlayer.y:
        bad.y += 1
    if bad.y > chasePlayer.y:
        bad.y -= 1


def hitPlayer(player1, player2, bad):
    global player1Alive, player2Alive
    if bad.x == player1.x:
        if bad.y == player1.y:
            player1Alive = False

    if bad.x == player2.x:
        if bad.y == player2.y:
            player2Alive = False


def main():
    player1 = pygame.Rect(200, 200, CHAR_WIDTH, CHAR_HEIGHT)
    player2 = pygame.Rect(700, 200, CHAR_WIDTH, CHAR_HEIGHT)
    bad1 = pygame.Rect(0, 0, CHAR_WIDTH, CHAR_HEIGHT)
    bad2 = pygame.Rect(1030, 0, CHAR_WIDTH, CHAR_HEIGHT)
    bad3 = pygame.Rect(0, 530, CHAR_WIDTH, CHAR_HEIGHT)

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
        draw_window(player1, player2, bad1, bad2, bad3)

        chasePlayer(player1, player2, bad1)
        chasePlayer(player1, player2, bad2)
        chasePlayer(player1, player2, bad3)

        hitPlayer(player1, player2, bad1)
        hitPlayer(player1, player2, bad2)
        hitPlayer(player1, player2, bad3)

    # shut down Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
