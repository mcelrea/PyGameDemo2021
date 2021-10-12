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

    # functions: what a Bullet can do
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)