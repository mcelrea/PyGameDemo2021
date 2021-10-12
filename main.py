import pygame
from player import *
from wall import *
from bullet import *

#start the pygame engine
pygame.init()

#game variables
gameOver = False
p1 = Player(100,200,(0,255,0))
walls = [] #create a LIST where I can store EVERY wall
player_bullets = [] #create a LIST where I can store EVERY player bullet on the screen

#game independent variables (needed for every pygame)
FPS = 60 #60 Frames Per Second for the game update cycle
fpsClock = pygame.time.Clock() #used to lock the game to 60 FPS
screen = pygame.display.set_mode((1280,720)); #initialize the game window

def create_level_1():
    global walls
    walls.clear() #empty the list out
    walls.append(Wall(200,300,30,100,(255,0,0)))
    walls.append(Wall(500,0,300,5,(0,0,255)))
    walls.append(Wall(40,400,50,50,(50,100,255)))

#Abstraction: It will use a list, for loop and if statements
def check_for_wall_collision():
    for i in range(len(walls)):
        if p1.getCollisionRectangle().colliderect(walls[i].getCollisionRectangle()):
            return True #found a collision

    return False #no collision


# abstraction: a piece of code that solves a particular problem
#              and is resuseble. Preferable contains for loops and ifs
def draw_walls():
    for i in range(len(walls)):
        walls[i].draw(screen)

def draw_player_bullets():
    for i in range(len(player_bullets)):
        player_bullets[i].draw(screen)

def clear_screen():
    pygame.draw.rect(screen, (0,0,0), (0, 0, 1280, 720))

def checkPlayerInput():
    global p1
    global wall1
    oldx = p1.getX()
    oldy = p1.getY()

    pressed = pygame.key.get_pressed() #all the keys that have been pressed

    #MOVE PLAYER
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        p1.moveRight()
        if check_for_wall_collision() == True:
            p1.moveLeft() #undo the move right
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        p1.moveLeft()
        if check_for_wall_collision() == True:
            p1.moveRight() #undo the move left
    if pressed[pygame.K_w]  or pressed[pygame.K_UP]:
        p1.moveUp()
        if check_for_wall_collision() == True:
            p1.moveDown() #undo the move up
    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        p1.moveDown()
        if check_for_wall_collision() == True:
            p1.moveUp() #undo the move down

    if pressed[pygame.K_SPACE]:
        player_bullets.append(Bullet(p1.x, p1.y))


create_level_1()
#main while loop
while not gameOver:
    #loop through and empty the event queue, key presses
    #buttons, clicks, etc.
    for event in pygame.event.get():
        #if the event is a click on the "X" close button
        if event.type == pygame.QUIT:
            gameOver = True

    #(1) Check for player input
    checkPlayerInput()

    #(2) A.I. - Artificial Intelligence

    #(3) Check for collisions

    #(4) Draw everything to the screen
    clear_screen()
    p1.draw(screen)
    draw_walls()
    draw_player_bullets()

    #put all the graphics on the screen
    #should be the LAST LINE of game code
    pygame.display.flip()
    fpsClock.tick(FPS) #slow the loop down to 60 loops per second
