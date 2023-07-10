import pygame as pg
from pygame.math import Vector2
from helper import SpriteSheet


class Player(pg.sprite.Sprite):
    """управление свойства игрока"""
    speed=7
    def __init__(self, sprite_sheet_path, pos):
        """ответственносить за переменные"""
        super().__init__()

        self.sprite_sheet = SpriteSheet(sprite_sheet_path)
        self.image = self.sprite_sheet.get_image(0, 0, 32, 32)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        """обновляет текущую позицию"""
        self.moove()
    def moove(self):
        """движение по определенному вектору"""
        self.velocity=Vector2(0,0)
        keys=pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x-=3
        if keys[pg.K_w]:
            self.rect.y-=3
        if keys[pg.K_s]:
            self.rect.y+=3
        if keys[pg.K_d]:
            self.rect.x+=3
        if self.velocity.length()>1:
            self.velocity.x=0
        self.velocity*=Player.speed
        self.rect.center+=self.velocity
