import pygame
from permanent import HEIGHT, WIDTH, load_image, FPS
from fire_magician import Fire_magician
sp_Names = ['Gob_left1.png','Gob_left2.png','Gob_left3.png',
            'Gob_left4.png','Gob_left5.png','Gob_left6.png','Gob_left7.png',
            'Gob_left8.png','Gob_left9.png','Gob_left10.png']


class Goblin(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.GobLeft = []
        for i in range(10):
            self.GobLeft.append(load_image(sp_Names[i], -1))
        self.image = pygame.transform.rotozoom(load_image('Gob1.png'), 0, 0.6)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 500
        self.rect.y = 350
        self.v = 2
        self.Left = False
        self.Right = False
        self.animCount = 0 
        
    def Fire_x_y(self, player, rect):
        self.player = player
        self.Frect = rect
        self.Fx = rect[0] + rect[2]
        self.Fy = rect[1] + rect[3]
        self.update()

    def side(self):
        if self.animCount +1 >= 60:
            self.animCount = 0

        if self.Left:
            self.image = pygame.transform.rotozoom(self.GobLeft[self.animCount // 6],
                                                   0, 0.6)
            self.animCount += 1
        else:
            self.image = pygame.transform.rotozoom(load_image('Gob1.png'), 0, 0.6)
            
    def update(self):
        xN = self.rect.x
        yN = self.rect.y
        x = self.Fx
        y = self.Fy
        if xN != x or yN!= y:
            if xN >= x and yN >= y: #Left
                xN -= self.v
                yN -= self.v
                self.Left = True
                self.Right = False
            elif xN >= x and yN <= y: #Left
                xN -= self.v 
                yN += self.v
                self.Left = True
                self.Right = False
            elif xN <= x and yN <= y: #Right
                xN += self.v 
                yN += self.v
                self.Left = False
                self.Right = True
            elif xN <= x and yN >= y: #Right
                xN += self.v 
                yN -= self.v
                self.Left = False
                self.Right = True
        else:
            self.Feft = False
            self.Right = False
        if xN >= x and yN == y: #Left
            xN -= self.v 
        elif xN <= x and yN == y: # Right
            xN += self.v
        elif yN <= y and xN == x: 
            yN += self.v
        elif yN >= y and xN == x: 
            yN -= self.v
        if (abs(yN - y) - self.v) == 0:
            yN = y
        if  (abs(xN - x) - self.v) == 0:
            xN = x
        self.rect.x = xN
        self.rect.y = yN
        if not pygame.sprite.collide_mask(self, self.player):
            self.rect = self.rect.move(0, 1)
        elif pygame.sprite.collide_mask(self, self.player):
            self.Left = False
            self.Right = False
        self.side()
     
    def get_event(self, event):
        pass
        
