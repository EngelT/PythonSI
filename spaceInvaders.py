#Space Invaders with pyGame (my first attempt)

import pygame
import time
import random
pygame.init()
screen_width = 600
screen_height = 600
win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Space Invaders")

bg = pygame.image.load("bg.png")

clock = pygame.time.Clock()

score= 0

#player class
class player(object):
    ship = pygame.image.load("ship.png")
    ship = pygame.transform.scale(ship, (64, 64))
    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.vel = 5


    def draw(self, win):
        self.hitbox = (self.x , self.y + 27, 64, 29)
        win.blit (self.ship, (self.x, self.y))
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


#enemy class
class enemy(object):
    alien = pygame.image.load("alien.png")
    alien = pygame.transform.scale (alien, (64, 64))

    def __init__(self,x ,y, width, height, end, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y + 20, 64, 29)
        self.vel = 5
        self.end = end
        self.path = [self.x, self.end]
        self.visible = True
        self.health = health


    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


    def draw(self, win):
        if self.visible:
            self.move()
            self.hitbox = (self.x, self.y + 20, 64, 29)
            win.blit(self.alien, (self.x, self.y))
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1

#projectile class
class projectile(object):
    def __init__(self, x, y, radius, color, vel):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = vel

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)



#Startpoints of the aliens
starta = 36
starta0 =100
starta1 =164
starta2 =228
starta3 =292


#the diffrent character models
man = player(300, 520, 64, 64)
alien = enemy(starta , 200, 64, 64, 228, 4)
alien0 = enemy(starta0 , 200, 64, 64, 292, 4)
alien1 = enemy(starta1 , 200, 64, 64, 356, 4)
alien2 = enemy(starta2 , 200, 64, 64, 420, 4)
alien3 = enemy(starta3 , 200, 64, 64, 484, 4)
bulletsP = []
font = pygame.font.SysFont("lucida console", 30, True, False)
fontInfo = pygame.font.SysFont("lucida console", 13, False, True)
shootLoop = 0

#refresh the screen
def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = font.render("Score: "+str(score), 1, (255, 255, 255))
    win.blit(text, (screen_width/2 - (text.get_width()/2), 20))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_TAB]:
        menuText = font.render("GAME PAUSED", 1, (255, 0, 0))
        win.blit(menuText, (screen_width / 2 - (menuText.get_width() / 2), 200))
        menuText0 = font.render("SPACE INVADERS", 1, (255, 255, 255))
        win.blit(menuText0, (screen_width / 2 - (menuText0.get_width()/ 2), 160))
        menuText1 = font.render("use the arrow keys to", 1, (255, 255, 255))
        win.blit(menuText1, (screen_width / 2 - (menuText1.get_width() / 2), 240))
        menuText2 = font.render("move and space to shoot", 1, (255, 255, 255))
        win.blit(menuText2, (screen_width / 2 - (menuText2.get_width() / 2), 270))
    else:
        man.draw(win)
        alien.draw(win)
        alien0.draw(win)
        alien1.draw(win)
        alien2.draw(win)
        alien3.draw(win)
        for bullet in bulletsP:
            bullet.draw(win)
        info = fontInfo.render("Hold TAB for menu", 1, (255, 255, 255))
        win.blit(info, (5, 5))




    pygame.display.update()













#mainloop
run = True




while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #check if alien is hit
    if alien.visible:
        for bullet in bulletsP:
            if bullet.y - bullet.radius < alien.hitbox[1] + alien.hitbox[3] and bullet.y + bullet.radius > alien.hitbox[1]:
                if bullet.x + bullet.radius > alien.hitbox[0] and bullet.x - bullet.radius < alien.hitbox[0] + alien.hitbox[2]:
                    alien.hit()
                    score += 1
                    bulletsP.pop(bulletsP.index(bullet))
    if alien0.visible:
        for bullet in bulletsP:
            if bullet.y - bullet.radius < alien0.hitbox[1] + alien0.hitbox[3] and bullet.y + bullet.radius > alien0.hitbox[1]:
                if bullet.x + bullet.radius > alien0.hitbox[0] and bullet.x - bullet.radius < alien0.hitbox[0] + alien0.hitbox[2]:
                    alien0.hit()
                    score += 1
                    bulletsP.pop(bulletsP.index(bullet))
    if alien1.visible:
        for bullet in bulletsP:
            if bullet.y - bullet.radius < alien1.hitbox[1] + alien0.hitbox[3] and bullet.y + bullet.radius > alien1.hitbox[1]:
                if bullet.x + bullet.radius > alien1.hitbox[0] and bullet.x - bullet.radius < alien1.hitbox[0] + alien1.hitbox[2]:
                    alien1.hit()
                    score += 1
                    bulletsP.pop(bulletsP.index(bullet))
    if alien2.visible:
        for bullet in bulletsP:
            if bullet.y - bullet.radius < alien2.hitbox[1] + alien2.hitbox[3] and bullet.y + bullet.radius > alien2.hitbox[1]:
                if bullet.x + bullet.radius > alien2.hitbox[0] and bullet.x - bullet.radius < alien2.hitbox[0] + alien2.hitbox[2]:
                    alien2.hit()
                    score += 1
                    bulletsP.pop(bulletsP.index(bullet))
    if alien3.visible:
        for bullet in bulletsP:
            if bullet.y - bullet.radius < alien3.hitbox[1] + alien3.hitbox[3] and bullet.y + bullet.radius > alien3.hitbox[1]:
                if bullet.x + bullet.radius > alien3.hitbox[0] and bullet.x - bullet.radius < alien3.hitbox[0] + alien3.hitbox[2]:
                    alien3.hit()
                    score += 1
                    bulletsP.pop(bulletsP.index(bullet))



    if alien.visible == False and alien0.visible == False and alien1.visible == False and alien2.visible == False and alien3.visible == False:
        alien.visible = True
        alien0.visible = True
        alien1.visible = True
        alien2.visible = True
        alien3.visible = True
        print("NEXT WAVE")


    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 5:
        shootLoop = 0

    for bullet in bulletsP:
        if bullet.y < screen_width and bullet.y > 0:
            bullet.y -= bullet.vel
        else:
            bulletsP.pop(bulletsP.index(bullet))


    #controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and man.x < screen_width - man.vel - man.width:
        man.x += man.vel

    elif keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
    if keys [pygame.K_SPACE] and shootLoop == 0 :
        if len(bulletsP) < 5:
            bulletsP.append(projectile(round(man.x + man.width //2), round(man.y ), 6, (255, 255, 155), 20))







    redrawGameWindow()
















pygame.quit()