import pygame
from permanent import HEIGHT, WIDTH, load_image, FPS
from fire_magician import Fire_magician
from HP import HP
sp_Names_Left = ['Gob_left1.png','Gob_left2.png','Gob_left3.png',
                'Gob_left4.png','Gob_left5.png','Gob_left6.png','Gob_left7.png',
                'Gob_left8.png','Gob_left9.png','Gob_left10.png']
sp_Names_Right = ['Gob_right1.png','Gob_right2.png','Gob_right3.png',
                  'Gob_right4.png','Gob_right5.png','Gob_right6.png','Gob_right7.png',
                  'Gob_right8.png','Gob_right9.png','Gob_right10.png']
sp_Names_Down = ['Gob_down1.png','Gob_down2.png','Gob_down3.png',
                  'Gob_down4.png','Gob_down5.png','Gob_down6.png','Gob_down7.png',
                  'Gob_down8.png','Gob_down9.png','Gob_down10.png']
sp_Names_Up = ['Gob_up1.png','Gob_up2.png','Gob_up3.png',
               'Gob_up4.png','Gob_up5.png','Gob_up6.png','Gob_up7.png',
               'Gob_up8.png','Gob_up9.png','Gob_up10.png']
sp_Names_l_atak = ['Gob_l_atak1.png','Gob_l_atak2.png','Gob_l_atak3.png',
                   'Gob_l_atak4.png','Gob_l_atak5.png','Gob_l_atak6.png']
sp_Names_R_atak = ['Gob_R_atak1.png','Gob_R_atak2.png','Gob_R_atak3.png',
                   'Gob_R_atak4.png','Gob_R_atak5.png','Gob_R_atak6.png']
sp_Names_D_atak = ['Gob_D_atak1.png','Gob_D_atak2.png','Gob_D_atak3.png',
                   'Gob_D_atak4.png','Gob_D_atak5.png','Gob_D_atak6.png']
sp_Names_U_atak = ['Gob_U_atak1.png','Gob_U_atak2.png','Gob_U_atak3.png',
                   'Gob_U_atak4.png','Gob_U_atak5.png','Gob_U_atak6.png']


class Goblin(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.GobLeft = []
        self.GobRight = []
        self.GobDown = []
        self.GobUp = []
        self.GobAtakL = []
        self.GobAtakR = []
        self.GobAtakD = []
        self.GobAtakU = []
        self.image = pygame.transform.rotozoom(load_image('Gob1.png', -1), 0, 0.6)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 500
        self.rect.y = 350
        self.v = 60 / FPS
        self.damage = 1
        self.Left = False
        self.Right = False
        self.Down = False
        self.Up = False
        self.Atak = False
        self.animCount = 0
        self.Pause = False
        self.full_sp()

    def full_sp(self):
        for i in range(10):
            self.GobLeft.append(load_image('gob-go/' + sp_Names_Left[i], -1))
            self.GobRight.append(load_image('gob-go/' + sp_Names_Right[i], -1))
            self.GobDown.append(load_image('gob-go/' + sp_Names_Down[i], -1))
            self.GobUp.append(load_image('gob-go/' + sp_Names_Up[i], -1))
        for i in range(6):
            self.GobAtakL.append(load_image('gob-atak/' + sp_Names_l_atak[i], -1))
            self.GobAtakR.append(load_image('gob-atak/' + sp_Names_R_atak[i], -1))
            self.GobAtakD.append(load_image('gob-atak/' + sp_Names_D_atak[i], -1))
            self.GobAtakU.append(load_image('gob-atak/' + sp_Names_U_atak[i], -1))
        
    def Fire_x_y(self, player, rect):
        if not self.Pause:
            self.player = player
            self.Frect = rect
            self.Fx = rect[0] + int(rect[2] / 2)
            self.Fy = rect[1] + int(rect[3] / 2)
            self.update()
        else:
            pass

        
    def update(self):
        if not self.Pause:
            if not pygame.sprite.collide_mask(self, self.player):
                self.rect = self.rect.move(0, 1)
                self.collision()
                self.Atak = False
                self.side()
            elif pygame.sprite.collide_mask(self, self.player):
                self.collision()
                self.Atak = True
                self.side()
        else:
            pass
        
    def side(self):
        if not self.Atak:
            if self.animCount +1 >= 30:
                self.animCount = 0
            
            elif self.Left: 
                self.image = pygame.transform.rotozoom(self.GobLeft[self.animCount // 3],
                                                       0, 0.6)
                self.animCount += 1
            elif self.Right:
                self.image = pygame.transform.rotozoom(self.GobRight[self.animCount // 3],
                                                       0, 0.6)
                self.animCount += 1
            elif self.Down:
                self.image = pygame.transform.rotozoom(self.GobDown[self.animCount // 3],
                                                       0, 0.6)
                self.animCount += 1
            elif self.Up:
                self.image = pygame.transform.rotozoom(self.GobUp[self.animCount // 3],
                                                       0, 0.6)
                self.animCount += 1
        elif self.Atak:
            if self.animCount +1 >= 30:
                self.animCount = 0

            if self.Left:
                self.image = pygame.transform.rotozoom(self.GobAtakL[self.animCount // 5],
                                                        0, 0.6)
                self.animCount += 1
            elif self.Right:
                self.image = pygame.transform.rotozoom(self.GobAtakR[self.animCount // 5],
                                                        0, 0.6)
                self.animCount += 1
            elif self.Down:
                self.image = pygame.transform.rotozoom(self.GobAtakD[self.animCount // 5],
                                                        0, 0.6)
                self.animCount += 1
            elif self.Up:
                self.image = pygame.transform.rotozoom(self.GobAtakU[self.animCount // 5],
                                                        0, 0.6)
                self.animCount += 1
            
        
    def collision(self):
        xN = self.rect.x
        yN = self.rect.y
        x = self.Fx
        y = self.Fy
        if xN > x and yN > y: #Left
            xN -= self.v 
            yN -= self.v 
            self.Left = True
            self.Right = False
            self.Down = False
            self.Up = False
        elif xN > x and yN < y: #Left
            xN -= self.v  
            yN += self.v 
            self.Left = True
            self.Right = False
            self.Down = False
            self.Up = False
        elif xN < x and yN < y: #Right
            xN += self.v 
            yN += self.v 
            self.Left = False
            self.Right = True
            self.Down = False
            self.Up = False
        elif xN < x and yN > y: #Right
            xN += self.v 
            yN -= self.v 
            self.Left = False
            self.Right = True
            self.Down = False
            self.Up = False
        elif xN > x and yN == y: #Right 
            xN -= self.v
            self.Left = True
            self.Right = False
            self.Down = False
            self.Up = False
        elif xN < x and yN == y: #Left
            xN += self.v
            self.Left = False
            self.Right = True
            self.Down = False
            self.Up = False
        elif yN < y and xN == x: #Down
            yN += self.v
            self.Left = False
            self.Right = False
            self.Down = True
            self.Up = False
        elif yN > y and xN == x: #Up
            yN -= self.v
            self.Left = False
            self.Right = False
            self.Down = False
            self.Up = True
        if (abs(yN - y) - self.v) == 0:
            yN = y
        if  (abs(xN - x) - self.v) == 0:
            xN = x
        self.rect.x = xN
        self.rect.y = yN
     
    def get_event(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            if not self.Pause:
                self.Pause = True
            else:
                self.Pause = False
        
