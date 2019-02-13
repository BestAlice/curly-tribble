import pygame
import os
from permanent import WIDTH, HEIGHT, FPS, load_image
from fire_magician import Fire_magician
from fire_ball import Fire_ball
from goblin import Goblin
from HP import HP

pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
Pause = False
USEREVENT = 1

all_sprites = pygame.sprite.Group()
gobs = Goblin(all_sprites)
player = Fire_magician(all_sprites)
hp = HP(all_sprites, screen)
Fon = load_image('Fon.png')
Game_over = load_image('Game_over.png')
Pausa = load_image('Pausa.png', -1)

pygame.time.set_timer(USEREVENT, 1000)

while running:
    if hp.hp > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == USEREVENT:
                if gobs.Atak:
                    hp.damage(gobs.damage)
                    print(hp.hp)
            if event.type == pygame.KEYDOWN:
                if event.key == 112:
                    if not Pause:
                        Pause = True
                    else:
                        Pause = False
            for sprite in all_sprites:
                sprite.get_event(event)
        gobs.Fire_x_y(player, player.rect)
        screen.blit(Fon, (0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        if Pause:
            screen.blit(Pausa, (0, 0))
    else:
        screen.blit(Game_over, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()

