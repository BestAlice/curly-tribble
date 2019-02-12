import pygame
from permanent import load_image, FPS

class Fire_ball(pygame.sprite.Sprite):
    def __init__(self, group, direction, gamer_rect): #direction -наравление
        super().__init__(group)
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
        self.damage = 1
        self.direction = direction
        self.speed = 200 / FPS
    
    def update(self):
        if self.direction == 'Left':
            self.rect.x -= self.speed
        elif self.direction == 'Right':
            self.rect.x += self.speed
        elif self.direction == 'Down':
            self.rect.y += self.speed
        elif self.direction == 'Up':
            self.rect.y -= self.speed
        
