#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 13:10:30 2017

@author: kamil
"""


import pygame
import pygame.locals
import configparser
import sys
import os


class IsoGame:
    
    
    class Tekst(pygame.sprite.Sprite):
        def __init__(self, xpos, ypos, text, size, width, height):
            pygame.sprite.Sprite.__init__(self)
            self.font = pygame.font.SysFont("Arial", size)
            self.textSurf = self.font.render(text, 1, (255, 255, 0))
            self.image = pygame.Surface((width, height))
            W = self.textSurf.get_width()
            H = self.textSurf.get_height()
            self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
            self.rect = self.image.get_rect(x = xpos, y = ypos)
    
    
    class Gracz(pygame.sprite.Sprite):
        
        def __init__(self, xpos, ypos):
            pygame.sprite.Sprite.__init__(self) #Self.groups?
            self.image = pygame.image.load(os.path.join('../pictures','player.png'))
            self.rect = self.image.get_rect(x = xpos, y = ypos)
            
            
        def move(self, xmove, ymove, somescreen):
            # sprawdz czy nie trafiasz w ograniczenia
            self.rect.move_ip(xmove, ymove)
            if (self.rect.bottom > somescreen.bottom or
                self.rect.right > somescreen.right or
                self.rect.left < somescreen.left or
                self.rect.top < somescreen.top):
                self.rect.move_ip(-xmove, -ymove)
            elif self.czy_kolizja(grupa=wallsgroup) != None:
                self.rect.move_ip(-xmove, -ymove)

                                        
        def czy_kolizja(self, grupa):
            lista_sprite = pygame.sprite.spritecollide(self, grupa, dokill = False)
            if len(lista_sprite) == 0:
                return None
            else:
                return lista_sprite[0]
            
            
            
            
    class Pudlo(pygame.sprite.Sprite):
        
        def __init__(self, xpos, ypos):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(os.path.join('../pictures', 'crate_04.png'))
            self.rect = self.image.get_rect(x = xpos, y = ypos)
            
            
        def move(self, xmove, ymove, somescreen):
            self.rect.move_ip(xmove, ymove)
            if (self.rect.bottom > somescreen.bottom or
                self.rect.right > somescreen.right or
                self.rect.left < somescreen.left or
                self.rect.top < somescreen.top):
                self.rect.move_ip(-xmove, -ymove)                
            elif self.czy_kolizja(grupa=wallsgroup) != None:
                self.rect.move_ip(-xmove, -ymove)
            #elif self.czy_kolizja(grupa=boxgroup) != None:
            #    self.rect.move_ip(-xmove, -ymove)
            elif self.czy_kolizja_box() != None:
                self.rect.move_ip(-xmove, -ymove)

                                        
        def czy_kolizja(self, grupa):
            lista_sprite = pygame.sprite.spritecollide(self, grupa, dokill = False)
            if len(lista_sprite) == 0:
                return None
            else:
                return lista_sprite[0]     

#==============================================================================
#         def czy_kolizja_box(self):
#             if pygame.sprite.spritecollideany(self, self.groups().pop()) == None:
#                 return None
#             else:
#                 return 1
#==============================================================================
        def czy_kolizja_box(self):
            _grupa = self.groups().pop()
            self.remove(_grupa)
            if pygame.sprite.spritecollideany(self, _grupa) == None:
                self.add(_grupa)
                return None
            else:
                self.add(_grupa)
                return 1
           
            
                
                
    class Wall(pygame.sprite.Sprite):
        
        def __init__(self, xpos, ypos):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(os.path.join('../pictures', 'block_01.png'))
            self.rect = self.image.get_rect(x = xpos, y = ypos)
            
            
    class Goal(pygame.sprite.Sprite):
        
        def __init__(self, xpos, ypos):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(os.path.join('../pictures', 'ground_03.png'))
            self.rect = self.image.get_rect(x = xpos, y = ypos)
    
    
    class Level:
        
        def load_file(self, filename = "level.map"):
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
    
            
        def render_background(self, tiles):
            
            
            """
            ta funkcja zwraca backgroundowy obiekt Surface, tj.
            wylicza wymiary mapy i wrzuca podloge oraz sciany w
            return image
            """
            
            #wall = self.is_wall
            
            MAP_TILE_WIDTH, MAP_TILE_HEIGHT = 64, 64
            
#==============================================================================
#             tiles = [pygame.image.load(os.path.join('../pictures', 'ground_06.png')), 
#                      pygame.image.load(os.path.join('../pictures', 'block_01.png')) ]
#==============================================================================
     
    
            image = pygame.Surface((self.width*MAP_TILE_WIDTH, self.height*MAP_TILE_HEIGHT))
            
            #overlays = {}
            
    
            for map_y, line in enumerate(self.map): # mapy_y to numer linii, line to wektorek znakow
                for map_x, c in enumerate(line):
                    if self.get_tile(map_x, map_y)['name'] == 'wall':
                        tile = 1
                    elif self.get_tile(map_x, map_y)['name'] == 'goal':
                        tile = 2
                    else:
                        tile = 0
                        
                    tile_image = tiles[tile]
    
                    image.blit(tile_image, (map_x*MAP_TILE_WIDTH, map_y*MAP_TILE_HEIGHT))
                    
            return image

        

        def render_objects(self):
            
            walls = []
            goals = []
            boxes_startpos = []
            
            for map_y, line in enumerate(self.map): # mapy_y to numer linii, line to wektorek znakow
                for map_x, c in enumerate(line):
                    if self.get_tile(map_x, map_y)['name'] == 'wall':
                        walls.append((map_x, map_y))
                    elif self.get_tile(map_x, map_y)['name'] == 'box':
                        boxes_startpos.append((map_x, map_y))
                    elif self.get_tile(map_x, map_y)['name'] == 'goal':
                        goals.append((map_x, map_y))
                    elif self.get_tile(map_x, map_y)['name'] == 'player':
                        _gracz_startpos = (map_x, map_y)

            return _gracz_startpos, boxes_startpos, walls, goals
            
        
    
 #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#   
    
    def __init__(self):
        pygame.init()
        #screen = pygame.display.set_mode((100,100))
        
        
        # ustawienie textu

        
        
        
        # zmienne - szerokosc/wysokosc obiektow
        self.MAP_TILE_WIDTH, self.MAP_TILE_HEIGHT = 64, 64
        MAP_TILE_WIDTH, MAP_TILE_HEIGHT = self.MAP_TILE_WIDTH, self.MAP_TILE_HEIGHT
        
        
        # ustawienie buforu na grafike
        self.screen = pygame.display.set_mode((1600, 1000))
        screen = self.screen

        
        # budowa obietku Level
        
        self.level = self.Level()
        level = self.level
 
        #self.sciezka_nazw = os.path.join("pyfiles","level.map")
        #self.sciezka_nazw = "level.map"
        #self.level.load_file(self.sciezka_nazw)
        
        self.sciezka_nazwa = "level.map"
        level.load_file(self.sciezka_nazwa)
        
        
        # zegar
        self.clock = pygame.time.Clock()
        
        
        #graniczne punkty
        self.bound_y_d = self.level.height * self.MAP_TILE_HEIGHT
        self.bound_x_p = self.level.width * self.MAP_TILE_WIDTH
        
        bound_y_d, bound_x_p = self.bound_y_d, self.bound_x_p
        
        
        
        
        # tworzymy obiekt BACKGROUND
        
        self.tiles = [pygame.image.load(os.path.join('../pictures', 'ground_06.png')), 
                      pygame.image.load(os.path.join('../pictures', 'block_01.png')),
                      pygame.image.load(os.path.join('../pictures', 'ground_03.png'))]

        tiles = self.tiles


#==============================================================================
#         self.background, self.gracz_startpos, self.pudlo_startpos = self.level.render_background(self.tiles)
#         background, gracz_startpos, pudlo_startpos = self.background, self.gracz_startpos, self.pudlo_startpos
#==============================================================================
        
        self.background = self.level.render_background(self.tiles)
        background = self.background

        gracz_startpos, boxes_startpos, walls_pos, goals_pos = level.render_objects()

        
        # grupy spriteow
        
        self.allgroup = pygame.sprite.Group()
        self.boxgroup = pygame.sprite.Group()
        self.wallsgroup = pygame.sprite.Group()
        self.goalsgroup = pygame.sprite.Group()
        self.Tekstgroup = pygame.sprite.Group()
        
        global wallsgroup
        allgroup, boxgroup, wallsgroup, goalsgroup = self.allgroup, self.boxgroup, self.wallsgroup, self.goalsgroup
        
        
        # tworzymy gracza
        
        self.gracz1 = self.Gracz(xpos = gracz_startpos[0]*64, ypos = gracz_startpos[1]*64)
        gracz1 = self.gracz1
        
        gracz1.add(allgroup)
        
#!+++++++++++++++++++++++++++++++++++++++
#!+++++++++++++++++++++++++++++++++++++++
#!+++++++++++++++++++++++++++++++++++++++        
        
        
        # tworzymy pudla
        self.pudla = []
        
        for i in range(len(boxes_startpos)):            
            self.pudla.append(self.Pudlo(xpos = boxes_startpos[i][0]*64, 
                ypos = boxes_startpos[i][1]*64))
        
        
            self.pudla[i].add(self.boxgroup)
            
            
            
        # tworzymy sciany
        
        self.walls = []
    
        for i in range(len(walls_pos)):
            self.walls.append(self.Wall(xpos = walls_pos[i][0]*64,
                                        ypos = walls_pos[i][1]*64))
            
            self.walls[i].add(wallsgroup)
            
            
        # tworzymy cele
        
        self.goals = []
            
        for i in range(len(goals_pos)):
            self.goals.append(self.Goal(xpos = goals_pos[i][0]*64,
                                        ypos = goals_pos[i][1]*64))
            
            self.walls[i].add(goalsgroup)        

            
        # ustawienia tla
        
        self.font = pygame.font.SysFont("comicsansms", 72)
        #self.label = self.font.render("Zabawa", 1, (255, 255, 0))
        
        
        
        screen.blit(background, (0, 0))

        allgroup.draw(screen)
        boxgroup.draw(screen)
        
        pygame.display.flip()
    
    
        self.loop()
        
        
    def loop(self):
        while True:
            pygame.display.flip()
            self.clock.tick(15)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.locals.KEYDOWN:
                    #pressed_key = event.key
                    keys = pygame.key.get_pressed()
                    
                    if keys[pygame.K_DOWN]:
                        self.gracz1.move(0, 64, self.background.get_rect())                        
                        z = self.gracz1.czy_kolizja(self.boxgroup)
                        if z == None:
                            pass
                        else:
                            _czy_move = z.rect.center
                            z.move(0, 64, self.background.get_rect())
                            if z.rect.center == _czy_move:
                                self.gracz1.move(0, -64, self.background.get_rect())
                            
                    elif keys[pygame.K_UP]:
                        self.gracz1.move(0,-64, self.background.get_rect())
                        z = self.gracz1.czy_kolizja(self.boxgroup)
                        if z == None:
                            pass
                        else:
                            _czy_move = z.rect.center
                            z.move(0, -64, self.background.get_rect())
                            if z.rect.center == _czy_move:
                                self.gracz1.move(0, 64, self.background.get_rect())                            
                            
                    elif keys[pygame.K_RIGHT]:
                        self.gracz1.move(64,0, self.background.get_rect())
                        z = self.gracz1.czy_kolizja(self.boxgroup)
                        if z == None:
                            pass
                        else:
                            _czy_move = z.rect.center
                            z.move(64, 0, self.background.get_rect())  
                            if z.rect.center == _czy_move:
                                self.gracz1.move(-64, 0, self.background.get_rect())
                                
                    elif keys[pygame.K_LEFT]:
                        self.gracz1.move(-64,0, self.background.get_rect())
                        z = self.gracz1.czy_kolizja(self.boxgroup)
                        if z == None:
                            pass
                        else:
                            _czy_move = z.rect.center
                            z.move(-64, 0, self.background.get_rect())     
                            if z.rect.center == _czy_move:
                                self.gracz1.move(64, 0, self.background.get_rect())                            
                
                # wyrysowanie wszystkiego z for-a
                
#==============================================================================
#                 goals_number = len(pygame.sprite.groupcollide(self.goalsgroup,
#                     self.boxgroup, False, False))
#==============================================================================
                count = 0
                for j in range(len(self.goals)):
                    if pygame.sprite.spritecollideany(self.goals[j], self.boxgroup) != None:
                        count += 1
                
                #if count > 0:

                
                Tekst_inst = self.Tekst(650, 10, "goli "+str(count), 10, 60, 60)
                Tekst_inst.add(self.Tekstgroup)
                                                                                            
                self.allgroup.clear(self.screen, self.background)
                self.boxgroup.clear(self.screen, self.background)
                self.Tekstgroup.clear(self.screen, self.background)
                
                self.boxgroup.draw(self.screen)
                self.allgroup.draw(self.screen)
                self.Tekstgroup.draw(self.screen)
                
                Tekst_inst.kill()
                
                #self.boxgroup.draw(self.screen)
                

                                                 

                    
if __name__ == '__main__':
    IsoGame()                   
                    
                    
