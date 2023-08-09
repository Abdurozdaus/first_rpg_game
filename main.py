import pygame as pg
from player import Player
from settings import *
from helper import res
from class_mapa import Gamingmap
import csv



class Game():
    """создание окна"""
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_TITLE)
        pg.display.set_icon(pg.image.load(res / 'sprites' / 'frog.png'))
        self.running=True
    def new(self):
        """спрайты"""
        player = Player(res/'sprites'/'player_sheet.png',(100, 100))
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(player)
        self.map=Gamingmap(self,res/'map'/'map.csv', res/'map'/'rpg_tileset.png')
    def _events(self):
        """игровой цикл"""
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN
                                         and event.key == pg.K_ESCAPE):
                self.running = False
    def _upadte(self):
        """обновление всех спрайтов"""
        self.all_sprites.update()
    def _draw(self):
        """отрисовка игры"""
        self.screen.fill('grey')
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self._events()
            self._draw()
            self._upadte()
if __name__=="__main__":
    game=Game()
    game.new()
    game.run()

