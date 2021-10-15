import pygame

class Bullet:

    # attributes, what a Bullet is
    x = 0
    y = 0
    color = (255,255,255)
    radius = 5
    xvel = 0 #x-velocity of the bullet
    yvel = 0 #y-velocity of the bullet

    # constructor: how new Bullets get made
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, x, y, xvel, yvel):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel

    def getCollisionRectangle(self):
        return pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)

    # functions: what a Bullet can do
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        #the next two lines will draw the collision rectangle for debugging purposes
        #myRect = self.getCollisionRectangle()
        #pygame.draw.rect(screen, (255,0,0), myRect, 1)

    def update(self):
        self.x += self.xvel
        self.y += self.yvel

    def isOnScreen(self):
        if self.x + self.radius*2 < 0 or self.y + self.radius*2 < 0 or self.x > 1280 or self.y > 720:
            return False
        else:
            return True