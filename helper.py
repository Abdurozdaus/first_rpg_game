import pygame as pg
from pathlib import Path
import sys

class SpriteSheet:
    """размещение спрайтов"""

    def __init__(self, file_path):
        """зашружает картинку"""
        self.sheet = pg.image.load(file_path).convert_alpha()

    def get_image(self, x, y, width, height):
        """отрисовывает картинку в нужном месте"""
        return self.sheet.subsurface(x, y, width, height)
res=Path(sys.argv[0]).parent/'res'