import pygame
from permanent import HEIGHT, WIDTH, load_image

class Goblin(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.transform.rotozoom(load_image("Gob1.png", -1), 0, 0.5)
        self.rect = self.image.get_rect()        
        self.rect.x = 500
        self.rect.y = 350