import pygame as pg
from settings import *
from helper import res
import csv

class Gamingmap():
    def __init__(self, csv_pass, image_pass, game, speactating=0):
        data_list=self._privat(csv_pass)
        image_list=self._dasdasdsa(image_pass, speactating)
        self._load_tilez(game, data_list, image_list)

    def _privat(self, csv_pass):
        with open(csv_pass) as fn:
            reader=csv.reader(fn)
            data=list(reader)
        return data
    def _dasdasdsa(self, image_pass, speactating):
        list=[]
        image=pg.image.load(image_pass).convert()
        width,height=image.get_size()
        for y in range(0, height, TILE_SIZE+speactating):
            for x in range(0, width, TILE_SIZE+speactating):
                tile=image.subsurface(x,y,TILE_SIZE,TILE_SIZE)
                list.append(tile)
        return list
    def _load_tilez(self, game, data_list, image_list):
        for i,row in enumerate(data_list):
            for u, index in enumerate(row):
                Tilesik(game, u,i,image_list[int(index)])

class Tilesik(pg.sprite.Sprite):
    def __init__(self, game, x, y, image):
        super().__init__(game.all_sprites)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x*TILE_SIZE
        self.rect.y=y*TILE_SIZE
