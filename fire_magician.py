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

if __name__ == "__main__":
    pygame.init()
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    all_sprites = pygame.sprite.Group()
    player = Fire_magician(all_sprites)
    all_sprites.draw(screen)
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()