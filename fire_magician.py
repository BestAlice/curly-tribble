import pygame
from permanent import HEIGHT, WIDTH, load_image, FPS


class Fire_magician(pygame.sprite.Sprite):
    def __init__(self, group):
        global size
        super().__init__(group)
        self.MagDown = [pygame.transform.rotozoom(load_image(f"mag-go/down/{i}.png", -1), 0, 0.5) for i in range(1, 7)]
        self.MagUp = [pygame.transform.rotozoom(load_image(f"mag-go/up/{i}.png", -1), 0, 0.5) for i in range(1, 7)]
        self.MagLeft = [pygame.transform.rotozoom(load_image(f"mag-go/left/{i}.png", -1), 0, 0.5) for i in range(1, 7)]
        self.MagRight = [pygame.transform.rotozoom(load_image(f"mag-go/right/{i}.png", -1), 0, 0.5) for i in range(1, 7)]
        self.mainMag = self.MagDown
        self.frame = 0
        self.image = pygame.transform.rotozoom(load_image("mag.png", -1), 0, 0.5)
        self.rect = self.image.get_rect()        
        self.rect.x = 100
        self.rect.y = 100
        print(self.rect)
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
        self.image = self.mainMag[self.frame//5]
        self.frame = self.frame + 1 if self.frame != 29 else 0

    def get_event(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.left = True
            self.mainMag = self.MagLeft
        else:
            self.left = False
        if keys[pygame.K_RIGHT]:
            self.right = True
            self.mainMag = self.MagRight
        else:
            self.right = False
        if keys[pygame.K_DOWN]:
            self.down = True
            self.mainMag = self.MagDown
        else:
            self.down = False
        if keys[pygame.K_UP]:
            self.up = True
            self.mainMag = self.MagUp
        else:
            self.up = False

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
