import pygame
from permanent import HEIGHT, WIDTH, load_image, FPS

class Fire_magician(pygame.sprite.Sprite):
    def __init__(self, group):
        global size
        super().__init__(group)
        self.image = pygame.transform.rotozoom(load_image("mag.png", -1), 0, 0.5)
        self.rect = self.image.get_rect()        
        self.rect.x = 100
        self.rect.y = 100
        self.mask = pygame.mask.from_surface(self.image)
        self.down = False 
        self.up = False
        self.left = False
        self.right = False

    def update(self):
        #нужны рамки!!!!!!!!!!!
        if self.down:
            self.rect.y += 10 if self.rect[1] + self.rect[3] < HEIGHT else 0
        if self.up:
            self.rect.y -= 10 if self.rect[1] > 0 else 0 
        if self.left:
            self.rect.x -= 10 if self.rect[0] > 0 else 0 
        if self.right:
            self.rect.x += 10 if self.rect[0] + self.rect[2] < WIDTH else 0

    def get_event(self, event):
        keys = pygame.key.get_pressed()
        self.down = True if keys[pygame.K_DOWN] else False
        self.up = True if keys[pygame.K_UP] else False
        self.left = True if keys[pygame.K_LEFT] else False
        self.right = True if keys[pygame.K_RIGHT] else False



if __name__ == "__main__":
    pygame.init()
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    all_sprites = pygame.sprite.Group()
    player = Fire_magician(all_sprites)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            player.get_event(event)
        all_sprites.update()
        screen.fill(pygame.Color('black'))
        all_sprites.draw(screen)
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
    pygame.quit()
