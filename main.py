import pygame
import os
from permanent import WIDTH, HEIGHT, FPS
from Camera import Camera
from fire_magician import Fire_magician
from goblin import Goblin

pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

all_sprites = pygame.sprite.Group()
player = Fire_magician(all_sprites)
gob = Goblin(all_sprites)

screen.fill(pygame.Color('black')) #почему бы и нет

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for sprite in all_sprites:
            sprite.get_event(event)
    screen.fill(pygame.Color('black'))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()

