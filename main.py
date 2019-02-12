import pygame
import os
from permanent import WIDTH, HEIGHT, FPS, load_image
from Camera import Camera

from fire_magician import Fire_magician
from goblin import Goblin

pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

all_sprites = pygame.sprite.Group()
gobs = Goblin(all_sprites)
player = Fire_magician(all_sprites)

gobs.Fire_x_y(player, player.rect)
Fon = load_image('Fon.png')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for sprite in all_sprites:
            sprite.get_event(event)
    gobs.Fire_x_y(player, player.rect)
    screen.blit(Fon, (0, 0))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()

