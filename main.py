#Griffin Hampton FNAD V:2

import pygame
from pygame import *
from config import *
from menu import *
from time import *
from PIL import Image, ImageSequence
from random import *
pygame.mixer.init()
pygame.mixer.music.load('img\scaryTitleScreen.ogg')
pygame.mixer.music.set_volume(.4)
pygame.mixer.music.play(loops=10)




def loadGIF(filename):
    pilImage = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(pilImage):
        frame = frame.convert('RGBA')
        pygameImage = pygame.image.fromstring(
            frame.tobytes(), frame.size, frame.mode).convert_alpha()
        frames.append(pygameImage)
    return frames

class AnimatedSpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, bottom, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom = (x, bottom))
        self.image_index = 0

    def update(self):
        self.image_index += 1
        pygame.time.delay(100)
        if self.image_index >= len(self.images):
            self.image_index = 0
        
        self.image = self.images[self.image_index]

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('img/8bitoperator.ttf', 120)
        self.smallfont = pygame.font.Font('img/8bitoperator.ttf', 24)
        self.running=True

        self.flashmid = pygame.image.load('img\MiddleFlashMaybeBall.png')
        self.flashmid = pygame.transform.scale(self.flashmid, (SCREENSIZE))
        self.darkmid = pygame.image.load('img\MiddleDark.png')
        self.darkmid = pygame.transform.scale(self.darkmid, (SCREENSIZE))

        self.flashright = pygame.image.load('img\MaybeRightFlash2.jpg')
        self.flashright = pygame.transform.scale(self.flashright, (SCREENSIZE))
        self.darkright = pygame.image.load('img\RightLookDark.png')
        self.darkright = pygame.transform.scale(self.darkright, (SCREENSIZE))

        self.flashleft = pygame.image.load('img\LeftLookFlashlight.png')
        self.flashleft = pygame.transform.scale(self.flashleft, (SCREENSIZE))
        self.darkleft = pygame.image.load('img\LeftLookDark.png')
        self.darkleft = pygame.transform.scale(self.darkleft, (SCREENSIZE))

        self.midCam = pygame.image.load('img\Middle.jpg')
        self.midCam = pygame.transform.scale(self.midCam, (SCREENSIZE))

        self.midCamBackup = pygame.image.load('img\Middle.jpg')
        self.midCamBackup = pygame.transform.scale(self.midCamBackup, (SCREENSIZE))
        
        self.leftHall = pygame.image.load('img\LeftHallway.jpg')
        self.leftHall = pygame.transform.scale(self.leftHall, (SCREENSIZE))
        
        self.leftCorner = pygame.image.load('img\LeftCorner.jpg')
        self.leftCorner = pygame.transform.scale(self.leftCorner, (SCREENSIZE))
        
        self.rightHall = pygame.image.load('img\Right HallwayR.jpg')
        self.rightHall = pygame.transform.scale(self.rightHall, (SCREENSIZE))
        
        self.rightCorner = pygame.image.load('img\RightCorner.jpg')
        self.rightCorner = pygame.transform.scale(self.rightCorner, (SCREENSIZE))
        
        self.preBoiler = pygame.image.load('img\preBoiler.jpg')
        self.preBoiler = pygame.transform.scale(self.preBoiler, (SCREENSIZE))

        self.boiler = pygame.image.load('img/boilerRoom.jpeg')
        self.boiler = pygame.transform.scale(self.boiler, (SCREENSIZE))

        self.goblinRoom = pygame.image.load('img\goblinRoom.PNG')
        self.goblinRoom = pygame.transform.scale(self.goblinRoom, (SCREENSIZE))

        self.leftBar = pygame.image.load('img\LeftBar.png')
        self.leftBar = pygame.transform.scale(self.leftBar, (SCREENSIZE))

        self.rightBar = pygame.image.load('img\RightBar.png')
        self.rightBar = pygame.transform.scale(self.rightBar, (SCREENSIZE))

        self.middleBar = pygame.image.load(r'img/UpBar.png')
        self.middleBar = pygame.transform.scale(self.middleBar, (600,50))

        self.topLeft = pygame.image.load('img/AllOfThem (1).jpg')
        self.topLeft = pygame.transform.scale(self.topLeft, (SCREENSIZE))

        self.camUI = pygame.image.load('img/camUI.png')
        self.camUI.set_colorkey(WHITE)
        self.camUI = pygame.transform.scale(self.camUI, (500,400))

        self.fullbat = pygame.image.load('img/batteryFull.png')
        self.quarterfullbat = pygame.image.load('img/75PercentBatter.png')
        self.halfbat = pygame.image.load('img\halfBattery.png')
        self.quarterleftbat= pygame.image.load('img/25PercentBattery.png')
        self.nobat = pygame.image.load('img\EmptyBattery.png')

        self.grassRoom = pygame.image.load('img\FarRightCam.jpg')
        self.grassRoom = pygame.transform.scale(self.grassRoom, (SCREENSIZE))

        self.nightWin = pygame.image.load('img\congratsW.png')
        self.nightWin = pygame.transform.scale(self.nightWin, (SCREENSIZE))

        self.bois1 = pygame.image.load('img\Bois1.png')
        self.bois1 = pygame.transform.scale(self.bois1, (SCREENSIZE))

        self.bois2 = pygame.image.load('img\Bois2.jpg')
        self.bois2 = pygame.transform.scale(self.bois2, (SCREENSIZE))

        self.bois3 = pygame.image.load('img\Bois3.jpg')
        self.bois3 = pygame.transform.scale(self.bois3, (SCREENSIZE))

        self.bois4 = pygame.image.load('img\VertScare.png')
        self.bois4 = pygame.transform.scale(self.bois4, (SCREENSIZE))

        self.smile1 = pygame.image.load('img\AllOfThem (1).jpg')
        self.smile1 = pygame.transform.scale(self.smile1, (SCREENSIZE))

        self.smile2 = pygame.image.load('img\AllOfThem.jpg')
        self.smile2 = pygame.transform.scale(self.smile2, (SCREENSIZE))

        self.smile3 = pygame.image.load('img\Main RoomR - scaryfacephase2.jpg')
        self.smile3 = pygame.transform.scale(self.smile3, (SCREENSIZE))

        self.smile4 = pygame.image.load('img\Main RoomR - scaryfacephase3.jpg')
        self.smile4 = pygame.transform.scale(self.smile4, (SCREENSIZE))

        self.smile5 = pygame.image.load('img\eyes.png')

        self.gif = loadGIF('img\cat-dance.gif')

        self.gif2 = loadGIF('img/boisvert.gif')
        
        animated_sprite = AnimatedSpriteObject(950,700, self.gif)
        self.all_sprites = pygame.sprite.Group(animated_sprite)

        self.deathNoise = pygame.mixer.Sound("img/scarySighting.wav")

        animated_spriteBois = AnimatedSpriteObject(950,1080, self.gif2)
        self.all_sprites2 = pygame.sprite.Group(animated_spriteBois)
        self.text = '12AM'
        self.camOff=False

        self.boisDeath = False


        self.time = 0
        self.time_speed=.5
        self.nighttime = 0

        self.facing = 'middle'
        self.cam = ''
        self.camNumber = 5
        self.camOffNumber = 0

        self.night=1

        self.monsterSpeed = .01
        self.boisDeathTime = 0

        self.winningTime =0

        self.battery_percent = 100
        self.batphase= ''
        self.boilerPower = 100

        self.smilePhase = 0

        self.nightWinner = self.font.render(('You survived a night....'), True, BLACK)

        self.scaryText = self.font.render(('It is in your room.'), True, WHITE)
        self.deathText = self.font.render(('You died :P press [ESCAPE] to exit'), True, WHITE)
        
        self.smileLocationName = ''

    def newNight(self):
        self.screen.blit(self.nightWin, (0, 0))
        self.screen.blit(self.nightWinner, (400, 900))
        self.text = '12AM'
        self.night+=0.00142857142
        self.battery_percent = 100
        self.boilerPower = 100
        self.facing = 'middle'
        if self.nighttime >=4895:
            self.monsterSpeed = self.monsterSpeed*self.night
            print(self.monsterSpeed)

        

    def events(self):
        mouse_pos_x,mouse_pos_y = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        keys=pygame.key.get_pressed()
        self.time+=1
        self.nighttime+=self.time_speed
        self.smilePhase+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    self.running=False
            if event.type == pygame.KEYDOWN:
                if self.facing =='down':
                    if event.key == pygame.K_1:
                        self.cam = 'LCorner'
                    if event.key == pygame.K_3:
                        self.cam = 'RCorner'
                    if event.key == pygame.K_8:
                        self.cam = 'TopLeft'
                    if event.key == pygame.K_7:
                        self.cam = 'Grass'
                    if event.key == pygame.K_0:
                        self.cam = 'Boiler'
                    if event.key == pygame.K_9:
                        self.cam = 'PBoiler'
                    if event.key == pygame.K_6:
                        self.cam = 'Goblin'
                    if event.key == pygame.K_2:
                        self.cam = 'LHall'
                    if event.key == pygame.K_4:
                        self.cam = 'RHall'
                    if event.key == pygame.K_5:
                        self.cam = 'Mid'
            if self.facing=='middle' and mouse_pos_x >= 1900 and self.time >=50:
                self.facing='right'
                self.time = 0
            if self.facing=='middle' and mouse_pos_x <= 50 and self.time >=50:
                self.facing='left'
                self.time = 0
            if self.facing=='left' and mouse_pos_x >= 1900 and self.time >=50:
                self.facing='middle'
                self.time = 0
            if self.facing=='right' and mouse_pos_x <= 50 and self.time >=50:
                self.facing='middle'
                self.time = 0
            if self.facing != 'down' and mouse_pos_y>=1050 and self.time >=50 and self.battery_percent>0:
                self.facing='down'
                self.cam = 'Mid'
                self.time = 0

            if self.facing =='down':
                self.camtime=0
            
            if self.facing == 'down' and mouse_pos_y>=1050 and self.time >=50:
                self.facing='middle'
                self.cam = ''
                self.time = 0
            

    def main(self):
        self.events()
        self.update()
        self.draw()

    def draw(self):
        self.clock.tick(FPS)
        pygame.display.update()

    def boilerUI(self):
        boilerText = self.smallfont.render((f'Boiler percent power left: {int(self.boilerPower)}% use SPACE to recharge'), True, WHITE)
        self.screen.blit(boilerText, (700, 700))

    def camUIAll(self):
        self.screen.blit(self.camUI,(1400,550))
        camText = self.font.render((f'Cam {int(self.camNumber)}'), True, WHITE)
        self.screen.blit(camText, (1500, 100))
        if self.boisDeathTime>900 or self.smilePhase>=1300:
                self.screen.blit(self.scaryText, (500, 500))

    def update(self):
        if self.boilerPower>0:
            self.boilerPower-=self.monsterSpeed*self.night
        else:
            self.boisDeath = True
        if self.smilePhase >=1300 and self.smilePhase<=1400 and self.smileLocation == 1:
                self.smileLocationName = 'left'
        if self.smilePhase >=1300 and self.smilePhase<=1400 and self.smileLocation == 2:
                self.smileLocationName = 'mid'
        if self.smilePhase >=1300 and self.smilePhase<=1400 and self.smileLocation == 3:
                self.smileLocationName = 'right'
        if self.smilePhase<1299:
            self.smileLocationName = ''
        keys=pygame.key.get_pressed()

        if self.boisDeath ==True:
            self.boisDeathTime+=1
            if self.boisDeathTime>=0 and self.boisDeathTime<=300:
                self.grassRoom = self.bois1
            if self.boisDeathTime>=300 and self.boisDeathTime<=600:
                self.grassRoom = self.bois2
            if self.boisDeathTime>=600 and self.boisDeathTime<=900:
                self.grassRoom = self.bois3
            if self.boisDeathTime>900:
                self.grassRoom = pygame.image.load('img\FarRightCam.jpg')
                self.grassRoom = pygame.transform.scale(self.grassRoom, (SCREENSIZE))
            
            
        if self.facing == 'down'and self.battery_percent >= 0:
            self.battery_percent-=.01
        if self.facing == 'middle':
            self.screen.blit(self.darkmid,(0,0))
            self.screen.blit(self.middleBar,(660,1000))
            if self.boisDeathTime>1200:
                self.smilePhase = 0
                self.camOff = True
                pygame.mixer.Sound.play(self.deathNoise)
                self.all_sprites2.update()
                self.all_sprites2.draw(self.screen)
                self.screen.blit(self.deathText, (500, 500))
            if self.smileLocationName == 'mid':
                self.screen.blit(self.smile5, (400,400))
            if self.smilePhase >=1450:
                #PUT A COOL JUMP SCARE HERE
                pass
            if keys[pygame.K_f] and self.battery_percent>0:
                self.battery_percent-=.1
                self.screen.blit(self.flashmid,(0,0))
                self.screen.blit(self.middleBar,(660,1000))
                if self.smileLocationName == 'mid':
                    self.smilePhase -= 500/self.night
        if self.facing == 'right':
            self.screen.blit(self.darkright,(0,0))
            self.screen.blit(self.middleBar,(660,1000))
            if self.boisDeathTime>1200:
                self.smilePhase = 0
                self.camOff = True
                pygame.mixer.Sound.play(self.deathNoise)
                self.all_sprites2.update()
                self.all_sprites2.draw(self.screen)
                self.screen.blit(self.deathText, (500, 500))
            if self.smilePhase >=1450:
                #PUT A COOL JUMP SCARE HERE
                pass
            if self.smileLocationName == 'right':
                self.screen.blit(self.smile5, (400,400))
            if keys[pygame.K_f] and self.battery_percent>0:
                self.battery_percent-=.1
                self.screen.blit(self.flashright,(0,0))
                self.screen.blit(self.middleBar,(660,1000))
                if self.smileLocationName == 'right':
                    self.smilePhase -= 500/self.night
        if self.facing == 'left':
            self.screen.blit(self.darkleft,(0,0))
            self.screen.blit(self.middleBar,(660,1000))
            if self.boisDeathTime>1200:
                self.smilePhase = 0
                self.camOff = True
                pygame.mixer.Sound.play(self.deathNoise)
                self.all_sprites2.update()
                self.all_sprites2.draw(self.screen)
                self.screen.blit(self.deathText, (500, 500))
            if self.smilePhase >=1450:
                #PUT A COOL JUMP SCARE HERE
                pass
            if self.smileLocationName == 'left':
                self.screen.blit(self.smile5, (400,400))
            if keys[pygame.K_f] and self.battery_percent>0:
                self.battery_percent-=.05
                self.screen.blit(self.flashleft,(0,0))
                self.screen.blit(self.middleBar,(660,1000))
                if self.smileLocationName == 'left':
                    self.smilePhase -= 500/self.night
    
        if self.cam =='Mid'and self.battery_percent >= 0:
            if self.smilePhase>=700 and self.smilePhase<=1000:
                self.midCam = self.smile3
            if self.smilePhase >=1000 and self.smilePhase<=1300:
                self.midCam = self.smile4
            if self.smilePhase == 1300:
                self.smileLocation = randrange(3)+1
            if self.smilePhase>=1300:
                self.midCam = self.midCamBackup
            self.screen.blit(self.midCam,(0,0))
            self.screen.blit(self.middleBar,(660,1000))
            self.camNumber = 5
            self.camUIAll()
        if self.cam =='Boiler'and keys[pygame.K_SPACE] and self.boilerPower <=100:
            self.boilerPower+=.1
        if self.cam =='TopLeft'and self.battery_percent >= 0:
            if self.smilePhase >=700:
                self.topLeft = self.smile1
            self.screen.blit(self.topLeft,(0,0))
            self.screen.blit(self.middleBar,(660,1000))
            self.camNumber = 8
            self.camUIAll()

        if self.cam =='LCorner'and self.battery_percent >= 0:
            self.screen.blit(self.leftCorner,(0,0))
            self.screen.blit(self.middleBar,(660,1000))
            self.camNumber = 1
            self.camUIAll()

        if self.cam =='Grass'and self.battery_percent >= 0:
            self.screen.blit(self.grassRoom,(0,0))
            self.screen.blit(self.middleBar,(660,1000))
            self.camNumber = 7
            self.camUIAll()
        
        if self.cam =='RCorner'and self.battery_percent >= 0:
            self.screen.blit(self.rightCorner,(0,0))
            self.screen.blit(self.middleBar,(660,1000))
            self.camNumber = 3
            self.camUIAll()

        if self.cam =='Boiler'and self.battery_percent >= 0:
            self.screen.blit(self.boiler,(0,0))
            self.screen.blit(self.middleBar,(660,1000))
            self.camNumber = 0
            self.camUIAll()
            self.boilerUI()

        if self.cam =='PBoiler'and self.battery_percent >= 0:
            self.screen.blit(self.preBoiler,(0,0))
            self.screen.blit(self.middleBar,(660,1000))
            self.camNumber = 9
            self.camUIAll()

        if self.cam =='Goblin'and self.battery_percent >= 0:
            self.screen.blit(self.goblinRoom,(0,0))
            self.screen.blit(self.middleBar,(660,1000))
            self.camNumber = 6
            self.camUIAll()
            

        if self.cam =='LHall'and self.battery_percent >= 0:
            self.screen.blit(self.leftHall,(0,0))
            self.screen.blit(self.middleBar,(660,1000))
            self.camNumber = 2
            self.camUIAll()

        if self.cam =='RHall'and self.battery_percent >= 0:
            self.screen.blit(self.rightHall,(0,0))
            self.screen.blit(self.middleBar,(660,1000))
            self.camNumber = 4
            self.camUIAll()
        if self.time<=700:
            self.text='12AM'
        if self.nighttime>=700 and self.nighttime<=1400:
            self.text='1AM'
        if self.nighttime>=1400 and self.nighttime<=2100:
            self.text='2AM'
        if self.nighttime>=2100 and self.nighttime<=2800:
            self.text='3AM'
        if self.nighttime>=2800 and self.nighttime<=3500:
            self.text='4AM'
        if self.nighttime>=3500 and self.nighttime<=4200:
            self.text='5AM'
        if self.battery_percent>=75:
            self.batphase = self.fullbat
        if self.battery_percent>=50 and self.battery_percent<=75:
            self.batphase = self.quarterfullbat
        if self.battery_percent>=25 and self.battery_percent<=50:
            self.batphase = self.halfbat
        if self.battery_percent<=25 and self.battery_percent!=0:
            self.batphase = self.quarterleftbat
        if self.battery_percent <= 0:
            self.batphase = self.nobat
            self.camOff = True
        if self.boilerPower == 0:
            self.screen.fill(BLACK)
        if self.camOff == True and self.camOffNumber<1:
            self.facing = 'middle'
            self.camOff = False 
            self.camOffNumber +=1

            

        

        

        text = self.font.render(self.text, True, WHITE)
        nightText = self.font.render((f'Night {int(self.night)}'), True, WHITE)
        self.screen.blit(text, (100, 900))
        self.screen.blit(self.batphase, (400, 900))
        self.screen.blit(nightText, (100, 100))

        if self.nighttime>=4200 and self.nighttime<=4550:
            self.newNight()
            
        if self.nighttime>=4550:
            self.nighttime = 0
            
        if self.night>4.5:
            self.nighttime=4899
            self.winningTime+=1
            self.screen.fill(BLACK)
            winnerText = self.font.render(('YOU WON!!! CONGRATS!!!!'), True, WHITE)
            self.screen.blit(winnerText, (400, 900))
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            if self.winningTime>=3000:
                self.running=False


        

        


        



        



g=Game()
while g.running:
    g.main()

pygame.quit()
