import pygame
from permanent import HEIGHT, WIDTH, load_image, FPS
from fire_ball import Fire_ball


class Fire_magician(pygame.sprite.Sprite):
    def __init__(self, group, enemy):
        global size
        super().__init__(group)
        self.grop = group
        self.enemy = enemy
        self.MagDown = [pygame.transform.rotozoom(load_image(f"mag-go/down/{i}.png", -1), 0, 0.5) for i in range(1, 7)] 
        self.MagDown.append(pygame.transform.rotozoom(load_image("mag-go/down/damage.png", -1), 0, 0.5))
        self.MagUp = [pygame.transform.rotozoom(load_image(f"mag-go/up/{i}.png", -1), 0, 0.5) for i in range(1, 7)] 
        self.MagUp.append(pygame.transform.rotozoom(load_image("mag-go/up/damage.png", -1), 0, 0.5))
        self.MagLeft = [pygame.transform.rotozoom(load_image(f"mag-go/left/{i}.png", -1), 0, 0.5) for i in range(1, 7)] 
        self.MagLeft.append(pygame.transform.rotozoom(load_image("mag-go/left/damage.png", -1), 0, 0.5))
        self.MagRight = [pygame.transform.rotozoom(load_image(f"mag-go/right/{i}.png", -1), 0, 0.5) for i in range(1, 7)] 
        self.MagRight.append(pygame.transform.rotozoom(load_image("mag-go/right/damage.png", -1), 0, 0.5))
        self.mainMag = self.MagDown
        self.frame = 0
        self.image = pygame.transform.rotozoom(load_image("mag.png", -1), 0, 0.3)
        self.rect = self.image.get_rect()        
        self.rect.x = 100
        self.rect.y = 100
        self.mask = pygame.mask.from_surface(self.image)
        self.down = False 
        self.up = False
        self.left = False
        self.right = False
        self.red_image = False
        self.speed = 450 / FPS
        self.tick = pygame.time.get_ticks()


    def update(self):
        if self.down:
            self.rect.y += self.speed if self.rect[1] + self.rect[3] < HEIGHT - 160 else 0
        if self.up:
            self.rect.y -= self.speed if self.rect[1] > 0 else 0 
        if self.left:
            self.rect.x -= self.speed if self.rect[0] > 100 else 0 
        if self.right:
            self.rect.x += self.speed if self.rect[0] + self.rect[2] < WIDTH - 160 else 0
        self.image = self.mainMag[self.frame//5]
        self.frame = self.frame + 1 if self.frame != 29 else 0
        if self.red_image and self.frame < 5:
            self.image = self.mainMag[-1]
        else:
            self.red_image = False

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
        if keys[pygame.K_SPACE]:
            if pygame.time.get_ticks() - self.tick > 500:
                if self.mainMag == self.MagLeft:
                    self.fire_atack = Fire_ball(self.grop, 'Left', self.rect, self.enemy)
                elif self.mainMag == self.MagRight:
                    self.fire_atack = Fire_ball(self.grop, 'Right', self.rect, self.enemy)
                elif self.mainMag == self.MagDown:
                    self.fire_atack = Fire_ball(self.grop, 'Down', self.rect, self.enemy)
                elif self.mainMag == self.MagUp:
                    self.fire_atack = Fire_ball(self.grop, 'Up', self.rect, self.enemy)
                self.tick = pygame.time.get_ticks()
    
    def wound(self):
        self.frame = 0
        self.red_image = True