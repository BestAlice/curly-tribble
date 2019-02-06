import pygame
from permanent import WIDTH, HEIGHT

class Camera:
    def __init__(self):
        global WIDTH, HEIGHT
        self.dx = 0
        self.dy = 0
 
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy
 
    def update(self):
        self.dx = 0
        self.dy = 0