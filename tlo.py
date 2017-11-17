#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:45:49 2017

@author: kamil
"""

import pygame
import pygame.locals
import configparser


class Level:
    
    def load_file(self, filename = "level.map"):
        self.map = []
        self.key = {}
        parser = configparser.ConfigParser()
        parser.read(filename)
        
        #self.tileset = parser.get("level", "tileset")
        self.map = parser.get("level", "map").split("\n")
        
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
        
        
    def is_blocking(self, x, y):
        if not 0 <= x <= self.width or not 0 <= y <= self.height:
            return True
        return self.get_bool(x, y, 'block')
        
        
    def render(self):
        wall = self.is_wall
        
        MAP_TILE_WIDTH, MAP_TILE_HEIGHT = 64, 64
        tiles = [pygame.image.load('player.png'), pygame.image.load('block_01.png')]

        image = pygame.Surface((self.width*MAP_TILE_WIDTH, self.height*MAP_TILE_HEIGHT))
        
        overlays = {}

        for map_y, line in enumerate(self.map): # mapy_y to numer linii, line to wektorek znakow
            for map_x, c in enumerate(line):
                if wall(map_x, map_y):
                    if not wall(map_x, map_y+1):
                        if wall(map_x+1, map_y) and wall(map_x-1, map_y):
                            tile = 1
                        elif wall(map_x+1, map_y):
                            tile = 0
                        elif wall(map_x-1, map_y):
                            tile = 0
                        else:
                            tile = 1
                    else:
                        if wall(map_x+1, map_y+1) and wall(map_x-1, map_y+1):
                            tile = 0
                        elif wall(map_x+1, map_y+1):
                            tile = 1
                        elif wall(map_x-1, map_y+1):
                            tile = 0
                        else:
                            tile = 0
                    # Add overlays if the wall may be obscuring something
                    if not wall(map_x, map_y-1):
                        if wall(map_x+1, map_y) and wall(map_x-1, map_y):
                            over = 1
                        elif wall(map_x+1, map_y):
                            over = 0
                        elif wall(map_x-1, map_y):
                            over = 0
                        else:
                            over = 1
                        overlays[(map_x, map_y)] = tiles[over]
                else:
                    tile = 0
                
                tile_image = tiles[tile]

                image.blit(tile_image, (map_x*MAP_TILE_WIDTH, map_y*MAP_TILE_HEIGHT))
                
        return image, overlays

            
        
        

if __name__ == "__main__":
    screen = pygame.display.set_mode((1600, 1000))
    
    MAP_TILE_WIDTH = 64
    MAP_TILE_HEIGHT = 64
    
    level = Level()
    level.load_file("level.map")
    
    clock = pygame.time.Clock()
    
    
    
    background, overlay_dict = level.render()
    
    overlays = pygame.sprite.RenderUpdates()
    
    for (x,y), image in overlay_dict.items(): # iteritems():
        overlay = pygame.sprite.Sprite(overlays)
        overlay.image= image
        overlay.rect = image.get_rect().move(x * 64, y * 64 - 64)
        
    screen.blit(background, (0,0))
    overlays.draw(screen)

    pygame.display.flip()
    
    game_over = False
        
    while not game_over:
        overlays.draw(screen)
        pygame.display.flip()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                game_over = True
            elif event.type == pygame.locals.KEYDOWN:
                pressed_key = event.key