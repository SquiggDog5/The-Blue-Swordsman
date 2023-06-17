#   слава Україні


#   Import stuff
import pygame
import random
from pygame import mixer
from os.path import exists as file_exists

#   Define some variables
useText = False

lvl = 65

lives = 3

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DGREEN = (0, 100, 0)
DDGREEN = (0, 50, 0)
RED = (240, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 100, 0)
SHADOW = (11, 11, 11)
ENERGY = (255, 196, 0)
ENERGY2 = (255, 160, 0)
ENERGY3 = (255, 215, 0)
GREY = (100, 100, 100)
STAM1 = (136, 0, 255)
STAM2 = (190, 134, 240)
STAM3 = (50, 14, 82)
YELLOW = (255, 255, 0)
HEAL1 = (255, 55, 0)
HEAL2 = (182, 39, 0)
HEAL3 = (255, 152, 124)
MIRE = (31, 0, 48)
DBLUE = (0, 0, 100)
DDBLUE = (0, 0, 50)
BROWN = (171, 132, 73)
PALERED = (143, 71, 66)
PURPLE1 = (58, 23, 145)
PURPLE2 = (85, 2, 181)
PURPLE3 = (0, 6, 74)
bosssize = 50
x = 20
y = 560
if lvl == 16:
    x = 400
    y = 560
vel = 1.5
time = 0
sid = 20
guage = 800
tired = False
tiredtim = 0
showexpl = 0
normaltargetspeed = 1.7
w = False
a = False
s = False
d = False
hp = 800
bombs = 0
explode = False
invincibleTimer = 0
sethp = 0
xtrastam = 0
mvol = .4
musicTick = 0
musicOn = True
paused = False
mired = False
mireFactor = 0
endTimer = 162
click = False
username = ""
password = ""
chosenTF = -1
keyinp = ""
bckspce = False
buttonpressed = False
globalf = ""
globalf2 = ""
globalf3 = ""
globalpass = ""
newName = "Blue Swordsman"
firstTick = False
tickSize = 1 / 60
tick32 = 0
tick63 = 0
tick64 = 0
terminateOldGuy = False
finalNum = 65
enemiesLeft = 0
done = False
goneFD = False
allLevelSetup = []
hasTicked64 = False
usedLinkCombos = []
cheat = True  # <---------------------------------                 This variable, when "True," makes you invulnerable and faster to observe and fly through levels

### Initializing stuff + setting up
pygame.init()
mixer.init()
mixer.music.set_volume(mvol)
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.font.init()
textf = pygame.font.SysFont('Courier New', 20)
texts = pygame.font.SysFont('Courier New', 15)
texti = pygame.font.SysFont('Courier New', 12)
textfin = pygame.font.SysFont('Courier New', 30)
textfb = pygame.font.SysFont('Courier New', 40)
pygame_icon = pygame.image.load('gameIcon.png')
pygame.display.set_icon(pygame_icon)
clock = pygame.time.Clock()


### Classes for game
class TextField:
    def __init__(self, ex, ey, xl, yw, txt, typeOfField):
        self.x = ex
        self.y = ey
        self.l = xl
        self.w = yw
        self.msg = txt
        self.t = typeOfField
        self.activated = False
        self.inp = ""
        self.inpback = self.inp
        self.code = random.randrange(100000000000000000)
        self.classtype = "TextField"

    def update(self):
        global username
        global password
        global chosenTF
        global textf
        global mx
        global my
        global click
        global keyinp
        global bckspce
        global buttonpressed
        if mx > self.x and mx < self.x + self.l and my > self.y and my < self.y + self.w:
            pygame.draw.rect(screen, DDBLUE, [self.x, self.y, self.l, self.w])
        else:
            pygame.draw.rect(screen, DBLUE, [self.x, self.y, self.l, self.w])
        txt = textf.render(self.msg, True, BLUE)
        textCoor = txt.get_rect(center=(self.x + (self.l / 2), self.y + (self.w / 2)))
        if len(self.inp) == 0:
            txt = textf.render(self.msg, True, BLUE)
            textCoor = txt.get_rect(center=(self.x + (self.l / 2), self.y + (self.w / 2)))
            if not self.activated:
                screen.blit(txt, textCoor)
            else:
                if len(self.inp) == 0:
                    screen.blit(txt, textCoor)
        else:
            txt = textf.render(self.inp, True, GREEN)
            textCoor = txt.get_rect(center=(self.x + (self.l / 2), self.y + (self.w / 2)))
            screen.blit(txt, textCoor)
        if mx > self.x and mx < self.x + self.l and my > self.y and my < self.y + self.w and click:
            buttonPressed()
            self.activated = True
            chosenTF = self.code
        elif chosenTF != self.code:
            self.activated = False
        if self.activated:
            if mx > self.x and mx < self.x + self.l and my > self.y and my < self.y + self.w and len(self.inp) == 0:
                pygame.draw.rect(screen, DDBLUE, [self.x, self.y, self.l, self.w])
            pygame.draw.rect(screen, (random.uniform(50, 255), 0, 0), [self.x + 10, self.y + 10, 20, self.w - 20])
            if buttonpressed:
                if not bckspce:
                    if len(self.inp) < 17:
                        self.inp += keyinp
                else:
                    if len(self.inp) > 0:
                        self.inp = self.inp[:-1]


class Button:
    def __init__(self, sx, sy, xl, yw, txt, func, tfields):
        self.x = sx
        self.y = sy
        self.l = xl
        self.w = yw
        self.t = txt
        self.f = func
        self.tf = tfields  # (username, passcode) --- LIST
        self.classtype = "Button"

    def update(self):
        global BLUE
        global GREEN
        global textf
        global mx
        global my
        global click
        global useText
        global lvl
        global lives
        global DBLUE
        global globalf
        global globalf2
        global globalf3
        global globalpass
        global newName
        if mx > self.x and mx < self.x + self.l and my > self.y and my < self.y + self.w:
            pygame.draw.rect(screen, DDGREEN, [self.x, self.y, self.l, self.w])
        else:
            pygame.draw.rect(screen, DGREEN, [self.x, self.y, self.l, self.w])
        txt = textf.render(self.t, True, GREEN)
        textCoor = txt.get_rect(center=(self.x + (self.l / 2), self.y + (self.w / 2)))
        screen.blit(txt, textCoor)
        if mx > self.x and mx < self.x + self.l and my > self.y and my < self.y + self.w and click and len(
                str(self.tf[0].inp)) > 0 and len(str(self.tf[1].inp)) > 0:
            un1 = str(self.tf[0].inp) + ".txt"
            un2 = str(self.tf[0].inp) + "lives.txt"
            un3 = str(self.tf[0].inp) + "level.txt"
            globalf = un1
            globalf2 = un2
            globalf3 = un3
            globalpass = str(self.tf[1].inp)
            if self.f == "save":
                useText = True
                if file_exists(un1) and file_exists(un2) and file_exists(un3):
                    file = open(un1, "r+")
                    file2 = open(un2, "r+")
                    file3 = open(un3, "r+")
                    if str(file.read()) == str(self.tf[1].inp):
                        lives = int(file2.read())
                        lvl = int(file3.read())
                else:
                    file = open(str(self.tf[0].inp) + ".txt", "w")
                    file.write("")
                    resetFiles(True, str(self.tf[0].inp), str(self.tf[1].inp))
                    lvl = 1
                newName = str(self.tf[0].inp)
            if self.f == "reset":
                if file_exists(un1):
                    if open(un1, "r+").read() == str(self.tf[1].inp):
                        resetFiles(True, str(self.tf[0].inp), str(self.tf[1].inp))
        if mx > self.x and mx < self.x + self.l and my > self.y and my < self.y + self.w and click:
            buttonPressed()
            if self.f == "go":
                lvl = 1


class Enemy:
    def __init__(self, enalive, ex, ey, enableMovement, doesTarget, doesHide, doesShoot, xdelta, ydelta, hasBlades,
                 speedOfTarget, invincible, jug):
        self.enalive = enalive
        self.x = ex
        self.y = ey
        self.enableMovement = enableMovement
        self.doesTarget = doesTarget
        self.xd = xdelta
        self.yd = ydelta
        self.hasBlades = hasBlades
        self.nts = -1 * speedOfTarget
        self.ots = speedOfTarget
        self.doesHide = doesHide
        self.hidden = doesHide
        self.doesShoot = doesShoot
        self.sx = self.x
        self.sy = self.y
        self.sxd = 0
        self.syd = 0
        self.firstShot = True
        self.surpriseSfx = True
        self.inv = invincible
        self.jug = jug
        self.ehp = 200
        self.bladedmg = True
        self.linked = False
        self.lvllistlink = []
        self.classtype = "Enemy"
        self.lvlid = 0
        self.id = str(random.randrange(100000))

    def update(self):
        global x
        global y
        global hp
        global sid
        global RED
        global WHITE
        global ORANGE
        global SHADOW
        global lvl
        global explode
        global mx
        global my
        global invincibleTimer
        if self.enalive:
            self.lvlid = lvl
            if self.hidden:
                pygame.draw.rect(screen, SHADOW, [self.x, self.y, sid, sid])
            elif not self.inv and not self.jug:
                pygame.draw.rect(screen, RED, [self.x, self.y, sid, sid])
            elif self.jug:
                if self.ehp < 200:
                    if self.y > 5:
                        pygame.draw.rect(screen, RED, [self.x + 5, self.y - 5, ((self.ehp / 200) * 10), 3])
                    else:
                        pygame.draw.rect(screen, RED, [self.x + 5, self.y + 22, ((self.ehp / 200) * 10), 3])
                pygame.draw.rect(screen, ORANGE, [self.x, self.y, sid, sid])
            if not self.inv:
                if not self.jug:
                    if d and self.x > x + 25 - sid and self.x < x + 35 and self.y > y + .5 * sid - 2 - sid and self.y < y + .5 * sid + 2:
                        self.enalive = False
                        stab()
                    elif s and self.x > x + .5 * sid - 2 - sid and self.x < x + .5 * sid + 2 and self.y > y + 25 - sid and self.y < y + 35:
                        self.enalive = False
                        stab()
                    elif a and self.x > x - 15 - sid and self.x < x - 5 and self.y > y + .5 * sid - 2 - sid and self.y < y + .5 * sid + 2:
                        self.enalive = False
                        stab()
                    elif w and self.x > x + .5 * sid - 2 - sid and self.x < x + .5 * sid + 2 and self.y > y - 15 - sid and self.y < y - 5:
                        self.enalive = False
                        stab()
                if self.jug:
                    if d and self.x > x + 25 - sid and self.x < x + 35 and self.y > y + .5 * sid - 2 - sid and self.y < y + .5 * sid + 2:
                        self.ehp -= 30
                        stab()
                    elif s and self.x > x + .5 * sid - 2 - sid and self.x < x + .5 * sid + 2 and self.y > y + 25 - sid and self.y < y + 35:
                        self.ehp -= 30
                        stab()
                    elif a and self.x > x - 15 - sid and self.x < x - 5 and self.y > y + .5 * sid - 2 - sid and self.y < y + .5 * sid + 2:
                        self.ehp -= 30
                        stab()
                    elif w and self.x > x + .5 * sid - 2 - sid and self.x < x + .5 * sid + 2 and self.y > y - 15 - sid and self.y < y - 5:
                        self.ehp -= 30
                        stab()
                    if self.ehp < 0:
                        self.enalive = False
            if self.enableMovement:
                if self.hidden:
                    if self.doesTarget:
                        if x < self.x:
                            self.xd = self.nts
                        if x > self.x:
                            self.xd = self.ots
                        if y < self.y:
                            self.yd = self.nts
                        if y > self.y:
                            self.yd = self.ots
                    else:
                        if self.x < 0 or self.x > 780:
                            self.xd = self.xd * -1
                        if self.y < 0 or self.y > 580:
                            self.yd = self.yd * -1
                elif self.doesTarget:
                    if x < self.x:
                        self.xd = self.nts
                    if x > self.x:
                        self.xd = self.ots
                    if y < self.y:
                        self.yd = self.nts
                    if y > self.y:
                        self.yd = self.ots
                else:
                    if self.x > 780 or self.x < 0:
                        self.xd = self.xd * -1
                    if self.y > 580 or self.y < 0:
                        self.yd = self.yd * -1
                self.x += self.xd
                self.y += self.yd
            if self.doesHide:
                if x >= self.x - sid - 40 and x <= self.x + sid + 40 and y >= self.y - sid - 40 and y <= self.y + sid + 40 and self.surpriseSfx:
                    self.hidden = False
                    self.doesTarget = True
                    surprise()
                    self.surpriseSfx = False
            if self.hasBlades and not self.hidden:
                if x >= self.x:
                    pygame.draw.rect(screen, WHITE, [self.x + sid + 5, self.y + .5 * sid - 2, 20, 4])
                if y >= self.y:
                    pygame.draw.rect(screen, WHITE, [self.x + .5 * sid - 2, self.y + sid + 5, 4, 20])
                if x <= self.x:
                    pygame.draw.rect(screen, WHITE, [self.x - sid - 5, self.y + .5 * sid - 2, 20, 4])
                if y <= self.y:
                    pygame.draw.rect(screen, WHITE, [self.x + .5 * sid - 2, self.y - sid - 5, 4, 20])

                if x >= self.x - 5 - sid - sid and x <= self.x + sid + 5 + sid and y <= self.y + .5 * sid + 2 and y >= self.y + .5 * sid - 2 - sid:
                    if self.bladedmg:
                        hp -= 50
                        self.bladedmg = False
                if y >= self.y - 5 - sid - sid and y <= self.y + sid + 5 + sid and x <= self.x + .5 * sid + 2 and x >= self.x + .5 * sid - 2 - sid:
                    if self.bladedmg:
                        hp -= 50
                        self.bladedmg = False
                self.bladedmg = True
            if self.doesShoot:
                pygame.draw.rect(screen, WHITE, [self.sx, self.sy, 10, 10])
                if self.firstShot:
                    self.sx = self.x + 5
                    self.sy = self.y + 5
                    self.firstShot = False
                if self.sx < -200 or self.sx > 1000 or self.sy < -200 or self.sy > 800:
                    self.sx = self.x + 5
                    self.sy = self.y + 5
                    enemyShot()
                if self.sx == self.x + 5 and self.sy == self.y + 5:
                    self.sxd = (x + 5 - self.x) / 60
                    self.syd = (y + 5 - self.y) / 60
                if x >= self.sx - sid and x <= self.sx + 10 and y >= self.sy - sid and y <= self.sy + 10 and invincibleTimer <= 0:
                    hp -= 200
                self.sx += self.sxd
                self.sy += self.syd
            if explode:
                if mx > self.x and mx < self.x + sid and my > self.y and my < self.y + sid:
                    self.enalive = False
                explode = False
        if self.linked:
            for enemy in self.lvllistlink:
                if not enemy.enalive:
                    self.enalive = False
                if self.enalive:
                    if enemy.classtype == "Enemy":
                        pygame.draw.line(screen, (150, 150, 150), (self.x + 10, self.y + 10),
                                         (enemy.x + 10, enemy.y + 10), 2)
                    if enemy.classtype == "PathEnemy":
                        pygame.draw.line(screen, (150, 150, 150), (self.x + 10, self.y + 10),
                                         (enemy.entity.x + 10, enemy.entity.y + 10), 2)
                    if enemy.classtype == "Boss":
                        pygame.draw.line(screen, (150, 150, 150), (self.x + 10, self.y + 10),
                                         (enemy.x + 25, enemy.y + 25), 2)

    def returnAlive(self):
        return self.enalive


class ScatterEnemy:
    def __init__(self, enalive, ex, ey, speed):
        self.enalive = enalive
        self.x = ex
        self.y = ey
        self.v = speed
        self.entity = Enemy(self.enalive, self.x, self.y, True, True, False, False, 0, 0, False, -1 * self.v, False,
                            False)
        self.classtype = "ScatterEnemy"

    def update(self):
        self.entity.update()
        if self.entity.x > 780:
            self.entity.x = 780
        if self.entity.y > 580:
            self.entity.y = 580
        if self.entity.x < 0:
            self.entity.x = 0
        if self.entity.y < 0:
            self.entity.y = 0
        self.enalive = self.entity.returnAlive()

    def returnAlive(self):
        return self.enalive


class PathEnemy:
    def __init__(self, enalive, direction, ex, ey, pathx, pathy, pathxlength, pathywidth, basespeed, rotationDirection,
                 doesShoot, hasBlades, invincible, jug):
        self.enalive = enalive
        self.direction = direction
        self.x = ex
        self.y = ey
        self.px = pathx
        self.py = pathy
        self.pxl = pathxlength
        self.pyw = pathywidth
        self.spd = basespeed
        self.shoot = doesShoot
        self.blades = hasBlades
        self.inv = invincible
        self.jug = jug
        self.spawn = False
        self.xd = 0
        self.yd = 0
        self.rot = rotationDirection  # Either "cw" or "ccw"
        self.entity = Enemy(self.enalive, self.x, self.y, False, False, False, self.shoot, 0, 0, self.blades, 0,
                            self.inv, self.jug)
        self.linked = False
        self.lvllistlink = []
        self.classtype = "PathEnemy"
        self.lvlid = 0
        self.id = str(random.randrange(100000))

    def update(self):
        if self.enalive:
            self.lvlid = lvl
            global entity
            if not self.spawn:
                if self.direction == "up":
                    self.xd = 0
                    self.yd = self.spd * -1
                if self.direction == "down":
                    self.xd = 0
                    self.yd = self.spd
                if self.direction == "right":
                    self.xd = self.spd
                    self.yd = 0
                if self.direction == "left":
                    self.xd = self.spd * -1
                    self.yd = 0
                self.spawn = True
            if self.rot == "cw":
                if self.direction == "up" and self.entity.y < self.py:
                    self.xd = self.spd
                    self.yd = 0
                    self.direction = "right"
                if self.direction == "right" and self.entity.x > self.px + self.pxl:
                    self.xd = 0
                    self.yd = self.spd
                    self.direction = "down"
                if self.direction == "down" and self.entity.y > self.py + self.pyw:
                    self.xd = self.spd * -1
                    self.yd = 0
                    self.direction = "left"
                if self.direction == "left" and self.entity.x < self.px:
                    self.xd = 0
                    self.yd = self.spd * -1
                    self.direction = "up"
            if self.rot == "ccw":
                if self.direction == "up" and self.entity.y < self.py:
                    self.xd = self.spd * -1
                    self.yd = 0
                    self.direction = "left"
                if self.direction == "left" and self.entity.x < self.px:
                    self.xd = 0
                    self.yd = self.spd
                    self.direction = "down"
                if self.direction == "down" and self.entity.y > self.py + self.pyw:
                    self.xd = self.spd
                    self.yd = 0
                    self.direction = "right"
                if self.direction == "right" and self.entity.x > self.px + self.pxl:
                    self.xd = 0
                    self.yd = self.spd * -1
                    self.direction = "up"
            self.entity.update()
            self.entity.x += self.xd
            self.entity.y += self.yd
        if not self.entity.enalive:
            self.enalive = False
        if self.linked:
            for enemy in self.lvllistlink:
                if not enemy.enalive:
                    self.enalive = False
                if self.enalive:
                    if enemy.classtype == "Enemy":
                        pygame.draw.line(screen, (150, 150, 150), (self.entity.x + 10, self.entity.y + 10),
                                         (enemy.x + 10, enemy.y + 10), 2)
                    if enemy.classtype == "PathEnemy":
                        pygame.draw.line(screen, (150, 150, 150), (self.entity.x + 10, self.entity.y + 10),
                                         (enemy.entity.x + 10, enemy.entity.y + 10), 2)
                    if enemy.classtype == "Boss":
                        pygame.draw.line(screen, (150, 150, 150), (self.entity.x + 25, self.entity.y + 25),
                                         (enemy.x + 25, enemy.y + 25), 2)

    def returnAlive(self):
        return self.enalive


class Collectible:
    def __init__(self, mode, enalive, ex, ey):
        self.mode = mode
        self.enalive = enalive
        self.x = ex
        self.y = ey
        self.classtype = "Collectible"
        self.id = str(random.randrange(100000))

    def update(self):
        global x
        global y
        global lives
        global invincibleTimer
        global hp
        global sethp
        global bombs
        global sid
        global xtrastam
        global lvl
        if self.enalive:
            if self.mode == "life":
                drawLife(self.x, self.y)
                if x > self.x - sid and x < self.x + 10 and y > self.y - sid and y < self.y + 10:
                    self.enalive = False
                    lives += 1
                    getLife()
            if self.mode == "invincible":
                drawInvincible(self.x, self.y)
                if x > self.x - sid and x < self.x + 10 and y > self.y - sid and y < self.y + 10:
                    self.enalive = False
                    sethp = hp
                    invincibleTimer = 300
                    getLife()
            if self.mode == "stam":
                drawStam(self.x, self.y)
                if x > self.x - sid and x < self.x + 10 and y > self.y - sid and y < self.y + 10:
                    self.enalive = False
                    xtrastam += 160
                    getLife()
            if self.mode == "bomb":
                drawBomb(self.x, self.y)
                if x > self.x - sid and x < self.x + sid and y > self.y - sid and y < self.y + sid:
                    self.enalive = False
                    bombs += 1
                    pickUpBomb()
            if self.mode[0] == "chain":
                #   When you use chain, it becomes ([mode, [alleninlvllist]] enalive, ex, ey) for parameters. If it's in the allLevelSetup list, it becomes ([mode, []] enalive, ex, ey).
                #   Make sure loe contains names, not the variable for whether it's alive or not.
                drawChain(self.x, self.y)
                if lvl != 40:
                    self.mode[1].clear()
                for entity in allLevelSetup[lvl]:
                    if entity.classtype == "Enemy" or entity.classtype == "PathEnemy":
                        self.mode[1].append(entity)
                        if not entity.enalive or entity.inv:
                            self.mode[1].remove(entity)
                    if entity.classtype == "Boss":
                        self.mode[1].append(entity)
                        if not entity.enalive:
                            self.mode[1].remove(entity)
                if x > self.x - sid and x < self.x + 30 and y > self.y - sid - 5 and y < self.y + 10:
                    self.enalive = False
                    link(self.mode[1])
                    getLife()

    def returnAlive(self):
        return self.enalive


class Blade:
    def __init__(self, enalive, ex, ey, xl, yl, dmg):
        self.x = ex
        self.y = ey
        self.xl = xl
        self.yl = yl
        self.enalive = enalive
        self.dmg = dmg
        self.classtype = "Blade"
        self.id = str(random.randrange(100000))

    def update(self):
        global x
        global y
        global hp
        global sid
        global WHITE
        if self.enalive:
            pygame.draw.rect(screen, WHITE, [self.x, self.y, self.xl, self.yl])
            if x > self.x - sid and x < self.x + self.xl and y > self.y - sid and y < self.y + self.yl and invincibleTimer <= 0:
                hp -= self.dmg

    def returnAlive(self):
        return self.enalive


class MBlade:
    def __init__(self, enalive, ex, ey, xl, yl, xd, yd, dmg):
        self.x = ex
        self.y = ey
        self.xl = xl
        self.yl = yl
        self.enalive = enalive
        self.dmg = dmg
        self.xd = xd
        self.yd = yd
        self.classtype = "MBlade"
        self.id = str(random.randrange(100000))

    def update(self):
        global x
        global y
        global hp
        global sid
        global WHITE
        if self.enalive:
            pygame.draw.rect(screen, WHITE, [self.x, self.y, self.xl, self.yl])
            if x > self.x - sid and x < self.x + self.xl and y > self.y - sid and y < self.y + self.yl:
                hp -= self.dmg
            self.x += self.xd
            self.y += self.yd
            if self.x < 0 or self.x + self.xl > 800:
                self.xd = self.xd * -1
            if self.y < 0 or self.y + self.yl > 600:
                self.yd = self.yd * -1

    def returnAlive(self):
        return self.enalive


class PathBlade:
    def __init__(self, enalive, direction, ex, ey, xlength, ywidth, pathx, pathy, pathxlength, pathywidth, basespeed,
                 rotationDirection, dmg):
        self.enalive = enalive
        self.direction = direction
        self.x = ex
        self.y = ey
        self.px = pathx
        self.py = pathy
        self.pxl = pathxlength
        self.pyw = pathywidth
        self.spd = basespeed
        self.dmg = dmg
        self.spawn = False
        self.xd = 0
        self.yd = 0
        self.rot = rotationDirection  # Either "cw" or "ccw"
        self.x1 = xlength
        self.y1 = ywidth
        self.entity = Blade(self.enalive, self.x, self.y, self.x1, self.y1, self.dmg)
        self.classtype = "PathBlade"
        self.id = str(random.randrange(100000))

    def update(self):
        if self.enalive:
            global entity
            if not self.spawn:
                if self.direction == "up":
                    self.xd = 0
                    self.yd = self.spd * -1
                if self.direction == "down":
                    self.xd = 0
                    self.yd = self.spd
                if self.direction == "right":
                    self.xd = self.spd
                    self.yd = 0
                if self.direction == "left":
                    self.xd = self.spd * -1
                    self.yd = 0
                self.spawn = True
            if self.rot == "cw":
                if self.direction == "up" and self.entity.y < self.py:
                    self.xd = self.spd
                    self.yd = 0
                    self.direction = "right"
                if self.direction == "right" and self.entity.x > self.px + self.pxl:
                    self.xd = 0
                    self.yd = self.spd
                    self.direction = "down"
                if self.direction == "down" and self.entity.y > self.py + self.pyw:
                    self.xd = self.spd * -1
                    self.yd = 0
                    self.direction = "left"
                if self.direction == "left" and self.entity.x < self.px:
                    self.xd = 0
                    self.yd = self.spd * -1
                    self.direction = "up"
            if self.rot == "ccw":
                if self.direction == "up" and self.entity.y < self.py:
                    self.xd = self.spd * -1
                    self.yd = 0
                    self.direction = "left"
                if self.direction == "left" and self.entity.x < self.px:
                    self.xd = 0
                    self.yd = self.spd
                    self.direction = "down"
                if self.direction == "down" and self.entity.y > self.py + self.pyw:
                    self.xd = self.spd
                    self.yd = 0
                    self.direction = "right"
                if self.direction == "right" and self.entity.x > self.px + self.pxl:
                    self.xd = 0
                    self.yd = self.spd * -1
                    self.direction = "up"
            self.entity.update()
            self.entity.x += self.xd
            self.entity.y += self.yd
        if not self.entity.enalive:
            self.enalive = False

    def returnAlive(self):
        return self.enalive


class Boss:
    def __init__(self, enalive, color, spd, ex, ey, doesTarget, ehp, takesPDamage, takesBDamage, hasBlades, hasShell,
                 bladeDmg, randomBounce):
        self.enalive = enalive
        self.color = color
        self.speed = spd
        self.x = ex
        self.y = ey
        self.trgt = doesTarget
        xstart = random.uniform(-1, 1)
        ystart = random.uniform(-1, 1)
        self.xd = self.speed * xstart
        self.yd = self.speed * ystart
        self.hp = 1800 * ehp
        self.mhp = self.hp
        self.pd = takesPDamage
        self.bd = takesBDamage
        self.blades = hasBlades
        self.shell = hasShell
        self.bladedmg = True
        self.dmg = bladeDmg * 50
        self.rb = randomBounce
        self.linked = False
        self.lvllistlink = []
        self.classtype = "Boss"
        self.lvlid = 0
        self.id = str(random.randrange(100000))

    def update(self):
        global x
        global y
        global bosssize
        global WHITE
        global hp
        global explode
        global RED
        if self.enalive:
            self.lvlid = lvl
            pygame.draw.rect(screen, self.color, [self.x, self.y, bosssize, bosssize])
            if self.shell:
                pygame.draw.rect(screen, WHITE, [self.x, self.y, bosssize, bosssize], 5)
            if self.trgt:
                if x > self.x + 15:
                    self.x += self.speed
                if x < self.x + 15:
                    self.x -= self.speed
                if y > self.y + 15:
                    self.y += self.speed
                if y < self.y + 15:
                    self.y -= self.speed
            else:
                self.x += self.xd
                self.y += self.yd
            if self.rb:
                if self.x > 750 or self.x < 0:
                    self.xd = self.xd * -1
                    self.yd = random.uniform(-1 * self.speed, self.speed)
                if self.y > 550 or self.y < 0:
                    self.yd = self.yd * -1
                    self.xd = random.uniform(-1 * self.speed, self.speed)
                if self.x < 0 and self.y < 0:
                    self.x = 3
                    self.y = 3
                if self.x < 0 and self.y > 550:
                    self.x = 3
                    self.y = 447
                if self.x > 750 and self.y < 0:
                    self.x = 747
                    self.y = 3
                if self.x > 750 and self.y > 550:
                    self.x = 747
                    self.y = 447
            if not self.rb:
                if self.x > 750 or self.x < 0:
                    self.xd = self.xd * -1
                if self.y > 550 or self.y < 0:
                    self.yd = self.yd * -1
            if self.blades:
                if x >= self.x + 15:
                    pygame.draw.rect(screen, WHITE, [self.x + bosssize + 5, self.y + .5 * bosssize - 5, 50, 10])
                if y >= self.y + 15:
                    pygame.draw.rect(screen, WHITE, [self.x + .5 * bosssize - 2, self.y + bosssize + 5, 10, 50])
                if x <= self.x + 15:
                    pygame.draw.rect(screen, WHITE, [self.x - bosssize - 5, self.y + .5 * bosssize - 5, 50, 10])
                if y <= self.y + 15:
                    pygame.draw.rect(screen, WHITE, [self.x + .5 * bosssize - 2, self.y - bosssize - 5, 10, 50])

                if x >= self.x - 5 - bosssize - sid and x <= self.x + bosssize + 5 + bosssize and y <= self.y + .5 * bosssize + 5 and y >= self.y + .5 * bosssize - 5 - sid:
                    if self.bladedmg:
                        hp -= self.dmg
                        self.bladedmg = False
                if y >= self.y - 5 - bosssize - sid and y <= self.y + bosssize + 5 + bosssize and x <= self.x + .5 * bosssize + 2 and x >= self.x + .5 * bosssize - 2 - sid:
                    if self.bladedmg:
                        hp -= self.dmg
                        self.bladedmg = False
                self.bladedmg = True
            if self.shell:
                if x >= self.x - sid and y >= self.y - sid and x <= self.x + bosssize and y <= self.y + bosssize:
                    hp -= 100
            elif self.pd:
                if d and self.x > x + 25 - bosssize and self.x < x + 35 and self.y > y + .5 * sid - 2 - bosssize and self.y < y + .5 * sid + 2:
                    self.hp -= 30
                    stab()
                elif s and self.x > x + .5 * sid - 2 - bosssize and self.x < x + .5 * sid + 2 and self.y > y + 25 - bosssize and self.y < y + 35:
                    self.hp -= 30
                    stab()
                elif a and self.x > x - 15 - bosssize and self.x < x - 5 and self.y > y + .5 * sid - 2 - bosssize and self.y < y + .5 * sid + 2:
                    self.hp -= 30
                    stab()
                elif w and self.x > x + .5 * sid - 2 - bosssize and self.x < x + .5 * sid + 2 and self.y > y - 15 - bosssize and self.y < y - 5:
                    self.hp -= 30
                    stab()
                if self.hp <= 0:
                    self.enalive = False
                elif self.hp < self.mhp:
                    if self.y > 5:
                        pygame.draw.rect(screen, RED, [self.x + 8, self.y - 5, ((self.hp / self.mhp) * 34), 3])
                    else:
                        pygame.draw.rect(screen, RED, [self.x + 8, self.y + 52, ((self.hp / self.mhp) * 34), 3])
            if self.bd:
                if explode:
                    if mx > self.x and mx < self.x + bosssize and my > self.y and my < self.y + bosssize:
                        self.hp -= 1800
                        if self.hp <= 0:
                            self.enalive = False
                    explode = False
            if self.linked:
                for enemy in self.lvllistlink:
                    if not enemy.enalive:
                        self.enalive = False
                    if self.enalive:
                        if enemy.classtype == "Enemy":
                            pygame.draw.line(screen, (150, 150, 150), (self.x + 25, self.y + 25),
                                             (enemy.x + 10, enemy.y + 10), 2)
                        if enemy.classtype == "PathEnemy":
                            pygame.draw.line(screen, (150, 150, 150), (self.x + 25, self.y + 25),
                                             (enemy.entity.x + 10, enemy.entity.y + 10), 2)
                        if enemy.classtype == "Boss":
                            pygame.draw.line(screen, (150, 150, 150), (self.x + 25, self.y + 25),
                                             (enemy.x + 25, enemy.y + 25), 2)

    def returnAlive(self):
        return self.enalive


class Mire:
    def __init__(self, enalive, mx, my, xl, yw, mifa):
        self.x = mx
        self.y = my
        self.xl = xl
        self.yw = yw
        self.enalive = enalive
        self.mf = mifa
        self.classtype = "Mire"
        self.id = str(random.randrange(100000))

    def update(self):
        global MIRE
        global x
        global y
        global mired
        global sid
        global MIRE
        global mireFactor
        if self.enalive:
            if x > self.x - sid and x < self.x + self.xl and y > self.y - sid and y < self.y + self.yw:
                mired = True
                mireFactor = self.mf
            if self.mf < 1:
                pygame.draw.rect(screen, MIRE, [self.x, self.y, self.xl, self.yw])
            if self.mf > 1:
                pygame.draw.rect(screen, (0, 0, 40), [self.x, self.y, self.xl, self.yw])

    def returnAlive(self):
        return self.enalive


class OldGuy:
    def __init__(self, enalive, ex, ey):
        self.enalive = enalive
        self.x = ex
        self.y = ey
        self.cx = ex
        self.cy = ey
        self.box = [self.x, self.y, self.x + 4, self.y + 2]
        self.v = [.8, .3]
        self.state = "normal"
        self.timeSynapse = 0
        self.classtype = "OldGuy"
        self.id = str(random.randrange(100000))

    def update(self):
        if self.enalive:
            if self.state == "normal":
                self.x += self.v[0]
                self.y += self.v[1]
                if self.x > self.box[2] or self.x < self.box[0]:
                    self.v[0] = self.v[0] * -1
                if self.y > self.box[3] or self.y < self.box[1]:
                    self.v[1] = self.v[1] * -1
                pygame.draw.rect(screen, RED, [self.x, self.y, 70, 70])
                pygame.draw.rect(screen, BROWN, [self.cx - 20, self.cy + 30, 30, 8])
                pygame.draw.rect(screen, BROWN, [self.cx - 20, self.cy + 30, 8, 50])
                if allLevelSetup[63][0].x > self.x - 35:
                    self.getStabbed()
            elif self.state == "stabbed":
                pygame.draw.rect(screen, PALERED, [self.x, self.y, 70, 70])
        if terminateOldGuy:
            self.die()

    def getStabbed(self):
        self.state = "stabbed"
        stab()

    def die(self):
        global lvl
        if self.enalive:
            success()  # <--- hardly that
        self.enalive = False  # :(
        self.timeSynapse += tickSize
        if self.timeSynapse > 3:
            lvl += 1

    def returnAlive(self):
        return self.enalive


class FadeWords:
    def __init__(self, ex, ey, txt, t):
        self.enalive = True
        self.x = ex
        self.y = ey
        self.terminate = False
        if t == finalNum:
            self.terminate = True
        self.t = t
        self.gv = 0
        self.txt = txt
        self.tspeed = 2
        self.hasMaxed = False
        self.run = True
        self.classtype = "FadeWords"
        self.id = str(random.randrange(100000))

    def update(self):
        global terminateOldGuy
        if self.run:
            if self.gv > 250 or self.hasMaxed:
                self.hasMaxed = True
                self.gv -= self.tspeed
                if self.gv < 1:
                    self.gv = 0
                    self.run = False
            elif tick63 > self.t and lvl == 63:
                self.gv += self.tspeed
            elif tick64 > self.t and lvl == 64:
                self.gv += self.tspeed
        if self.gv > 0:
            fadeText = textfin.render(self.txt, True, (0, self.gv, 0))
            screen.blit(fadeText, (self.x, self.y))
        if self.terminate:
            if tick63 > finalNum + 5:
                terminateOldGuy = True

    def returnAlive(self):
        return True


class MoveWords:
    def __init__(self, txt, t):
        self.enalive = True
        self.x = 20
        self.y = 600
        self.txt = txt
        self.t = t
        self.classtype = "MoveWords"
        self.id = str(random.randrange(100000))

    def update(self):
        if tick64 > self.t:
            moveText = textfin.render(self.txt, True, (0, 255, 0))
            screen.blit(moveText, (self.x, self.y))
            self.y -= 1.4

    def returnAlive(self):
        return True


class Murderer:
    def __init__(self, enalive, ex, ey, vel, bladeOn):
        self.enalive = True
        self.x = ex
        self.y = ey
        self.spd = vel
        self.v = 0
        self.b = bladeOn
        self.classtype = "Murderer"
        self.id = str(random.randrange(100000))

    def update(self):
        if self.enalive:
            self.x += self.v
            pygame.draw.rect(screen, BLUE, [self.x, self.y, sid, sid])
            if self.b:
                pygame.draw.rect(screen, WHITE, [self.x + 25, self.y + .5 * sid - 2, 10, 4])
            if not allLevelSetup[63][1].enalive:
                self.enalive = False

    def move(self):
        self.v = self.spd

    def toggleBlade(self, use):
        if use:
            self.b = True
        if not use:
            self.b = False

    def stop(self):
        self.v = 0

    def moveBKWDS(self):
        self.v = -.8 * self.spd

    def returnAlive(self):
        return True


class Back:
    def __init__(self, savedLvl):
        self.x = 10
        self.y = 50
        self.sl = savedLvl

    def update(self):
        global x
        global y
        global lvl
        pygame.draw.rect(screen, random.choice([PURPLE1, PURPLE2, PURPLE3]), [self.x, self.y, 50, 50])
        pygame.draw.line(screen, BLUE, (self.x + 40, self.y + 25), (self.x + 10, self.y + 25), 5)
        pygame.draw.line(screen, BLUE, (self.x + 30, self.y + 8), (self.x + 10, self.y + 25), 5)
        pygame.draw.line(screen, BLUE, (self.x + 30, self.y + 42), (self.x + 10, self.y + 25), 5)
        if x > self.x - sid and x < self.x + 50 and y > self.y - sid and y < self.y + 50:
            success()
            lvl = self.sl
            x = 20
            y = 560
            if lvl == 16:
                x = 400
                y = 560

    def returnAlive(self):
        return True


class ToHiddenRoom:
    def __init__(self, ex, ey, lvlToGo):
        self.x = ex
        self.y = ey
        self.ltg = lvlToGo
        self.counter = 180

    def update(self):
        global x
        global y
        global lvl
        if x > self.x - sid and x < self.x + 50 and y > self.y - sid and y < self.y + 50:
            self.counter -= 1
        else:
            self.counter = 180
        if self.counter < 0:
            lvl = self.ltg
            x = 20
            y = 560

    def returnAlive(self):
        return True


class HiddenItem:
    def __init__(self, item):
        self.i = item
        # Items are "car", "fire", "blood", "deadSwordsman"

    def update(self):
        BLOOD = (random.randrange(120, 135), 0, 0)
        if self.i == "car":
            imp = pygame.image.load("car.png").convert()
            imp = pygame.transform.scale(imp, (220, 220))
            screen.blit(imp, (300, 200))
        if self.i == "fire":
            imp = pygame.image.load("fire.png").convert()
            imp = pygame.transform.scale(imp, (220, 220))
            screen.blit(imp, (300, 200))
        if self.i == "blood":
            screen.fill(BLOOD)
        if self.i == "deadSwordsman":
            DEADSWORDSMAN = (80, 80, 150)
            pygame.draw.rect(screen, DEADSWORDSMAN, [0, 580, 20, 20])
            pygame.draw.rect(screen, BLOOD, [12, 587, 6, 6])
            pygame.draw.rect(screen, BLOOD, [14, 587, 2, 15])
            pygame.draw.rect(screen, WHITE, [15, 588, 10, 4])

    def returnAlive(self):
        return True


###   Functions for game
def Music(title, rep, v):
    mixer.music.load(title)
    mixer.music.set_volume(v)
    mixer.music.play(rep)


def resetFiles(boo, name, passcode):
    global lives
    if boo:
        file = open(name + ".txt", "w")
        file.write(passcode)
        file.close()
        file2 = open(name + "lives.txt", "w")
        file2.write("3")
        file2.close()
        file3 = open(name + "level.txt", "w")
        file3.write("1")
        file3.close()


def initTitleScreen():
    allLevelSetup[0][2].tf.append(allLevelSetup[0][0])
    allLevelSetup[0][2].tf.append(allLevelSetup[0][1])
    allLevelSetup[0][3].tf.append(allLevelSetup[0][0])
    allLevelSetup[0][3].tf.append(allLevelSetup[0][1])
    allLevelSetup[0][4].tf.append(allLevelSetup[0][0])
    allLevelSetup[0][4].tf.append(allLevelSetup[0][1])


def link(loe):
    global allChains
    global usedLinkCombos
    le = []
    canLink = 0
    willBreak = 0
    revle = []
    start = True
    while ((usedLinkCombos.count(le) > 1 or usedLinkCombos.count(revle) > 1) and len(
            le) < 2 and willBreak < 100) or start:
        willBreak += 1
        start = False
        for entry in loe:
            if not entry.enalive:
                loe.remove(entry)
            elif entry.classtype == "Boss" or entry.classtype == "PathEnemy" or entry.classtype == "Enemy":
                canLink += 1
        if len(loe) > 1 and canLink >= 1:
            loeUse = loe
            chosenEnemy1 = random.choice(loeUse)
            loeUse.remove(chosenEnemy1)
            chosenEnemy2 = random.choice(loeUse)
            idlist = [chosenEnemy1.id, chosenEnemy2.id]
            while usedLinkCombos.count(idlist) > 1 and enemiesLeft > 2:
                loeUse = loe
                chosenEnemy1 = random.choice(loeUse)
                loeUse.remove(chosenEnemy1)
                chosenEnemy2 = random.choice(loeUse)
                idlist = [chosenEnemy1.id, chosenEnemy2.id]
            le.append(chosenEnemy1)
            le.append(chosenEnemy2)
            chosenEnemy1.linked = True
            chosenEnemy2.linked = True
            revle = [le[1].id, le[0].id]
            if not usedLinkCombos.count(le) > 1 or usedLinkCombos.count(revle) > 1:
                usedLinkCombos.append([le[0].id, le[1].id])
                usedLinkCombos.append(revle)
            if len(le) == 2 and not usedLinkCombos.count(le) > 1 or usedLinkCombos.count(revle) > 1:
                le[0].lvllistlink.append(le[1])
                le[1].lvllistlink.append(le[0])
                for chain in allChains:
                    for enemy in chain.mode[1]:
                        if enemy == le[1]:
                            chain.mode[1].remove(enemy)
            if usedLinkCombos.count(le) > 1 or usedLinkCombos.count(revle) > 1:
                le = []
                canLink = 0
                willBreak = 0
                revle = []
                start = True


def randomCoor(widthOfObject):
    return [random.uniform(0, 800 - widthOfObject), random.uniform(0, 600 - widthOfObject)]


def randomSpeed():
    return random.uniform(-10, 10)


def renderText(level):
    global screen
    global paused
    if not paused:
        if level == 15:
            screen.blit(text15, (10, 50))
        if level == 16:
            screen.blit(text16a, (10, 70))
            screen.blit(text16b, (10, 90))
        if level == 17:
            screen.blit(text17, (10, 70))
        if level == 18:
            screen.blit(text18, (210, 50))
        if level == 19:
            screen.blit(text19, (10, 50))
        if level == 21:
            screen.blit(text21, (20, 40))
        if level == 22:
            screen.blit(text22, (310, 290))
        if level == 23:
            screen.blit(text23, (310, 290))
        if level == 24:
            screen.blit(text24, (310, 290))
        if level == 25:
            screen.blit(text25, (220, 290))
        if level == 26:
            screen.blit(text26, (20, 40))
        if level == 27:
            screen.blit(text27, (20, 40))
        if level == 28:
            screen.blit(text28, (20, 40))
        if level == 29:
            screen.blit(text29, (20, 40))
        if level == 30:
            screen.blit(text30, (20, 40))
        if level == 31:
            screen.blit(text31a, (20, 40))
            screen.blit(text31b, (20, 60))
            screen.blit(text31c, (20, 80))
            screen.blit(text31d, (20, 300))
            screen.blit(text31e, (20, 320))
        if level == 32:
            screen.blit(text32, (20, 40))
        if level == 33:
            screen.blit(text33, (20, 40))
        if level == 34:
            screen.blit(text34, (20, 40))
        if level == 35:
            screen.blit(text35, (20, 40))
        if level == 36:
            screen.blit(text36, (20, 40))
        if level == 37:
            screen.blit(text37, (20, 420))
        if level == 38:
            screen.blit(text38, (20, 40))
        if level == 39:
            screen.blit(text39, (20, 40))
        if level == 41:
            screen.blit(text41a, (450, 120))
            screen.blit(text41b, (450, 140))
            screen.blit(text41c, (450, 160))
            screen.blit(text41d, (450, 180))
        if level == 42:
            screen.blit(text42, (375, 295))
        if level == 43:
            screen.blit(text43, (20, 40))
        if level == 44:
            screen.blit(text44, (20, 40))
        if level == 45:
            screen.blit(text45, (20, 40))
        if level == 46:
            screen.blit(text46, (20, 40))
        if level == 47:
            screen.blit(text47, (20, 40))
        if level == 48:
            screen.blit(text48a, (20, 40))
            screen.blit(text48b, (20, 60))
        if level == 49:
            screen.blit(text49, (20, 40))
        if level == 50:
            screen.blit(text50, (270, 290))
        if level == 51:
            screen.blit(text51, (100, 290))
        if level == 52:
            screen.blit(text52, (180, 290))
        if level == 53:
            screen.blit(text53, (180, 290))
        if level == 54:
            screen.blit(text54, (20, 40))
        if level == 55:
            screen.blit(text55, (280, 290))
        if level == 56:
            screen.blit(text56, (135, 290))
        if level == 57:
            screen.blit(text57, (135, 290))
        if level == 58:
            screen.blit(text58, (135, 250))
        if level == 59:
            screen.blit(text59a, (135, 280))
            screen.blit(text59b, (115, 300))
        if level == -1:
            screen.blit(textwin, (350, 280))
            screen.blit(textwin2, (140, 300))


def gameUpdate():
    global x
    global y
    global lvl
    global hp
    global allLevelSetup
    global backupSetup
    global invincibleTimer
    global paused
    global tick32
    global tick63
    global tick64
    global goneFD
    global enemiesLeft
    appendChains()
    if not paused and lvl != 20 and lvl != 40 and lvl > 14 and not lvl == 0 and not lvl == -1:
        lvllist = allLevelSetup[lvl]
        comp = False
        totalKillsForComp = len(lvllist)
        killsInLvl = 0
        for item in lvllist:
            item.update()
            item.enalive = item.returnAlive()
            if type(item) == Blade or type(item) == MBlade or type(item) == PathBlade or type(
                    item) == Collectible or type(item) == Mire or type(item) == ToHiddenRoom:
                totalKillsForComp -= 1
            if type(item) == Enemy or type(item) == PathEnemy:
                if item.inv:
                    totalKillsForComp -= 1
            if not item.enalive and type(item) != Collectible:
                killsInLvl += 1
            if killsInLvl == totalKillsForComp and lvl < 63:
                if lvl == 15:
                    x = 400
                    y = 560
                    lvl += 1
                    success()
                else:
                    x = 20
                    y = 560
                    lvl += 1
                    success()
        if lvl == 32:
            canWin = True
            tick32 += tickSize
            for e in lvllist:
                if not e.enalive:
                    canWin = False
            if tick32 > 120 and canWin:
                lvl = -1
        if lvl == 63:
            tick63 += tickSize
            mixer.music.stop()
            if round(tick63) < 2:
                allLevelSetup[63][0].move()
            elif round(tick63) == 56:
                allLevelSetup[63][0].move()
                allLevelSetup[63][0].toggleBlade(True)
                goneFD = True
            else:
                if not goneFD:
                    allLevelSetup[63][0].stop()
            if allLevelSetup[63][0].x > 580:
                allLevelSetup[63][0].moveBKWDS()
                allLevelSetup[63][0].toggleBlade(False)
            if allLevelSetup[63][0].v < 0:
                if allLevelSetup[63][0].x < 450:
                    allLevelSetup[63][0].stop()
        if lvl == 64:
            tick64 += tickSize
        if hp <= 0:
            setLevels()
        enemiesLeft = totalKillsForComp - killsInLvl
    elif lvl == 0:
        paused = False
        lvllist = allLevelSetup[lvl]
        for item in lvllist:
            item.update()
    elif lvl == -1:
        paused = False
    renderText(lvl)


def appendChains():
    global allLevelSetup
    sampleList = ["This", "is", "a", "list"]
    for level in allLevelSetup:
        for entity in level:
            if type(entity) == Collectible:
                if type(entity.mode) == type(sampleList):
                    entity.mode[1].clear()
    for level in allLevelSetup:
        chainsInLevel = []
        livingEntitiesInLevel = []
        ln = allLevelSetup.index(level)
        for entity in level:
            if type(entity) == Enemy or type(entity) == PathEnemy:
                en = allLevelSetup[ln].index(entity)
                if not entity.inv:
                    livingEntitiesInLevel.append(en)
        for entity in level:
            if type(entity) == Collectible:
                en = allLevelSetup[ln].index(entity)
                if type(entity.mode) == type(sampleList):
                    chainsInLevel.append(en)

        for chain in chainsInLevel:
            for entity in livingEntitiesInLevel:
                allLevelSetup[ln][chain].mode[1].append(allLevelSetup[ln][entity])


def setLevels():
    # Comments for levels are below their corresponding level
    global allLevelSetup
    ### ------------------------------------------------   This is my main list for the game. It sets up all the levels with all the objects in them.
    allLevelSetup = [
        [TextField(75, 200, 400, 75, "username", "username"), TextField(75, 400, 400, 75, "passcode", "passcode"),
         Button(75, 287.5, 200, 100, "Start/Create", "save", []),
         Button(287.5, 287.5, 187.5, 100, "Reset profile", "reset", []),
         Button(500, 200, 275, 200, "Play without saving", "go", [])],
        [1],
        [2],
        [3],
        [4],
        [5],
        [6],
        [7],
        [8],
        [9],
        [10],
        [11],
        [12],
        [12],
        [14],
        [Enemy(True, 600, 280, True, False, False, True, 0, 12, False, 0, False, False),
         Enemy(True, 600, 180, True, False, False, True, 0, 12, False, 0, False, False),
         Enemy(True, 600, 80, True, False, False, True, 0, 12, False, 0, False, False),
         Enemy(True, 600, 380, True, False, False, True, 0, 12, False, 0, False, False),
         Enemy(True, 600, 480, True, False, False, True, 0, 12, False, 0, False, False),
         Collectible("invincible", True, 200, 280), Blade(True, 400, 0, 20, 600, 700)],
        [Enemy(True, 600, 100, True, False, False, False, 19, 0, True, 0, True, False),
         Enemy(True, 600, 200, True, False, False, False, 17, 0, True, 0, True, False),
         Enemy(True, 600, 300, True, False, False, False, 15, 0, True, 0, True, False),
         Enemy(True, 600, 400, True, False, False, False, 13, 0, True, 0, True, False),
         Blade(True, 300, 0, 20, 600, 700), Blade(True, 500, 0, 20, 600, 700),
         Enemy(True, 400, 40, False, False, False, False, 0, 0, False, 0, False, False),
         Collectible("stam", True, 405, 470)],
        [Enemy(True, 380, 280, True, False, False, True, random.uniform(-3, 3), random.uniform(-3, 3), True, 0, False,
               True)],
        [Enemy(True, 500, 100, True, False, False, True, 0, 5, False, 0, False, False),
         Enemy(True, 600, 300, True, False, False, True, 0, -5, False, 0, False, False),
         Enemy(True, 700, 500, True, False, False, True, 0, 5, False, 0, False, False),
         Blade(True, 200, 0, 2, 600, 800), Collectible("bomb", True, 50, 50), Collectible("bomb", True, 100, 50),
         Collectible("bomb", True, 50, 100), Collectible("bomb", True, 100, 100), Collectible("bomb", True, 75, 75)],
        [Enemy(True, 700, 500, True, True, False, True, 0, 5, True, 1, True, False),
         Enemy(True, 80, 80, True, True, False, True, 0, 5, True, .75, True, False),
         Enemy(True, 600, 80, True, False, False, False, random.uniform(-5, 5), random.uniform(-5, 5), False, 0, False,
               True),
         Enemy(True, 720, 100, True, False, False, False, random.uniform(-5, 5), random.uniform(-5, 5), False, 0, False,
               True)],
        [],  # 20 boss
        [Enemy(True, 600, 10, True, True, False, False, 0, 0, True, .75, False, True),
         Enemy(True, 100, 10, True, True, False, False, 0, 0, True, .75, False, True),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, random.uniform(-5, 5),
               random.uniform(-5, 5), False, 0, True, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, random.uniform(-5, 5),
               random.uniform(-5, 5), False, 0, True, False)],
        [ToHiddenRoom(750, 0, 65), Blade(True, 150, 50, 600, 400, 500),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, False, random.uniform(-10, 10),
               random.uniform(-10, 10), False, 0, False, False)],
        [Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, False, random.uniform(-10, 10),
               random.uniform(-10, 10), False, 0, False, False), Blade(True, 150, 50, 600, 400, 500)],
        [Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, random.uniform(-10, 10),
               random.uniform(-10, 10), False, 0, False, False), Blade(True, 150, 50, 600, 400, 500)],
        [ToHiddenRoom(750, 0, 66), MBlade(True, 395, 50, 10, 500, 3, 0, 500),
         MBlade(True, 395, 50, 10, 500, -3, 0, 500), Blade(True, 0, 50, 350, 10, 500),
         Blade(True, 0, 440, 100, 10, 500), Blade(True, 100, 440, 10, 100, 500), Blade(True, 100, 540, 250, 10, 500),
         Blade(True, 450, 50, 350, 10, 500), Blade(True, 450, 540, 350, 10, 500),
         Enemy(True, randomCoor(20)[0], 290, True, False, False, False, random.uniform(-10, 10), 0, False, 0, False,
               True), Collectible("life", True, 690, 70)],
        [PathEnemy(True, "up", 700, -100, 700, -100, 150, 400, 3, "cw", True, True, False, False),
         PathEnemy(True, "up", 400, 300, 200, 200, 200, 200, 3, "ccw", True, True, False, False),
         PathEnemy(True, "right", -100, 200, -200, 200, 1200, 200, 15, "cw", False, False, False, True)],
        [PathEnemy(True, "right", 300, 100, 300, 100, 400, 400, 4, "cw", True, True, False, False),
         PathEnemy(True, "right", 500, 100, 300, 100, 400, 400, 4, "cw", False, False, False, True),
         PathEnemy(True, "down", 700, 100, 300, 100, 400, 400, 4, "cw", True, True, False, False),
         PathEnemy(True, "up", 300, 500, 300, 100, 400, 400, 4, "cw", True, True, False, False),
         PathEnemy(True, "left", 500, 500, 300, 100, 400, 400, 4, "cw", False, False, False, True),
         PathEnemy(True, "left", 700, 500, 300, 100, 400, 400, 4, "cw", True, True, False, False),
         PathEnemy(True, "up", 300, 300, 300, 100, 400, 400, 4, "cw", False, False, False, True),
         PathEnemy(True, "down", 700, 300, 300, 100, 400, 400, 4, "cw", False, False, False, True),
         Enemy(True, 500, 300, False, False, False, True, 0, 0, True, 0, False, True)],
        [Collectible("life", True, 395, 295), Collectible("life", True, 405, 295),
         PathEnemy(True, "right", 285, 175, 285, 175, 210, 210, 20, "cw", False, False, False, False)],
        [PathEnemy(True, "right", 300, 100, 300, 100, 200, 400, 10, "cw", False, False, False, False),
         PathEnemy(True, "up", 600, 400, 200, 200, 400, 200, 10, "ccw", False, False, False, False),
         PathEnemy(True, "right", 500, 100, 500, 100, 200, 400, 10, "cw", False, False, False, False),
         PathEnemy(True, "up", 600, 250, 200, 50, 400, 200, 10, "ccw", False, False, False, False),
         Blade(True, 350, 0, 100, 600, 500), Blade(True, 0, 250, 800, 100, 500), Blade(True, 150, 350, 200, 200, 500),
         Collectible("invincible", True, 10, 360)],
        [PathEnemy(True, "right", -110, -110, -110, -110, 1000, 800, 10, "cw", True, False, True, False),
         PathEnemy(True, "down", 890, -110, -110, -110, 1000, 800, 10, "cw", True, False, True, False),
         PathEnemy(True, "left", 890, 690, -110, -110, 1000, 800, 10, "cw", True, False, True, False),
         PathEnemy(True, "up", -110, 690, -110, -110, 1000, 800, 10, "cw", True, False, True, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, True, False, random.uniform(-10, 10),
               random.uniform(-10, 10), True, 4, False, False)],
        [Enemy(True, 500, randomCoor(20)[1], True, False, False, False, 0, random.uniform(-10, 10), False, 0, False,
               False),
         Enemy(True, 150, randomCoor(20)[1], True, False, False, False, 0, random.uniform(-10, 10), False, 0, False,
               False), Blade(True, 400, 0, 50, 600, 500), Collectible(["chain", []], True, 10, 360)],
        [PathEnemy(True, "left", 300, 200, 300, 200, 200, 200, 3, "cw", False, False, False, False),
         Enemy(True, randomCoor(20)[1], randomCoor(20)[1], True, False, False, False, random.uniform(-10, 10),
               random.uniform(-10, 10), False, 0, False, False)],
        [PathEnemy(True, "down", 300, 200, 300, 200, 200, 200, 3, "ccw", False, False, False, False),
         Enemy(True, randomCoor(20)[1], randomCoor(20)[1], True, False, False, False, random.uniform(-10, 10),
               random.uniform(-10, 10), False, 0, False, False),
         Enemy(True, randomCoor(20)[1], randomCoor(20)[1], True, False, False, False, random.uniform(-10, 10),
               random.uniform(-10, 10), False, 0, False, False),
         Enemy(True, randomCoor(20)[1], randomCoor(20)[1], True, False, False, False, random.uniform(-10, 10),
               random.uniform(-10, 10), False, 0, False, False)],
        [PathEnemy(True, "down", 300, 200, 300, 200, 200, 200, 3, "ccw", False, False, False, False),
         Enemy(True, randomCoor(20)[1], randomCoor(20)[1], True, False, False, False, random.uniform(-10, 10),
               random.uniform(-10, 10), False, 0, False, False),
         Enemy(True, randomCoor(20)[1], randomCoor(20)[1], True, False, False, False, random.uniform(-10, 10),
               random.uniform(-10, 10), False, 0, False, False),
         Enemy(True, randomCoor(20)[1], randomCoor(20)[1], True, False, False, False, random.uniform(-10, 10),
               random.uniform(-10, 10), False, 0, False, False),
         Enemy(True, randomCoor(20)[1], randomCoor(20)[1], True, False, False, False, random.uniform(-10, 10),
               random.uniform(-10, 10), False, 0, False, False),
         Enemy(True, randomCoor(20)[1], randomCoor(20)[1], True, False, False, False, random.uniform(-10, 10),
               random.uniform(-10, 10), False, 0, False, False)],
        [PathEnemy(True, "right", 20, 20, 20, 20, 750, 550, 20, "cw", True, False, False, True),
         Enemy(True, randomCoor(20)[1], randomCoor(20)[1], True, True, False, False, 0, 0, True, 1.5, False, True)],
        [Enemy(True, randomCoor(20)[1], randomCoor(20)[1], True, False, False, False, randomSpeed(), randomSpeed(),
               True, 0, False, True),
         Enemy(True, randomCoor(20)[1], randomCoor(20)[1], True, False, False, False, randomSpeed(), randomSpeed(),
               True, 0, False, True),
         Enemy(True, randomCoor(20)[1], randomCoor(20)[1], True, False, False, False, randomSpeed(), randomSpeed(),
               True, 0, False, True), Collectible(["chain", []], True, 10, 100),
         Collectible(["chain", []], True, 760, 100)],
        [Blade(True, 0, 50, 800, 350, 500),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, 0, random.uniform(-10, 10), False,
               0, False, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, 0, random.uniform(-10, 10), False,
               0, False, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, 0, random.uniform(-10, 10), False,
               0, False, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, 0, random.uniform(-10, 10), False,
               0, False, False)],
        [Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, True, False, True, 0, 0, True, 1.2, False, True)],
        [PathEnemy(True, "right", 20, 20, 20, 20, 750, 550, 20, "cw", True, False, False, True),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, True, False, True, 0, 0, True, 1.2, False, True),
         Collectible("life", True, 780, 10)],
        [],  # 40 boss
        [Mire(True, 0, 500, 800, 100, .5), Mire(True, 0, 0, 800, 5, .5), Mire(True, 0, 15, 800, 5, .5),
         Mire(True, 0, 35, 800, 65, .5),
         Enemy(True, randomCoor(20)[0], 200, True, False, False, False, randomSpeed(), 0, False, 0, False, False),
         MBlade(True, 200, 50, 20, 550, 0, 2, 500), MBlade(True, 400, 50, 20, 550, 0, 2, 500),
         Enemy(True, 100, 100, True, False, True, False, 0, 0, True, 2, False, False),
         Enemy(True, 300, 100, True, False, True, False, 0, 0, True, 2, False, False),
         Enemy(True, 500, 100, True, False, True, False, 0, 0, True, 2, False, False)],
        [Mire(True, 0, 0, 800, 5, .8), Mire(True, 0, 15, 800, 5, .8), Mire(True, 0, 35, 800, 565, .8),
         Enemy(True, randomCoor(20)[1], randomCoor(20)[1], True, True, False, True, 0, 0, True, 1, False, True)],
        [],
        [Blade(True, 700, 0, 10, 200, 500), Blade(True, 550, 150, 300, 100, 500),
         Enemy(True, 750, 30, False, False, False, False, 0, 0, False, 0, False, False),
         PathEnemy(True, "down", 900, -120, 600, -120, 300, 300, 20, "cw", False, False, False, False),
         PathEnemy(True, "right", 600, -120, 600, -120, 300, 300, 20, "cw", False, False, False, False),
         PathEnemy(True, "up", 600, 180, 600, -120, 300, 300, 20, "cw", False, False, False, False),
         PathEnemy(True, "left", 900, 180, 600, -120, 300, 300, 20, "cw", False, False, False, False),
         PathEnemy(True, "right", -110, -110, -110, -110, 1000, 800, 10, "cw", True, False, True, False),
         PathEnemy(True, "down", 890, -110, -110, -110, 1000, 800, 10, "cw", True, False, True, False),
         PathEnemy(True, "left", 890, 690, -110, -110, 1000, 800, 10, "cw", True, False, True, False),
         PathEnemy(True, "up", -110, 690, -110, -110, 1000, 800, 10, "cw", True, False, True, False),
         Collectible("bomb", True, 395, 295)],
        [],
        [Mire(True, 0, 0, 800, 5, 2), Mire(True, 0, 15, 800, 5, 2), Mire(True, 0, 35, 800, 565, 2),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, 2 * randomSpeed(),
               2 * randomSpeed(), True, 0, False, True)],
        [MBlade(True, randomCoor(20)[0], randomCoor(20)[1], 20, 20, randomSpeed(), randomSpeed(), 500),
         MBlade(True, randomCoor(20)[0], randomCoor(20)[1], 20, 20, randomSpeed(), randomSpeed(), 500),
         MBlade(True, randomCoor(20)[0], randomCoor(20)[1], 20, 20, randomSpeed(), randomSpeed(), 500),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, False, randomSpeed() * 2,
               randomSpeed() * 2, False, 0, False, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, False, randomSpeed() * 2,
               randomSpeed() * 2, False, 0, False, False),
         Collectible("life", True, randomCoor(10)[0], randomCoor(10)[1]),
         Collectible("stam", True, randomCoor(10)[0], randomCoor(10)[1])],
        [MBlade(True, 100, 50, 20, 550, 0, 2, 500), MBlade(True, 300, 50, 20, 550, 0, 2, 500),
         MBlade(True, 500, 50, 20, 550, 0, 2, 500), MBlade(True, 700, 50, 20, 550, 0, 2, 500),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, randomSpeed(), randomSpeed(),
               False, 0, False, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, randomSpeed(), randomSpeed(),
               False, 0, False, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, randomSpeed(), randomSpeed(),
               False, 0, False, False), Collectible("life", True, 780, 10), Collectible("life", True, 780, 560)],
        [ToHiddenRoom(750, 0, 67), MBlade(True, 100, 50, 20, 200, 0, 18, 500),
         MBlade(True, 300, 50, 20, 200, 0, 18, 500), MBlade(True, 500, 50, 20, 200, 0, 18, 500),
         MBlade(True, 700, 50, 20, 200, 0, 18, 500), MBlade(True, 50, 200, 250, 20, 18, 0, 500),
         MBlade(True, 50, 400, 250, 20, 18, 0, 500),
         Enemy(True, 400, 300, True, False, False, False, 0, 0, False, 0, False, False),
         PathBlade(True, "down", 370, 270, 20, 20, 370, 270, 60, 60, 5, "ccw", 800),
         PathBlade(True, "up", 430, 330, 20, 20, 370, 270, 60, 60, 5, "ccw", 800)],
        [Enemy(True, 100, 50, False, False, False, True, 0, 0, True, 0, False, True),
         Enemy(True, 300, 50, False, False, False, True, 0, 0, True, 0, False, True),
         Enemy(True, 500, 50, False, False, False, True, 0, 0, True, 0, False, True),
         Enemy(True, 700, 50, False, False, False, True, 0, 0, True, 0, False, True)],
        [MBlade(True, 200, 0, 200, 30, 0, 14, 500), MBlade(True, 400, 570, 200, 30, 0, -14, 500),
         Blade(True, 0, 90, 750, 30, 500), PathBlade(True, "right", 200, 5, 5, 5, 200, 5, 300, 75, 5, "cw", 800),
         Enemy(True, 10, 10, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 10, 30, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 10, 50, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 30, 10, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 30, 30, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 30, 50, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 50, 10, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 50, 30, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 50, 50, False, False, False, False, 0, 0, False, 0, False, False)],
        [MBlade(True, 200, 0, 200, 30, 0, 14, 500), MBlade(True, 400, 570, 200, 30, 0, -14, 500),
         Blade(True, 0, 90, 750, 30, 500), PathBlade(True, "right", 200, 5, 5, 5, 200, 5, 300, 75, 5, "cw", 800),
         PathBlade(True, "left", 500, 80, 5, 5, 200, 5, 300, 75, 5, "cw", 800),
         Enemy(True, 10, 10, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 10, 30, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 10, 50, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 30, 10, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 30, 30, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 30, 50, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 50, 10, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 50, 30, False, False, False, False, 0, 0, False, 0, False, False),
         Enemy(True, 50, 50, False, False, False, False, 0, 0, False, 0, False, False)],
        [MBlade(True, 400, 0, 30, 500, randomSpeed() * .1, randomSpeed() * .4, 500),
         MBlade(True, 0, 50, 700, 30, randomSpeed() * .4, randomSpeed() * .1, 500),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, False, randomSpeed() * 2,
               randomSpeed() * 2, False, 0, False, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, False, randomSpeed() * 2,
               randomSpeed() * 2, False, 0, False, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, False, randomSpeed() * 2,
               randomSpeed() * 2, False, 0, False, False), Collectible(["chain", []], True, 760, 100)],
        [MBlade(True, 400, 0, 30, 500, randomSpeed() * .1, randomSpeed() * .4, 500),
         MBlade(True, 0, 50, 700, 30, randomSpeed() * .4, randomSpeed() * .1, 500),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, False, randomSpeed() * 2,
               randomSpeed() * 2, False, 0, False, False), Blade(True, 300, 200, 200, 200, 500),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, False, randomSpeed() * 2,
               randomSpeed() * 2, False, 0, False, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, False, randomSpeed() * 2,
               randomSpeed() * 2, False, 0, False, False), Collectible(["chain", []], True, 760, 100)],
        [Enemy(True, randomCoor(2)[0], randomCoor(2)[1], True, False, False, True, randomSpeed() * 6, randomSpeed() * 6,
               False, 0, False, False), Collectible("life", True, randomCoor(10)[0], randomCoor(10)[1]),
         Collectible("life", True, randomCoor(10)[0], randomCoor(10)[1])],
        [Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, randomSpeed(), randomSpeed(), True,
               0, False, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, randomSpeed(), randomSpeed(), True,
               0, False, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, True, False, True, 0, 0, True, 1.5, False, False)],
        [Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, randomSpeed(), randomSpeed(), True,
               0, False, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, randomSpeed(), randomSpeed(), True,
               0, False, False),
         Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, True, False, True, 0, 0, True, 1.2, False, True)],
        [ToHiddenRoom(0, 0, 68), Blade(True, 0, 35, 800, 265, 500), Blade(True, 140, 35, 400, 600, 500),
         Blade(True, 140, 400, 800, 600, 500), Blade(True, 580, 35, 400, 600, 500), Blade(True, 510, 0, 100, 35, 500),
         Enemy(True, 550, randomCoor(20)[1], True, False, False, False, 0, randomSpeed(), False, 0, False, True),
         Collectible("invincible", True, 135, 295)],
        [Enemy(True, 550, randomCoor(20)[1], True, True, False, True, 0, 0, True, 1.7, False, True),
         Collectible("stam", True, randomCoor(10)[0], randomCoor(10)[1]),
         Collectible("stam", True, randomCoor(10)[0], randomCoor(10)[1]),
         Collectible("stam", True, randomCoor(10)[0], randomCoor(10)[1])],
        [],
        # innocents - all levels with innocents should use a new class called "Scatter", which entails the entities running AWAY from the swordsman, not towards him. However, they shouldn't go off the screen, which wasn't an issue in the past.
        [],
        # innocents
        [],
        # innocents
        [Murderer(True, 0, 327.5, 2, False), OldGuy(True, 600, 300), FadeWords(50, 80, fw17, finalNum),
         FadeWords(50, 80, fw16, 60), FadeWords(50, 80, fw15b, 52), FadeWords(50, 50, fw15a, 52),
         FadeWords(50, 110, fw14c, 48), FadeWords(50, 80, fw14b, 48), FadeWords(50, 50, fw14a, 48),
         FadeWords(50, 110, fw13c, 44), FadeWords(50, 80, fw13b, 44), FadeWords(50, 50, fw13a, 44),
         FadeWords(50, 50, fw12, 40), FadeWords(50, 50, fw11, 36), FadeWords(50, 50, fw10, 32),
         FadeWords(50, 50, fw9, 28), FadeWords(50, 80, fw8, 24), FadeWords(50, 50, fw7, 20),
         FadeWords(50, 80, fw6b, 16), FadeWords(50, 50, fw6a, 16), FadeWords(50, 110, fw5, 12),
         FadeWords(50, 80, fw4, 11), FadeWords(50, 50, fw3, 10), FadeWords(50, 80, fw2b, 6), FadeWords(50, 50, fw2a, 6),
         FadeWords(50, 50, fw1, 2)],
        # Death cutscene for Narrator
        [FadeWords(50, 345, ew31d, 150), FadeWords(50, 315, ew31c, 149), FadeWords(50, 285, ew31b, 148),
         FadeWords(50, 255, ew31a, 147), FadeWords(50, 285, ew30, 140), FadeWords(50, 285, ew29, 132),
         FadeWords(50, 285, ew28, 127), FadeWords(50, 285, ew27, 121), FadeWords(50, 285, ew26, 116),
         FadeWords(50, 285, ew24, 94), FadeWords(50, 285, ew23, 90), FadeWords(50, 315, ew22b, 86),
         FadeWords(50, 285, ew22a, 86), FadeWords(50, 285, ew21, 82), FadeWords(50, 285, ew20, 78),
         FadeWords(50, 315, ew19b, 74), FadeWords(50, 285, ew19a, 74), FadeWords(50, 285, ew18, 70),
         FadeWords(50, 315, ew17b, 66), FadeWords(50, 285, ew17a, 66), FadeWords(50, 285, ew16, 62),
         FadeWords(50, 285, ew15, 57), FadeWords(50, 285, ew14, 53), FadeWords(50, 285, ew13, 49),
         FadeWords(50, 315, ew12b, 45), FadeWords(50, 285, ew12a, 45), FadeWords(550, 285, ew11b, 42),
         FadeWords(50, 285, ew11a, 40), FadeWords(50, 285, ew10, 35), FadeWords(50, 285, ew9, 30),
         FadeWords(50, 285, ew8, 26), MoveWords(ew7, 17), MoveWords(ew6, 16), MoveWords(ew5, 15), MoveWords(ew4, 14),
         FadeWords(50, 285, ew3, 10), FadeWords(50, 240, ew1a, 1), FadeWords(50, 270, ew1b, 1),
         FadeWords(50, 240, ew2a, 6), FadeWords(50, 270, ew2b, 6), FadeWords(50, 300, ew2c, 6)],
        # Final credits --- lvl 64
        [HiddenItem("car"), Back(22)],  # Hidden rooms from here on out, starting here at 65
        [HiddenItem("deadSwordsman"), Back(25)],
        [HiddenItem("blood"), Back(49)],
        [HiddenItem("fire"), Back(58)]]
    ew25time = 98
    for place in ew25list:
        allLevelSetup[64].append(MoveWords(place, ew25time))
        ew25time += (12 / len(ew25list))
    for i in range(60):
        allLevelSetup[56].insert(0, Mire(True, randomCoor(100)[0], randomCoor(100)[1], 100, 100, random.uniform(.3, .85)))
        allLevelSetup[56].insert(0, Mire(True, randomCoor(100)[0], randomCoor(100)[1], 100, 100, random.uniform(1.5, 4)))
        allLevelSetup[57].insert(0, Mire(True, randomCoor(100)[0], randomCoor(100)[1], 100, 100, random.uniform(.3, .85)))
        allLevelSetup[57].insert(0, Mire(True, randomCoor(100)[0], randomCoor(100)[1], 100, 100, random.uniform(1.5, 4)))
    for i in range(3):
        allLevelSetup[60].append(ScatterEnemy(True, randomCoor(20)[0], randomCoor(20)[1], abs(randomSpeed() * .5)))
    for i in range(6):
        allLevelSetup[61].append(ScatterEnemy(True, randomCoor(20)[0], randomCoor(20)[1], abs(randomSpeed() * .5)))
    for i in range(220):
        allLevelSetup[62].append(ScatterEnemy(True, randomCoor(20)[0], randomCoor(20)[1], abs(randomSpeed() * .5)))
    for i in range(8):
        allLevelSetup[43].append(Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, False, randomSpeed(), randomSpeed(),True, 0, False, False))
        allLevelSetup[45].append(Enemy(True, randomCoor(20)[0], randomCoor(20)[1], True, False, False, False, randomSpeed(), randomSpeed(),True, 0, False, False))
    for i in range(5):
        allLevelSetup[43].append(Collectible(["chain", []], True, randomCoor(20)[0], randomCoor(20)[1]))
        if (i + 1) % 2:
            allLevelSetup[45].append(Collectible("life", True, randomCoor(20)[0], randomCoor(20)[1]))
        else:
            allLevelSetup[45].append(Collectible(["chain", []], True, randomCoor(20)[0], randomCoor(20)[1]))
            
    appendChains()


# The rest of these functions are drawing functions for the collectibles
def drawBomb(x, y):
    pygame.draw.rect(screen, GREY, [x, y, sid, sid])
    pygame.draw.rect(screen, BLUE, [x + 8, y + 8, 4, 4])


def drawInvincible(x, y):
    energy_decision = random.randrange(3)
    if energy_decision == 0:
        energy_decision = ENERGY
    elif energy_decision == 1:
        energy_decision = ENERGY2
    elif energy_decision == 2:
        energy_decision = ENERGY3
    pygame.draw.rect(screen, energy_decision, [x, y, 10, 10])


def drawStam(x, y):
    energy_decision = random.randrange(3)
    if energy_decision == 0:
        energy_decision = STAM1
    elif energy_decision == 1:
        energy_decision = STAM2
    elif energy_decision == 2:
        energy_decision = STAM3
    pygame.draw.rect(screen, energy_decision, [x, y, 10, 10])


def drawInvinciblePlayer(x, y):
    energy_decision = random.randrange(3)
    if energy_decision == 0:
        energy_decision = ENERGY
    elif energy_decision == 1:
        energy_decision = ENERGY2
    elif energy_decision == 2:
        energy_decision = ENERGY3
    pygame.draw.rect(screen, energy_decision, [x, y, sid, sid])
    if y > 5:
        pygame.draw.rect(screen, energy_decision, [x + 5, y - 5, ((invincibleTimer / 300) * 10), 3])
    else:
        pygame.draw.rect(screen, energy_decision, [x + 5, y + 22, ((invincibleTimer / 300) * 10), 3])


def drawLife(x, y):
    rgcol = random.randrange(0, 200, 50)
    pygame.draw.rect(screen, (rgcol, rgcol, random.randrange(200, 255)), [x, y, 10, 10])


def drawChain(x, y):
    pygame.draw.rect(screen, (150, 150, 150), [x, y, 30, 5])
    pygame.draw.rect(screen, (150, 150, 150), [x + 5, y - 5, 5, 15])
    pygame.draw.rect(screen, (150, 150, 150), [x + 20, y - 5, 5, 15])


### Begin music
Music('blueSwordsmanTheme.wav', -1, .1)
###

### This is text for last two levels
fw1 = "I guess that's it."
fw2a = "You make me the last President"
fw2b = "of the past version of our country."
fw3 = "You drew."
fw4 = "They ignored."
fw5 = "We couldn't react."
fw6a = "This isn't from your strength"
fw6b = "or our weakness."
fw7 = "This is from your recklessness"
fw8 = "and our divided blindness."
fw9 = "Go on."
fw10 = "I'm at your mercy."
fw11 = "Do what you're going to do."
fw12 = "But first, let me just say this:"
fw13a = "If there is some form of"
fw13b = "intelligent beings in another"
fw13c = "universe,"
fw14a = "or realm, perhaps,"
fw14b = "watching over us, let this"
fw14c = "be a lesson for them,"
fw15a = "so they don't fall into the"
fw15b = "same rabbit hole as us."
# Swordsman stabs him
fw16 = "Hello... change..."
fw17 = "If only I met you sooner..."
# He dies

#   Words for end credits
ew1a = "The US has the weakest gun laws"
ew1b = "of high-income countries."
ew2a = "39k gun-related deaths anually-"
ew2b = "That's 100 per day. This is"
ew2c = "25x more likey than elsewhere."
ew3 = "And that number is only getting worse..."
ew4 = "Developer: Jordan Roosevelt"
ew5 = "Help with storyline ideas: Ryan Mauzy"
ew6 = "Help with game ideas: Ryan Mauzy"
ew7 = "Music: Jordan Roosevelt"
ew8 = "Think..."
ew9 = "about the futility of separation."
ew10 = "What's the point?"
ew11a = "I don't know..."
ew11b = "but..."
ew12a = "I know that it categorizes"
ew12b = "with no room for middle ground."
ew13 = "Red and blue..."
ew14 = "are just arbitrarily named symbols"
ew15 = "for whatever we want to polarize."
ew16 = "So"
ew17a = "Let's stop wasting time and make"
ew17b = "the US truly safe."
ew18 = "Who cares, blue or red?"
ew19a = "We all know what's right,"
ew19b = "so we must act on it."
ew20 = "It's too late for these characters"
ew21 = "but it's not too late for us."
ew22a = "Now, I'm sure you're wondering,"
ew22b = '"Did I win?"'
ew23 = "Well..."
ew24 = "I'll leave that for you to decide."
ew25list = ["Uvalde", "Buffalo", "Parkland", "Highland Park", "Columbine", "Chesapeake", "Colorado Springs", "Tulsa",
            "Portland", "New York City", "Monterey Park", "Half Moon Bay",
            "and too, too many more"]
ew26 = "This isn't just a game."
ew27 = "It is also a warning:"
ew28 = "We must make a change soon."
ew29 = '"We" also entails you.'
ew30 = "As the President of this game said:"
ew31a = """"What's good is good is good;"""
ew31b = "what's bad is bad"
ew31c = "and what's wrong is wrong;"
ew31d = "what's right is right."
ew31d += '"'
# I just used a for loop in the setLevels() to iterate the spacing rather than typing it all out. I might as well have just done this normally, but it adds some complexity to it.

setLevels()
###   Stuff that this wouldn't work without on start of specific level
lvl2en3r = False
lvl2en3l = False
lvl2en3d = False
lvl2en3u = False
lvl3en1r = False
lvl3en1l = False
lvl3en1d = False
lvl3en1u = False
lvl4en1r = False
lvl4en1l = False
lvl4en1d = False
lvl4en1u = False
lvl4en2r = False
lvl4en2l = False
lvl4en2d = False
lvl4en2u = False
lvl4en3r = False
lvl4en3l = False
lvl4en3d = False
lvl4en3u = False
lvl5en1r = False
lvl5en1l = False
lvl5en1d = False
lvl5en1u = False
lvl5en2r = False
lvl5en2l = False
lvl5en2d = False
lvl5en2u = False
lvl5en3r = False
lvl5en3l = False
lvl5en3d = False
lvl5en3u = False
###1
lvl1en1x = 300
lvl1en1y = 50
lvl1en2x = 500
lvl1en2y = 500
lvl1en1ydelta = 2
lvl1en2ydelta = -2
lvl1en1alive = True
lvl1en2alive = True
###2
lvl2en1x = 300
lvl2en1y = 50
lvl2en2x = 500
lvl2en2y = 500
lvl2en3x = 400
lvl2en3y = 300 - .5 * sid
lvl2en1ydelta = 2
lvl2en2ydelta = -2
lvl2en1alive = True
lvl2en2alive = True
lvl2en3alive = True
###3
lvl3en1x = 760
lvl3en1y = 20
lvl3en1xdelta = 0
lvl3en1ydelta = 0
lvl3en1alive = True
###4
lvl4en1x = 760
lvl4en1y = 20
lvl4en1xdelta = 0
lvl4en1ydelta = 0
lvl4en1alive = True
lvl4en2x = 760
lvl4en2y = 290
lvl4en2xdelta = 0
lvl4en2ydelta = 0
lvl4en2alive = True
lvl4en3x = 760
lvl4en3y = 560
lvl4en3xdelta = 0
lvl4en3ydelta = 0
lvl4en3alive = True
###5
lvl5en1x = 760
lvl5en1y = 20
lvl5en1xdelta = 0
lvl5en1ydelta = 0
lvl5en2x = 760
lvl5en2y = 290
lvl5en2xdelta = 0
lvl5en2ydelta = 0
lvl5en3x = 760
lvl5en3y = 560
lvl5en3xdelta = 0
lvl5en3ydelta = 0
lvl5en4x = 740
lvl5en4y = 560
lvl5en4xdelta = random.uniform(7, 20)
lvl5en4ydelta = random.uniform(7, 20)
lvl5en4alive = True
###6
lvl6en1x = 330
lvl6en1y = 100
lvl6en1alive = True
lvl6en2x = 0
lvl6en2y = 50
lvl6en2xdelta = -2
###7
lvl7en1x = 300
lvl7en1y = 100
lvl7en2x = 500
lvl7en2y = 100
lvl7en3x = 700
lvl7en3y = 100
lvl7en4x = 700
lvl7en4y = 300
lvl7en5x = 700
lvl7en5y = 500
lvl7en6x = 500
lvl7en6y = 500
lvl7en7x = 300
lvl7en7y = 500
lvl7en8x = 300
lvl7en8y = 300
lvl7en9x = 500
lvl7en9y = 300
lvl7en1xdelta = 4
lvl7en1ydelta = 0
lvl7en2xdelta = 4
lvl7en2ydelta = 0
lvl7en3xdelta = 0
lvl7en3ydelta = 4
lvl7en4xdelta = 0
lvl7en4ydelta = 4
lvl7en5xdelta = -4
lvl7en5ydelta = 0
lvl7en6xdelta = -4
lvl7en6ydelta = 0
lvl7en7xdelta = 0
lvl7en7ydelta = -4
lvl7en8xdelta = 0
lvl7en8ydelta = -4
lvl7en1alive = True
lvl7en2alive = True
lvl7en3alive = True
lvl7en4alive = True
lvl7en5alive = True
lvl7en6alive = True
lvl7en7alive = True
lvl7en8alive = True
lvl7en9alive = True
###8
lvl8en1x = 600
lvl8en1y = 50
lvl8en1xdelta = random.uniform(1.5, 4)
lvl8en1ydelta = random.uniform(1.5, 4)
lvl8en1hidden = True
lvl8en1alive = True
###9
lvl9en1x = 600
lvl9en1y = 50
lvl9en1xdelta = random.uniform(1.5, 4)
lvl9en1ydelta = random.uniform(1.5, 4)
lvl9en1hidden = True
lvl9en1alive = True
lvl9en2x = 600
lvl9en2y = 290
lvl9en2xdelta = random.uniform(-4, -1.5)
lvl9en2ydelta = random.uniform(-4, -1.5)
lvl9en2hidden = True
lvl9en2alive = True
lvl9en3x = 600
lvl9en3y = 500
lvl9en3xdelta = random.uniform(1.5, 4)
lvl9en3ydelta = random.uniform(1.5, 4)
lvl9en3hidden = True
lvl9en3alive = True
###10
lvl10en1x = 290
lvl10en1y = 50
lvl10en1xdelta = random.uniform(1.5, 4)
lvl10en1ydelta = random.uniform(1.5, 4)
lvl10en1hidden = True
lvl10en1alive = True
lvl10en2x = 200
lvl10en2y = 0
lvl10en3x = 500
lvl10en3y = 20.0000001
lvl10en4x = 225
lvl10en4y = 560
lvl10en4alive = True
lvl10en5x = 700
lvl10en5y = 400
lvl10en5alive = True
###11
lvl11bomb1x = 50
lvl11bomb1y = 50
lvl11bomb1alive = True
###12
lvl12bomb1x = 770
lvl12bomb1y = 10
lvl12bomb1alive = True
lvl12en1x = 740
lvl12en1y = 10
lvl12en1alive = True
lvl12en2x = 770
lvl12en2y = 40
lvl12en2alive = True
lvl12bullet1x = 745
lvl12bullet1y = 15
lvl12bullet1xdelta = 0
lvl12bullet1ydelta = 0
lvl12bullet2x = 775
lvl12bullet2y = 45
lvl12bullet2xdelta = 0
lvl12bullet2ydelta = 0
lvl12en3alive = True
lvl12firstshot = False
###13
lvl13lifealive = True
lvl13bomb1alive = True
lvl13bomb1x = 20
lvl13bomb1y = 290
lvl13en1x = 750
lvl13en1y = 290
lvl13en1alive = True
lvl13bullet1x = 700
###14
lvl14blade1y = 0
lvl14blade2y = 580
lvl14blade3y = 0
lvl14blade4y = 580
lvl14blade5y = 0
lvl14blade6y = 580
lvl14blade7y = 0
lvl14blade8y = 580
lvl14blade9y = 0
lvl14blade10y = 580
lvl14blade11y = 0
lvl14blade12y = 580
lvl14blade13y = 0
lvl14blade14y = 580
lvl14blade1ydelta = 7
lvl14blade2ydelta = -7
lvl14blade3ydelta = 7
lvl14blade4ydelta = -7
lvl14blade5ydelta = 7
lvl14blade6ydelta = -7
lvl14blade7ydelta = 7
lvl14blade8ydelta = -7
lvl14blade9ydelta = 7
lvl14blade10ydelta = -7
lvl14blade11ydelta = 7
lvl14blade12ydelta = -7
lvl14blade13ydelta = 7
lvl14blade14ydelta = -7
lvl14en1x = random.randrange(550, 650)
lvl14en1y = random.randrange(250, 450)
lvl14en1xdelta = random.uniform(-2, 2)
lvl14en1ydelta = random.uniform(-2, 2)
lvl14en1alive = True
lvl14lifealive = True
######
###20
boss1aalive = True
boss1a = Boss(boss1aalive, (255, 255, 0), 1.4, 500, 200, True, 1, True, False, True, False, 1, False)
initialKillOfB1 = False
boss1balive = False
boss1b = Boss(boss1balive, (255, 255, 0), 7, 500, 200, False, 4, False, True, True, True, 3, True)
switchtick = 100
lvl20co1alive = True
lvl20co1 = Collectible("bomb", lvl20co1alive, randomCoor(20)[0], randomCoor(20)[1])
lvl20co2alive = True
lvl20co2 = Collectible("bomb", lvl20co2alive, randomCoor(20)[0], randomCoor(20)[1])
lvl20co3alive = True
lvl20co3 = Collectible("bomb", lvl20co3alive, randomCoor(20)[0], randomCoor(20)[1])
lvl20co4alive = True
lvl20co4 = Collectible("bomb", lvl20co4alive, randomCoor(20)[0], randomCoor(20)[1])
lvl20co5alive = True
lvl20co5 = Collectible("bomb", lvl20co5alive, randomCoor(20)[0], randomCoor(20)[1])
###40
boss2aalive = True
boss2a = Boss(boss2aalive, (129, 129, 129), 2.5, 575, 275, False, 2, True, False, True, False, .7, True)
initialKillOfB2 = False
boss2balive = False
boss2b = Boss(boss2balive, (129, 129, 129), 1, 575, 275, True, 1, False, False, True, True, .7, False)
lvl40en1alive = True
lvl40en1 = Enemy(lvl40en1alive, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, randomSpeed(),
                 randomSpeed(), False, 0, False, True)
lvl40co1alive = True
lvl40co1 = Collectible(["chain", [lvl40en1, boss2b]], lvl40co1alive, randomCoor(20)[0], randomCoor(20)[1])

### This is all the stuff to set up the text that the narrator says for each of the levels.
text0 = textfb.render('The Blue Swordsman', True, BLUE)
text0r = text0.get_rect(center=(400, 300))
text1b = textf.render('Use wasd to move, and arrow keys to use your sword.', True, GREEN)
text1c = textf.render('Slay all the red squares in each level to progress.', True, GREEN)
text1d = textf.render('Press h to expend stamina to rapidly gain hp.', True, GREEN)
text1e = textf.render('Press m to toggle music, and p to pause.', True, GREEN)
text2a = textf.render('All white objects are blades. Avoid them.', True, GREEN)
text2b = textf.render('They reduce your HP, which is the red bar on top.', True, GREEN)
text3a = textf.render('Try holding the left shift or spacebar while moving.', True, GREEN)
text3b = textf.render("The yellow bar is stamina. Don't run out.", True, GREEN)
text4a = textf.render("Bottom right is life count. When you lose all 3,", True, GREEN)
text4b = textf.render("it brings you back to the last level after a multiple of 5.", True, GREEN)
text5 = textf.render("Catch it if you can!", True, GREEN)
text6 = textf.render("Go ahead. Try to get through.", True, GREEN)
text7 = textf.render("Take your time. You have as much as you need.", True, GREEN)
text8 = textf.render("It will strike when it gets close. Watch carefully...", True, GREEN)
text9 = textf.render("Watch your back. This will test your snap-reflexes.", True, GREEN)
text10 = textf.render("This is the last  boring one. I promise.", True, GREEN)
text11a = textf.render("Is that a bomb?", True, GREEN)
text11b = textf.render("Ooh, a crosshair!", True, GREEN)
text12 = textf.render("Watch out! They shoot!", True, GREEN)
text13a = textf.render("Get the extra life. You deserve it.", True, GREEN)
text13b = textf.render("At least you have an extra life.", True, GREEN)
text14 = textf.render("Here's a challenge.", True, GREEN)
text15 = textf.render("With this, nothing can stop you!", True, GREEN)
text16a = textf.render("Press the", True, GREEN)
text16b = textf.render("Right-shift to use this.", True, GREEN)
text17 = textf.render("This should give you practice for the upcoming level...", True, GREEN)
text18 = textf.render("5 shots and 3 targets", True, GREEN)
text19 = textf.render("Go nuts on this one.", True, GREEN)
text20a = textf.render("Here, fight one of my boss minions!", True, GREEN)
text20b = textf.render("Ha! Your foolishness will lead to your demise.", True, GREEN)
text21 = textf.render("WhAt?! HoW dId YoU bEaT tHaT?!", True, GREEN)
text22 = textf.render("Watch your step.", True, GREEN)
text23 = textf.render("Watch carefully.", True, GREEN)
text24 = textf.render("Keep moving.", True, GREEN)
text25 = textf.render("You're getting the hang of this.", True, GREEN)
text26 = textf.render("Learn the patterns.", True, GREEN)
text27 = textf.render("Look familiar?", True, GREEN)
text28 = textf.render("Take a breather. No tricks here.", True, GREEN)
text29 = textf.render("Think before you act.", True, GREEN)
text30 = textf.render("Let's see if you can survive the rain of gunfire.", True, GREEN)
text31a = textf.render("Ok, this is the last level", True, GREEN)
text31b = textf.render("with dummy enemies.", True, GREEN)
text31c = textf.render("Don't kill more after.", True, GREEN)
text31d = textf.render("This is a chain. It links", True, GREEN)
text31e = textf.render("enemies together.", True, GREEN)
text32 = textf.render("These are real people; be careful with that thing!", True, GREEN)
text33 = textf.render("Have some self-control!", True, GREEN)
text34 = textf.render("You can't just rampage on like that!", True, GREEN)
text35 = textf.render("Cops have been notified of you.", True, GREEN)
text36 = textf.render("There's a fine line between freedom and recklessness.", True, GREEN)
text37 = textf.render("What were you feeling when you bought those?", True, GREEN)
text38 = textf.render("Frustration? Sadness? Hatred? It all ends the same...", True, GREEN)
text39 = textf.render("It's only a factor, not THE problem.", True, GREEN)
text40 = textf.render("My secret service guard! I can't thank him enough.", True, GREEN)
text41a = textf.render("How could you? He", True, GREEN)
text41b = textf.render("had a life, a family...", True, GREEN)
text41c = textf.render("I guess that just", True, GREEN)
text41d = textf.render("doesn't matter to you.", True, GREEN)
text42 = textf.render("...", True, GREEN)
text43 = textf.render("How DID they let you buy those, you murderer?", True, GREEN)
text44 = textf.render("Wha... what? No check or inspection?", True, GREEN)
text45 = textf.render("It's right in front of them, but they just won't see it.", True, GREEN)
text46 = textf.render("I certainly don't care if you're blue or red...", True, GREEN)
text47 = textf.render("But what's good is good is good; what's bad is bad...", True, GREEN)
text48a = textf.render("And      what's wrong       is wrong;      what's right", True, GREEN)
text48b = textf.render("is         right...", True, GREEN)
text49 = textf.render("You are beyond atrocious- all of your kind!", True, GREEN)
text50 = textf.render("We must stop you now.", True, GREEN)
text51 = textf.render("As our President, I declare you a national threat.", True, GREEN)
text52 = textf.render("NO! They're buying you time... again.", True, GREEN)
text53 = textf.render("We're doomed to your wild kind...", True, GREEN)
text54 = textf.render("Whatever happened to common sense?", True, GREEN)
text55 = textf.render("Or reasonability?", True, GREEN)
text56 = textf.render("I can feel the nation cracking under my feet.", True, GREEN)
text57 = textf.render("They've gone too far... no stopping you now...", True, GREEN)
text58 = textf.render("They saw us on fire... but they never put it out...", True, GREEN)
text59a = textf.render("I guess now all we are is an empty shell of a", True, GREEN)
text59b = textf.render("once-great power... Just a past story to learn from.", True, GREEN)
textwin = textf.render("You win!", True, GREEN)
textwin2 = texts.render("Try tucking yourself in corners to discover hidden rooms!", True, GREEN)
textinstructions1 = texti.render("Enter in valid username and password", True, GREEN)
textinstructions2 = texti.render("to start or reset a profile, or enter", True, GREEN)
textinstructions3 = texti.render("unused ones to create a new profile.", True, GREEN)
pygame.display.set_caption("The Blue Swordsman")
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
initTitleScreen()
###   INITIALIZING CHAIN LIST
allChains = []


def allChainsUpdate():
    global allChains
    allChains = []
    listForUse = ["this", "is", "a", "list"]
    for item in allLevelSetup:
        for entity in item:
            if type(entity) == Collectible:
                if type(entity.mode) == type(listForUse):
                    allChains.append(entity)


allChainsUpdate()


###   Sound Effects:

def stab():
    stabsfx = mixer.Sound('kill.wav')
    stabsfx.set_volume(.1)
    stabsfx.play(0)


def success():
    successsfx = mixer.Sound('success.mp3')
    successsfx.set_volume(.4)
    successsfx.play(0)


def death():
    deathsfx = mixer.Sound('death.wav')
    deathsfx.play(0)


def gameOver():
    gameOversfx = mixer.Sound('gameOver.mp3')
    gameOversfx.play(0)


def kerBOOM():
    boomsfx = mixer.Sound('explosion.wav')
    boomsfx.set_volume(.5)
    boomsfx.play(0)


def pickUpBomb():
    pubsfx = mixer.Sound('pickUpBomb.mp3')
    pubsfx.set_volume(.5)
    pubsfx.play(0)


def surprise():
    surprisesfx = mixer.Sound('surprise.mp3')
    surprisesfx.set_volume(.1)
    surprisesfx.play(0)


def getLife():
    getLifesfx = mixer.Sound('getLife.mp3')
    getLifesfx.play(0)


def enemyShot():
    enemyShotsfx = mixer.Sound('enemyShot.mp3')
    enemyShotsfx.play(0)


def buttonPressed():
    buttonsfx = mixer.Sound('buttonPress.wav')
    buttonsfx.set_volume(.2)
    buttonsfx.play(0)


def keypress():
    keysfx = mixer.Sound('keypress.wav')
    keysfx.set_volume(.2)
    keysfx.play(0)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    #   resetting certain variables per tick
    healing = False
    isSprinting = False
    useStam = False
    keys = pygame.key.get_pressed()

    if not paused and lvl != 0:

        if bombs > 0 or lvl == 0:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)

        if keys[pygame.K_SPACE] and not tired or keys[pygame.K_LSHIFT] and not tired:
            guage -= 7
            vel = 4
            isSprinting = True
            if invincibleTimer > 0:
                vel = 2

        if keys[pygame.K_RSHIFT]:
            if xtrastam > 0:
                if tired:
                    tiredtim += 7
                guage += 7
                xtrastam -= 2
                useStam = True

        # if up arrow key is pressed
        if keys[pygame.K_h] and guage > 0 and not tired:
            guage -= 25
            hp += 12.5
            vel = 0
            healing = True

        newvel = vel * mireFactor
        if keys[pygame.K_w] and y > 0:

            # decrement in y co-ordinate 
            y -= vel
            if mired:
                y += vel
                y -= newvel
        # if down arrow key is pressed    
        if keys[pygame.K_s] and y < 600 - sid:
            # increment in y co-ordinate 
            y += vel
            if mired:
                y -= vel
                y += newvel
        if keys[pygame.K_a] and x > 0:
            x -= vel
            if mired:
                x += vel
                x -= newvel

        if keys[pygame.K_d] and x < 800 - sid:
            x += vel
            if mired:
                x -= vel
                x += newvel
        mired = False
        if guage > 800:
            guage = 800
        if guage <= 0:
            tired = True
    # --- Screen-clearing code

    screen.fill(BLACK)

    # --- Drawing code here
    if paused and lvl != 64 and lvl != 63 and lvl != 0:
        pygame.draw.rect(screen, WHITE, [325, 150, 50, 300])
        pygame.draw.rect(screen, WHITE, [425, 150, 50, 300])
    mx, my = pygame.mouse.get_pos()
    if showexpl > 0:
        pygame.draw.line(screen, (255, 165, 0), (explx, exply), (mx, my), 5)
        pygame.draw.circle(screen, (255, 0, 0), (mx, my), 50)
        showexpl -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and not paused and lvl != 64 and lvl != 63:
            click = True
            if bombs > 0:
                bombs -= 1
                showexpl = 5
                explode = True
                explx = x + 10
                exply = y + 10
                kerBOOM()

        if event.type == pygame.KEYDOWN and lvl != 64 and lvl != 63:
            if event.key == pygame.K_m:
                if lvl != 0:
                    if musicOn:
                        mixer.music.stop()
                        musicOn = False
                    else:
                        mixer.music.play(-1)
                        musicOn = True

            if event.key == pygame.K_p:
                if lvl != 63 and lvl != 64:
                    paused = not paused

            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                bckspce = True

            # Unicode standard is used for string
            # formation
            else:
                keyinp += event.unicode

            if cheat:
                if event.key == pygame.K_n and lvl < 68:
                    lvl += 1
                    print(lvl)
                if event.key == pygame.K_b and lvl > -1:
                    lvl -= 1
                    print(lvl)

            buttonpressed = True
            if lvl == 0:
                for level in allLevelSetup:
                    if allLevelSetup.index(level) == 0:
                        for entity in level:
                            if entity.classtype == "TextField":
                                if entity.activated:
                                    if not bckspce:
                                        if len(entity.inp) < 17:
                                            keypress()
                                    else:
                                        if len(entity.inp) > 0:
                                            keypress()
    nameText = f"Welcome, {newName}!"
    text1a = textf.render(nameText, True, GREEN)
    if newName != "Blue Swordsman" and lvl > 0:
        pygame.display.set_caption(f"The Blue Swordsman - {newName}")
    
    if explode:
        if x < mx < x + sid and y < my < y + sid:
            hp -= 850
    if lvl != 63 and lvl != 64 and lvl != 0 and lvl != -1:
        pygame.draw.rect(screen, ENERGY, [0, 20, guage, 10])
        pygame.draw.rect(screen, (110, 0, 0), [0, 5, hp, 10])
        if isSprinting or tired:
            energy_decision = random.randrange(3)
            if energy_decision == 0:
                energy_decision = ENERGY
            elif energy_decision == 1:
                energy_decision = ENERGY2
            elif energy_decision == 2:
                energy_decision = ENERGY3
            pygame.draw.rect(screen, energy_decision, [0, 20, guage, 10])
        if healing and invincibleTimer <= 0:
            h_decision = random.randrange(3)
            if h_decision == 0:
                h_decision = HEAL1
            elif h_decision == 1:
                h_decision = HEAL2
            elif h_decision == 2:
                h_decision = HEAL3
            pygame.draw.rect(screen, h_decision, [0, 20, guage, 10])
        elif invincibleTimer > 0:
            energy_decision = random.randrange(3)
            if energy_decision == 0:
                energy_decision = ENERGY
            elif energy_decision == 1:
                energy_decision = ENERGY2
            elif energy_decision == 2:
                energy_decision = ENERGY3
            pygame.draw.rect(screen, energy_decision, [0, 5, hp, 10])

        pygame.draw.rect(screen, STAM1, [0, 30, 2 * xtrastam, 5])

        if keys[pygame.K_UP] and not tired and not invincibleTimer > 0:
            guage -= 7
            w = True

        if keys[pygame.K_DOWN] and not tired and not invincibleTimer > 0:
            guage -= 7
            s = True

        if keys[pygame.K_LEFT] and not tired and not invincibleTimer > 0:
            guage -= 7
            a = True

        if keys[pygame.K_RIGHT] and not tired and not invincibleTimer > 0:
            guage -= 7
            d = True

    mx, my = pygame.mouse.get_pos()

    if lvl == 0:
        screen.blit(text0, (text0r[0], text0r[1] - 260))
        screen.blit(textinstructions1, (503, 420))
        screen.blit(textinstructions2, (500, 435))
        screen.blit(textinstructions3, (505, 450))

    ##############################   BEGINNING OF LEVELS   ##############################

    if lvl == 1 and not paused:
        screen.blit(text1a, (10, 50))
        screen.blit(text1b, (10, 70))
        screen.blit(text1c, (10, 90))
        screen.blit(text1d, (10, 110))
        screen.blit(text1e, (10, 130))
        if lvl1en1alive:
            pygame.draw.rect(screen, RED, [lvl1en1x, lvl1en1y, sid, sid])
        if lvl1en2alive:
            pygame.draw.rect(screen, RED, [lvl1en2x, lvl1en2y, sid, sid])

        lvl1en1y += lvl1en1ydelta
        lvl1en2y += lvl1en2ydelta

        if lvl1en1y > 500:
            lvl1en1ydelta = lvl1en1ydelta * -1
        if lvl1en2y > 500:
            lvl1en2ydelta = lvl1en2ydelta * -1

        if lvl1en1y < 50:
            lvl1en1ydelta = lvl1en1ydelta * -1
        if lvl1en2y < 50:
            lvl1en2ydelta = lvl1en2ydelta * -1

        if lvl1en1alive:
            if lvl1en1ydelta < 0:
                pygame.draw.rect(screen, WHITE, [lvl1en1x + .5 * sid - 2, lvl1en1y - 15, 4, 10])
                lvl1en1posy = False
            if lvl1en1ydelta > 0:
                pygame.draw.rect(screen, WHITE, [lvl1en1x + .5 * sid - 2, lvl1en1y + 25, 4, 10])
                lvl1en1posy = True
        if lvl1en2alive:
            if lvl1en2ydelta < 0:
                pygame.draw.rect(screen, WHITE, [lvl1en2x + .5 * sid - 2, lvl1en2y - 15, 4, 10])
                lvl1en2posy = False
            if lvl1en2ydelta > 0:
                pygame.draw.rect(screen, WHITE, [lvl1en2x + .5 * sid - 2, lvl1en2y + 25, 4, 10])
                lvl1en2posy = True

        if d and lvl1en1x > x + 25 - sid and lvl1en1x < x + 35 and lvl1en1y > y + .5 * sid - 2 - sid and lvl1en1y < y + .5 * sid + 2 and lvl1en1alive:
            lvl1en1alive = False
            stab()
        elif s and lvl1en1x > x + .5 * sid - 2 - sid and lvl1en1x < x + .5 * sid + 2 and lvl1en1y > y + 25 - sid and lvl1en1y < y + 35 and lvl1en1alive:
            lvl1en1alive = False
            stab()
        elif a and lvl1en1x > x - 15 - sid and lvl1en1x < x - 5 and lvl1en1y > y + .5 * sid - 2 - sid and lvl1en1y < y + .5 * sid + 2 and lvl1en1alive:
            lvl1en1alive = False
            stab()
        elif w and lvl1en1x > x + .5 * sid - 2 - sid and lvl1en1x < x + .5 * sid + 2 and lvl1en1y > y - 15 - sid and lvl1en1y < y - 5 and lvl1en1alive:
            lvl1en1alive = False
            stab()

        if d and lvl1en2x > x + 25 - sid and lvl1en2x < x + 35 and lvl1en2y > y + .5 * sid - 2 - sid and lvl1en2y < y + .5 * sid + 2 and lvl1en2alive:
            lvl1en2alive = False
            stab()
        elif s and lvl1en2x > x + .5 * sid - 2 - sid and lvl1en2x < x + .5 * sid + 2 and lvl1en2y > y + 25 - sid and lvl1en2y < y + 35 and lvl1en2alive:
            lvl1en2alive = False
            stab()
        elif a and lvl1en2x > x - 15 - sid and lvl1en2x < x - 5 and lvl1en2y > y + .5 * sid - 2 - sid and lvl1en2y < y + .5 * sid + 2 and lvl1en2alive:
            lvl1en2alive = False
            stab()
        elif w and lvl1en2x > x + .5 * sid - 2 - sid and lvl1en2x < x + .5 * sid + 2 and lvl1en2y > y - 15 - sid and lvl1en2y < y - 5 and lvl1en2alive:
            lvl1en2alive = False
            stab()

        if lvl1en1posy and lvl1en1alive and x >= lvl1en1x + .5 * sid - 2 - sid and x <= lvl1en1x + .5 * sid + 2 and y >= lvl1en1y + 25 - sid and y <= lvl1en1y + 35:
            hp -= 50
        if not lvl1en1posy and lvl1en1alive and x >= lvl1en1x + .5 * sid - 2 - sid and x <= lvl1en1x + .5 * sid + 2 and y >= lvl1en1y - 15 - sid and y <= lvl1en1y - 5:
            hp -= 50

        if lvl1en2posy and lvl1en2alive and x >= lvl1en2x + .5 * sid - 2 - sid and x <= lvl1en2x + .5 * sid + 2 and y >= lvl1en2y + 25 - sid and y <= lvl1en2y + 35:
            hp -= 50
        if not lvl1en2posy and lvl1en2alive and x >= lvl1en2x + .5 * sid - 2 - sid and x <= lvl1en2x + .5 * sid + 2 and y >= lvl1en2y - 15 - sid and y <= lvl1en2y - 5:
            hp -= 50

        if not lvl1en1alive and not lvl1en2alive:
            setLevels()
            lvl = 2
            x = 20
            y = 560
            success()

    if lvl == 2 and not paused:
        screen.blit(text2a, (10, 50))
        screen.blit(text2b, (10, 70))
        if lvl2en1alive:
            pygame.draw.rect(screen, RED, [lvl2en1x, lvl2en1y, sid, sid])
        if lvl2en2alive:
            pygame.draw.rect(screen, RED, [lvl2en2x, lvl2en2y, sid, sid])
        if lvl2en3alive:
            pygame.draw.rect(screen, RED, [lvl2en3x, lvl2en3y, sid, sid])

        lvl2en1y += lvl2en1ydelta
        lvl2en2y += lvl2en2ydelta

        if lvl2en1y > 500:
            lvl2en1ydelta = lvl2en1ydelta * -1
        if lvl2en2y > 500:
            lvl2en2ydelta = lvl2en2ydelta * -1

        if lvl2en1y < 50:
            lvl2en1ydelta = lvl2en1ydelta * -1
        if lvl2en2y < 50:
            lvl2en2ydelta = lvl2en2ydelta * -1

        if lvl2en1alive:
            if lvl2en1ydelta < 0:
                pygame.draw.rect(screen, WHITE, [lvl2en1x + .5 * sid - 2, lvl2en1y - 15, 4, 10])
                lvl2en1posy = False
            if lvl2en1ydelta > 0:
                pygame.draw.rect(screen, WHITE, [lvl2en1x + .5 * sid - 2, lvl2en1y + 25, 4, 10])
                lvl2en1posy = True
        if lvl2en2alive:
            if lvl2en2ydelta < 0:
                pygame.draw.rect(screen, WHITE, [lvl2en2x + .5 * sid - 2, lvl2en2y - 15, 4, 10])
                lvl2en2posy = False
            if lvl2en2ydelta > 0:
                pygame.draw.rect(screen, WHITE, [lvl2en2x + .5 * sid - 2, lvl2en2y + 25, 4, 10])
                lvl2en2posy = True
        if lvl2en3alive:
            if x >= lvl2en3x:
                pygame.draw.rect(screen, WHITE, [lvl2en3x + sid + 5, lvl2en3y + .5 * sid - 2, 20, 4])
                lvl2en3r = True
            if x <= lvl2en3x:
                pygame.draw.rect(screen, WHITE, [lvl2en3x - 25, lvl2en3y + .5 * sid - 2, 20, 4])
                lvl2en3l = True
            if y >= lvl2en3y:
                pygame.draw.rect(screen, WHITE, [lvl2en3x + .5 * sid - 2, lvl2en3y + sid + 5, 4, 20])
                lvl2en3d = True
            if y <= lvl2en3y:
                pygame.draw.rect(screen, WHITE, [lvl2en3x + .5 * sid - 2, lvl2en3y - 25, 4, 20])
                lvl2en3u = True

        if d and lvl2en1x > x + 25 - sid and lvl2en1x < x + 35 and lvl2en1y > y + .5 * sid - 2 - sid and lvl2en1y < y + .5 * sid + 2 and lvl2en1alive:
            lvl2en1alive = False
            stab()
        elif s and lvl2en1x > x + .5 * sid - 2 - sid and lvl2en1x < x + .5 * sid + 2 and lvl2en1y > y + 25 - sid and lvl2en1y < y + 35 and lvl2en1alive:
            lvl2en1alive = False
            stab()
        elif a and lvl2en1x > x - 15 - sid and lvl2en1x < x - 5 and lvl2en1y > y + .5 * sid - 2 - sid and lvl2en1y < y + .5 * sid + 2 and lvl2en1alive:
            lvl2en1alive = False
            stab()
        elif w and lvl2en1x > x + .5 * sid - 2 - sid and lvl2en1x < x + .5 * sid + 2 and lvl2en1y > y - 15 - sid and lvl2en1y < y - 5 and lvl2en1alive:
            lvl2en1alive = False
            stab()

        if d and lvl2en2x > x + 25 - sid and lvl2en2x < x + 35 and lvl2en2y > y + .5 * sid - 2 - sid and lvl2en2y < y + .5 * sid + 2 and lvl2en2alive:
            lvl2en2alive = False
            stab()
        elif s and lvl2en2x > x + .5 * sid - 2 - sid and lvl2en2x < x + .5 * sid + 2 and lvl2en2y > y + 25 - sid and lvl2en2y < y + 35 and lvl2en2alive:
            lvl2en2alive = False
            stab()
        elif a and lvl2en2x > x - 15 - sid and lvl2en2x < x - 5 and lvl2en2y > y + .5 * sid - 2 - sid and lvl2en2y < y + .5 * sid + 2 and lvl2en2alive:
            lvl2en2alive = False
            stab()
        elif w and lvl2en2x > x + .5 * sid - 2 - sid and lvl2en2x < x + .5 * sid + 2 and lvl2en2y > y - 15 - sid and lvl2en2y < y - 5 and lvl2en2alive:
            lvl2en2alive = False
            stab()

        if d and lvl2en3x > x + 25 - sid and lvl2en3x < x + 35 and lvl2en3y > y + .5 * sid - 2 - sid and lvl2en3y < y + .5 * sid + 2 and lvl2en3alive:
            lvl2en3alive = False
            stab()
        elif s and lvl2en3x > x + .5 * sid - 2 - sid and lvl2en3x < x + .5 * sid + 2 and lvl2en3y > y + 25 - sid and lvl2en3y < y + 35 and lvl2en3alive:
            lvl2en3alive = False
            stab()
        elif a and lvl2en3x > x - 15 - sid and lvl2en3x < x - 5 and lvl2en3y > y + .5 * sid - 2 - sid and lvl2en3y < y + .5 * sid + 2 and lvl2en3alive:
            lvl2en3alive = False
            stab()
        elif w and lvl2en3x > x + .5 * sid - 2 - sid and lvl2en3x < x + .5 * sid + 2 and lvl2en3y > y - 15 - sid and lvl2en3y < y - 5 and lvl2en3alive:
            lvl2en3alive = False
            stab()

        if lvl2en1posy and lvl2en1alive and x >= lvl2en1x + .5 * sid - 2 - sid and x <= lvl2en1x + .5 * sid + 2 and y >= lvl2en1y + 25 - sid and y <= lvl2en1y + 35:
            hp -= 50
        if not lvl2en1posy and lvl2en1alive and x >= lvl2en1x + .5 * sid - 2 - sid and x <= lvl2en1x + .5 * sid + 2 and y >= lvl2en1y - 15 - sid and y <= lvl2en1y - 5:
            hp -= 50

        if lvl2en2posy and lvl2en2alive and x >= lvl2en2x + .5 * sid - 2 - sid and x <= lvl2en2x + .5 * sid + 2 and y >= lvl2en2y + 25 - sid and y <= lvl2en2y + 35:
            hp -= 50
        if not lvl2en2posy and lvl2en2alive and x >= lvl2en2x + .5 * sid - 2 - sid and x <= lvl2en2x + .5 * sid + 2 and y >= lvl2en2y - 15 - sid and y <= lvl2en2y - 5:
            hp -= 50

        if lvl2en3r and x >= lvl2en3x + 5 and x <= lvl2en3x + sid + 25 and y >= lvl2en3y + .5 * sid - 2 - sid and y <= lvl2en3y + .5 * sid + 2:
            hp -= 50
        if lvl2en3l and x >= lvl2en3x - 25 - sid and x <= lvl2en3x - 5 and y >= lvl2en3y + .5 * sid - 2 - sid and y <= lvl2en3y + .5 * sid + 2:
            hp -= 50
        if lvl2en3d and x >= lvl2en3x + .5 * sid - 2 - sid and x <= lvl2en3x + .5 * sid + 2 and y >= lvl2en3y + 5 and y <= lvl2en3y + sid + 25:
            hp -= 50
        if lvl2en3u and x >= lvl2en3x + .5 * sid - 2 - sid and x <= lvl2en3x + .5 * sid + 2 and y >= lvl2en3y - 25 - sid and y <= lvl2en3y - 5:
            hp -= 50

        if not lvl2en1alive and not lvl2en2alive and not lvl2en3alive:
            setLevels()
            lvl = 3
            x = 20
            y = 560
            success()

    if lvl == 3 and not paused:
        screen.blit(text3a, (10, 50))
        screen.blit(text3b, (10, 70))
        if lvl3en1alive:
            pygame.draw.rect(screen, RED, [lvl3en1x, lvl3en1y, sid, sid])

        lvl3en1x += lvl3en1xdelta
        lvl3en1y += lvl3en1ydelta

        if x >= lvl3en1x and lvl3en1alive:
            lvl3en1xdelta = 1.7
            pygame.draw.rect(screen, WHITE, [lvl3en1x + sid + 5, lvl3en1y + .5 * sid - 2, 20, 4])
            lvl3en1r = True
        if x <= lvl3en1x and lvl3en1alive:
            lvl3en1xdelta = -1.7
            pygame.draw.rect(screen, WHITE, [lvl3en1x - 25, lvl3en1y + .5 * sid - 2, 20, 4])
            lvl3en1l = True
        if y >= lvl3en1y and lvl3en1alive:
            lvl3en1ydelta = 1.7
            pygame.draw.rect(screen, WHITE, [lvl3en1x + .5 * sid - 2, lvl3en1y + sid + 5, 4, 20])
            lvl3en1d = True
        if y <= lvl3en1y and lvl3en1alive:
            lvl3en1ydelta = -1.7
            pygame.draw.rect(screen, WHITE, [lvl3en1x + .5 * sid - 2, lvl3en1y - 25, 4, 20])
            lvl3en1u = True

        if d and lvl3en1x > x + 25 - sid and lvl3en1x < x + 35 and lvl3en1y > y + .5 * sid - 2 - sid and lvl3en1y < y + .5 * sid + 2:
            lvl3en1alive = False
            stab()
        elif s and lvl3en1x > x + .5 * sid - 2 - sid and lvl3en1x < x + .5 * sid + 2 and lvl3en1y > y + 25 - sid and lvl3en1y < y + 35:
            lvl3en1alive = False
            stab()
        elif a and lvl3en1x > x - 15 - sid and lvl3en1x < x - 5 and lvl3en1y > y + .5 * sid - 2 - sid and lvl3en1y < y + .5 * sid + 2:
            lvl3en1alive = False
            stab()
        elif w and lvl3en1x > x + .5 * sid - 2 - sid and lvl3en1x < x + .5 * sid + 2 and lvl3en1y > y - 15 - sid and lvl3en1y < y - 5:
            lvl3en1alive = False
            stab()

        if lvl3en1r and x >= lvl3en1x + 5 and x <= lvl3en1x + sid + 25 and y >= lvl3en1y + .5 * sid - 2 - sid and y <= lvl3en1y + .5 * sid + 2:
            hp -= 50
        if lvl3en1l and x >= lvl3en1x - 25 - sid and x <= lvl3en1x - 5 and y >= lvl3en1y + .5 * sid - 2 - sid and y <= lvl3en1y + .5 * sid + 2:
            hp -= 50
        if lvl3en1d and x >= lvl3en1x + .5 * sid - 2 - sid and x <= lvl3en1x + .5 * sid + 2 and y >= lvl3en1y + 5 and y <= lvl3en1y + sid + 25:
            hp -= 50
        if lvl3en1u and x >= lvl3en1x + .5 * sid - 2 - sid and x <= lvl3en1x + .5 * sid + 2 and y >= lvl3en1y - 25 - sid and y <= lvl3en1y - 5:
            hp -= 50
        if x >= lvl3en1x + .5 * sid - 2 - sid and x <= lvl3en1x + 2 and y >= lvl3en1y + .5 * sid - 2 - sid and y <= lvl3en1y:
            hp -= 50

        if not lvl3en1alive:
            setLevels()
            lvl = 4
            x = 20
            y = 560
            success()

    if lvl == 4 and not paused:
        screen.blit(text4a, (10, 50))
        screen.blit(text4b, (10, 70))
        if lvl4en1alive:
            pygame.draw.rect(screen, RED, [lvl4en1x, lvl4en1y, sid, sid])

        lvl4en1x += lvl4en1xdelta
        lvl4en1y += lvl4en1ydelta

        if x >= lvl4en1x and lvl4en1alive:
            lvl4en1xdelta = random.uniform(1, 1.75)
            pygame.draw.rect(screen, WHITE, [lvl4en1x + sid + 5, lvl4en1y + .5 * sid - 2, 20, 4])
            lvl4en1r = True
        if x <= lvl4en1x and lvl4en1alive:
            lvl4en1xdelta = random.uniform(-1.75, -1)
            pygame.draw.rect(screen, WHITE, [lvl4en1x - 25, lvl4en1y + .5 * sid - 2, 20, 4])
            lvl4en1l = True
        if y >= lvl4en1y and lvl4en1alive:
            lvl4en1ydelta = random.uniform(1, 1.75)
            pygame.draw.rect(screen, WHITE, [lvl4en1x + .5 * sid - 2, lvl4en1y + sid + 5, 4, 20])
            lvl4en1d = True
        if y <= lvl4en1y and lvl4en1alive:
            lvl4en1ydelta = random.uniform(-1.75, -1)
            pygame.draw.rect(screen, WHITE, [lvl4en1x + .5 * sid - 2, lvl4en1y - 25, 4, 20])
            lvl4en1u = True

        if d and lvl4en1x > x + 25 - sid and lvl4en1x < x + 35 and lvl4en1y > y + .5 * sid - 2 - sid and lvl4en1y < y + .5 * sid + 2 and lvl4en1alive:
            lvl4en1alive = False
            stab()
        elif s and lvl4en1x > x + .5 * sid - 2 - sid and lvl4en1x < x + .5 * sid + 2 and lvl4en1y > y + 25 - sid and lvl4en1y < y + 35 and lvl4en1alive:
            lvl4en1alive = False
            stab()
        elif a and lvl4en1x > x - 15 - sid and lvl4en1x < x - 5 and lvl4en1y > y + .5 * sid - 2 - sid and lvl4en1y < y + .5 * sid + 2 and lvl4en1alive:
            lvl4en1alive = False
            stab()
        elif w and lvl4en1x > x + .5 * sid - 2 - sid and lvl4en1x < x + .5 * sid + 2 and lvl4en1y > y - 15 - sid and lvl4en1y < y - 5 and lvl4en1alive:
            lvl4en1alive = False
            stab()

        if lvl4en1alive:
            if lvl4en1r and x >= lvl4en1x + 5 and x <= lvl4en1x + sid + 25 and y >= lvl4en1y + .5 * sid - 2 - sid and y <= lvl4en1y + .5 * sid + 2:
                hp -= 50
            if lvl4en1l and x >= lvl4en1x - 25 - sid and x <= lvl4en1x - 5 and y >= lvl4en1y + .5 * sid - 2 - sid and y <= lvl4en1y + .5 * sid + 2:
                hp -= 50
            if lvl4en1d and x >= lvl4en1x + .5 * sid - 2 - sid and x <= lvl4en1x + .5 * sid + 2 and y >= lvl4en1y + 5 and y <= lvl4en1y + sid + 25:
                hp -= 50
            if lvl4en1u and x >= lvl4en1x + .5 * sid - 2 - sid and x <= lvl4en1x + .5 * sid + 2 and y >= lvl4en1y - 25 - sid and y <= lvl4en1y - 5:
                hp -= 50
            if x >= lvl4en1x + .5 * sid - 2 - sid and x <= lvl4en1x + 2 and y >= lvl4en1y + .5 * sid - 2 - sid and y <= lvl4en1y:
                hp -= 50

        if lvl4en2alive:
            pygame.draw.rect(screen, RED, [lvl4en2x, lvl4en2y, sid, sid])

        lvl4en2x += lvl4en2xdelta
        lvl4en2y += lvl4en2ydelta

        if x >= lvl4en2x and lvl4en2alive:
            lvl4en2xdelta = random.uniform(.75, 1.25)
            pygame.draw.rect(screen, WHITE, [lvl4en2x + sid + 5, lvl4en2y + .5 * sid - 2, 20, 4])
            lvl4en2r = True
        if x <= lvl4en2x and lvl4en2alive:
            lvl4en2xdelta = random.uniform(-1.25, -.75)
            pygame.draw.rect(screen, WHITE, [lvl4en2x - 25, lvl4en2y + .5 * sid - 2, 20, 4])
            lvl4en2l = True
        if y >= lvl4en2y and lvl4en2alive:
            lvl4en2ydelta = random.uniform(.75, 1.25)
            pygame.draw.rect(screen, WHITE, [lvl4en2x + .5 * sid - 2, lvl4en2y + sid + 5, 4, 20])
            lvl4en2d = True
        if y <= lvl4en2y and lvl4en2alive:
            lvl4en2ydelta = random.uniform(-1.25, -.75)
            pygame.draw.rect(screen, WHITE, [lvl4en2x + .5 * sid - 2, lvl4en2y - 25, 4, 20])
            lvl4en2u = True

        if d and lvl4en2x > x + 25 - sid and lvl4en2x < x + 35 and lvl4en2y > y + .5 * sid - 2 - sid and lvl4en2y < y + .5 * sid + 2 and lvl4en2alive:
            lvl4en2alive = False
            stab()
        elif s and lvl4en2x > x + .5 * sid - 2 - sid and lvl4en2x < x + .5 * sid + 2 and lvl4en2y > y + 25 - sid and lvl4en2y < y + 35 and lvl4en2alive:
            lvl4en2alive = False
            stab()
        elif a and lvl4en2x > x - 15 - sid and lvl4en2x < x - 5 and lvl4en2y > y + .5 * sid - 2 - sid and lvl4en2y < y + .5 * sid + 2 and lvl4en2alive:
            lvl4en2alive = False
            stab()
        elif w and lvl4en2x > x + .5 * sid - 2 - sid and lvl4en2x < x + .5 * sid + 2 and lvl4en2y > y - 15 - sid and lvl4en2y < y - 5 and lvl4en2alive:
            lvl4en2alive = False
            stab()

        if lvl4en2alive:
            if lvl4en2r and x >= lvl4en2x + 5 and x <= lvl4en2x + sid + 25 and y >= lvl4en2y + .5 * sid - 2 - sid and y <= lvl4en2y + .5 * sid + 2:
                hp -= 50
            if lvl4en2l and x >= lvl4en2x - 25 - sid and x <= lvl4en2x - 5 and y >= lvl4en2y + .5 * sid - 2 - sid and y <= lvl4en2y + .5 * sid + 2:
                hp -= 50
            if lvl4en2d and x >= lvl4en2x + .5 * sid - 2 - sid and x <= lvl4en2x + .5 * sid + 2 and y >= lvl4en2y + 5 and y <= lvl4en2y + sid + 25:
                hp -= 50
            if lvl4en2u and x >= lvl4en2x + .5 * sid - 2 - sid and x <= lvl4en2x + .5 * sid + 2 and y >= lvl4en2y - 25 - sid and y <= lvl4en2y - 5:
                hp -= 50
            if x >= lvl4en2x + .5 * sid - 2 - sid and x <= lvl4en2x + 2 and y >= lvl4en2y + .5 * sid - 2 - sid and y <= lvl4en2y:
                hp -= 50

        if lvl4en3alive:
            pygame.draw.rect(screen, RED, [lvl4en3x, lvl4en3y, sid, sid])

        lvl4en3x += lvl4en3xdelta
        lvl4en3y += lvl4en3ydelta

        if x >= lvl4en3x and lvl4en3alive:
            lvl4en3xdelta = random.uniform(.25, 1)
            pygame.draw.rect(screen, WHITE, [lvl4en3x + sid + 5, lvl4en3y + .5 * sid - 2, 20, 4])
            lvl4en3r = True
        if x <= lvl4en3x and lvl4en3alive:
            lvl4en3xdelta = random.uniform(-1, -.25)
            pygame.draw.rect(screen, WHITE, [lvl4en3x - 25, lvl4en3y + .5 * sid - 2, 20, 4])
            lvl4en3l = True
        if y >= lvl4en3y and lvl4en3alive:
            lvl4en3ydelta = random.uniform(.25, 1)
            pygame.draw.rect(screen, WHITE, [lvl4en3x + .5 * sid - 2, lvl4en3y + sid + 5, 4, 20])
            lvl4en3d = True
        if y <= lvl4en3y and lvl4en3alive:
            lvl4en3ydelta = random.uniform(-1, -.25)
            pygame.draw.rect(screen, WHITE, [lvl4en3x + .5 * sid - 2, lvl4en3y - 25, 4, 20])
            lvl4en3u = True

        if d and lvl4en3x > x + 25 - sid and lvl4en3x < x + 35 and lvl4en3y > y + .5 * sid - 2 - sid and lvl4en3y < y + .5 * sid + 2 and lvl4en3alive:
            lvl4en3alive = False
            stab()
        elif s and lvl4en3x > x + .5 * sid - 2 - sid and lvl4en3x < x + .5 * sid + 2 and lvl4en3y > y + 25 - sid and lvl4en3y < y + 35 and lvl4en3alive:
            lvl4en3alive = False
            stab()
        elif a and lvl4en3x > x - 15 - sid and lvl4en3x < x - 5 and lvl4en3y > y + .5 * sid - 2 - sid and lvl4en3y < y + .5 * sid + 2 and lvl4en3alive:
            lvl4en3alive = False
            stab()
        elif w and lvl4en3x > x + .5 * sid - 2 - sid and lvl4en3x < x + .5 * sid + 2 and lvl4en3y > y - 15 - sid and lvl4en3y < y - 5 and lvl4en3alive:
            lvl4en3alive = False
            stab()

        if lvl4en3alive:
            if lvl4en3r and x >= lvl4en3x + 5 and x <= lvl4en3x + sid + 25 and y >= lvl4en3y + .5 * sid - 2 - sid and y <= lvl4en3y + .5 * sid + 2:
                hp -= 50
            if lvl4en3l and x >= lvl4en3x - 25 - sid and x <= lvl4en3x - 5 and y >= lvl4en3y + .5 * sid - 2 - sid and y <= lvl4en3y + .5 * sid + 2:
                hp -= 50
            if lvl4en3d and x >= lvl4en3x + .5 * sid - 2 - sid and x <= lvl4en3x + .5 * sid + 2 and y >= lvl4en3y + 5 and y <= lvl4en3y + sid + 25:
                hp -= 50
            if lvl4en3u and x >= lvl4en3x + .5 * sid - 2 - sid and x <= lvl4en3x + .5 * sid + 2 and y >= lvl4en3y - 25 - sid and y <= lvl4en3y - 5:
                hp -= 50
            if x >= lvl4en3x + .5 * sid - 2 - sid and x <= lvl4en3x + 2 and y >= lvl4en3y + .5 * sid - 2 - sid and y <= lvl4en3y:
                hp -= 50

        if not lvl4en1alive and not lvl4en2alive and not lvl4en3alive:
            setLevels()
            lvl = 5
            x = 20
            y = 560
            success()

    if lvl == 5 and not paused:
        screen.blit(text5, (10, 50))
        if lvl5en4alive:
            pygame.draw.rect(screen, RED, [lvl5en4x, lvl5en4y, sid, sid])

        lvl5en4x += lvl5en4xdelta
        lvl5en4y += lvl5en4ydelta
        if lvl5en4x > 800 - sid or lvl5en4x < 0:
            lvl5en4xdelta = lvl5en4xdelta * -1
        if lvl5en4y > 600 - sid or lvl5en4y < 0:
            lvl5en4ydelta = lvl5en4ydelta * -1

        if d and lvl5en4x > x + 25 - sid and lvl5en4x < x + 35 and lvl5en4y > y + .5 * sid - 2 - sid and lvl5en4y < y + .5 * sid + 2:
            lvl5en4alive = False
            stab()
        elif s and lvl5en4x > x + .5 * sid - 2 - sid and lvl5en4x < x + .5 * sid + 2 and lvl5en4y > y + 25 - sid and lvl5en4y < y + 35:
            lvl5en4alive = False
            stab()
        elif a and lvl5en4x > x - 15 - sid and lvl5en4x < x - 5 and lvl5en4y > y + .5 * sid - 2 - sid and lvl5en4y < y + .5 * sid + 2:
            lvl5en4alive = False
            stab()
        elif w and lvl5en4x > x + .5 * sid - 2 - sid and lvl5en4x < x + .5 * sid + 2 and lvl5en4y > y - 15 - sid and lvl5en4y < y - 5:
            lvl5en4alive = False
            stab()

        lvl5en1x += lvl5en1xdelta
        lvl5en1y += lvl5en1ydelta

        if x >= lvl5en1x:
            lvl5en1xdelta = random.uniform(1, 1.75)
            pygame.draw.rect(screen, WHITE, [lvl5en1x + sid + 5, lvl5en1y + .5 * sid - 2, 20, 4])
            lvl5en1r = True
        if x <= lvl5en1x:
            lvl5en1xdelta = random.uniform(-1.75, -1)
            pygame.draw.rect(screen, WHITE, [lvl5en1x - 25, lvl5en1y + .5 * sid - 2, 20, 4])
            lvl5en1l = True
        if y >= lvl5en1y:
            lvl5en1ydelta = random.uniform(1, 1.75)
            pygame.draw.rect(screen, WHITE, [lvl5en1x + .5 * sid - 2, lvl5en1y + sid + 5, 4, 20])
            lvl5en1d = True
        if y <= lvl5en1y:
            lvl5en1ydelta = random.uniform(-1.75, -1)
            pygame.draw.rect(screen, WHITE, [lvl5en1x + .5 * sid - 2, lvl5en1y - 25, 4, 20])
            lvl5en1u = True

        if lvl5en1r and x >= lvl5en1x + 5 and x <= lvl5en1x + sid + 25 and y >= lvl5en1y + .5 * sid - 2 - sid and y <= lvl5en1y + .5 * sid + 2:
            hp -= 50
        if lvl5en1l and x >= lvl5en1x - 25 - sid and x <= lvl5en1x - 5 and y >= lvl5en1y + .5 * sid - 2 - sid and y <= lvl5en1y + .5 * sid + 2:
            hp -= 50
        if lvl5en1d and x >= lvl5en1x + .5 * sid - 2 - sid and x <= lvl5en1x + .5 * sid + 2 and y >= lvl5en1y + 5 and y <= lvl5en1y + sid + 25:
            hp -= 50
        if lvl5en1u and x >= lvl5en1x + .5 * sid - 2 - sid and x <= lvl5en1x + .5 * sid + 2 and y >= lvl5en1y - 25 - sid and y <= lvl5en1y - 5:
            hp -= 50
        if x >= lvl5en1x + .5 * sid - 2 - sid and x <= lvl5en1x + 2 and y >= lvl5en1y + .5 * sid - 2 - sid and y <= lvl5en1y:
            hp -= 50

        lvl5en2x += lvl5en2xdelta
        lvl5en2y += lvl5en2ydelta

        if x >= lvl5en2x:
            lvl5en2xdelta = random.uniform(.75, 1.25)
            pygame.draw.rect(screen, WHITE, [lvl5en2x + sid + 5, lvl5en2y + .5 * sid - 2, 20, 4])
            lvl5en2r = True
        if x <= lvl5en2x:
            lvl5en2xdelta = random.uniform(-1.25, -.75)
            pygame.draw.rect(screen, WHITE, [lvl5en2x - 25, lvl5en2y + .5 * sid - 2, 20, 4])
            lvl5en2l = True
        if y >= lvl5en2y:
            lvl5en2ydelta = random.uniform(.75, 1.25)
            pygame.draw.rect(screen, WHITE, [lvl5en2x + .5 * sid - 2, lvl5en2y + sid + 5, 4, 20])
            lvl5en2d = True
        if y <= lvl5en2y:
            lvl5en2ydelta = random.uniform(-1.25, -.75)
            pygame.draw.rect(screen, WHITE, [lvl5en2x + .5 * sid - 2, lvl5en2y - 25, 4, 20])
            lvl5en2u = True

        if lvl5en2r and x >= lvl5en2x + 5 and x <= lvl5en2x + sid + 25 and y >= lvl5en2y + .5 * sid - 2 - sid and y <= lvl5en2y + .5 * sid + 2:
            hp -= 50
        if lvl5en2l and x >= lvl5en2x - 25 - sid and x <= lvl5en2x - 5 and y >= lvl5en2y + .5 * sid - 2 - sid and y <= lvl5en2y + .5 * sid + 2:
            hp -= 50
        if lvl5en2d and x >= lvl5en2x + .5 * sid - 2 - sid and x <= lvl5en2x + .5 * sid + 2 and y >= lvl5en2y + 5 and y <= lvl5en2y + sid + 25:
            hp -= 50
        if lvl5en2u and x >= lvl5en2x + .5 * sid - 2 - sid and x <= lvl5en2x + .5 * sid + 2 and y >= lvl5en2y - 25 - sid and y <= lvl5en2y - 5:
            hp -= 50
        if x >= lvl5en2x + .5 * sid - 2 - sid and x <= lvl5en2x + 2 and y >= lvl5en2y + .5 * sid - 2 - sid and y <= lvl5en2y:
            hp -= 50

        lvl5en3x += lvl5en3xdelta
        lvl5en3y += lvl5en3ydelta

        if x >= lvl5en3x:
            lvl5en3xdelta = random.uniform(.25, 1)
            pygame.draw.rect(screen, WHITE, [lvl5en3x + sid + 5, lvl5en3y + .5 * sid - 2, 20, 4])
            lvl5en3r = True
        if x <= lvl5en3x:
            lvl5en3xdelta = random.uniform(-1, -.25)
            pygame.draw.rect(screen, WHITE, [lvl5en3x - 25, lvl5en3y + .5 * sid - 2, 20, 4])
            lvl5en3l = True
        if y >= lvl5en3y:
            lvl5en3ydelta = random.uniform(.25, 1)
            pygame.draw.rect(screen, WHITE, [lvl5en3x + .5 * sid - 2, lvl5en3y + sid + 5, 4, 20])
            lvl5en3d = True
        if y <= lvl5en3y:
            lvl5en3ydelta = random.uniform(-1, -.25)
            pygame.draw.rect(screen, WHITE, [lvl5en3x + .5 * sid - 2, lvl5en3y - 25, 4, 20])
            lvl5en3u = True

        if lvl5en3r and x >= lvl5en3x + 5 and x <= lvl5en3x + sid + 25 and y >= lvl5en3y + .5 * sid - 2 - sid and y <= lvl5en3y + .5 * sid + 2:
            hp -= 50
        if lvl5en3l and x >= lvl5en3x - 25 - sid and x <= lvl5en3x - 5 and y >= lvl5en3y + .5 * sid - 2 - sid and y <= lvl5en3y + .5 * sid + 2:
            hp -= 50
        if lvl5en3d and x >= lvl5en3x + .5 * sid - 2 - sid and x <= lvl5en3x + .5 * sid + 2 and y >= lvl5en3y + 5 and y <= lvl5en3y + sid + 25:
            hp -= 50
        if lvl5en3u and x >= lvl5en3x + .5 * sid - 2 - sid and x <= lvl5en3x + .5 * sid + 2 and y >= lvl5en3y - 25 - sid and y <= lvl5en3y - 5:
            hp -= 50
        if x >= lvl5en3x + .5 * sid - 2 - sid and x <= lvl5en3x + 2 and y >= lvl5en3y + .5 * sid - 2 - sid and y <= lvl5en3y:
            hp -= 50

        if not lvl5en4alive:
            lvl = 6
            x = 20
            y = 560
            success()

    if lvl == 6 and not paused:
        screen.blit(text6, (40, 50))
        if lvl6en1alive:
            pygame.draw.rect(screen, RED, [lvl6en1x, lvl6en1y, sid, sid])

        if d and lvl6en1x > x + 25 - sid and lvl6en1x < x + 35 and lvl6en1y > y + .5 * sid - 2 - sid and lvl6en1y < y + .5 * sid + 2:
            lvl6en1alive = False
            stab()
        elif s and lvl6en1x > x + .5 * sid - 2 - sid and lvl6en1x < x + .5 * sid + 2 and lvl6en1y > y + 25 - sid and lvl6en1y < y + 35:
            lvl6en1alive = False
            stab()
        elif a and lvl6en1x > x - 15 - sid and lvl6en1x < x - 5 and lvl6en1y > y + .5 * sid - 2 - sid and lvl6en1y < y + .5 * sid + 2:
            lvl6en1alive = False
            stab()
        elif w and lvl6en1x > x + .5 * sid - 2 - sid and lvl6en1x < x + .5 * sid + 2 and lvl6en1y > y - 15 - sid and lvl6en1y < y - 5:
            lvl6en1alive = False
            stab()

        pygame.draw.rect(screen, WHITE, [lvl6en2x, lvl6en2y, 30, 400])

        if x >= lvl6en2x + 30 and y >= 30 and y <= 450:
            lvl6en2xdelta = 10

        lvl6en2x += lvl6en2xdelta

        if lvl6en2x < 0:
            lvl6en2x = 0

        if x >= lvl6en2x - sid and x <= lvl6en2x + 30 and y >= lvl6en2y - sid and y <= lvl6en2y + 400:
            hp -= 50

        if not lvl6en1alive:
            setLevels()
            lvl = 7
            x = 20
            y = 560
            success()

    if lvl == 7 and not paused:
        screen.blit(text7, (10, 50))

        if lvl7en1alive:
            pygame.draw.rect(screen, RED, [lvl7en1x, lvl7en1y, sid, sid])
        if lvl7en2alive:
            pygame.draw.rect(screen, RED, [lvl7en2x, lvl7en2y, sid, sid])
        if lvl7en3alive:
            pygame.draw.rect(screen, RED, [lvl7en3x, lvl7en3y, sid, sid])
        if lvl7en4alive:
            pygame.draw.rect(screen, RED, [lvl7en4x, lvl7en4y, sid, sid])
        if lvl7en5alive:
            pygame.draw.rect(screen, RED, [lvl7en5x, lvl7en5y, sid, sid])
        if lvl7en6alive:
            pygame.draw.rect(screen, RED, [lvl7en6x, lvl7en6y, sid, sid])
        if lvl7en7alive:
            pygame.draw.rect(screen, RED, [lvl7en7x, lvl7en7y, sid, sid])
        if lvl7en8alive:
            pygame.draw.rect(screen, RED, [lvl7en8x, lvl7en8y, sid, sid])
        if lvl7en9alive:
            pygame.draw.rect(screen, RED, [lvl7en9x, lvl7en9y, sid, sid])

        if d and lvl7en1x > x + 25 - sid and lvl7en1x < x + 35 and lvl7en1y > y + .5 * sid - 2 - sid and lvl7en1y < y + .5 * sid + 2 and lvl7en1alive:
            lvl7en1alive = False
            stab()
        elif s and lvl7en1x > x + .5 * sid - 2 - sid and lvl7en1x < x + .5 * sid + 2 and lvl7en1y > y + 25 - sid and lvl7en1y < y + 35 and lvl7en1alive:
            lvl7en1alive = False
            stab()
        elif a and lvl7en1x > x - 15 - sid and lvl7en1x < x - 5 and lvl7en1y > y + .5 * sid - 2 - sid and lvl7en1y < y + .5 * sid + 2 and lvl7en1alive:
            lvl7en1alive = False
            stab()
        elif w and lvl7en1x > x + .5 * sid - 2 - sid and lvl7en1x < x + .5 * sid + 2 and lvl7en1y > y - 15 - sid and lvl7en1y < y - 5 and lvl7en1alive:
            lvl7en1alive = False
            stab()
        if d and lvl7en2x > x + 25 - sid and lvl7en2x < x + 35 and lvl7en2y > y + .5 * sid - 2 - sid and lvl7en2y < y + .5 * sid + 2 and lvl7en2alive:
            lvl7en2alive = False
            stab()
        elif s and lvl7en2x > x + .5 * sid - 2 - sid and lvl7en2x < x + .5 * sid + 2 and lvl7en2y > y + 25 - sid and lvl7en2y < y + 35 and lvl7en2alive:
            lvl7en2alive = False
            stab()
        elif a and lvl7en2x > x - 15 - sid and lvl7en2x < x - 5 and lvl7en2y > y + .5 * sid - 2 - sid and lvl7en2y < y + .5 * sid + 2 and lvl7en2alive:
            lvl7en2alive = False
            stab()
        elif w and lvl7en2x > x + .5 * sid - 2 - sid and lvl7en2x < x + .5 * sid + 2 and lvl7en2y > y - 15 - sid and lvl7en2y < y - 5 and lvl7en2alive:
            lvl7en2alive = False
            stab()
        if d and lvl7en3x > x + 25 - sid and lvl7en3x < x + 35 and lvl7en3y > y + .5 * sid - 2 - sid and lvl7en3y < y + .5 * sid + 2 and lvl7en3alive:
            lvl7en3alive = False
            stab()
        elif s and lvl7en3x > x + .5 * sid - 2 - sid and lvl7en3x < x + .5 * sid + 2 and lvl7en3y > y + 25 - sid and lvl7en3y < y + 35 and lvl7en3alive:
            lvl7en3alive = False
            stab()
        elif a and lvl7en3x > x - 15 - sid and lvl7en3x < x - 5 and lvl7en3y > y + .5 * sid - 2 - sid and lvl7en3y < y + .5 * sid + 2 and lvl7en3alive:
            lvl7en3alive = False
            stab()
        elif w and lvl7en3x > x + .5 * sid - 2 - sid and lvl7en3x < x + .5 * sid + 2 and lvl7en3y > y - 15 - sid and lvl7en3y < y - 5 and lvl7en3alive:
            lvl7en3alive = False
            stab()
        if d and lvl7en4x > x + 25 - sid and lvl7en4x < x + 35 and lvl7en4y > y + .5 * sid - 2 - sid and lvl7en4y < y + .5 * sid + 2 and lvl7en4alive:
            lvl7en4alive = False
            stab()
        elif s and lvl7en4x > x + .5 * sid - 2 - sid and lvl7en4x < x + .5 * sid + 2 and lvl7en4y > y + 25 - sid and lvl7en4y < y + 35 and lvl7en4alive:
            lvl7en4alive = False
            stab()
        elif a and lvl7en4x > x - 15 - sid and lvl7en4x < x - 5 and lvl7en4y > y + .5 * sid - 2 - sid and lvl7en4y < y + .5 * sid + 2 and lvl7en4alive:
            lvl7en4alive = False
            stab()
        elif w and lvl7en4x > x + .5 * sid - 2 - sid and lvl7en4x < x + .5 * sid + 2 and lvl7en4y > y - 15 - sid and lvl7en4y < y - 5 and lvl7en4alive:
            lvl7en4alive = False
            stab()
        if d and lvl7en5x > x + 25 - sid and lvl7en5x < x + 35 and lvl7en5y > y + .5 * sid - 2 - sid and lvl7en5y < y + .5 * sid + 2 and lvl7en5alive:
            lvl7en5alive = False
            stab()
        elif s and lvl7en5x > x + .5 * sid - 2 - sid and lvl7en5x < x + .5 * sid + 2 and lvl7en5y > y + 25 - sid and lvl7en5y < y + 35 and lvl7en5alive:
            lvl7en5alive = False
            stab()
        elif a and lvl7en5x > x - 15 - sid and lvl7en5x < x - 5 and lvl7en5y > y + .5 * sid - 2 - sid and lvl7en5y < y + .5 * sid + 2 and lvl7en5alive:
            lvl7en5alive = False
            stab()
        elif w and lvl7en5x > x + .5 * sid - 2 - sid and lvl7en5x < x + .5 * sid + 2 and lvl7en5y > y - 15 - sid and lvl7en5y < y - 5 and lvl7en5alive:
            lvl7en5alive = False
            stab()
        if d and lvl7en6x > x + 25 - sid and lvl7en6x < x + 35 and lvl7en6y > y + .5 * sid - 2 - sid and lvl7en6y < y + .5 * sid + 2 and lvl7en6alive:
            lvl7en6alive = False
            stab()
        elif s and lvl7en6x > x + .5 * sid - 2 - sid and lvl7en6x < x + .5 * sid + 2 and lvl7en6y > y + 25 - sid and lvl7en6y < y + 35 and lvl7en6alive:
            lvl7en6alive = False
            stab()
        elif a and lvl7en6x > x - 15 - sid and lvl7en6x < x - 5 and lvl7en6y > y + .5 * sid - 2 - sid and lvl7en6y < y + .5 * sid + 2 and lvl7en6alive:
            lvl7en6alive = False
            stab()
        elif w and lvl7en6x > x + .5 * sid - 2 - sid and lvl7en6x < x + .5 * sid + 2 and lvl7en6y > y - 15 - sid and lvl7en6y < y - 5 and lvl7en6alive:
            lvl7en6alive = False
            stab()
        if d and lvl7en7x > x + 25 - sid and lvl7en7x < x + 35 and lvl7en7y > y + .5 * sid - 2 - sid and lvl7en7y < y + .5 * sid + 2 and lvl7en7alive:
            lvl7en7alive = False
            stab()
        elif s and lvl7en7x > x + .5 * sid - 2 - sid and lvl7en7x < x + .5 * sid + 2 and lvl7en7y > y + 25 - sid and lvl7en7y < y + 35 and lvl7en7alive:
            lvl7en7alive = False
            stab()
        elif a and lvl7en7x > x - 15 - sid and lvl7en7x < x - 5 and lvl7en7y > y + .5 * sid - 2 - sid and lvl7en7y < y + .5 * sid + 2 and lvl7en7alive:
            lvl7en7alive = False
            stab()
        elif w and lvl7en7x > x + .5 * sid - 2 - sid and lvl7en7x < x + .5 * sid + 2 and lvl7en7y > y - 15 - sid and lvl7en7y < y - 5 and lvl7en7alive:
            lvl7en7alive = False
            stab()
        if d and lvl7en8x > x + 25 - sid and lvl7en8x < x + 35 and lvl7en8y > y + .5 * sid - 2 - sid and lvl7en8y < y + .5 * sid + 2 and lvl7en8alive:
            lvl7en8alive = False
            stab()
        elif s and lvl7en8x > x + .5 * sid - 2 - sid and lvl7en8x < x + .5 * sid + 2 and lvl7en8y > y + 25 - sid and lvl7en8y < y + 35 and lvl7en8alive:
            lvl7en8alive = False
            stab()
        elif a and lvl7en8x > x - 15 - sid and lvl7en8x < x - 5 and lvl7en8y > y + .5 * sid - 2 - sid and lvl7en8y < y + .5 * sid + 2 and lvl7en8alive:
            lvl7en8alive = False
            stab()
        elif w and lvl7en8x > x + .5 * sid - 2 - sid and lvl7en8x < x + .5 * sid + 2 and lvl7en8y > y - 15 - sid and lvl7en8y < y - 5 and lvl7en8alive:
            lvl7en8alive = False
            stab()
        if d and lvl7en9x > x + 25 - sid and lvl7en9x < x + 35 and lvl7en9y > y + .5 * sid - 2 - sid and lvl7en9y < y + .5 * sid + 2 and lvl7en9alive:
            lvl7en9alive = False
            stab()
        elif s and lvl7en9x > x + .5 * sid - 2 - sid and lvl7en9x < x + .5 * sid + 2 and lvl7en9y > y + 25 - sid and lvl7en9y < y + 35 and lvl7en9alive:
            lvl7en9alive = False
            stab()
        elif a and lvl7en9x > x - 15 - sid and lvl7en9x < x - 5 and lvl7en9y > y + .5 * sid - 2 - sid and lvl7en9y < y + .5 * sid + 2 and lvl7en9alive:
            lvl7en9alive = False
            stab()
        elif w and lvl7en9x > x + .5 * sid - 2 - sid and lvl7en9x < x + .5 * sid + 2 and lvl7en9y > y - 15 - sid and lvl7en9y < y - 5 and lvl7en9alive:
            lvl7en9alive = False
            stab()

        lvl7en1x += lvl7en1xdelta
        lvl7en1y += lvl7en1ydelta
        lvl7en2x += lvl7en2xdelta
        lvl7en2y += lvl7en2ydelta
        lvl7en3x += lvl7en3xdelta
        lvl7en3y += lvl7en3ydelta
        lvl7en4x += lvl7en4xdelta
        lvl7en4y += lvl7en4ydelta
        lvl7en5x += lvl7en5xdelta
        lvl7en5y += lvl7en5ydelta
        lvl7en6x += lvl7en6xdelta
        lvl7en6y += lvl7en6ydelta
        lvl7en7x += lvl7en7xdelta
        lvl7en7y += lvl7en7ydelta
        lvl7en8x += lvl7en8xdelta
        lvl7en8y += lvl7en8ydelta

        if lvl7en1x > 700 and lvl7en1y == 100:
            lvl7en1x = 700
            lvl7en1xdelta = 0
            lvl7en1ydelta = 4
        if lvl7en1x == 700 and lvl7en1y > 500:
            lvl7en1y = 500
            lvl7en1xdelta = -4
            lvl7en1ydelta = 0
        if lvl7en1x < 300 and lvl7en1y == 500:
            lvl7en1x = 300
            lvl7en1xdelta = 0
            lvl7en1ydelta = -4
        if lvl7en1x == 300 and lvl7en1y < 100:
            lvl7en1y = 100
            lvl7en1xdelta = 4
            lvl7en1ydelta = 0

        if lvl7en2x > 700 and lvl7en2y == 100:
            lvl7en2x = 700
            lvl7en2xdelta = 0
            lvl7en2ydelta = 4
        if lvl7en2x == 700 and lvl7en2y > 500:
            lvl7en2y = 500
            lvl7en2xdelta = -4
            lvl7en2ydelta = 0
        if lvl7en2x < 300 and lvl7en2y == 500:
            lvl7en2x = 300
            lvl7en2xdelta = 0
            lvl7en2ydelta = -4
        if lvl7en2x == 300 and lvl7en2y < 100:
            lvl7en2y = 100
            lvl7en2xdelta = 4
            lvl7en2ydelta = 0

        if lvl7en3x > 700 and lvl7en3y == 100:
            lvl7en3x = 700
            lvl7en3xdelta = 0
            lvl7en3ydelta = 4
        if lvl7en3x == 700 and lvl7en3y > 500:
            lvl7en3y = 500
            lvl7en3xdelta = -4
            lvl7en3ydelta = 0
        if lvl7en3x < 300 and lvl7en3y == 500:
            lvl7en3x = 300
            lvl7en3xdelta = 0
            lvl7en3ydelta = -4
        if lvl7en3x == 300 and lvl7en3y < 100:
            lvl7en3y = 100
            lvl7en3xdelta = 4
            lvl7en3ydelta = 0

        if lvl7en4x > 700 and lvl7en4y == 100:
            lvl7en4x = 700
            lvl7en4xdelta = 0
            lvl7en4ydelta = 4
        if lvl7en4x == 700 and lvl7en4y > 500:
            lvl7en4y = 500
            lvl7en4xdelta = -4
            lvl7en4ydelta = 0
        if lvl7en4x < 300 and lvl7en4y == 500:
            lvl7en4x = 300
            lvl7en4xdelta = 0
            lvl7en4ydelta = -4
        if lvl7en4x == 300 and lvl7en4y < 100:
            lvl7en4y = 100
            lvl7en4xdelta = 4
            lvl7en4ydelta = 0

        if lvl7en5x > 700 and lvl7en5y == 100:
            lvl7en5x = 700
            lvl7en5xdelta = 0
            lvl7en5ydelta = 4
        if lvl7en5x == 700 and lvl7en5y > 500:
            lvl7en5y = 500
            lvl7en5xdelta = -4
            lvl7en5ydelta = 0
        if lvl7en5x < 300 and lvl7en5y == 500:
            lvl7en5x = 300
            lvl7en5xdelta = 0
            lvl7en5ydelta = -4
        if lvl7en5x == 300 and lvl7en5y < 100:
            lvl7en5y = 100
            lvl7en5xdelta = 4
            lvl7en5ydelta = 0

        if lvl7en6x > 700 and lvl7en6y == 100:
            lvl7en6x = 700
            lvl7en6xdelta = 0
            lvl7en6ydelta = 4
        if lvl7en6x == 700 and lvl7en6y > 500:
            lvl7en6y = 500
            lvl7en6xdelta = -4
            lvl7en6ydelta = 0
        if lvl7en6x < 300 and lvl7en6y == 500:
            lvl7en6x = 300
            lvl7en6xdelta = 0
            lvl7en6ydelta = -4
        if lvl7en6x == 300 and lvl7en6y < 100:
            lvl7en6y = 100
            lvl7en6xdelta = 4
            lvl7en6ydelta = 0

        if lvl7en7x > 700 and lvl7en7y == 100:
            lvl7en7x = 700
            lvl7en7xdelta = 0
            lvl7en7ydelta = 4
        if lvl7en7x == 700 and lvl7en7y > 500:
            lvl7en7y = 500
            lvl7en7xdelta = -4
            lvl7en7ydelta = 0
        if lvl7en7x < 300 and lvl7en7y == 500:
            lvl7en7x = 300
            lvl7en7xdelta = 0
            lvl7en7ydelta = -4
        if lvl7en7x == 300 and lvl7en7y < 100:
            lvl7en7y = 100
            lvl7en7xdelta = 4
            lvl7en7ydelta = 0

        if lvl7en8x > 700 and lvl7en8y == 100:
            lvl7en8x = 700
            lvl7en8xdelta = 0
            lvl7en8ydelta = 4
        if lvl7en8x == 700 and lvl7en8y > 500:
            lvl7en8y = 500
            lvl7en8xdelta = -4
            lvl7en8ydelta = 0
        if lvl7en8x < 300 and lvl7en8y == 500:
            lvl7en8x = 300
            lvl7en8xdelta = 0
            lvl7en8ydelta = -4
        if lvl7en8x == 300 and lvl7en8y < 100:
            lvl7en8y = 100
            lvl7en8xdelta = 4
            lvl7en8ydelta = 0

        if lvl7en1alive:
            pygame.draw.rect(screen, WHITE, [lvl7en1x - 25, lvl7en1y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en1x + sid + 5, lvl7en1y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en1x + .5 * sid - 2, lvl7en1y - 25, 4, 20])
            pygame.draw.rect(screen, WHITE, [lvl7en1x + .5 * sid - 2, lvl7en1y + sid + 5, 4, 20])
        if lvl7en2alive:
            pygame.draw.rect(screen, WHITE, [lvl7en2x - 25, lvl7en2y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en2x + sid + 5, lvl7en2y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en2x + .5 * sid - 2, lvl7en2y - 25, 4, 20])
            pygame.draw.rect(screen, WHITE, [lvl7en2x + .5 * sid - 2, lvl7en2y + sid + 5, 4, 20])
        if lvl7en3alive:
            pygame.draw.rect(screen, WHITE, [lvl7en3x - 25, lvl7en3y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en3x + sid + 5, lvl7en3y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en3x + .5 * sid - 2, lvl7en3y - 25, 4, 20])
            pygame.draw.rect(screen, WHITE, [lvl7en3x + .5 * sid - 2, lvl7en3y + sid + 5, 4, 20])
        if lvl7en4alive:
            pygame.draw.rect(screen, WHITE, [lvl7en4x - 25, lvl7en4y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en4x + sid + 5, lvl7en4y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en4x + .5 * sid - 2, lvl7en4y - 25, 4, 20])
            pygame.draw.rect(screen, WHITE, [lvl7en4x + .5 * sid - 2, lvl7en4y + sid + 5, 4, 20])
        if lvl7en5alive:
            pygame.draw.rect(screen, WHITE, [lvl7en5x - 25, lvl7en5y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en5x + sid + 5, lvl7en5y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en5x + .5 * sid - 2, lvl7en5y - 25, 4, 20])
            pygame.draw.rect(screen, WHITE, [lvl7en5x + .5 * sid - 2, lvl7en5y + sid + 5, 4, 20])
        if lvl7en6alive:
            pygame.draw.rect(screen, WHITE, [lvl7en6x - 25, lvl7en6y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en6x + sid + 5, lvl7en6y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en6x + .5 * sid - 2, lvl7en6y - 25, 4, 20])
            pygame.draw.rect(screen, WHITE, [lvl7en6x + .5 * sid - 2, lvl7en6y + sid + 5, 4, 20])
        if lvl7en7alive:
            pygame.draw.rect(screen, WHITE, [lvl7en7x - 25, lvl7en7y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en7x + sid + 5, lvl7en7y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en7x + .5 * sid - 2, lvl7en7y - 25, 4, 20])
            pygame.draw.rect(screen, WHITE, [lvl7en7x + .5 * sid - 2, lvl7en7y + sid + 5, 4, 20])
        if lvl7en8alive:
            pygame.draw.rect(screen, WHITE, [lvl7en8x - 25, lvl7en8y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en8x + sid + 5, lvl7en8y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en8x + .5 * sid - 2, lvl7en8y - 25, 4, 20])
            pygame.draw.rect(screen, WHITE, [lvl7en8x + .5 * sid - 2, lvl7en8y + sid + 5, 4, 20])
        if lvl7en9alive:
            pygame.draw.rect(screen, WHITE, [lvl7en9x - 25, lvl7en9y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en9x + sid + 5, lvl7en9y + .5 * sid - 2, 20, 4])
            pygame.draw.rect(screen, WHITE, [lvl7en9x + .5 * sid - 2, lvl7en9y - 25, 4, 20])
            pygame.draw.rect(screen, WHITE, [lvl7en9x + .5 * sid - 2, lvl7en9y + sid + 5, 4, 20])

        if lvl7en1alive:
            if x >= lvl7en1x + 5 and x <= lvl7en1x + sid + 25 and y >= lvl7en1y + .5 * sid - 2 - sid and y <= lvl7en1y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en1x - 25 - sid and x <= lvl7en1x - 5 and y >= lvl7en1y + .5 * sid - 2 - sid and y <= lvl7en1y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en1x + .5 * sid - 2 - sid and x <= lvl7en1x + .5 * sid + 2 and y >= lvl7en1y + 5 and y <= lvl7en1y + sid + 25:
                hp -= 50
            if x >= lvl7en1x + .5 * sid - 2 - sid and x <= lvl7en1x + .5 * sid + 2 and y >= lvl7en1y - 25 - sid and y <= lvl7en1y - 5:
                hp -= 50

        if lvl7en2alive:
            if x >= lvl7en2x + 5 and x <= lvl7en2x + sid + 25 and y >= lvl7en2y + .5 * sid - 2 - sid and y <= lvl7en2y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en2x - 25 - sid and x <= lvl7en2x - 5 and y >= lvl7en2y + .5 * sid - 2 - sid and y <= lvl7en2y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en2x + .5 * sid - 2 - sid and x <= lvl7en2x + .5 * sid + 2 and y >= lvl7en2y + 5 and y <= lvl7en2y + sid + 25:
                hp -= 50
            if x >= lvl7en2x + .5 * sid - 2 - sid and x <= lvl7en2x + .5 * sid + 2 and y >= lvl7en2y - 25 - sid and y <= lvl7en2y - 5:
                hp -= 50

        if lvl7en3alive:
            if x >= lvl7en3x + 5 and x <= lvl7en3x + sid + 25 and y >= lvl7en3y + .5 * sid - 2 - sid and y <= lvl7en3y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en3x - 25 - sid and x <= lvl7en3x - 5 and y >= lvl7en3y + .5 * sid - 2 - sid and y <= lvl7en3y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en3x + .5 * sid - 2 - sid and x <= lvl7en3x + .5 * sid + 2 and y >= lvl7en3y + 5 and y <= lvl7en3y + sid + 25:
                hp -= 50
            if x >= lvl7en3x + .5 * sid - 2 - sid and x <= lvl7en3x + .5 * sid + 2 and y >= lvl7en3y - 25 - sid and y <= lvl7en3y - 5:
                hp -= 50

        if lvl7en4alive:
            if x >= lvl7en4x + 5 and x <= lvl7en4x + sid + 25 and y >= lvl7en4y + .5 * sid - 2 - sid and y <= lvl7en4y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en4x - 25 - sid and x <= lvl7en4x - 5 and y >= lvl7en4y + .5 * sid - 2 - sid and y <= lvl7en4y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en4x + .5 * sid - 2 - sid and x <= lvl7en4x + .5 * sid + 2 and y >= lvl7en4y + 5 and y <= lvl7en4y + sid + 25:
                hp -= 50
            if x >= lvl7en4x + .5 * sid - 2 - sid and x <= lvl7en4x + .5 * sid + 2 and y >= lvl7en4y - 25 - sid and y <= lvl7en4y - 5:
                hp -= 50

        if lvl7en5alive:
            if x >= lvl7en5x + 5 and x <= lvl7en5x + sid + 25 and y >= lvl7en5y + .5 * sid - 2 - sid and y <= lvl7en5y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en5x - 25 - sid and x <= lvl7en5x - 5 and y >= lvl7en5y + .5 * sid - 2 - sid and y <= lvl7en5y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en5x + .5 * sid - 2 - sid and x <= lvl7en5x + .5 * sid + 2 and y >= lvl7en5y + 5 and y <= lvl7en5y + sid + 25:
                hp -= 50
            if x >= lvl7en5x + .5 * sid - 2 - sid and x <= lvl7en5x + .5 * sid + 2 and y >= lvl7en5y - 25 - sid and y <= lvl7en5y - 5:
                hp -= 50

        if lvl7en6alive:
            if x >= lvl7en6x + 5 and x <= lvl7en6x + sid + 25 and y >= lvl7en6y + .5 * sid - 2 - sid and y <= lvl7en6y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en6x - 25 - sid and x <= lvl7en6x - 5 and y >= lvl7en6y + .5 * sid - 2 - sid and y <= lvl7en6y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en6x + .5 * sid - 2 - sid and x <= lvl7en6x + .5 * sid + 2 and y >= lvl7en6y + 5 and y <= lvl7en6y + sid + 25:
                hp -= 50
            if x >= lvl7en6x + .5 * sid - 2 - sid and x <= lvl7en6x + .5 * sid + 2 and y >= lvl7en6y - 25 - sid and y <= lvl7en6y - 5:
                hp -= 50

        if lvl7en7alive:
            if x >= lvl7en7x + 5 and x <= lvl7en7x + sid + 25 and y >= lvl7en7y + .5 * sid - 2 - sid and y <= lvl7en7y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en7x - 25 - sid and x <= lvl7en7x - 5 and y >= lvl7en7y + .5 * sid - 2 - sid and y <= lvl7en7y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en7x + .5 * sid - 2 - sid and x <= lvl7en7x + .5 * sid + 2 and y >= lvl7en7y + 5 and y <= lvl7en7y + sid + 25:
                hp -= 50
            if x >= lvl7en7x + .5 * sid - 2 - sid and x <= lvl7en7x + .5 * sid + 2 and y >= lvl7en7y - 25 - sid and y <= lvl7en7y - 5:
                hp -= 50

        if lvl7en8alive:
            if x >= lvl7en8x + 5 and x <= lvl7en8x + sid + 25 and y >= lvl7en8y + .5 * sid - 2 - sid and y <= lvl7en8y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en8x - 25 - sid and x <= lvl7en8x - 5 and y >= lvl7en8y + .5 * sid - 2 - sid and y <= lvl7en8y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en8x + .5 * sid - 2 - sid and x <= lvl7en8x + .5 * sid + 2 and y >= lvl7en8y + 5 and y <= lvl7en8y + sid + 25:
                hp -= 50
            if x >= lvl7en8x + .5 * sid - 2 - sid and x <= lvl7en8x + .5 * sid + 2 and y >= lvl7en8y - 25 - sid and y <= lvl7en8y - 5:
                hp -= 50
        if lvl7en9alive:
            if x >= lvl7en9x + 5 and x <= lvl7en9x + sid + 25 and y >= lvl7en9y + .5 * sid - 2 - sid and y <= lvl7en9y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en9x - 25 - sid and x <= lvl7en9x - 5 and y >= lvl7en9y + .5 * sid - 2 - sid and y <= lvl7en9y + .5 * sid + 2:
                hp -= 50
            if x >= lvl7en9x + .5 * sid - 2 - sid and x <= lvl7en9x + .5 * sid + 2 and y >= lvl7en9y + 5 and y <= lvl7en9y + sid + 25:
                hp -= 50
            if x >= lvl7en9x + .5 * sid - 2 - sid and x <= lvl7en9x + .5 * sid + 2 and y >= lvl7en9y - 25 - sid and y <= lvl7en9y - 5:
                hp -= 50

        if not lvl7en1alive and not lvl7en2alive and not lvl7en3alive and not lvl7en4alive and not lvl7en5alive and not lvl7en6alive and not lvl7en7alive and not lvl7en8alive and not lvl7en9alive:
            setLevels()
            lvl = 8
            x = 20
            y = 560
            success()

    if lvl == 8 and not paused:
        if lvl8en1alive:
            if lvl8en1hidden:
                pygame.draw.rect(screen, SHADOW, [lvl8en1x, lvl8en1y, sid, sid])
                lvl8en1x += lvl8en1xdelta
                lvl8en1y += lvl8en1ydelta
                if lvl8en1x > 800 or lvl8en1x < 0:
                    lvl8en1xdelta = lvl8en1xdelta * -1
                if lvl8en1y > 600 or lvl8en1y < 30:
                    lvl8en1ydelta = lvl8en1ydelta * -1
                if x >= lvl8en1x - sid - 40 and x <= lvl8en1x + sid + 40 and y >= lvl8en1y - sid - 40 and y <= lvl8en1y + sid + 40:
                    lvl8en1hidden = False
                    surprise()
            if not lvl8en1hidden:
                pygame.draw.rect(screen, RED, [lvl8en1x, lvl8en1y, sid, sid])
                if x >= lvl8en1x:
                    lvl8en1xdelta = 2
                if x <= lvl8en1x:
                    lvl8en1xdelta = -2
                if y >= lvl8en1y:
                    lvl8en1ydelta = 2
                if y <= lvl8en1y:
                    lvl8en1ydelta = -2
                lvl8en1x += lvl8en1xdelta
                lvl8en1y += lvl8en1ydelta
                if x >= lvl8en1x + 5 and x <= lvl8en1x + sid + 25 and y >= lvl8en1y + .5 * sid - 2 - sid and y <= lvl8en1y + .5 * sid + 2:
                    hp -= 50
                if x >= lvl8en1x - 25 - sid and x <= lvl8en1x - 5 and y >= lvl8en1y + .5 * sid - 2 - sid and y <= lvl8en1y + .5 * sid + 2:
                    hp -= 50
                if x >= lvl8en1x + .5 * sid - 2 - sid and x <= lvl8en1x + .5 * sid + 2 and y >= lvl8en1y + 5 and y <= lvl8en1y + sid + 25:
                    hp -= 50
                if x >= lvl8en1x + .5 * sid - 2 - sid and x <= lvl8en1x + .5 * sid + 2 and y >= lvl8en1y - 25 - sid and y <= lvl8en1y - 5:
                    hp -= 50
                if x >= lvl8en1x + .5 * sid - 2 - sid and x <= lvl8en1x + .5 * sid + 2 and y >= lvl8en1y + .5 * sid - 2 - sid and y <= lvl8en1y + .5 * sid + 2:
                    hp -= 50
                pygame.draw.rect(screen, WHITE, [lvl8en1x - 25, lvl8en1y + .5 * sid - 2, 20, 4])
                pygame.draw.rect(screen, WHITE, [lvl8en1x + 25, lvl8en1y + .5 * sid - 2, 20, 4])
                pygame.draw.rect(screen, WHITE, [lvl8en1x + .5 * sid - 2, lvl8en1y - 25, 4, 20])
                pygame.draw.rect(screen, WHITE, [lvl8en1x + .5 * sid - 2, lvl8en1y + 25, 4, 20])
                if d and lvl8en1x > x + 25 - sid and lvl8en1x < x + 35 and lvl8en1y > y + .5 * sid - 2 - sid and lvl8en1y < y + .5 * sid + 2:
                    lvl8en1alive = False
                    stab()
                elif s and lvl8en1x > x + .5 * sid - 2 - sid and lvl8en1x < x + .5 * sid + 2 and lvl8en1y > y + 25 - sid and lvl8en1y < y + 35:
                    lvl8en1alive = False
                    stab()
                elif a and lvl8en1x > x - 15 - sid and lvl8en1x < x - 5 and lvl8en1y > y + .5 * sid - 2 - sid and lvl8en1y < y + .5 * sid + 2:
                    lvl8en1alive = False
                    stab()
                elif w and lvl8en1x > x + .5 * sid - 2 - sid and lvl8en1x < x + .5 * sid + 2 and lvl8en1y > y - 15 - sid and lvl8en1y < y - 5:
                    lvl8en1alive = False
                    stab()
        screen.blit(text8, (10, 50))
        if not lvl8en1alive:
            setLevels()
            lvl = 9
            x = 20
            y = 560
            success()

    if lvl == 9 and not paused:

        if lvl9en1alive:
            if lvl9en1hidden:
                pygame.draw.rect(screen, SHADOW, [lvl9en1x, lvl9en1y, sid, sid])
                lvl9en1x += lvl9en1xdelta
                lvl9en1y += lvl9en1ydelta
                if lvl9en1x > 800 or lvl9en1x < 0:
                    lvl9en1xdelta = lvl9en1xdelta * -1
                if lvl9en1y > 600 or lvl9en1y < 30:
                    lvl9en1ydelta = lvl9en1ydelta * -1
                if x >= lvl9en1x - sid - 40 and x <= lvl9en1x + sid + 40 and y >= lvl9en1y - sid - 40 and y <= lvl9en1y + sid + 40:
                    lvl9en1hidden = False
                    surprise()
            if not lvl9en1hidden:
                pygame.draw.rect(screen, RED, [lvl9en1x, lvl9en1y, sid, sid])
                if x >= lvl9en1x:
                    lvl9en1xdelta = 2
                if x <= lvl9en1x:
                    lvl9en1xdelta = -2
                if y >= lvl9en1y:
                    lvl9en1ydelta = 2
                if y <= lvl9en1y:
                    lvl9en1ydelta = -2
                lvl9en1x += lvl9en1xdelta
                lvl9en1y += lvl9en1ydelta
                if x >= lvl9en1x + 5 and x <= lvl9en1x + sid + 25 and y >= lvl9en1y + .5 * sid - 2 - sid and y <= lvl9en1y + .5 * sid + 2:
                    hp -= 50
                if x >= lvl9en1x - 25 - sid and x <= lvl9en1x - 5 and y >= lvl9en1y + .5 * sid - 2 - sid and y <= lvl9en1y + .5 * sid + 2:
                    hp -= 50
                if x >= lvl9en1x + .5 * sid - 2 - sid and x <= lvl9en1x + .5 * sid + 2 and y >= lvl9en1y + 5 and y <= lvl9en1y + sid + 25:
                    hp -= 50
                if x >= lvl9en1x + .5 * sid - 2 - sid and x <= lvl9en1x + .5 * sid + 2 and y >= lvl9en1y - 25 - sid and y <= lvl9en1y - 5:
                    hp -= 50
                if x >= lvl9en1x + .5 * sid - 2 - sid and x <= lvl9en1x + .5 * sid + 2 and y >= lvl9en1y + .5 * sid - 2 - sid and y <= lvl9en1y + .5 * sid + 2:
                    hp -= 50
                pygame.draw.rect(screen, WHITE, [lvl9en1x - 25, lvl9en1y + .5 * sid - 2, 20, 4])
                pygame.draw.rect(screen, WHITE, [lvl9en1x + 25, lvl9en1y + .5 * sid - 2, 20, 4])
                pygame.draw.rect(screen, WHITE, [lvl9en1x + .5 * sid - 2, lvl9en1y - 25, 4, 20])
                pygame.draw.rect(screen, WHITE, [lvl9en1x + .5 * sid - 2, lvl9en1y + 25, 4, 20])
                if d and lvl9en1x > x + 25 - sid and lvl9en1x < x + 35 and lvl9en1y > y + .5 * sid - 2 - sid and lvl9en1y < y + .5 * sid + 2 and lvl9en1alive:
                    lvl9en1alive = False
                    stab()
                elif s and lvl9en1x > x + .5 * sid - 2 - sid and lvl9en1x < x + .5 * sid + 2 and lvl9en1y > y + 25 - sid and lvl9en1y < y + 35 and lvl9en1alive:
                    lvl9en1alive = False
                    stab()
                elif a and lvl9en1x > x - 15 - sid and lvl9en1x < x - 5 and lvl9en1y > y + .5 * sid - 2 - sid and lvl9en1y < y + .5 * sid + 2 and lvl9en1alive:
                    lvl9en1alive = False
                    stab()
                elif w and lvl9en1x > x + .5 * sid - 2 - sid and lvl9en1x < x + .5 * sid + 2 and lvl9en1y > y - 15 - sid and lvl9en1y < y - 5 and lvl9en1alive:
                    lvl9en1alive = False
                    stab()

        if lvl9en2alive:

            if lvl9en2hidden:
                pygame.draw.rect(screen, SHADOW, [lvl9en2x, lvl9en2y, sid, sid])
                lvl9en2x += lvl9en2xdelta
                lvl9en2y += lvl9en2ydelta
                if lvl9en2x > 800 or lvl9en2x < 0:
                    lvl9en2xdelta = lvl9en2xdelta * -1
                if lvl9en2y > 600 or lvl9en2y < 30:
                    lvl9en2ydelta = lvl9en2ydelta * -1
                if x >= lvl9en2x - sid - 40 and x <= lvl9en2x + sid + 40 and y >= lvl9en2y - sid - 40 and y <= lvl9en2y + sid + 40:
                    lvl9en2hidden = False
                    surprise()
            if not lvl9en2hidden:
                pygame.draw.rect(screen, RED, [lvl9en2x, lvl9en2y, sid, sid])
                if x >= lvl9en2x:
                    lvl9en2xdelta = 2
                if x <= lvl9en2x:
                    lvl9en2xdelta = -2
                if y >= lvl9en2y:
                    lvl9en2ydelta = 2
                if y <= lvl9en2y:
                    lvl9en2ydelta = -2
                lvl9en2x += lvl9en2xdelta
                lvl9en2y += lvl9en2ydelta
                if x >= lvl9en2x + 5 and x <= lvl9en2x + sid + 25 and y >= lvl9en2y + .5 * sid - 2 - sid and y <= lvl9en2y + .5 * sid + 2:
                    hp -= 50
                if x >= lvl9en2x - 25 - sid and x <= lvl9en2x - 5 and y >= lvl9en2y + .5 * sid - 2 - sid and y <= lvl9en2y + .5 * sid + 2:
                    hp -= 50
                if x >= lvl9en2x + .5 * sid - 2 - sid and x <= lvl9en2x + .5 * sid + 2 and y >= lvl9en2y + 5 and y <= lvl9en2y + sid + 25:
                    hp -= 50
                if x >= lvl9en2x + .5 * sid - 2 - sid and x <= lvl9en2x + .5 * sid + 2 and y >= lvl9en2y - 25 - sid and y <= lvl9en2y - 5:
                    hp -= 50
                if x >= lvl9en2x + .5 * sid - 2 - sid and x <= lvl9en2x + .5 * sid + 2 and y >= lvl9en2y + .5 * sid - 2 - sid and y <= lvl9en2y + .5 * sid + 2:
                    hp -= 50
                pygame.draw.rect(screen, WHITE, [lvl9en2x - 25, lvl9en2y + .5 * sid - 2, 20, 4])
                pygame.draw.rect(screen, WHITE, [lvl9en2x + 25, lvl9en2y + .5 * sid - 2, 20, 4])
                pygame.draw.rect(screen, WHITE, [lvl9en2x + .5 * sid - 2, lvl9en2y - 25, 4, 20])
                pygame.draw.rect(screen, WHITE, [lvl9en2x + .5 * sid - 2, lvl9en2y + 25, 4, 20])
                if d and lvl9en2x > x + 25 - sid and lvl9en2x < x + 35 and lvl9en2y > y + .5 * sid - 2 - sid and lvl9en2y < y + .5 * sid + 2 and lvl9en2alive:
                    lvl9en2alive = False
                    stab()
                elif s and lvl9en2x > x + .5 * sid - 2 - sid and lvl9en2x < x + .5 * sid + 2 and lvl9en2y > y + 25 - sid and lvl9en2y < y + 35 and lvl9en2alive:
                    lvl9en2alive = False
                    stab()
                elif a and lvl9en2x > x - 15 - sid and lvl9en2x < x - 5 and lvl9en2y > y + .5 * sid - 2 - sid and lvl9en2y < y + .5 * sid + 2 and lvl9en2alive:
                    lvl9en2alive = False
                    stab()
                elif w and lvl9en2x > x + .5 * sid - 2 - sid and lvl9en2x < x + .5 * sid + 2 and lvl9en2y > y - 15 - sid and lvl9en2y < y - 5 and lvl9en2alive:
                    lvl9en2alive = False
                    stab()

        if lvl9en3alive:
            if lvl9en3hidden:
                pygame.draw.rect(screen, SHADOW, [lvl9en3x, lvl9en3y, sid, sid])
                lvl9en3x += lvl9en3xdelta
                lvl9en3y += lvl9en3ydelta
                if lvl9en3x > 800 or lvl9en3x < 0:
                    lvl9en3xdelta = lvl9en3xdelta * -1
                if lvl9en3y > 600 or lvl9en3y < 30:
                    lvl9en3ydelta = lvl9en3ydelta * -1
                if x >= lvl9en3x - sid - 40 and x <= lvl9en3x + sid + 40 and y >= lvl9en3y - sid - 40 and y <= lvl9en3y + sid + 40:
                    lvl9en3hidden = False
                    surprise()
            if not lvl9en3hidden:
                pygame.draw.rect(screen, RED, [lvl9en3x, lvl9en3y, sid, sid])
                if x >= lvl9en3x:
                    lvl9en3xdelta = 2
                if x <= lvl9en3x:
                    lvl9en3xdelta = -2
                if y >= lvl9en3y:
                    lvl9en3ydelta = 2
                if y <= lvl9en3y:
                    lvl9en3ydelta = -2
                lvl9en3x += lvl9en3xdelta
                lvl9en3y += lvl9en3ydelta
                if x >= lvl9en3x + 5 and x <= lvl9en3x + sid + 25 and y >= lvl9en3y + .5 * sid - 2 - sid and y <= lvl9en3y + .5 * sid + 2:
                    hp -= 50
                if x >= lvl9en3x - 25 - sid and x <= lvl9en3x - 5 and y >= lvl9en3y + .5 * sid - 2 - sid and y <= lvl9en3y + .5 * sid + 2:
                    hp -= 50
                if x >= lvl9en3x + .5 * sid - 2 - sid and x <= lvl9en3x + .5 * sid + 2 and y >= lvl9en3y + 5 and y <= lvl9en3y + sid + 25:
                    hp -= 50
                if x >= lvl9en3x + .5 * sid - 2 - sid and x <= lvl9en3x + .5 * sid + 2 and y >= lvl9en3y - 25 - sid and y <= lvl9en3y - 5:
                    hp -= 50
                if x >= lvl9en3x + .5 * sid - 2 - sid and x <= lvl9en3x + .5 * sid + 2 and y >= lvl9en3y + .5 * sid - 2 - sid and y <= lvl9en3y + .5 * sid + 2:
                    hp -= 50
                pygame.draw.rect(screen, WHITE, [lvl9en3x - 25, lvl9en3y + .5 * sid - 2, 20, 4])
                pygame.draw.rect(screen, WHITE, [lvl9en3x + 25, lvl9en3y + .5 * sid - 2, 20, 4])
                pygame.draw.rect(screen, WHITE, [lvl9en3x + .5 * sid - 2, lvl9en3y - 25, 4, 20])
                pygame.draw.rect(screen, WHITE, [lvl9en3x + .5 * sid - 2, lvl9en3y + 25, 4, 20])
                if d and lvl9en3x > x + 25 - sid and lvl9en3x < x + 35 and lvl9en3y > y + .5 * sid - 2 - sid and lvl9en3y < y + .5 * sid + 2 and lvl9en3alive:
                    lvl9en3alive = False
                    stab()
                elif s and lvl9en3x > x + .5 * sid - 2 - sid and lvl9en3x < x + .5 * sid + 2 and lvl9en3y > y + 25 - sid and lvl9en3y < y + 35 and lvl9en3alive:
                    lvl9en3alive = False
                    stab()
                elif a and lvl9en3x > x - 15 - sid and lvl9en3x < x - 5 and lvl9en3y > y + .5 * sid - 2 - sid and lvl9en3y < y + .5 * sid + 2 and lvl9en3alive:
                    lvl9en3alive = False
                    stab()
                elif w and lvl9en3x > x + .5 * sid - 2 - sid and lvl9en3x < x + .5 * sid + 2 and lvl9en3y > y - 15 - sid and lvl9en3y < y - 5 and lvl9en3alive:
                    lvl9en3alive = False
                    stab()
        screen.blit(text9, (10, 50))

        if not lvl9en1alive and not lvl9en2alive and not lvl9en3alive:
            setLevels()
            lvl = 10
            x = 20
            y = 560
            success()

    if lvl == 10 and not paused:
        if lvl10en1alive:
            if lvl10en1hidden:
                pygame.draw.rect(screen, SHADOW, [lvl10en1x, lvl10en1y, sid, sid])
                lvl10en1x += lvl10en1xdelta
                lvl10en1y += lvl10en1ydelta
                if lvl10en1x > lvl10en3x - sid or lvl10en1x < lvl10en2x + 20:
                    lvl10en1xdelta = lvl10en1xdelta * -1
                if lvl10en1y > 600 or lvl10en1y < 30:
                    lvl10en1ydelta = lvl10en1ydelta * -1
                if x >= lvl10en1x - sid - 40 and x <= lvl10en1x + sid + 40 and y >= lvl10en1y - sid - 40 and y <= lvl10en1y + sid + 40:
                    lvl10en1hidden = False
                    surprise()
            if not lvl10en1hidden:
                pygame.draw.rect(screen, RED, [lvl10en1x, lvl10en1y, sid, sid])
                if x >= lvl10en1x:
                    lvl10en1xdelta = 2
                if x <= lvl10en1x:
                    lvl10en1xdelta = -2
                if y >= lvl10en1y:
                    lvl10en1ydelta = 2
                if y <= lvl10en1y:
                    lvl10en1ydelta = -2
                lvl10en1x += lvl10en1xdelta
                lvl10en1y += lvl10en1ydelta
                if x >= lvl10en1x + 5 and x <= lvl10en1x + sid + 25 and y >= lvl10en1y + .5 * sid - 2 - sid and y <= lvl10en1y + .5 * sid + 2:
                    hp -= 50
                if x >= lvl10en1x - 25 - sid and x <= lvl10en1x - 5 and y >= lvl10en1y + .5 * sid - 2 - sid and y <= lvl10en1y + .5 * sid + 2:
                    hp -= 50
                if x >= lvl10en1x + .5 * sid - 2 - sid and x <= lvl10en1x + .5 * sid + 2 and y >= lvl10en1y + 5 and y <= lvl10en1y + sid + 25:
                    hp -= 50
                if x >= lvl10en1x + .5 * sid - 2 - sid and x <= lvl10en1x + .5 * sid + 2 and y >= lvl10en1y - 25 - sid and y <= lvl10en1y - 5:
                    hp -= 50
                if x >= lvl10en1x + .5 * sid - 2 - sid and x <= lvl10en1x + .5 * sid + 2 and y >= lvl1en1y + .5 * sid - 2 - sid and y <= lvl10en1y + .5 * sid + 2:
                    hp -= 50
                pygame.draw.rect(screen, WHITE, [lvl10en1x - 25, lvl10en1y + .5 * sid - 2, 20, 4])
                pygame.draw.rect(screen, WHITE, [lvl10en1x + 25, lvl10en1y + .5 * sid - 2, 20, 4])
                pygame.draw.rect(screen, WHITE, [lvl10en1x + .5 * sid - 2, lvl10en1y - 25, 4, 20])
                pygame.draw.rect(screen, WHITE, [lvl10en1x + .5 * sid - 2, lvl10en1y + 25, 4, 20])
                if d and lvl10en1x > x + 25 - sid and lvl10en1x < x + 35 and lvl10en1y > y + .5 * sid - 2 - sid and lvl10en1y < y + .5 * sid + 2 and lvl10en1alive:
                    lvl10en1alive = False
                    stab()
                elif s and lvl10en1x > x + .5 * sid - 2 - sid and lvl10en1x < x + .5 * sid + 2 and lvl10en1y > y + 25 - sid and lvl10en1y < y + 35 and lvl10en1alive:
                    lvl10en1alive = False
                    stab()
                elif a and lvl10en1x > x - 15 - sid and lvl10en1x < x - 5 and lvl10en1y > y + .5 * sid - 2 - sid and lvl10en1y < y + .5 * sid + 2 and lvl10en1alive:
                    lvl10en1alive = False
                    stab()
                elif w and lvl10en1x > x + .5 * sid - 2 - sid and lvl10en1x < x + .5 * sid + 2 and lvl10en1y > y - 15 - sid and lvl10en1y < y - 5 and lvl10en1alive:
                    lvl10en1alive = False
                    stab()

        pygame.draw.rect(screen, WHITE, [lvl10en2x, lvl10en2y, 20, 579.9999])
        pygame.draw.rect(screen, WHITE, [lvl10en3x, lvl10en3y, 20, 580])
        screen.blit(text10, (10, 50))

        if x >= lvl10en2x - sid and x <= lvl10en2x + 20 and y <= 579.9999:
            hp -= 50
        if x >= lvl10en3x - sid and x <= lvl10en3x + 20 and y >= 20.00001:
            hp -= 50

        if lvl10en4alive:
            if x >= lvl10en4x + .5 * sid - 2 - sid and x <= lvl10en4x + sid + 2 and y >= lvl10en4y + 5 and y <= lvl10en4y + 35:
                pygame.draw.rect(screen, WHITE, [lvl10en4x + .5 * sid - 2, lvl10en4y + 25, 4, 10])
                hp -= 50
            pygame.draw.rect(screen, RED, [lvl10en4x, lvl10en4y, sid, sid])
        if d and lvl10en4x > x + 25 - sid and lvl10en4x < x + 35 and lvl10en4y > y + .5 * sid - 2 - sid and lvl10en4y < y + .5 * sid + 2 and lvl10en4alive:
            lvl10en4alive = False
            stab()
        elif s and lvl10en4x > x + .5 * sid - 2 - sid and lvl10en4x < x + .5 * sid + 2 and lvl10en4y > y + 25 - sid and lvl10en4y < y + 35 and lvl10en4alive:
            lvl10en4alive = False
            stab()
        elif a and lvl10en4x > x - 15 - sid and lvl10en4x < x - 5 and lvl10en4y > y + .5 * sid - 2 - sid and lvl10en4y < y + .5 * sid + 2 and lvl10en4alive:
            lvl10en4alive = False
            stab()
        elif w and lvl10en4x > x + .5 * sid - 2 - sid and lvl10en4x < x + .5 * sid + 2 and lvl10en4y > y - 15 - sid and lvl10en4y < y - 5 and lvl10en4alive:
            lvl10en4alive = False
            stab()

        if lvl10en5alive:
            pygame.draw.rect(screen, RED, [lvl10en5x, lvl10en5y, sid, sid])
        if d and lvl10en5x > x + 25 - sid and lvl10en5x < x + 35 and lvl10en5y > y + .5 * sid - 2 - sid and lvl10en5y < y + .5 * sid + 2 and lvl10en5alive:
            lvl10en5alive = False
            stab()
        elif s and lvl10en5x > x + .5 * sid - 2 - sid and lvl10en5x < x + .5 * sid + 2 and lvl10en5y > y + 25 - sid and lvl10en5y < y + 35 and lvl10en5alive:
            lvl10en5alive = False
            stab()
        elif a and lvl10en5x > x - 15 - sid and lvl10en5x < x - 5 and lvl10en5y > y + .5 * sid - 2 - sid and lvl10en5y < y + .5 * sid + 2 and lvl10en5alive:
            lvl10en5alive = False
            stab()
        elif w and lvl10en5x > x + .5 * sid - 2 - sid and lvl10en5x < x + .5 * sid + 2 and lvl10en5y > y - 15 - sid and lvl10en5y < y - 5 and lvl10en5alive:
            lvl10en5alive = False
            stab()

        if not lvl10en1alive and not lvl10en4alive and not lvl10en5alive:
            setLevels()
            lvl = 11
            x = 20
            y = 560
            success()

    if lvl == 11 and not paused:
        pygame.draw.rect(screen, WHITE, [300, 0, 80, 600])
        pygame.draw.rect(screen, RED, [750, 290, sid, sid])
        if x > 280:
            hp -= 50
        if lvl11bomb1alive:
            drawBomb(50, 50)
            screen.blit(text11a, (10, 150))
        else:
            screen.blit(text11b, (10, 150))
        if x > 30 and x < 70 and y > 30 and y < 70:
            if lvl11bomb1alive:
                bombs += 1
                pickUpBomb()
            lvl11bomb1alive = False
        if explode:
            if mx > 750 and mx < 770 and my > 290 and my < 310:
                setLevels()
                lvl = 12
                x = 20
                y = 560
            explode = False

    if lvl == 12 and not paused:
        if not lvl12firstshot:
            enemyShot()
            lvl12firstshot = True
        screen.blit(text12, (520, 550))
        if lvl12en1alive:
            pygame.draw.rect(screen, WHITE, [lvl12bullet1x, lvl12bullet1y, 10, 10])
            pygame.draw.rect(screen, RED, [lvl12en1x, lvl12en1y, sid, sid])
        if lvl12en2alive:
            pygame.draw.rect(screen, WHITE, [lvl12bullet2x, lvl12bullet2y, 10, 10])
            pygame.draw.rect(screen, RED, [lvl12en2x, lvl12en2y, sid, sid])
        if lvl12en3alive:
            pygame.draw.rect(screen, RED, [0, 0, sid, sid])
        if lvl12bullet1x == 745 and lvl12bullet1y == 15:
            lvl12bullet1xdelta = (x + 5 - 750) / 60
            lvl12bullet1ydelta = (y + 5 - 20) / 60
        if lvl12en1alive:
            lvl12bullet1x += lvl12bullet1xdelta
            lvl12bullet1y += lvl12bullet1ydelta
        if lvl12bullet2x == 775 and lvl12bullet2y == 45:
            lvl12bullet2xdelta = (x + 5 - 780) / 60
            lvl12bullet2ydelta = (y + 5 - 50) / 60
        if lvl12en2alive:
            lvl12bullet2x += lvl12bullet2xdelta
            lvl12bullet2y += lvl12bullet2ydelta
        if lvl12bullet1x < -200 or lvl12bullet1x > 1000 or lvl12bullet1y < -200 or lvl12bullet1y > 800:
            lvl12bullet1x = 745
            lvl12bullet1y = 15
            enemyShot()
        if lvl12bullet2x < -200 or lvl12bullet2x > 1000 or lvl12bullet2y < -200 or lvl12bullet2y > 800:
            lvl12bullet2x = 775
            lvl12bullet2y = 45
            enemyShot()
        if lvl12bomb1alive:
            drawBomb(lvl12bomb1x, lvl12bomb1y)
        if x > 750 and x < 790 and y > -10 and y < 30:
            if lvl12bomb1alive:
                bombs += 1
                pickUpBomb()
            lvl12bomb1alive = False

        if d and lvl12en1x > x + 25 - sid and lvl12en1x < x + 35 and lvl12en1y > y + .5 * sid - 2 - sid and lvl12en1y < y + .5 * sid + 2 and lvl12en1alive:
            lvl12en1alive = False
            stab()
        elif s and lvl12en1x > x + .5 * sid - 2 - sid and lvl12en1x < x + .5 * sid + 2 and lvl12en1y > y + 25 - sid and lvl12en1y < y + 35 and lvl12en1alive:
            lvl12en1alive = False
            stab()
        elif a and lvl12en1x > x - 15 - sid and lvl12en1x < x - 5 and lvl12en1y > y + .5 * sid - 2 - sid and lvl12en1y < y + .5 * sid + 2 and lvl12en1alive:
            lvl12en1alive = False
            stab()
        elif w and lvl12en1x > x + .5 * sid - 2 - sid and lvl12en1x < x + .5 * sid + 2 and lvl12en1y > y - 15 - sid and lvl12en1y < y - 5 and lvl12en1alive:
            lvl12en1alive = False
            stab()

        if d and lvl12en2x > x + 25 - sid and lvl12en2x < x + 35 and lvl12en2y > y + .5 * sid - 2 - sid and lvl12en2y < y + .5 * sid + 2 and lvl12en2alive:
            lvl12en2alive = False
            stab()
        elif s and lvl12en2x > x + .5 * sid - 2 - sid and lvl12en2x < x + .5 * sid + 2 and lvl12en2y > y + 25 - sid and lvl12en2y < y + 35 and lvl12en2alive:
            lvl12en2alive = False
            stab()
        elif a and lvl12en2x > x - 15 - sid and lvl12en2x < x - 5 and lvl12en2y > y + .5 * sid - 2 - sid and lvl12en2y < y + .5 * sid + 2 and lvl12en2alive:
            lvl12en1alive = False
            stab()
        elif w and lvl12en2x > x + .5 * sid - 2 - sid and lvl12en2x < x + .5 * sid + 2 and lvl12en2y > y - 15 - sid and lvl12en2y < y - 5 and lvl12en2alive:
            lvl12en2alive = False
            stab()

        if lvl12en1alive:
            if x >= lvl12bullet1x - sid and x <= lvl12bullet1x + 10 and y >= lvl12bullet1y - sid and y <= lvl12bullet1y + 10:
                hp -= 200
        if lvl12en2alive:
            if x >= lvl12bullet2x - sid and x <= lvl12bullet2x + 10 and y >= lvl12bullet2y - sid and y <= lvl12bullet2y + 10:
                hp -= 200

        pygame.draw.rect(screen, WHITE, [20, 0, 80, 100])
        pygame.draw.rect(screen, WHITE, [0, 20, 100, 80])

        if x < 100 and y < 100:
            hp -= 50

        if explode:
            if mx > 740 and mx < 760 and my > 10 and my < 30:
                lvl12en1alive = False
            if mx > 770 and mx < 790 and my > 40 and my < 60:
                lvl12en2alive = False
            if mx > 0 and mx < 20 and my > 0 and my < 20:
                lvl12en3alive = False
            explode = False
        if not lvl12en1alive and not lvl12en2alive and not lvl12en3alive:
            setLevels()
            lvl = 13
            x = 20
            y = 560
            success()

    if lvl == 13 and not paused:

        if lvl13lifealive:
            drawLife(395, 295)
            screen.blit(text13a, (10, 50))
            if x > 375 and x < 405 and y > 275 and y < 305:
                lvl13lifealive = False
                lives += 1
                getLife()
        else:
            screen.blit(text13b, (10, 50))
            if lvl13bomb1alive:
                drawBomb(20, 290)
                if x > 0 and x < 40 and y > 270 and y < 310:
                    bombs += 1
                    pickUpBomb()
                    lvl13bomb1alive = False
            if lvl13en1alive:
                pygame.draw.rect(screen, RED, [lvl13en1x, lvl13en1y, sid, sid])
            lvl13bullet1x -= 4.5
            pygame.draw.rect(screen, WHITE, [lvl13bullet1x, 0, 30, 600])
            if x > lvl13bullet1x - 20:
                hp = 0

        if explode:
            if mx > 750 and mx < 770 and my > 290 and my < 310:
                lvl13en1alive = False
            explode = False

        if not lvl13en1alive:
            setLevels()
            lvl = 14
            x = 20
            y = 560
            success()

    if lvl == 14 and not paused:
        screen.blit(text14, (10, 50))

        if lvl14lifealive:
            drawLife(785, 295)
            if x > 765 and x < 795 and y > 275 and y < 305:
                lvl14lifealive = False
                lives += 1

        if lvl14en1alive:
            pygame.draw.rect(screen, RED, [lvl14en1x, lvl14en1y, sid, sid])
            lvl14en1x += lvl14en1xdelta
            lvl14en1y += lvl14en1ydelta
            if lvl14en1x > 780 or lvl14en1x < 500:
                lvl14en1xdelta = lvl14en1xdelta * -1
            if lvl14en1y > 580 or lvl14en1y < 0:
                lvl14en1ydelta = lvl14en1ydelta * -1
            if d and lvl14en1x > x + 25 - sid and lvl14en1x < x + 35 and lvl14en1y > y + .5 * sid - 2 - sid and lvl14en1y < y + .5 * sid + 2:
                lvl14en1alive = False
                stab()
            elif s and lvl14en1x > x + .5 * sid - 2 - sid and lvl14en1x < x + .5 * sid + 2 and lvl14en1y > y + 25 - sid and lvl14en1y < y + 35:
                lvl14en1alive = False
                stab()
            elif a and lvl14en1x > x - 15 - sid and lvl14en1x < x - 5 and lvl14en1y > y + .5 * sid - 2 - sid and lvl14en1y < y + .5 * sid + 2:
                lvl14en1alive = False
                stab()
            elif w and lvl14en1x > x + .5 * sid - 2 - sid and lvl14en1x < x + .5 * sid + 2 and lvl14en1y > y - 15 - sid and lvl14en1y < y - 5:
                lvl14en1alive = False
                stab()

        pygame.draw.rect(screen, WHITE, [780, lvl14blade1y, sid, sid])
        pygame.draw.rect(screen, WHITE, [750, lvl14blade2y, sid, sid])
        pygame.draw.rect(screen, WHITE, [720, lvl14blade3y, sid, sid])
        pygame.draw.rect(screen, WHITE, [690, lvl14blade4y, sid, sid])
        pygame.draw.rect(screen, WHITE, [660, lvl14blade5y, sid, sid])
        pygame.draw.rect(screen, WHITE, [630, lvl14blade6y, sid, sid])
        pygame.draw.rect(screen, WHITE, [600, lvl14blade7y, sid, sid])
        pygame.draw.rect(screen, WHITE, [570, lvl14blade8y, sid, sid])
        pygame.draw.rect(screen, WHITE, [540, lvl14blade9y, sid, sid])
        pygame.draw.rect(screen, WHITE, [510, lvl14blade10y, sid, sid])
        pygame.draw.rect(screen, WHITE, [480, lvl14blade11y, sid, sid])
        pygame.draw.rect(screen, WHITE, [450, lvl14blade12y, sid, sid])
        pygame.draw.rect(screen, WHITE, [420, lvl14blade13y, sid, sid])
        pygame.draw.rect(screen, WHITE, [390, lvl14blade14y, sid, sid])
        lvl14blade14y += lvl14blade14ydelta
        lvl14blade13y += lvl14blade13ydelta
        lvl14blade12y += lvl14blade12ydelta
        lvl14blade11y += lvl14blade11ydelta
        lvl14blade10y += lvl14blade10ydelta
        lvl14blade9y += lvl14blade9ydelta
        lvl14blade8y += lvl14blade8ydelta
        lvl14blade7y += lvl14blade7ydelta
        lvl14blade6y += lvl14blade6ydelta
        lvl14blade5y += lvl14blade5ydelta
        lvl14blade4y += lvl14blade4ydelta
        lvl14blade3y += lvl14blade3ydelta
        lvl14blade2y += lvl14blade2ydelta
        lvl14blade1y += lvl14blade1ydelta
        if lvl14blade1y > 580 or lvl14blade1y < 0:
            lvl14blade1ydelta = lvl14blade1ydelta * -1
            lvl14blade2ydelta = lvl14blade2ydelta * -1
            lvl14blade3ydelta = lvl14blade3ydelta * -1
            lvl14blade4ydelta = lvl14blade4ydelta * -1
            lvl14blade5ydelta = lvl14blade5ydelta * -1
            lvl14blade6ydelta = lvl14blade6ydelta * -1
            lvl14blade7ydelta = lvl14blade7ydelta * -1
            lvl14blade8ydelta = lvl14blade8ydelta * -1
            lvl14blade9ydelta = lvl14blade9ydelta * -1
            lvl14blade10ydelta = lvl14blade10ydelta * -1
            lvl14blade11ydelta = lvl14blade11ydelta * -1
            lvl14blade12ydelta = lvl14blade12ydelta * -1
            lvl14blade13ydelta = lvl14blade13ydelta * -1
            lvl14blade14ydelta = lvl14blade14ydelta * -1
        if x > 760 and x < 800 and y > lvl14blade1y - sid and y < lvl14blade1y + sid:
            hp -= 150
        if x > 730 and x < 770 and y > lvl14blade2y - sid and y < lvl14blade2y + sid:
            hp -= 150
        if x > 700 and x < 740 and y > lvl14blade3y - sid and y < lvl14blade3y + sid:
            hp -= 150
        if x > 670 and x < 710 and y > lvl14blade4y - sid and y < lvl14blade4y + sid:
            hp -= 150
        if x > 640 and x < 680 and y > lvl14blade5y - sid and y < lvl14blade5y + sid:
            hp -= 150
        if x > 610 and x < 650 and y > lvl14blade6y - sid and y < lvl14blade6y + sid:
            hp -= 150
        if x > 580 and x < 620 and y > lvl14blade7y - sid and y < lvl14blade7y + sid:
            hp -= 150
        if x > 550 and x < 590 and y > lvl14blade8y - sid and y < lvl14blade8y + sid:
            hp -= 150
        if x > 520 and x < 560 and y > lvl14blade9y - sid and y < lvl14blade9y + sid:
            hp -= 150
        if x > 490 and x < 530 and y > lvl14blade10y - sid and y < lvl14blade10y + sid:
            hp -= 150
        if x > 460 and x < 500 and y > lvl14blade11y - sid and y < lvl14blade11y + sid:
            hp -= 150
        if x > 430 and x < 470 and y > lvl14blade12y - sid and y < lvl14blade12y + sid:
            hp -= 150
        if x > 400 and x < 440 and y > lvl14blade13y - sid and y < lvl14blade13y + sid:
            hp -= 150
        if x > 370 and x < 410 and y > lvl14blade14y - sid and y < lvl14blade14y + sid:
            hp -= 150

        if not lvl14en1alive:
            setLevels()
            x = 20
            y = 560
            lvl = 15
            success()

    if lvl == 20 and not paused:
        if not boss1aalive:
            lvl20co1.update()
            lvl20co1alive = lvl20co1.returnAlive()
            lvl20co2.update()
            lvl20co2alive = lvl20co2.returnAlive()
            lvl20co3.update()
            lvl20co3alive = lvl20co3.returnAlive()
            lvl20co4.update()
            lvl20co4alive = lvl20co4.returnAlive()
            lvl20co5.update()
            lvl20co5alive = lvl20co5.returnAlive()
        boss1a.update()
        boss1aalive = boss1a.returnAlive()
        if not boss1aalive:
            screen.blit(text20b, (10, 50))
            if not initialKillOfB1:
                initialKillOfB1 = True
                boss1b.x = boss1a.x
                boss1b.y = boss1a.y
                boss1b.enalive = True
                boss1balive = True
            if not boss1balive:
                setLevels()
                x = 20
                y = 560
                lvl = 21
                success()
        else:
            screen.blit(text20a, (10, 50))
        boss1b.update()
        boss1balive = boss1b.returnAlive()
        switchtick -= 1
        if switchtick < 0:
            switchtick = 100
            lvl20co1.x = randomCoor(20)[0]
            lvl20co1.y = randomCoor(20)[1]
            lvl20co2.x = randomCoor(20)[0]
            lvl20co2.y = randomCoor(20)[1]
            lvl20co3.x = randomCoor(20)[0]
            lvl20co3.y = randomCoor(20)[1]
            lvl20co4.x = randomCoor(20)[0]
            lvl20co4.y = randomCoor(20)[1]
            lvl20co5.x = randomCoor(20)[0]
            lvl20co5.y = randomCoor(20)[1]

    if lvl == 40 and not paused:
        if not boss2aalive:
            lvl40co1.update()
            lvl40co1alive = lvl40co1.returnAlive()
            lvl40en1.update()
            lvl40en1alive = lvl40en1.returnAlive()
        boss2a.update()
        boss2aalive = boss2a.returnAlive()
        if not boss2aalive:
            screen.blit(text40, (10, 50))
            if not initialKillOfB2:
                initialKillOfB2 = True
                boss2b.x = boss2a.x
                boss2b.y = boss2a.y
                boss2b.enalive = True
                boss2balive = True
                boss2b.x = randomCoor(bosssize)[0]
                boss2b.y = randomCoor(bosssize)[1]
            if not boss2balive:
                setLevels()
                x = 20
                y = 560
                lvl = 41
                success()
        else:
            screen.blit(text40, (10, 50))
        boss2b.update()
        boss2balive = boss2b.returnAlive()
        switchtick -= 1
        if switchtick < 0:
            switchtick = 50
            lvl40co1.x = randomCoor(20)[0]
            lvl40co1.y = randomCoor(20)[1]

    gameUpdate()

    ##############################   END OF PLAYABLE LEVELS   ##############################

    if lvl == 64:
        if not hasTicked64:
            mixer.music.stop()
            hasTicked64 = True
            Music('blueSwordsmanEnd.wav', 1, 1)
        endTimer -= tickSize
        if endTimer <= 0:
            if useText:
                resetFiles(True, str(allLevelSetup[0][0].inp) + ".txt", str(allLevelSetup[0][1].inp) + ".txt")
            done = True

    if lvl != 63 and lvl != 64 and lvl != 0 and lvl != -1:
        if healing and invincibleTimer <= 0 and not paused:
            h_decision = random.randrange(3)
            if h_decision == 0:
                h_decision = HEAL1
            elif h_decision == 1:
                h_decision = HEAL2
            elif h_decision == 2:
                h_decision = HEAL3
            pygame.draw.rect(screen, h_decision, [x, y, sid, sid])
        elif isSprinting and invincibleTimer <= 0 and not paused:
            rgcol = random.randrange(0, 200, 50)
            pygame.draw.rect(screen, (rgcol, rgcol, random.randrange(200, 255)), [x, y, sid, sid])
        elif useStam and invincibleTimer <= 0 and not paused:
            s_decision = random.randrange(3)
            if s_decision == 0:
                s_decision = STAM1
            elif s_decision == 1:
                s_decision = STAM2
            elif s_decision == 2:
                s_decision = STAM3
            pygame.draw.rect(screen, s_decision, [x, y, sid, sid])
            energy_decision = random.randrange(3)
            if energy_decision == 0:
                energy_decision = STAM1
            elif energy_decision == 1:
                energy_decision = STAM2
            elif energy_decision == 2:
                energy_decision = STAM3
            pygame.draw.rect(screen, energy_decision, [0, 20, guage, 10])
        elif invincibleTimer <= 0 and not paused:
            pygame.draw.rect(screen, BLUE, [x, y, sid, sid])
        else:
            if not paused:
                drawInvinciblePlayer(x, y)

        if lives > 0:
            pygame.draw.rect(screen, BLUE, [770, 580, 10, 10])
        if lives > 1:
            pygame.draw.rect(screen, BLUE, [750, 580, 10, 10])
        if lives > 2:
            pygame.draw.rect(screen, BLUE, [730, 580, 10, 10])
        if lives > 3:
            pygame.draw.rect(screen, ENERGY, [710, 580, 10, 10])
        if lives > 4:
            pygame.draw.rect(screen, ENERGY, [690, 580, 10, 10])
        if lives > 5:
            lives = 5
        # please DO NOT consider the practicality of following 8 lines of code into your grading; I did it just to annoy a friend. I know how to correct this (easily) and that it is ridiculous and inefficient, but it was just too funny to exclude.
        if lives == 1:
            choiceforcolorwhenlivesequalsonehahahahathisisaverylongvariablenameandibetyoucannotreaditquickly = [True,
                                                                                                                False]
            if random.choice(
                    choiceforcolorwhenlivesequalsonehahahahathisisaverylongvariablenameandibetyoucannotreaditquickly):
                pygame.draw.rect(screen, (0, 0, random.uniform(0, 255)), [770, 580, 10, 10])
            elif not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not not random.choice(
                    choiceforcolorwhenlivesequalsonehahahahathisisaverylongvariablenameandibetyoucannotreaditquickly):
                pygame.draw.rect(screen, (random.uniform(0, 255), 0, 0), [770, 580, 10, 10])

    if keys[
        pygame.K_UP] and not tired and not invincibleTimer > 0 and lvl != 63 and lvl != 64 and lvl != -1 and lvl != 0:
        pygame.draw.rect(screen, WHITE, [x + .5 * sid - 2, y - 15, 4, 10])

    if keys[
        pygame.K_DOWN] and not tired and not invincibleTimer > 0 and lvl != 63 and lvl != 64 and lvl != -1 and lvl != 0:
        pygame.draw.rect(screen, WHITE, [x + .5 * sid - 2, y + 25, 4, 10])

    if keys[
        pygame.K_LEFT] and not tired and not invincibleTimer > 0 and lvl != 63 and lvl != 64 and lvl != -1 and lvl != 0:
        pygame.draw.rect(screen, WHITE, [x - 15, y + .5 * sid - 2, 10, 4])

    if keys[
        pygame.K_RIGHT] and not tired and not invincibleTimer > 0 and lvl != 63 and lvl != 64 and lvl != -1 and lvl != 0:
        pygame.draw.rect(screen, WHITE, [x + 25, y + .5 * sid - 2, 10, 4])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
    vel = 1.5
    time += 1
    click = False
    if not paused:
        guage += 2
    if tired:
        tiredtim += 2
        vel = .5
        if tiredtim >= 800:
            tired = False
            tiredtim = 0
    if invincibleTimer > 0:
        invincibleTimer -= 1
        hp = sethp
        vel = .5 * vel

    w = False
    a = False
    s = False
    d = False
    lvl2en3r = False
    lvl2en3l = False
    lvl2en3d = False
    lvl2en3u = False
    lvl3en1r = False
    lvl3en1l = False
    lvl3en1d = False
    lvl3en1u = False
    lvl4en1r = False
    lvl4en1l = False
    lvl4en1d = False
    lvl4en1u = False
    lvl4en2r = False
    lvl4en2l = False
    lvl4en2d = False
    lvl4en2u = False
    lvl4en3r = False
    lvl4en3l = False
    lvl4en3d = False
    lvl4en3u = False
    lvl5en1r = False
    lvl5en1l = False
    lvl5en1d = False
    lvl5en1u = False
    lvl5en2r = False
    lvl5en2l = False
    lvl5en2d = False
    lvl5en2u = False
    lvl5en3r = False
    lvl5en3l = False
    lvl5en3d = False
    lvl5en3u = False
    lvl6en2xdelta = -2
    if hp <= 0:
        lives -= 1
        usedLinkCombos = []
        death()
        if lives == 0:
            gameOver()
            if lvl <= 5:
                lvl = 1
            if lvl >= 6 and lvl <= 10:
                lvl = 6
            if lvl >= 11 and lvl <= 15:
                lvl = 11
            if lvl >= 16 and lvl <= 20:
                lvl = 16
            if lvl >= 21 and lvl <= 25:
                lvl = 21
            if lvl >= 26 and lvl <= 30:
                lvl = 26
            if lvl >= 31 and lvl <= 35:
                lvl = 31
            if lvl >= 36 and lvl <= 40:
                lvl = 36
            if lvl >= 41 and lvl <= 45:
                lvl = 41
            if lvl >= 46 and lvl <= 50:
                lvl = 46
            if lvl >= 51 and lvl <= 55:
                lvl = 51
            if lvl >= 56 and lvl <= 60:
                lvl = 56
            lives = 3
        hp = 800
        guage = 800
        x = 20
        y = 560
        if lvl == 16:
            x = 400
            y = 560
        tired = False
        tiredtim = 800
        bombs = 0
        invincibleTimer = 0
        xtrastam = 0
        ###
        lvl1en1x = 300
        lvl1en1y = 50
        lvl1en2x = 500
        lvl1en2y = 500
        lvl1en1ydelta = 2
        lvl1en2ydelta = -2
        lvl1en1alive = True
        lvl1en2alive = True
        ###
        lvl2en1x = 300
        lvl2en1y = 50
        lvl2en2x = 500
        lvl2en2y = 500
        lvl2en3x = 400
        lvl2en3y = 300 - .5 * sid
        lvl2en1ydelta = 2
        lvl2en2ydelta = -2
        lvl2en1alive = True
        lvl2en2alive = True
        lvl2en3alive = True
        ###
        lvl3en1x = 760
        lvl3en1y = 20
        lvl3en1xdelta = 0
        lvl3en1ydelta = 0
        lvl3en1alive = True
        ###
        lvl4en1x = 760
        lvl4en1y = 20
        lvl4en1xdelta = 0
        lvl4en1ydelta = 0
        lvl4en1alive = True
        lvl4en2x = 760
        lvl4en2y = 290
        lvl4en2xdelta = 0
        lvl4en2ydelta = 0
        lvl4en2alive = True
        lvl4en3x = 760
        lvl4en3y = 560
        lvl4en3xdelta = 0
        lvl4en3ydelta = 0
        lvl4en3alive = True
        ###
        lvl5en1x = 760
        lvl5en1y = 20
        lvl5en1xdelta = 0
        lvl5en1ydelta = 0
        lvl5en2x = 760
        lvl5en2y = 290
        lvl5en2xdelta = 0
        lvl5en2ydelta = 0
        lvl5en3x = 760
        lvl5en3y = 560
        lvl5en3xdelta = 0
        lvl5en3ydelta = 0
        lvl5en4x = 740
        lvl5en4y = 560
        lvl5en4xdelta = random.uniform(7, 20)
        lvl5en4ydelta = random.uniform(7, 20)
        lvl5en4alive = True
        ###
        lvl6en1x = 330
        lvl6en1y = 100
        lvl6en1alive = True
        lvl6en2x = 0
        lvl6en2y = 50
        lvl6en2xdelta = -2
        ###
        lvl7en1x = 300
        lvl7en1y = 100
        lvl7en2x = 500
        lvl7en2y = 100
        lvl7en3x = 700
        lvl7en3y = 100
        lvl7en4x = 700
        lvl7en4y = 300
        lvl7en5x = 700
        lvl7en5y = 500
        lvl7en6x = 500
        lvl7en6y = 500
        lvl7en7x = 300
        lvl7en7y = 500
        lvl7en8x = 300
        lvl7en8y = 300
        lvl7en9x = 500
        lvl7en9y = 300
        lvl7en1xdelta = 4
        lvl7en1ydelta = 0
        lvl7en2xdelta = 4
        lvl7en2ydelta = 0
        lvl7en3xdelta = 0
        lvl7en3ydelta = 4
        lvl7en4xdelta = 0
        lvl7en4ydelta = 4
        lvl7en5xdelta = -4
        lvl7en5ydelta = 0
        lvl7en6xdelta = -4
        lvl7en6ydelta = 0
        lvl7en7xdelta = 0
        lvl7en7ydelta = -4
        lvl7en8xdelta = 0
        lvl7en8ydelta = -4
        lvl7en1alive = True
        lvl7en2alive = True
        lvl7en3alive = True
        lvl7en4alive = True
        lvl7en5alive = True
        lvl7en6alive = True
        lvl7en7alive = True
        lvl7en8alive = True
        lvl7en9alive = True
        ###
        lvl8en1x = 600
        lvl8en1y = 50
        lvl8en1xdelta = random.uniform(1.5, 4)
        lvl8en1ydelta = random.uniform(1.5, 4)
        lvl8en1hidden = True
        lvl8en1alive = True
        ###
        lvl9en1x = 600
        lvl9en1y = 50
        lvl9en1xdelta = random.uniform(1.5, 4)
        lvl9en1ydelta = random.uniform(1.5, 4)
        lvl9en1hidden = True
        lvl9en1alive = True
        lvl9en2x = 600
        lvl9en2y = 290
        lvl9en2xdelta = random.uniform(-4, -1.5)
        lvl9en2ydelta = random.uniform(-4, -1.5)
        lvl9en2hidden = True
        lvl9en2alive = True
        lvl9en3x = 600
        lvl9en3y = 500
        lvl9en3xdelta = random.uniform(1.5, 4)
        lvl9en3ydelta = random.uniform(1.5, 4)
        lvl9en3hidden = True
        lvl9en3alive = True
        ###
        lvl10en1x = 290
        lvl10en1y = 50
        lvl10en1xdelta = random.uniform(1.5, 4)
        lvl10en1ydelta = random.uniform(1.5, 4)
        lvl10en1hidden = True
        lvl10en1alive = True
        lvl10en2x = 200
        lvl10en2y = 0
        lvl10en3x = 500
        lvl10en3y = 20.0000001
        lvl10en4x = 225
        lvl10en4y = 560
        lvl10en4alive = True
        lvl10en5x = 700
        lvl10en5y = 400
        lvl10en5alive = True
        ###
        lvl11bomb1alive = True
        ###
        lvl12en1alive = True
        lvl12en2alive = True
        lvl12en3alive = True
        lvl12bullet1x = 745
        lvl12bullet1y = 15
        lvl12bullet2x = 775
        lvl12bullet2y = 45
        lvl12bomb1alive = True
        lvl12firstshot = False
        ###
        lvl13en1alive = True
        lvl13bomb1alive = True
        lvl13lifealive = True
        lvl13bullet1x = 700
        ###
        lvl14blade1y = 0
        lvl14blade2y = 580
        lvl14blade3y = 0
        lvl14blade4y = 580
        lvl14blade5y = 0
        lvl14blade6y = 580
        lvl14blade7y = 0
        lvl14blade8y = 580
        lvl14blade9y = 0
        lvl14blade10y = 580
        lvl14blade11y = 0
        lvl14blade12y = 580
        lvl14blade13y = 0
        lvl14blade14y = 580
        lvl14blade1ydelta = 7
        lvl14blade2ydelta = -7
        lvl14blade3ydelta = 7
        lvl14blade4ydelta = -7
        lvl14blade5ydelta = 7
        lvl14blade6ydelta = -7
        lvl14blade7ydelta = 7
        lvl14blade8ydelta = -7
        lvl14blade9ydelta = 7
        lvl14blade10ydelta = -7
        lvl14blade11ydelta = 7
        lvl14blade12ydelta = -7
        lvl14blade13ydelta = 7
        lvl14blade14ydelta = -7
        lvl14en1x = random.randrange(550, 650)
        lvl14en1y = random.randrange(250, 450)
        lvl14en1xdelta = random.uniform(-2, 2)
        lvl14en1ydelta = random.uniform(-2, 2)
        lvl14en1alive = True
        lvl14lifealive = True
        ###
        boss1aalive = True
        boss1a = Boss(boss1aalive, (255, 255, 0), 1.4, 500, 200, True, 1, True, False, True, False, 1, False)
        initialKillOfB1 = False
        boss1balive = False
        boss1b = Boss(boss1balive, (255, 255, 0), 7, 500, 200, False, 4, False, True, True, True, 3, True)
        switchtick = 100
        lvl20co1alive = True
        lvl20co1 = Collectible("bomb", lvl20co1alive, randomCoor(20)[0], randomCoor(20)[1])
        lvl20co2alive = True
        lvl20co2 = Collectible("bomb", lvl20co2alive, randomCoor(20)[0], randomCoor(20)[1])
        lvl20co3alive = True
        lvl20co3 = Collectible("bomb", lvl20co3alive, randomCoor(20)[0], randomCoor(20)[1])
        lvl20co4alive = True
        lvl20co4 = Collectible("bomb", lvl20co4alive, randomCoor(20)[0], randomCoor(20)[1])
        lvl20co5alive = True
        lvl20co5 = Collectible("bomb", lvl20co5alive, randomCoor(20)[0], randomCoor(20)[1])
        ###
        boss2aalive = True
        boss2a = Boss(boss2aalive, (129, 129, 129), 2.5, 575, 275, False, 2, True, False, True, False, .7, True)
        initialKillOfB2 = False
        boss2balive = False
        boss2b = Boss(boss2balive, (129, 129, 129), 1, 575, 275, True, 1, False, False, True, True, .7, False)
        lvl40en1alive = True
        lvl40en1 = Enemy(lvl40en1alive, randomCoor(20)[0], randomCoor(20)[1], True, False, False, True, randomSpeed(),
                         randomSpeed(), False, 0, False, True)
        lvl40co1alive = True
        lvl40co1 = Collectible(["chain", [lvl40en1, boss2b]], lvl40co1alive, randomCoor(20)[0], randomCoor(20)[1])
        setLevels()
    if not paused:
        hp += .25
        if hp >= 800:
            hp = 800
        if lives > 5:
            lives = 5
        if xtrastam > 400:
            xtrastam = 400
        if guage >= 790:
            hp += .35
    keyinp = ""
    bckspce = False
    buttonpressed = False
    allChainsUpdate()
    if cheat:
        guage = 10000
        hp = 10000
        vel = 6
# Close the window, save if needed, and quit.
if useText:
    file = open(globalf, "w")
    file.write(globalpass)
    file.close()
    file2 = open(globalf2, "w")
    file2.write(str(lives))
    file2.close()
    file3 = open(globalf3, "w")
    file3.write(str(lvl))
    file3.close()
pygame.quit()
