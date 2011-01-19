import pygame
import random
from math import *

class Asteroid(pygame.sprite.Sprite):
    
    color = (0,255,0)
    min_speed = 2
    max_speed = 4
    
    # draw an asteroid
    base_image = pygame.Surface((40,50))
    base_image.fill((1,2,3))
    base_image.set_colorkey((1,2,3))
    pointlist = [(10,0), (30,0), (40,15), (35,25), (20,50), (5,50), (0,25)]
    pygame.draw.polygon(base_image, color, pointlist)

    def __init__(self, screenrect):
        self.screenrect = screenrect
        pygame.sprite.Sprite.__init__(self)

        self.image = self.base_image.copy()

        x = int(self.screenrect.width * random.random())
        y = int(self.screenrect.height * random.random())
        self.rect = self.image.get_rect(center=(x,y))

        velocity = random.randint(self.min_speed, self.max_speed)
        angle = 2.0 * pi * random.random()
        self.vx = cos(angle) * velocity
        self.vy = sin(angle) * velocity

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        self.wrap()

    def wrap(self):
        if (self.rect.center[0] < 0):
            self.rect.move_ip(self.screenrect.width, 0)
        elif (self.rect.center[0] >= self.screenrect.width):
            self.rect.move_ip(-self.screenrect.width, 0)        

        if (self.rect.center[1] < 0):
            self.rect.move_ip(0, self.screenrect.height)
        elif (self.rect.center[1] >= self.screenrect.height):
            self.rect.move_ip(0, -self.screenrect.height)