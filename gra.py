# ctrl+4, ctrl+5


import pygame
import sys
from pygame.locals import *



class IsoGame:

    
    class ludzik:
        def __init__(self, x, y, img):
            self.position_x = x
            self.position_y = y
            self.obraz = img
            
        def move(self, x, y):
            self.position_x += x
            self.position_y += y
         
            
    def __init__(self):
        pygame.init()
        DISPLAYSURF = pygame.display.set_mode((1000,1000), 0, 32)
        self.surface = pygame.display.set_mode((1000,1000), 0, 32)
        pygame.display.set_caption('oco')

        #FPS = 30
        #self.WHITE = (255, 255, 255)
            
        self.man = self.ludzik(50, 10, pygame.image.load('player.png'))
        
        self.loop()
        
        
        
    def loop(self):
        while True:
            
            self.game_refresh()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #man.position_x += 5
                        self.man.move(5, 0)
                    elif event.key == pygame.K_LEFT:
                        self.man.move(-5, 0)
                    elif event.key == pygame.K_UP:
                        self.man.move(0, -5)
                    elif event.key == pygame.K_DOWN:
                        self.man.move(0, 5)
                    
            self.game_refresh()
            pygame.display.flip()
            
            
    def game_refresh(self):
        self.surface.fill((255, 255, 255))
        self.surface.blit(self.man.obraz, (self.man.position_x, self.man.position_y))
            
if __name__ == '__main__':
    IsoGame()
        











