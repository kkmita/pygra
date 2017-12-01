
import pygame
import pygame.locals
import os
import sys
import configparser
import csv


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Gra Sokoban')
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))    
    
    font = pygame.font.SysFont("comicsansms", 72)
    
    
    captions = ["Play", "Zmien uczciwosc"]
    buttons = [0, 0]

    for i in range(2):
        buttons[i] = font.render(captions[i], 1, (10, 10, 10))
        background.blit(buttons[i], (50, 100+100*i))
        
    active_button = 0
    

    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    
    
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
                        exec(open(os.path.join('pyfiles', 'gamelevel.py')).read())
                    elif active_button == 1:
                        exec(open(os.path.join('pyfiles', 'gamecheat.py')).read())
                        
        screen.blit(background, (0,0))
        
        buttons[active_button] = font.render(captions[active_button], 1, (250,10,255))
        
        screen.blit(buttons[active_button], (50,100+100*active_button))
                    
        pygame.display.flip()
                    

                
#==============================================================================
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_RETURN]:
#             exec(open(os.path.join('pyfiles', 'gamelevel.py')).read())
#==============================================================================
                
                
        pygame.display.flip()
        
if __name__ == '__main__':
    main()
