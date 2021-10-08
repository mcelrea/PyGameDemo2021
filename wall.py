import pygame

class Wall:
    #attributes - what a wall is
    x = 0
    y = 0
    width = 50
    height = 50
    color = (255,0,255)

    #constructor - how new walls are made
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    #functions - actions walls can do
    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y,self.width,self.height))

    def getCollisionRectangle(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)