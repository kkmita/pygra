#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:45:49 2017

@author: kamil
"""

import pygame
import pygame.locals
import configparser
import sys
import os


class IsoGame:
    
    
    
    class Gracz(pygame.sprite.Sprite):
        
        def __init__(self, xpos, ypos):
            pygame.sprite.Sprite.__init__(self) #Self.groups?
            self.image = pygame.image.load(os.path.join('../pictures','player.png'))
            self.rect = self.image.get_rect(x = xpos, y = ypos)
            
            
        def move(self, xmove, ymove):
            self.rect.move_ip(xmove, ymove)
            
    
    
    
    class Level:
        
        def load_file(self, filename = "pyfiles/ level.map"):
            self.map = []
            self.key = {}
            try:
                parser = configparser.ConfigParser()
            except ValueError:
                print("TO TU")
            try:
                parser.read(filename)
            except ValueError:
                print("TO TU 2")
            
            #self.tileset = parser.get("level", "tileset")
            try:
                self.map = parser.get("level", "map").split("\n")
            except ValueError:
                print("OOO")
            else:
                print("DUPA")
            
            for section in parser.sections():
                if len(section) == 1:
                    desc = dict(parser.items(section))
                    self.key[section] = desc
    
            self.width = len(self.map[0])
            self.height = len(self.map)
            
            
        def get_tile(self, x, y):
            try:
                char = self.map[y][x]
            except IndexError:
                return {}
            try:
                return self.key[char]
            except KeyError:
                return {}
    
    
        # name to NAME:VALUE z pliku konfiguracyjnego
        # patrzymy, czy wartosc zwrocona przez name zawiera sie w danym zbiorze
        def get_bool(self, x, y, name):
            value = self.get_tile(x, y).get(name)
            return value in (True, 1, 'true', 'yes', 'True', 'Yes', '1', 'on', 'On')
            
        
        def is_wall(self, x, y):
            return self.get_bool(x, y, 'wall')
            
            
    #==============================================================================
    #     def is_blocking(self, x, y):
    #         if not 0 <= x <= self.width or not 0 <= y <= self.height:
    #             return True
    #         return self.get_bool(x, y, 'block')
    #==============================================================================
    
            
        def render_background(self):
            
            
            """
            ta funkcja zwraca backgroundowy obiekt Surface, tj.
            wylicza wymiary mapy i wrzuca podloge oraz sciany w
            return image
            """
            
            #wall = self.is_wall
            
            MAP_TILE_WIDTH, MAP_TILE_HEIGHT = 64, 64
            
            tiles = [pygame.image.load(os.path.join('../pictures', 'ground_06.png')), 
                     pygame.image.load(os.path.join('../pictures', 'block_01.png')) ]
     
    
            image = pygame.Surface((self.width*MAP_TILE_WIDTH, self.height*MAP_TILE_HEIGHT))
            
            #overlays = {}
            
    
            for map_y, line in enumerate(self.map): # mapy_y to numer linii, line to wektorek znakow
                for map_x, c in enumerate(line):
                    if self.get_tile(map_x, map_y)['name'] == 'wall':
                        tile = 1
                    else:
                        tile = 0
                        if self.get_tile(map_x, map_y)['name'] == 'player':
                            _gracz_startpos = (map_x, map_y)
                            
                    
                    tile_image = tiles[tile]
    
                    image.blit(tile_image, (map_x*MAP_TILE_WIDTH, map_y*MAP_TILE_HEIGHT))
                    
            return image, _gracz_startpos

        
    #def render_objects(self)
            
        
    
 #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#   
    
    def __init__(self):
        pygame.init()
        #screen = pygame.display.set_mode((100,100))
        
        
        #ustawienia mapek i tak dalej
        self.MAP_TILE_WIDTH, self.MAP_TILE_HEIGHT = 64, 64
        
        #ustawienie buforu na grafike
        self.screen = pygame.display.set_mode((1600, 1000))

        self.level = self.Level()
        #self.level.load_file()
        self.sciezka_nazw = os.path.join("pyfiles","level.map")
        self.level.load_file(self.sciezka_nazw)
        
        self.clock = pygame.time.Clock()
        
        
        self.background, self.gracz_startpos = self.level.render_background()
        
        self.allgroup = pygame.sprite.Group()
        
        self.gracz1 = self.Gracz(xpos = self.gracz_startpos[0]*64, ypos = self.gracz_startpos[1]*64)
        self.gracz1.add(self.allgroup)
    
    
        self.screen.blit(self.background, (0, 0))
        self.allgroup.draw(self.screen)
        
        pygame.display.flip()
    
    
        self.loop()
        
        
    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
                    
if __name__ == '__main__':
    IsoGame()                   
                    
                    
#==============================================================================
#     screen.blit(background, (0,0))
#     allgroup.draw(screen)
# 
#     pygame.display.flip()
#     
#     game_over = True
#         
#     while game_over:
#         #overlays.draw(screen)
#         pygame.display.flip()
#         clock.tick(55)
#         for event in pygame.event.get():
#             if event.type == pygame.locals.QUIT:
#                 game_over = False
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.locals.KEYDOWN:
#                 #pressed_key = event.key
#                 keys = pygame.key.get_pressed()
#                 if keys[pygame.K_DOWN]:
#                     gracz1.move(0,64)
#                 elif keys[pygame.K_UP]:
#                     gracz1.move(0,-64)
#                 elif keys[pygame.K_RIGHT]:
#                     gracz1.move(64,0)
#                 elif keys[pygame.K_LEFT]:
#                     gracz1.move(-64,0)
#             allgroup.clear(screen, background)
#             allgroup.draw(screen)
#==============================================================================
                
                
                
                
                
                
                
                
                