

import pygame

import random

pygame.init()

#creating window
window = pygame.display.set_mode((800,600))

#title/icon
pygame.display.set_caption("Space Invaders Ripoff")
icon = pygame.image.load('img/space-invaders.png') # Icon made by Smashicons from www.flaticon.com
pygame.display.set_icon(icon)

#player code
playerImg = pygame.image.load('img/player.png') # Icon made by Freepik from www.flaticon.com
playerX = 370
playerY = 480
playerX_Change = 0

def player(x,y):
    window.blit(playerImg, (x, y))


#enemy code
enemyImg = pygame.image.load('img/alien.png') # Icon made by Smashicons from www.flaticon.com
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_Change = 0.3
enemyY_Change = 0

def enemy(x,y):
    window.blit(enemyImg, (x, y))

#game loop
running = True
while running:
    window.fill((255, 32, 214))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #catching key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left arrow pressed")
                playerX_Change = -0.3
            if event.key == pygame.K_RIGHT:
                print("right arrow pressed")
                playerX_Change = 0.3
        #catching key up
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("key released")
                playerX_Change = 0
    
    #player boundary check
    playerX += playerX_Change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #enemy boundary check and 
    enemyX += enemyX_Change

    if enemyX <= 0:
        enemyX_Change = 0.3
    elif enemyX >= 736:
        enemyX_Change = -0.3

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()