# coding: utf-8
from goblin import Goblin
from permanent import LEFT, RIGHT, UP, DOWN, HEIGHT, WIDTH, draw

class Levels():
    def __init__(self, screen, all_sprites, enemys):
        self.screen = screen
        self.all_sprites = all_sprites
        self.enemys = enemys
        self.level_now = 1
        self.max_level = 2
        self.menu_levels(self.level_now)

    def level_1(self):
        gob1 = Goblin(LEFT + 20, DOWN, (self.all_sprites, self.enemys), self.enemys)
        gob2 = Goblin(RIGHT - 20, UP + 350, (self.all_sprites, self.enemys), self.enemys)
        gob3 = Goblin(LEFT + 50, UP + 30, (self.all_sprites, self.enemys), self.enemys)

    def level_2(self):
        gob1 = Goblin(LEFT + 200, DOWN - 200, (self.all_sprites, self.enemys), self.enemys)
        gob2 = Goblin(RIGHT - 200, UP + 200, (self.all_sprites, self.enemys), self.enemys)
        gob3 = Goblin(LEFT + 200, UP + 200, (self.all_sprites, self.enemys), self.enemys) 
        gob4 = Goblin(RIGHT - 200, DOWN - 200, (self.all_sprites, self.enemys), self.enemys)

    def menu_levels(self, need_level):
        if need_level == 1:
            self.level_1()
        elif need_level == 2:
            self.level_2()

    def next_level(self, last_level=False):
        if self.level_now < self.max_level:
            self.level_now += 1     
        else:
            self.level_now = 1
        if last_level:
            self.level_now -= 1
        self.menu_levels(self.level_now)
