

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
    
    font = pygame.font.SysFont("comicsansms", 50)
    
    
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
                    
    
    captions = ["powrot", "lvl1", "lvl2", "lvl3", "lvl4", "lvl5", "lvl6", "lvl7", "lvl8"]
    buttons = ['']*9

    for i in range(len(buttons)):
        buttons[i] = font.render(captions[i], 1, (10, 10, 10))
        background.blit(buttons[i], (50, 100+50*i))
        
    active_button = 0
    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    
    
    # cheatujemy czy nie?
    with open(os.path.join('pyfiles', 'cheat.txt'), 'r') as ustaw:
        cheat = ustaw.readline().strip('\n\r')

    
    
    
    # funkcja zmieniajaca levele
    def change_button(updown):
        if updown == "down":
            if active_button < (len(buttons)-1)  and slownik[active_button][0] == 'T':
                return (active_button+1)
            else:
                return (active_button)
        else:
            if active_button > 0 and slownik[active_button-1][0] == 'T':
                return (active_button-1)
            else:
                return (active_button)
                
                
                
    # cheaterska funkcja zmieniajaca level
    def change_button_cheat(updown):
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
                    if cheat == 'N':
                        active_button = change_button("down")
                    else:
                        active_button = change_button_cheat("down")
                elif keys[pygame.K_UP]:
                    if cheat == 'N':
                        active_button = change_button("up")
                    else:
                        active_button = change_button_cheat("up")
                elif keys[pygame.K_RETURN]:
                    global path
                    if active_button == 1:
                        path = "level1.map"
                    elif active_button == 2:
                        path = "level2.map"
                    elif active_button == 3:
                        path = "level3.map"
                    elif active_button == 4:
                        path = "level4.map"
                    elif active_button == 5:
                        path = "level5.map"
                    elif active_button == 6:
                        path = "level6.map"
                    elif active_button == 7:
                        path = "level7.map"
                    elif active_button == 8:
                        path = "level8.map"
                    elif active_button == 9:
                        path = "level9.map"
                    elif active_button == 0:
                        exec(open(os.path.join('gamegui.py')).read())
                                        
                    exec(open(os.path.join('pyfiles', 'gameplay.py')).read(), globals())

        screen.blit(background, (0,0))
        
        buttons[active_button] = font.render(captions[active_button], 1, (250,10,255))
        
        screen.blit(buttons[active_button], (50,100+50*active_button))
                    
        pygame.display.flip()
        
if __name__ == '__main__':
    main()
