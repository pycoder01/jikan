#!/usr/bin/python
import os
import pygame
import random
from pygame.locals import *
from math import *

import actors.asteroid
import actors.player
import actors.cursor

WINFLAGS = 0
SCREENRECT = Rect(0, 0, 800, 600)
FPS = 30
NSTARS = 100
NASTEROIDS = 10
MUSIC = os.path.isfile('bgm.ogg')


# Colors
COLORS = {
    'BG': (0,0,0),
    'FG': (255,255,255),
    }

def main():
    pygame.init()
    score = 0
    screen = pygame.display.set_mode(SCREENRECT.size, WINFLAGS)
    
    background = pygame.Surface(SCREENRECT.size)
    background.fill(COLORS['BG'])
    for i in range(0, NSTARS):
        x = random.randint(0, SCREENRECT.width-1)
        y = random.randint(0, SCREENRECT.height-1)
        pygame.draw.circle(background, COLORS['FG'], (x,y), 0)
        
    screen.blit(background, (0,0))
    pygame.display.update()
    render = pygame.sprite.RenderUpdates()
    
    # create player
    player = actors.player.Player(SCREENRECT)
    render.add(player)
    
    # create mouse cursor
    cursor = actors.cursor.Cursor(SCREENRECT)
    pygame.mouse.set_visible(False)
    render.add(cursor)
    
    # create score text
    font = pygame.font.SysFont('Courier New', 17)
    text = font.render('Score: %s' % score, True, COLORS['FG'])
    textRect = text.get_rect()
    textRect.topleft = (10, 5)
    
    # create asteroids
    asteroids = pygame.sprite.Group()
    for i in range(0, NASTEROIDS):
        asteroid = actors.asteroid.Asteroid(SCREENRECT)
        render.add(asteroid)
        asteroids.add(asteroid)
    
    # clock, to limit framerate
    clock = pygame.time.Clock()
    
    # load BGM
    if MUSIC: pygame.mixer.music.load('bgm.ogg')
    
    while True:
        # check bgm and restart if needed
        if MUSIC and pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.rewind()
            pygame.mixer.music.play()
        
        # tick
        clock.tick(FPS)
        
        # get events
        for event in pygame.event.get():
            if event.type == QUIT or \
            (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
        
        # handle player actions
        keystate = pygame.key.get_pressed()
        if (keystate[K_UP] or keystate[ord('w')]):
            player.thrust()

        direction = (keystate[K_RIGHT] or keystate[ord('d')]) - (keystate[K_LEFT] or keystate[ord('a')])
        if (direction != 0):
            player.turn(direction)

        if (keystate[K_SPACE]):
            player.fire()
        
        # detect collisions, create a new asteroid when one is destroyed
        for asteroid in pygame.sprite.spritecollide(player, asteroids, False):
            asteroid.kill()
            new = actors.asteroid.Asteroid(SCREENRECT)
            render.add(new)
            asteroids.add(new)
            score += 10
        
        # render scene
        render.update()
        render.clear(screen, background)
        
        # display score - BROKEN!
        text = font.render('Score: %s' % score, True, COLORS['FG'])
        textRect = text.get_rect()
        textRect.topleft = (10, 5)
        screen.blit(text, textRect)
        
        dirty = render.draw(screen)
        pygame.display.update(dirty)
        
if __name__ == '__main__': main()