import pygame
from permanent import HEIGHT, WIDTH, load_image

class Fire_magician(pygame.sprite.Sprite):
    def __init__(self, group):
        global size
        super().__init__(group)
        self.image = pygame.transform.rotozoom(load_image("mag.png", -1), 0, 0.5)
        self.rect = self.image.get_rect()        
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        pass

