import pygame

class Player:

    #class attributes for every player
    #what a player IS
    size = 20 #20 pixels
    color = (255,0,0) #RED
    x = 0
    y = 0
    speed = 3 #3 pixels per update

    #constructor: how a Player MUST be declared with (x,y) and color
    #This is a SPECIAL Function you MUST write for every Object
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    #this function will draw the player to the screen
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def moveRight(self):
        self.x += self.speed

    def moveLeft(self):
        self.x -= self.speed

    def moveUp(self):
        self.y -= self.speed

    def moveDown(self):
        self.y += self.speed

    def getCollisionRectangle(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def getX(self):
        return self.x;

    def getY(self):
        return self.y;

    def changePosition(self,x,y):
        self.x = x
        self.y = y