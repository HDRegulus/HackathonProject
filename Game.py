import pygame
import os
import random
import numpy as np

WIDTH, HEIGHT = 1100, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")

PURPLE = (216, 191, 216)
FPS = 60
VEL = 5
CHAR_WIDTH, CHAR_HEIGHT = 70, 70

player1Alive = True
player2Alive = True

Player1Health = 100
Player2Health = 100



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
LetterA_Image = pygame.image.load(os.path.join('ASSETS', 'A.png'))
LetterA = pygame.transform.scale(LetterA_Image, (CHAR_WIDTH, CHAR_HEIGHT))
LetterE1_Image = pygame.image.load(os.path.join('ASSETS', 'E.png'))
LetterE1 = pygame.transform.scale(LetterE1_Image, (CHAR_WIDTH, CHAR_HEIGHT))
LetterE2_Image = pygame.image.load(os.path.join('ASSETS', 'E.png'))
LetterE2 = pygame.transform.scale(LetterE2_Image, (CHAR_WIDTH, CHAR_HEIGHT))
LetterG_Image = pygame.image.load(os.path.join('ASSETS', 'G.png'))
LetterG = pygame.transform.scale(LetterG_Image, (CHAR_WIDTH, CHAR_HEIGHT))
LetterM_Image = pygame.image.load(os.path.join('ASSETS', 'M.png'))
LetterM = pygame.transform.scale(LetterM_Image, (CHAR_WIDTH, CHAR_HEIGHT))
LetterO_Image = pygame.image.load(os.path.join('ASSETS', 'O.png'))
LetterO = pygame.transform.scale(LetterO_Image, (CHAR_WIDTH, CHAR_HEIGHT))
LetterR_Image = pygame.image.load(os.path.join('ASSETS', 'R.png'))
LetterR = pygame.transform.scale(LetterR_Image, (CHAR_WIDTH, CHAR_HEIGHT))
LetterV_Image = pygame.image.load(os.path.join('ASSETS', 'V.png'))
LetterV = pygame.transform.scale(LetterV_Image, (CHAR_WIDTH, CHAR_HEIGHT))


def draw_window(player1, player2, bad1, bad2, bad3, enemyArr):
    WIN.fill(PURPLE)
    WIN.blit(grass, (0, 0))
    if player1Alive == True:
        WIN.blit(charizard, (player1.x, player1.y))
    if player2Alive == True:
        WIN.blit(sonic, (player2.x, player2.y))
    for enemy in enemyArr:
        WIN.blit(rick, (enemy.x, enemy.y))
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
    global Player1Health, Player2Health
    global player1Alive, player2Alive
    if bad.x == player1.x:
        if bad.y == player1.y:
            Player1Health = Player1Health - 1
            if Player1Health <= 0:
                player1Alive = False
    if bad.x == player2.x:
        if bad.y == player2.y:
            Player2Health = Player2Health - 1
            if Player2Health <= 0:
                player2Alive = False

def gameOver(G, A, M, E, O, V, e, R):
    if player1Alive == False:
        if player2Alive == False:
            WIN.blit(LetterG, (G.x, G.y))
            WIN.blit(LetterA, (A.x, A.y))
            WIN.blit(LetterM, (M.x, M.y))
            WIN.blit(LetterE1, (E.x, E.y))
            WIN.blit(LetterO, (O.x, O.y))
            WIN.blit(LetterV, (V.x, V.y))
            WIN.blit(LetterE2, (e.x, e.y))
            WIN.blit(LetterR, (R.x, R.y))
    pygame.display.update()

def playerHealth(player1, player2):
    global Player1Health
    pygame.font.init()
    player1Font = pygame.font.Font('freesansbold.ttf', 20)
    player1Surface = player1Font.render('Player 1 Health: '+str(Player1Health), False, (0,0,0))
    WIN.blit(player1Surface,(0,0))
    player2Font = pygame.font.Font('freesansbold.ttf', 20)
    player2Surface = player2Font.render('Player 2 Health: ' + str(Player2Health), False, (0, 0, 0))
    WIN.blit(player2Surface, (0, 20))
    pygame.display.update()


def main():
    player1 = pygame.Rect(200, 200, CHAR_WIDTH, CHAR_HEIGHT)
    player2 = pygame.Rect(700, 200, CHAR_WIDTH, CHAR_HEIGHT)
    bad1 = pygame.Rect(0, 0, CHAR_WIDTH, CHAR_HEIGHT)
    bad2 = pygame.Rect(1030, 0, CHAR_WIDTH, CHAR_HEIGHT)
    bad3 = pygame.Rect(0, 530, CHAR_WIDTH, CHAR_HEIGHT)

    G = pygame.Rect(200, 200, CHAR_WIDTH, CHAR_WIDTH)
    A = pygame.Rect(300, 200, CHAR_WIDTH, CHAR_WIDTH)
    M = pygame.Rect(400, 200, CHAR_WIDTH, CHAR_WIDTH)
    E = pygame.Rect(500, 200, CHAR_WIDTH, CHAR_WIDTH)
    O = pygame.Rect(600, 200, CHAR_WIDTH, CHAR_WIDTH)
    V = pygame.Rect(700, 200, CHAR_WIDTH, CHAR_WIDTH)
    e = pygame.Rect(800, 200, CHAR_WIDTH, CHAR_WIDTH)
    R = pygame.Rect(900, 200, CHAR_WIDTH, CHAR_WIDTH)

    enemyArr = []

    clock = pygame.time.Clock()
    run = True
    spawnTime = 0
    while run:
        # control the frame rate
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if (player1Alive == True):
            player1_movement(keys_pressed, player1)
        if (player2Alive == True):
            player2_movement(keys_pressed, player2)
        draw_window(player1, player2, bad1, bad2, bad3, enemyArr)

        if spawnTime > 300:
            offset = 60
            randomArrSpawn = [pygame.Rect(random.randint(0, 1099), 0 - offset, CHAR_WIDTH, CHAR_HEIGHT),
                              pygame.Rect(0 - offset, random.randint(0, 599), CHAR_WIDTH, CHAR_HEIGHT),
                              pygame.Rect(1099 + offset, random.randint(0, 599), CHAR_WIDTH, CHAR_HEIGHT),
                              pygame.Rect(random.randint(0, 1099), 599 + offset, CHAR_WIDTH, CHAR_HEIGHT)]
            enemy = randomArrSpawn[random.randint(0,3)]
            enemyArr.append(enemy)
            spawnTime = 0

        for enemy in enemyArr:
            chasePlayer(player1, player2, enemy)
            hitPlayer(player1, player2, enemy)

        chasePlayer(player1, player2, bad1)
        chasePlayer(player1, player2, bad2)
        chasePlayer(player1, player2, bad3)

        hitPlayer(player1, player2, bad1)
        hitPlayer(player1, player2, bad2)
        hitPlayer(player1, player2, bad3)

        playerHealth(player1, player2)

        gameOver(G, A, M, E, O, V, e, R)

        spawnTime += 1

    # shut down Pygame
    pygame.quit()


if __name__ == "__main__":
    main()