import pygame

class SimpleEnemy:

    #attributes or variables
    #what IS an enemy
    x = 0
    y = 0
    size = 15
    color = (255,100,100)
    speed = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.polygon(screen,self.color,
                            ((self.x,self.y),
                             (self.x-self.size,self.y+self.size),
                             (self.x+self.size,self.y+self.size)))

    def act(self, player):
        deltaX = abs(player.x - self.x)
        deltaY = abs(player.y - self.y)

        if (deltaX >= deltaY):
            #move closer in x-direction
            if(self.x > player.x):
                self.x -= self.speed #move left
            else:
                self.x += self.speed #move right
        else:
            #move closer in y-direction
            if(self.y > player.y):
                self.y -= self.speed #move up
            else:
                self.y += self.speed #move down

