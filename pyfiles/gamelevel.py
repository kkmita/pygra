#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 22:35:04 2017

@author: kamil
"""

import pygame
import pygame.locals
import os
import configparser
import sys
import csv as csv


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Gra Sokoban - levele')
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))    
    
    font = pygame.font.SysFont("comicsansms", 72)
    
    
    # zaczytaj aktualny stan slownika!
    with open(os.path.join('pyfiles', 'settings.csv')) as csvfile:
        reader = csv.reader(csvfile)
        slownik = {}
        for row in reader:
            key = int(row[0])
            if key in slownik:
                pass
            else:
                slownik[key] = [row[1], int(row[2])]
                    
    
    captions = ["lvl1", "lvl2", "lvl3", "lvl4", "lvl5"]
    buttons = ['', '', '', '', '']

    for i in range(len(buttons)):
        buttons[i] = font.render(captions[i], 1, (10, 10, 10))
        background.blit(buttons[i], (50, 100+100*i))
        
    active_button = 0
    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    
    
    # funkcja zmieniajaca levele
    def change_button(updown):
        if updown == "down":
            if active_button < len(buttons) and slownik[active_button+1][0] == 'T':
                return (active_button+1)
            else:
                return (active_button)
        else:
            if active_button > 0 and slownik[active_button][0] == 'T':
                return (active_button-1)
            else:
                return (active_button)

        
    
    
    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return
            elif event.type == pygame.locals.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_DOWN]:
                    active_button = change_button("down")
                elif keys[pygame.K_UP]:
                    active_button = change_button("up")
                elif keys[pygame.K_RETURN]:
                    global path
                    if active_button == 0:
                        path = "level.map"
                    elif active_button == 1:
                        path = "level2.map"
                    exec(open(os.path.join('pyfiles', 'gameplay.py')).read(), globals())

        screen.blit(background, (0,0))
        
        buttons[active_button] = font.render(captions[active_button], 1, (250,10,255))
        
        screen.blit(buttons[active_button], (50,100+100*active_button))
                    
        pygame.display.flip()
        
if __name__ == '__main__':
    main()