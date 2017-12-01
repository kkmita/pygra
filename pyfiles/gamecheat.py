#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 13:56:19 2017

@author: kamil
"""

import pygame
import pygame.locals
import os


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Gra Sokoban - levele')
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))    
    
    font = pygame.font.SysFont("comicsansms", 50)
    
    
    # zaczytaj aktualny stan slownika!

                    
    
    captions = ["cheatuj", "uczciwy", "powrot"]
    buttons = ['']*3

    for i in range(len(buttons)):
        buttons[i] = font.render(captions[i], 1, (10, 10, 10))
        background.blit(buttons[i], (50, 100+50*i))
    
        
    active_button = 0
    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    
    
    # cheatujemy czy nie?
    with open(os.path.join('pyfiles', 'cheat.txt'), 'r') as ustaw:
        cheat = ustaw.readline().strip('\n\r')

    
    def change_button(updown):
        if updown == "down":
            if active_button < (len(buttons)-1):
                return (active_button+1)
            else:
                return (active_button)
        else:
            if active_button > 0:
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
                    if active_button == 0:
                        #cheatuj
                        with open(os.path.join('pyfiles', 'cheat.txt'), 'w') as file:
                            file.write('Y')
                    elif active_button == 1:
                        with open(os.path.join('pyfiles', 'cheat.txt'), 'w') as file:
                            file.write('N')
                    elif active_button == 2:
                        exec(open(os.path.join('gamegui.py')).read())
                    else:
                        pass
    
    


        screen.blit(background, (0,0))
        
        buttons[active_button] = font.render(captions[active_button], 1, (250,10,255))
        
        screen.blit(buttons[active_button], (50,100+50*active_button))
                    
        pygame.display.flip()
        
if __name__ == '__main__':
    main()



