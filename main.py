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

start_screen = load_image('Start.png')
space = load_image('переход.png')
Fon = load_image('Fon.png')
Game_over = load_image('Game_over.png')
Pausa = load_image('Pausa.png', -1)

v_start_fon = 200 // FPS
go_game = False
press_enter = False
fon_y = 0
while not go_game:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == 13: #Enter
                press_enter = True
    if press_enter:
        screen.blit(start_screen,(0, fon_y))
        screen.blit(space,(0, fon_y + 700))
        screen.blit(Fon,(0, fon_y + 1400))
        fon_y -= v_start_fon
    else:
        screen.blit(start_screen,(0, fon_y))
    if fon_y <= -1400:
        go_game = True
    pygame.display.flip()
    clock.tick(FPS)

player = Fire_magician(all_sprites, enemys)
hp = Hp(all_sprites, screen)
gobs = [Goblin(800, 200, (all_sprites, enemys)),
        Goblin(800, 500, (all_sprites, enemys))]


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
    if pygame.sprite.collide_circle(gobs[0], gobs[1]):
        gobs[0].rect.x += 2
        gobs[0].rect.y += 2
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
                gob.rect.x += 1000
                gob.rect.y += 1000
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