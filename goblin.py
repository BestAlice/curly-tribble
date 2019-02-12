import pygame
from permanent import HEIGHT, WIDTH, load_image, FPS
from fire_magician import Fire_magician
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


class Goblin(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.GobLeft = []
        self.GobRight = []
        self.GobDown = []
        self.GobUp = []
        self.GobAtakL = []
        self.GobAtakR = []
        self.full_sp()
        self.image = pygame.transform.rotozoom(load_image('Gob1.png'), 0, 0.6)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 500
        self.rect.y = 350
        self.v = 60 / FPS
        self.Left = False
        self.Right = False
        self.Down = False
        self.Up = False
        self.Atak = False
        self.animCount = 0

    def full_sp(self):
        for i in range(10):
            self.GobLeft.append(load_image('gob-go/' + sp_Names_Left[i], -1))
            self.GobRight.append(load_image('gob-go/' + sp_Names_Right[i], -1))
            self.GobDown.append(load_image('gob-go/' + sp_Names_Down[i], -1))
            self.GobUp.append(load_image('gob-go/' + sp_Names_Up[i], -1))
        for i in range(6):
            self.GobAtakL.append(load_image('gob-atak/' + sp_Names_l_atak[i], -1))
            self.GobAtakR.append(load_image('gob-atak/' + sp_Names_R_atak[i], -1))
        
    def Fire_x_y(self, player, rect):
        self.player = player
        self.Frect = rect
        self.Fx = rect[0] + int(rect[2] / 2)
        self.Fy = rect[1] + int(rect[3] / 2)
        self.update()

    def side(self):
        xN = self.rect.x
        yN = self.rect.y
        x = self.Fx
        y = self.Fy
        if self.animCount +1 >= 30:
            self.animCount = 0

        if self.Left:
            self.image = pygame.transform.rotozoom(self.GobLeft[self.animCount // 6],
                                                   0, 0.6)
            self.animCount += 1
        elif self.Right:
            self.image = pygame.transform.rotozoom(self.GobRight[self.animCount // 6],
                                                   0, 0.6)
            self.animCount += 1
        elif self.Down:
            self.image = pygame.transform.rotozoom(self.GobDown[self.animCount // 6],
                                                   0, 0.6)
            self.animCount += 1
        elif self.Up:
            self.image = pygame.transform.rotozoom(self.GobUp[self.animCount // 6],
                                                   0, 0.6)
            self.animCount += 1
        elif self.Atak:
            if (xN > x and yN > y) or(xN > x and yN < y) or (xN < x and yN == y):
                self.image = pygame.transform.rotozoom(self.GobAtakL[self.animCount // 10],
                                                       0, 0.6)
                self.animCount += 1
            else:
                self.image = pygame.transform.rotozoom(self.GobAtakR[self.animCount // 10],
                                                       0, 0.6)
                self.animCount += 1
                
             
    def update(self):
        if not pygame.sprite.collide_mask(self, self.player):
            self.rect = self.rect.move(0, 1)
            xN = self.rect.x
            yN = self.rect.y
            x = self.Fx
            y = self.Fy
            if xN > x and yN > y: #Left
                xN -= self.v 
                yN -= self.v 
                self.Left = True
                self.Right = False
            elif xN > x and yN < y: #Left
                xN -= self.v  
                yN += self.v 
                self.Left = True
                self.Right = False
            elif xN < x and yN < y: #Right
                xN += self.v 
                yN += self.v 
                self.Left = False
                self.Right = True
            elif xN < x and yN > y: #Right
                xN += self.v 
                yN -= self.v 
                self.Left = False
                self.Right = True
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
        elif pygame.sprite.collide_mask(self, self.player):
            self.Left = False
            self.Right = False
            self.Down = False
            self.Up = False
            self.Atak = True
        self.side()
     
    def get_event(self, event):
        pass
        
