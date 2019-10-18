import pygame
import math
import random

pygame.init()

#creating window
window = pygame.display.set_mode((800,600))

background =  pygame.image.load('img/background.jpg')

#title/icon
pygame.display.set_caption("Space Invaders Ripoff Clone Thing")
icon = pygame.image.load('img/space-invaders.png') # Icon made by Smashicons from www.flaticon.com
pygame.display.set_icon(icon)


score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
endFont = pygame.font.Font('freesansbold.ttf', 64)

def gameOver():
    over = endFont.render("GAME OVER", True, (255,255,255))
    window.blit(over, (200, 250))


def showScore(x,y):
    scoreDisplay = font.render("Score: " + str(score), True, (255,255,255))
    window.blit(scoreDisplay, (x, y))

#player code
playerImg = pygame.image.load('img/player.png') # Icon made by Freepik from www.flaticon.com
playerX = 370
playerY = 480
playerX_Change = 0

def player(x,y):
    window.blit(playerImg, (x, y))


#enemy code
enemyImg = []
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = []
numEnemies = 6
for enemy in range(numEnemies):
    enemyImg.append(pygame.image.load('img/alien.png')) # Icon made by Smashicons from www.flaticon.com
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_Change.append(2)
    enemyY_Change.append(40)

def enemy(x,y, i):
    window.blit(enemyImg[i], (x, y))

#bullet code
bulletImg = pygame.image.load('img/github.png') # Icon made by Smashicons from www.flaticon.com
bulletX = 0
bulletY = 480
bulletY_Change = 20
bullet_State = "ready"

def fire(x,y):
    global bullet_State 
    bullet_State = "fire"
    window.blit(bulletImg,(x + 16 , y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    return False


#game loop
running = True
while running:
    window.fill((0, 0, 0))
    window.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #catching key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left arrow pressed")
                playerX_Change = -5
            if event.key == pygame.K_RIGHT:
                print("right arrow pressed")
                playerX_Change = 5
            if event.key == pygame.K_SPACE:
                print("space pressed")
                if bullet_State is "ready":                    
                    bulletX = playerX
                    fire(bulletX, bulletY)
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

    #enemy boundary check 
    for i in range(numEnemies): 

        #game over
        if enemyY[i] > 200:
            for j in range(numEnemies):
                enemyY[j] = 2000
            gameOver()
            break
        enemyX[i] += enemyX_Change[i]

        if enemyX[i] <= 0:
            enemyX_Change[i] = 2
            enemyY[i] += enemyY_Change[i]
        elif enemyX[i] >= 736:
            enemyX_Change[i] = -2
            enemyY[i] += enemyY_Change[i]

        #collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_State = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

     #bullet stuff
    if bulletY <= 0:
        bulletY = 480
        bullet_State = "ready"
    if bullet_State is "fire":
        fire(bulletX, bulletY)
        bulletY -= bulletY_Change


    
    player(playerX, playerY)
    showScore(10, 10)
    pygame.display.update()