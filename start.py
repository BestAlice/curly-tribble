from permanent import load_image, FPS
import pygame

class Start(pygame.sprite.Sprite):
    def __init__(self, group):
        self.image = load_image('Старт.png'))
        self.image1.rect = pygame.Rect(0, 0, 1000, 700)
        self.image2 = load_image('переход.png')
        self.image1.rect = (0, 700, 1000, 700)
        self.image3 = load_image('Fon.png')
        self.image1.rect = (0, 1400, 1000, 700)
        self.image = self.image1
        self.v = 200 // FPS
        self.go_game = False
        self.press_enter = False

    def update(self):
        if self.press_enter:
            self.image1.rect.y -= self.v
            self.image2.rect.y -= self.v
            self.image3.rect.y -= self.v
        if self.image3.rect.y <= 0:
            self.go_game = True
            self.kill()

    def get_event(self, event):
        if event.key == 13: #Enter
            self.press_enter = True