import pygame
from math import *

class Player(pygame.sprite.Sprite):
    
    color = (255,255,0)
    thrust_value = 0.5
    turn_speed = 5
    max_speed = 6
    
    # draw base ship image
    base_image = pygame.Surface((20, 15))
    base_image.fill((1,2,3))
    base_image.set_colorkey((1,2,3))
    pointlist = [(0,0), (20,8), (0,15), (5,8)]
    pygame.draw.polygon(base_image, color, pointlist)
    
    def __init__(self, screenrect):
        pygame.sprite.Sprite.__init__(self)
        self.screenrect = screenrect
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect(center=self.screenrect.center)
        self.vx = 1
        self.vy = 0
        self.angle = 0
        
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
            
    def thrust(self):
        a = radians(self.angle)
        self.vx += self.thrust_value * cos(a)
        self.vy += self.thrust_value * sin(a)

        vel = sqrt(self.vx * self.vx + self.vy * self.vy)
        if (vel > self.max_speed):
            self.vx = self.vx * self.max_speed / vel
            self.vy = self.vy * self.max_speed / vel
        
    def turn(self, direction):
        self.angle += self.turn_speed * direction
        while (self.angle < 0):
            self.angle += 360
        while (self.angle >= 360):
            self.angle -= 360
            
        self.image = pygame.transform.rotate(self.base_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        
    def fire(self):
        print "fire"