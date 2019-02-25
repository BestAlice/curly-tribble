# coding: utf-8
import pygame
import os
from permanent import WIDTH, HEIGHT, FPS, load_image, load_music, draw
from fire_magician import Fire_magician
from goblin import Goblin
from HP import Hp
from Levels import Levels

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

level = Levels(screen, all_sprites, enemys)

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
            if event.key == 13 and press_enter:
                fon_y = -1400
            if event.key == 13: #Enter
                press_enter = True
    if press_enter:
        screen.blit(start_screen,(0, fon_y))
        screen.blit(space,(0, fon_y + 700))
        screen.blit(Fon,(0, fon_y + 1400))
        fon_y -= v_start_fon
    else:
        screen.blit(start_screen,(0, fon_y))
        draw(screen, "Press Enter", 320, 520)
    if fon_y <= -1400:
        go_game = True
    pygame.display.flip()
    clock.tick(FPS)
    
player = Fire_magician(all_sprites, enemys)
hp = Hp(all_sprites, screen)

name_music = 'data/battle.mp3'
load_music(name_music)

def music():
    global M
    if M:
        M = False
        pygame.mixer.music.pause()
    else:
        M = True
        pygame.mixer.music.unpause()

while running:
    if name_music == 'data/fail.wav' and not Game_Over:
        name_music = 'data/battle.mp3'
        load_music(name_music)
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
        if not enemys:
            level.next_level()
        for vrag1 in enemys:
            vrag1.Fire_x_y(player, player.rect)
        all_sprites.update()            
    all_sprites.draw(screen)
    if Pause:
        screen.blit(Pausa, (0, 0))
    if Game_Over:
        if name_music == 'data/battle.mp3':
            name_music = 'data/fail.wav'
            load_music(name_music)
        all_sprites.empty()
        enemys.empty()
        player = Fire_magician(all_sprites, enemys)
        hp = Hp(all_sprites, screen)
        level.next_level(True)
        screen.blit(Game_over, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
