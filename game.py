#!/usr/bin/python
import pygame,sys,time,random
from pygame.locals import *
from class_board import *


WHITE       = (255, 255, 255)
BLACK       = (  0,   0,   0)
GREEN       = (  0, 155,   0)
BLUE        = (  0,   0, 155)
RED         = (155,   0,   0)

COLORS =(BLUE,GREEN,RED,WHITE)

bw=20
bh=30
ww= 720
wh= 640
box_size=18


sidemarg= int((ww-bw*box_size)/2) 
topmarg = wh-bh*box_size-20

bordercol=BLUE
bgcol=BLACK
textcol=WHITE


global FPS,DISPLAY,BASICFONT,BIGFONT

pygame.init()
BIGFONT=pygame.font.Font('freesansbold.ttf',60)
BASICFONT=pygame.font.Font('freesansbold.ttf',18)
DISPLAY=pygame.display.set_mode((ww, wh))
pygame.display.set_caption('Tetris game')



class Block():
    def __init__(self):
        self.subblock=[[]]
        self.count=0
        self.shape=[]
        self.x=int(bw/2)-2
        self.y=-2
        self.color=random.randint(0,len(COLORS)-1)
        self.lastsidetime=time.time()
        self.lastdowntime=time.time()
    def rotate(self):
        self.count=(self.count+1)%len(self.subblock)
        self.shape=self.subblock[self.count]
    def moveLeft(self):
        self.x=self.x-1
        self.lastsidetime=time.time()
    def moveRight(self):
        self.x=self.x+1
        self.lastsidetime=time.time()
    def draw(self,pix_x=None,pix_y=None):
        shapeToDraw=self.shape
        if pix_x==None and pix_y==None:
            pix_x=sidemarg+(self.x*box_size)
            pix_y=topmarg+(self.y*box_size)

        for x in range(4):
            for y in range(4):
                if shapeToDraw[y][x]!='*':
                    pygame.draw.rect(DISPLAY,COLORS[self.color],(pix_x+(x*box_size)+1, pix_y+ (y*box_size) + 1,box_size-1,box_size-1))


    def drawNextPiece(self):
        surf=BASICFONT.render('Next:',True,textcol)
        rect=surf.get_rect()
        rect.topleft=(ww-80,80)
        DISPLAY.blit(surf,rect)
        self.draw(pix_x=ww-120,pix_y=100)


class block1(Block):
    def __init__(self):
        Block.__init__(self)
        self.subblock=[['****',
                        '0000',
                        '****',
                        '****'],
                        ['**0*',
                            '**0*',
                            '**0*',
                            '**0*']]
        self.count=random.randint(0,len(self.subblock)-1)
        self.shape=self.subblock[self.count]
class block2(Block):
    def __init__(self):
        Block.__init__(self)
        self.subblock=[['****',
                        '*00*',
                        '00**',
                        '****'],
                        ['*0**',
                            '*00*',
                            '**0*',
                            '****']]

        self.count=random.randint(0,len(self.subblock)-1)
        self.shape=self.subblock[self.count]
class block3(Block):
    def __init__(self):
        Block.__init__(self)
        self.subblock=[['****',
                        '*00*',
                        '**00',
                        '****'],
                        ['**0*',
                            '*00*',
                            '*0**',
                            '****']]
        self.count=random.randint(0,len(self.subblock)-1)
        self.shape=self.subblock[self.count]
                        
                        
class block4(Block):
    def __init__(self):
        Block.__init__(self)
        self.subblock=[['****',
                        '*00*',
                        '*00*',
                        '****']]
        self.count=random.randint(0,len(self.subblock)-1)
        self.shape=self.subblock[self.count]

class block5(Block):
    def __init__(self):
        Block.__init__(self)
        self.subblock=[['****',
                        '*0**',
                        '*0**',
                        '*00*'],
                        ['****',
                            '*000',
                            '*0**',
                            '****'],
                        ['****',
                            '*00*',
                            '**0*',
                            '**0*'],
                        ['****',
                            '***0',
                            '*000',
                            '****']]
        self.count=random.randint(0,len(self.subblock)-1)
        self.shape=self.subblock[self.count]

class block6(Block):
    def __init__(self):
        Block.__init__(self)
        self.subblock=[['****',
                        '**0*',
                        '**0*',
                        '*00*'],
                        ['****',
                            '0***',
                            '000*',
                            '****'],
                        ['00**',
                            '0***',
                            '0***',
                            '****'],
                        ['****',
                            '*000',
                            '***0',
                            '****']]
        self.count=random.randint(0,len(self.subblock)-1)
        self.shape=self.subblock[self.count]


FPS=pygame.time.Clock()

class Gameplay(Block,Board):
    def __init__(self):
        Board.__init__(self)
        Block.__init__(self)
        self.fallfreq=0.3-(self._level*0.02)
    def draw(self):
        pygame.draw.rect(DISPLAY,bordercol,(sidemarg-3,topmarg-5,(bw*box_size)+6,(bh*box_size)+6),4)

        pygame.draw.rect(DISPLAY,bgcol,(sidemarg,topmarg,box_size*bw,bh*box_size))
        
        for x in range(bw):
            for y in range(bh):
                if(self.board[x][y]=='*'):
                    continue
                _pix_x=sidemarg+(x*box_size)
                _pix_y=topmarg+(y*box_size)
                pygame.draw.rect(DISPLAY,COLORS[self.board[x][y]],(_pix_x+1,_pix_y+1,box_size-1,box_size-1))


    def checkRowFull(self,y):
        for x in range(bw):
            if self.board[x][y]=='*':
                return False
        return True
    def checkRowEmpty(self):
        for x in range(bw):
            if self.board[x][y]!='*':
                return False
        return True
    def updateScore(self):
        value=self.removerows()
        self._score=self._score+(value*100)+20
        self._level=int((self._score)/1000)
        self.fallfreq=0.3-(self._level*0.02)

    def selectPiece(self):
        val=random.randint(1,6)
        if(val==1):
            pie=block1()
            return pie
        elif(val==2):
            pie=block2()
            return pie
        elif(val==3):
            pie=block3()
            return pie
        elif(val==4):
            pie=block4()
            return pie
        elif(val==5):
            pie=block5()
            return pie
        elif(val==6):
            pie=block6()
            return pie
        
    def removerows(self):
        __number=0
        y=bh-1
        while y>=0:
            if self.checkRowFull(y):
                for var in range(y,0,-1):
                    for x in range(bw):
                       self.board[x][var]=self.board[x][var-1]
                for x in range(bw):
                    self.board[x][0]='*'
                __number+=1
            else:
                y=y-1
        return __number

    
    def draw_score(self):
        # draw the score text
        surface = BASICFONT.render('Score: %s' % self._score, True, textcol)
        rect = surface.get_rect()
        rect.topleft = (ww - 130, 20)
        DISPLAY.blit(surface, rect)

        surface2 = BASICFONT.render('Level: %s' % self._level, True, textcol)
        rect2 = surface2.get_rect()
        rect2.topleft = (ww - 130, 50)
        DISPLAY.blit(surface2, rect2)


def startgame():
    game=Gameplay()
    piece=game.selectPiece()
    nextpiece=game.selectPiece()
    lastfall=time.time()
    moveleftside=False
    moverightside=False
    movedown=False
    while True:
        if piece == None:

            piece=nextpiece

            nextpiece=game.selectPiece()

            lastfall=time.time()
            if not game.checkPiecePos(piece):
                return
        checkingforexit()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if(event.key == K_LEFT or event.key == K_a ):
                    if(game.checkPiecePos(piece,varX=-1)):
                        piece.moveLeft()
                        piece.lastsidetime=time.time()
                        moveleftside=True
                elif(event.key==K_DOWN):
                    if(game.checkPiecePos(piece,varY=1)):
                        piece.y=piece.y+1
                        piece.lastdowntime=time.time()
                        movedown=True
                elif(event.key ==K_RIGHT or event.key == K_d):
                    if(game.checkPiecePos(piece,varX=1)):
                        piece.moveRight()
                        piece.lastsidetime=time.time()
                        moverightside=True
                elif(event.key==K_SPACE):
                    moveleftside=False
                    moverightside=False
                    movedown=False
                    for i in range(1,bh):
                        if(game.checkPiecePos(piece,varY=i)==False):
                            break
                    piece.y=piece.y+i-1
                elif(event.key==K_s or event.key==K_UP):
                    piece.rotate()
                    if not game.checkPiecePos(piece):
                        piece.count=(piece.count-1)%len(piece.subblock)
                        piece.shape=piece.subblock[piece.count]
            if event.type == KEYUP:
                if(event.key==K_p):
                    DISPLAYSURF.fill(bgcol)
                    displaytext('PAUSED')
                    piece.lastsidetime=time.time()
                    piece.lastdowntime=time.time()
                    lastfall=time.time()
                elif ( event.key==K_a or event.key==K_LEFT):
                    moveleftside=False
                elif ( event.key==K_d or event.key==K_RIGHT):
                    moverightside=False
                elif(event.key==K_DOWN):
                    movedown=False
        if (moveleftside or moverightside) and time.time()-piece.lastsidetime > 0.15: 
            if moveleftside and game.checkPiecePos(piece,varX=-1):
                piece.x=piece.x-1
            elif moverightside and game.checkPiecePos(piece,varX=1):
                piece.x=piece.x+1
            piece.lastsidetime=time.time()
        if movedown and time.time()-piece.lastdowntime > 0.1 and game.checkPiecePos(piece,varY=1):
            piece.y=piece.y+1
            piece.lastdowntime=time.time()
        if time.time()-lastfall > game.fallfreq:
            if game.checkPiecePos(piece,varY=1)==False:
                game.fillPiecePos(piece)
                game.updateScore()
                piece=None
            else:
                piece.y=piece.y+1
                lastfall=time.time()
        DISPLAY.fill(bgcol)
        game.draw()
        game.draw_score()
        nextpiece.drawNextPiece()
        if piece!=None:
            piece.draw()
        pygame.display.update()
        FPS.tick(30)


def checkingforexit():
    for event in pygame.event.get(QUIT):
        pygame.quit()
        sys.exit()
    for event in pygame.event.get(KEYUP):
        if event.key==K_ESCAPE:
            pygame.quit()
            sys.exit()
        pygame.event.post(event)


def checkingkeyinterupt():
    checkingforexit()
    for event in pygame.event.get([KEYDOWN,KEYUP]):
        if event.type == KEYUP:
            return event.key
        else:
            continue
    return None
def displaytext(text):
    t_surf=BIGFONT.render(text,True,textcol)
    t_rect=t_surf.get_rect()
    t_rect.center=(int(ww/2),int(wh/2))
    DISPLAY.blit(t_surf,t_rect)
    p_surf=BASICFONT.render('PRESS ANY KEY TO PLAY.',True,textcol)
    p_rect=p_surf.get_rect()
    p_rect.center=(int(ww/2),int(wh/2)+100)
    DISPLAY.blit(p_surf,p_rect)
    while(checkingkeyinterupt()==None):
            pygame.display.update()
            FPS.tick()


displaytext('TETRIS')
while True:
    startgame()
    displaytext('GameOver')



    
