import pygame
import os
from permanent import WIDTH, HEIGHT, FPS, load_image
from fire_magician import Fire_magician
from goblin import Goblin
from HP import Hp

pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
Pause = False
Game_Over = False
M = True

all_sprites = pygame.sprite.Group()
enemys = pygame.sprite.Group()
player = Fire_magician(all_sprites, enemys)
hp = Hp(all_sprites, screen)
gobs = [Goblin(800, 200, (all_sprites, enemys)),
        Goblin(800, 500, (all_sprites, enemys))]

Fon = load_image('Fon.png')
Game_over = load_image('Game_over.png')
Pausa = load_image('Pausa.png', -1)

#pygame.mixer.music.load('data/audio.mp3') чтобы пока музыка не мешала 
#pygame.mixer.music.play()                 
#pygame.mixer.music.set_volume(0.1)

def music():
    global M
    if M:
        M = False
        pygame.mixer.music.pause()
    else:
        M = True
        pygame.mixer.music.unpause()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 112: # P - вкл/выкл музыку
                music()
            if event.key == 27: #ESC
                if not Pause:
                    Pause = True
                else:
                    Pause = False
            if event.key == 13: #Enter
                Game_Over = False
        if not Pause:
            for sprite in all_sprites:
                    sprite.get_event(event)
            for gob in enemys:
                if event.type == gob.USEREVENT:
                    if gob.Atak:
                        hp.damage(gob.damage)
                        player.wound()
    if hp.hp <= 0:
        Game_Over = True
    screen.blit(Fon, (0, 0))
    if not Pause:
        for i in enemys:
            i.Fire_x_y(player, player.rect)
        all_sprites.update()
        for gob in enemys:
            if gob.hp <= 0:
                gob.kill()
    all_sprites.draw(screen)
    if Pause:
        screen.blit(Pausa, (0, 0))
    if Game_Over:
        all_sprites = pygame.sprite.Group()
        enemys = pygame.sprite.Group()
        gobs = [Goblin(800, 200, (all_sprites, enemys)),
            Goblin(800, 500, (all_sprites, enemys))]
        player = Fire_magician(all_sprites, enemys)
        hp = Hp(all_sprites, screen)
        screen.blit(Game_over, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()

