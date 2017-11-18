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


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Gra Sokoban - levele')
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))    
    
    font = pygame.font.SysFont("comicsansms", 72)
    
    
    captions = ["lvl1", "lvl2"]
    buttons = ['', '']

    for i in range(2):
        buttons[i] = font.render(captions[i], 1, (10, 10, 10))
        background.blit(buttons[i], (50, 100+100*i))
        
    active_button = 0
    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return
            elif event.type == pygame.locals.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    exec(open(os.path.join('pyfiles', 'gameplay.py')).read())
                
#==============================================================================
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_RETURN]:
#             exec(open(os.path.join('gameplay.py')).read())
#==============================================================================
                
                
        pygame.display.flip()
        
if __name__ == '__main__':
    main()