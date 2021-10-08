import pygame
from player import *
from wall import *

#start the pygame engine
pygame.init()

#game variables
gameOver = False
p1 = Player(100,200,(0,255,0))
wall1 = Wall(500,300,200,40,(255,255,255))
wall2 = Wall(600,100,40,200,(255,255,0))

#game independent variables (needed for every pygame)
FPS = 60 #60 Frames Per Second for the game update cycle
fpsClock = pygame.time.Clock() #used to lock the game to 60 FPS
screen = pygame.display.set_mode((1280,720)); #initialize the game window

def clear_screen():
    pygame.draw.rect(screen, (0,0,0), (0, 0, 1280, 720))

def checkPlayerInput():
    global p1
    global wall1
    oldx = p1.getX()
    oldy = p1.getY()

    pressed = pygame.key.get_pressed() #all the keys that have been pressed
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        p1.moveRight()
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        p1.moveLeft()
    if pressed[pygame.K_w]  or pressed[pygame.K_UP]:
        p1.moveUp()
    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        p1.moveDown()

    if p1.getCollisionRectangle().colliderect(wall1.getCollisionRectangle()):
        p1.changePosition(oldx,oldy)
    if p1.getCollisionRectangle().colliderect(wall2.getCollisionRectangle()):
        p1.changePosition(oldx,oldy)




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
    wall1.draw(screen)
    wall2.draw(screen)

    #put all the graphics on the screen
    #should be the LAST LINE of game code
    pygame.display.flip()
    fpsClock.tick(FPS) #slow the loop down to 60 loops per second
