import pygame
from permanent import load_image, FPS

class Fire_ball(pygame.sprite.Sprite):
    def __init__(self, group, direction, gamer_rect, group_enemys): #direction -наравление
        super().__init__(group)
        self.group = group
        self.image = load_image('fire-ball.png', -1)
        self.rect = self.image.get_rect()
        if direction == 'Left':
            self.rect.x = gamer_rect.x   
            self.rect.y = gamer_rect.y + gamer_rect[3] // 2
        elif direction == 'Right':
            self.rect.x = gamer_rect.x + gamer_rect[2] + 30
            self.rect.y =  gamer_rect.y + gamer_rect[3] // 2
        elif direction == 'Down':
            self.rect.x = gamer_rect.x + gamer_rect[2] // 2 + 10
            self.rect.y = gamer_rect.y + gamer_rect[3] // 2 + 30
        elif direction == 'Up':
            self.rect.x = gamer_rect.x + gamer_rect[2] // 2 + 20
            self.rect.y = gamer_rect.y - 40
        self.mask = pygame.mask.from_surface(self.image)
        self.enemys = group_enemys
        self.damage = 1
        self.direction = direction
        self.speed = 400 / FPS
        self.boom = False

    def update(self):
        if self.direction == 'Left':
            self.rect.x -= self.speed
        elif self.direction == 'Right':
            self.rect.x += self.speed
        elif self.direction == 'Down':
            self.rect.y += self.speed
        elif self.direction == 'Up':
            self.rect.y -= self.speed
        if self.boom:
            if pygame.time.get_ticks() - self.time_boom > 300:
                self.group.remove(self)
        else:
            if self.rect.x < 100 or self.rect[2] + self.rect.x > 890:
                self.fire_boom()
            elif self.rect.y < 70 or self.rect[3] + self.rect.y > 580:
                self.fire_boom()
            
    def get_event(self, event):
        keys = pygame.key.get_pressed() 
        for gobs in self.enemys:
            if pygame.sprite.collide_mask(self, gobs):
                self.fire_boom()
        

    def fire_boom(self):
        self.speed = 0
        self.image = load_image('boom.png', -1)
        self.boom = True
        self.mask = pygame.mask.from_surface(self.image)
        self.boom_rect = self.image.get_rect()
        self.time_boom = pygame.time.get_ticks()