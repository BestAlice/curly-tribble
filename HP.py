# coding: utf-8
import pygame

class Hp(pygame.sprite.Sprite):
    def __init__(self, group, screen):
        super().__init__(group)
        self.hp = 100 
        self.pole = pygame.Surface((330, 60)) 
        self.obvodka = pygame.Rect(0, 0, 330, 60)
        self.red = pygame.Rect(0, 0, int(330 * self.hp // 100), 60)
        
        self.image = self.pole
        self.rect = self.image.get_rect()
        self.rect.x = 60
        self.rect.y = 630
        # 80, 630
    
    def update(self):
        self.red = pygame.Rect(0, 0, 330 * self.hp // 100, 60)
        self.pole.fill(pygame.Color('black'))
        pygame.draw.rect(self.pole, (180, 6, 6), self.red)
        pygame.draw.rect(self.pole, pygame.Color('black'), self.obvodka, 5)
        self.image = self.pole
        self.rect.x = 60
        self.rect.y = 630

    def get_event(self, event):
        pass
       # if pygame.sprite.collide_mask(self, self.player)

    def damage(self, damage):
        self.hp -= damage
