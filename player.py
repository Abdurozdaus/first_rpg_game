import pygame as pg
from pygame.math import Vector2
from helper import SpriteSheet


class Player(pg.sprite.Sprite):
    """управление свойства игрока"""
    speed=7
    def __init__(self, sprite_sheet_path, pos):
        """ответственносить за переменные"""
        super().__init__()

        # self.sprite_sheet = SpriteSheet(sprite_sheet_path)
        # self.image = self.sprite_sheet.get_image(0, 0, 32, 32)
        sprite_sheet=SpriteSheet(sprite_sheet_path, 2)
        self._loadimage(sprite_sheet)
        self.image=self.walk_right[0]
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

    def _loadimage(self, sheet):
        self.walk_right=[]
        self.walk_down=[]
        self.walk_left=[]
        self.walk_up=[]
        w,h=sheet.w//4, sheet.h//4
        for i in range(0,w*4,w):
            self.walk_right.append(sheet.get_image(i, h*2, w, h))
            self.walk_down.append(sheet.get_image(i, 0, w, h))
            self.walk_left.append(sheet.get_image(i, h, w, h))
            self.walk_up.append(sheet.get_image(i, h * 3, w, h))

