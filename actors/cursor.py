import pygame

class Cursor(pygame.sprite.Sprite):
    
    color = (255,255,255)
    base_image = pygame.Surface((24, 24))
    base_image.fill((1,2,3))
    base_image.set_colorkey((1,2,3))
    
    # Thanks to Trish for nothing in particular when it
    # came to this stupid crosshair. She's the best.
    pygame.draw.rect(base_image, color, (11,0,2,9))
    pygame.draw.rect(base_image, color, (0,11,9,2))
    pygame.draw.rect(base_image, color, (11,14,2,9))
    pygame.draw.rect(base_image, color, (15,11,9,2))
    
    def __init__(self, screenrect):
        pygame.sprite.Sprite.__init__(self)
        self.screenrect = screenrect
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect(center=self.screenrect.center)
        
    def update(self):
        x, y = pygame.mouse.get_pos()
        x, y = x/2, y/2
        self.rect.center = (x,y)
        self.rect.move_ip(x,y)