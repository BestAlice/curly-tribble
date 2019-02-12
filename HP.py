import pygame

class HP(pygame.sprite.Sprite):
    def __init__(self, group, screen):
        super().__init__(group)
        self.hp = 100 
        self.pole = pygame.Surface((330, 60)) 
        self.obvodka = pygame.Rect(0, 0, 330, 60)
        self.red = pygame.Rect(0, 0, int(330 * self.hp // 100), 60)

        pygame.draw.rect(self.pole, (180, 6, 6), self.red)
        pygame.draw.rect(self.pole, pygame.Color('black'), self.obvodka, 5)
        
        self.image = self.pole
        self.rect = self.image.get_rect()
        self.rect.x = 60
        self.rect.y = 630
        # 80, 630
    
    def update(self):
        pygame.draw.rect(self.pole, (180, 6, 6), self.red)
        pygame.draw.rect(self.pole, pygame.Color('black'), self.obvodka, 5)
        self.image = self.pole

    def get_event(self, event):
        pass
       # if pygame.sprite.collide_mask(self, self.player)

    def damage(self, damage):
        self.hp -= damage