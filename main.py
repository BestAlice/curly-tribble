import pygame
import os
#плохо работает слейдующая строчка
from Camera import Camera

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    image = image.convert_alpha()
    return image

pygame.init()
WIDTH = 1000 #ширина
HEIGHT = 700 #высота
#откорректировать размеры
screen = pygame.display.set_mode(WIDTH, HEIGHT)
FPS = 60
clock = pygame.time.Clock()
running = True

all_sprites = pygame.sprite.Group()

screen.fill(pygame.Color('blue')) #почему бы и нет
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()
    
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()

