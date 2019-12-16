import sys
import random
import pygame
from salinim import *
from pixel import *
from pygame.locals import *
from ekran import *
from itertools import cycle
def main():
    global SCREEN, FPSCLOCK
    #Tüm import edilen pygamelerin tanımlanması yapılır.
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    #Screen tanımlanır.
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    #Oyun başlığı seçilir.
    pygame.display.set_caption('Bird Learning --- Group 1')
    #Toprak zemini base olarak eklenir.
    IMAGES['zemin'] = pygame.image.load('photos/zemin.png').convert_alpha()
    while True:
        # arka plan
        IMAGES['arkaplan'] = pygame.image.load('photos/arkaplan.png').convert()
        # kuşların kanat çırpması
        IMAGES['bird'] = (
            pygame.image.load('photos/ust.png').convert_alpha(),
            pygame.image.load('photos/orta.png').convert_alpha(),
            pygame.image.load('photos/alt.png').convert_alpha(),
        )

        IMAGES['boru'] = (
            pygame.transform.flip(
                pygame.image.load('photos/boru.png').convert_alpha(), False, True),
            pygame.image.load('photos/boru.png').convert_alpha(),
        )

        HITMASKS['boru'] = (
            getHitmask(IMAGES['boru'][0]),
            getHitmask(IMAGES['boru'][1]),
        )

        HITMASKS['bird'] = (
            getHitmask(IMAGES['bird'][0]),
            getHitmask(IMAGES['bird'][1]),
            getHitmask(IMAGES['bird'][2]),
        )

        hareket = anaekran()
        carpma = mainGame(hareket)
        


def anaekran():

    bird_Index = 0
    birdIndexCycle = cycle([0, 1, 2, 1])
    count = 0
    birdx = int(SCREENWIDTH * 0.2)
    birdy = int((SCREENHEIGHT - IMAGES['bird'][0].get_height()) / 2)
    zeminx = 0
    zemin_move = IMAGES['zemin'].get_width() - IMAGES['arkaplan'].get_width()
    birdShmVals = {'val': 0, 'dir': 1}
    while True:
        for event in pygame.event.get():
            #Oyundan çıkış yapma
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            #Oyun hareketlerinin keyboard üzerinden gösterimi
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):

                return {
                    'birdy': birdy + birdShmVals['val'],
                    'zeminx': zeminx,
                    'BirdIndexGen': birdIndexCycle,
                }
        #ayarlamalar
        if (count + 1) % 5 == 0:
            bird_Index = next(birdIndexCycle)
        count = (count + 1) % 30
        zeminx = -((-zeminx + 4) % zemin_move)
        salinim(birdShmVals)

        # blit() --> pygame
        SCREEN.blit(IMAGES['arkaplan'], (0,0))
        SCREEN.blit(IMAGES['bird'][bird_Index],
                    (birdx, birdy + birdShmVals['val']))
        SCREEN.blit(IMAGES['zemin'], (zeminx, SCREENHEIGHT * 0.79))
        pygame.display.update()
        FPSCLOCK.tick(FPS)
def mainGame(hareket):
    bird_Index = count = 0
    BirdIndexGen = hareket['BirdIndexGen']
    birdx, birdy = int(SCREENWIDTH * 0.2), hareket['birdy']
    zeminx = hareket['zeminx']
    zemin_move = IMAGES['zemin'].get_width() - IMAGES['arkaplan'].get_width()

    # alt ve üst borunun seçilmesi
    boru1 = borusecme()
    boru2 = borusecme()

    # üst borular
    ustborular = [
        {'x': SCREENWIDTH + 200, 'y': boru1[0]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': boru2[0]['y']},
    ]

    # alt borular
    altborular = [
        {'x': SCREENWIDTH + 200, 'y': boru1[1]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': boru2[1]['y']},
    ]

    boruX = -4

    # Kuşun hareket ile alakalı özellikleri
    birdVelY    =  -9   # Kuşun y boyunca hızı
    birdMaxVelY =  10   # max y boyunca hız
    birdAccY    =   1   # aşağı ivme
    birdRot     =  45   # kuşun konumu
    birdVelRot  =   3   # açısal hız
    birdRotThr  =  20   # dönme eşiği
    birdFlapAcc =  -9   # uçma anında
    bird_flapp = False # uçarken true


    while True:
        for event in pygame.event.get():
            # Oyun hareketlerinin keyboard üzerinden gösterimi
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if birdy > -2 * IMAGES['bird'][0].get_height():
                    birdVelY = birdFlapAcc
                    bird_flapp = True
        # Çarpma kontrolü
        carpmaTesti = carpmakontrolu({'x': birdx, 'y': birdy, 'index': bird_Index},
                               ustborular, altborular)
        if carpmaTesti[0]:
            return {
            }

        if (count + 1) % 3 == 0:
            bird_Index = next(BirdIndexGen)
        count = (count + 1) % 30
        zeminx = -((-zeminx + 100) % zemin_move)

        # Kuşun konumlandırılması
        if birdRot > -90:
            birdRot -= birdVelRot

        # oyuncunun hareketi
        if birdVelY < birdMaxVelY and not bird_flapp:
            birdVelY += birdAccY
        if bird_flapp:
            bird_flapp = False
            birdRot = 50

        birdHeight = IMAGES['bird'][bird_Index].get_height()
        birdy += min(birdVelY, SCREENHEIGHT * 0.79 - birdy - birdHeight)

        # boruların sola hareketi
        for uboru, aboru in zip(ustborular, altborular):
            uboru['x'] += boruX
            aboru['x'] += boruX

        # bir boru soldan çıktığında yeni borunun eklenmesi
        if 0 < ustborular[0]['x'] < 5:
            yeni = borusecme()
            ustborular.append(yeni[0])
            altborular.append(yeni[1])

        # boruların çıkarılması pop()
        if ustborular[0]['x'] < -IMAGES['boru'][0].get_width():
            ustborular.pop(0)
            altborular.pop(0)
        SCREEN.blit(IMAGES['arkaplan'], (0,0))

        for uboru, aboru in zip(ustborular, altborular):
            SCREEN.blit(IMAGES['boru'][0], (uboru['x'], uboru['y']))
            SCREEN.blit(IMAGES['boru'][1], (aboru['x'], aboru['y']))

        SCREEN.blit(IMAGES['zemin'], (zeminx, SCREENHEIGHT * 0.79))

        visibleRot = birdRotThr
        if birdRot <= birdRotThr:
            visibleRot = birdRot
        
        bird_yuzey = pygame.transform.rotate(IMAGES['bird'][bird_Index], visibleRot)
        SCREEN.blit(bird_yuzey, (birdx, birdy))

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def borusecme():

    # Rastgele olarak boruların konumlandırılması
    gapY = random.randrange(0, int(SCREENHEIGHT * 0.79 * 0.6 - PIPEGAPSIZE))
    gapY += int(SCREENHEIGHT * 0.79 * 0.2)
    pipeHeight = IMAGES['boru'][0].get_height()
    pipeX = SCREENWIDTH + 10

    return [
        {'x': pipeX, 'y': gapY - pipeHeight},  # upper pipe
        {'x': pipeX, 'y': gapY + PIPEGAPSIZE}, # lower pipe
    ]

def carpmakontrolu(bird, ustborular, altborular):
    """returns True if player collders with base or pipes."""
    pi = bird['index']
    bird['w'] = IMAGES['bird'][0].get_width()
    bird['h'] = IMAGES['bird'][0].get_height()

    # kuş zemine çarparsa
    if bird['y'] + bird['h'] >= SCREENHEIGHT * 0.79 - 1:
        return [True, True]
    else:

        birdRect = pygame.Rect(bird['x'], bird['y'],
                      bird['w'], bird['h'])
        pipeW = IMAGES['boru'][0].get_width()
        pipeH = IMAGES['boru'][0].get_height()

        for uboru, aboru in zip(ustborular, altborular):

            ustborukenar = pygame.Rect(uboru['x'], uboru['y'], pipeW, pipeH)
            altborukenar = pygame.Rect(aboru['x'], aboru['y'], pipeW, pipeH)
            pHitMask = HITMASKS['bird'][pi]
            uHitmask = HITMASKS['boru'][0]
            lHitmask = HITMASKS['boru'][1]
            uCollide = pixelCollision(birdRect, ustborukenar, pHitMask, uHitmask)
            lCollide = pixelCollision(birdRect, altborukenar, pHitMask, lHitmask)

            if uCollide or lCollide:
                return [True, False]

    return [False, False]

if __name__ == '__main__':
    main()
