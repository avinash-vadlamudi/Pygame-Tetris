#!/usr/bin/python

import random,sys,time

bw=20
bh=30



class Board():
    def __init__(self):
        self.board=[]
        self._score=0
        self._level=0
        for i in range(bw):
            self.board.append(['*']*bh)
    def checkPiecePos(self,piece,varX=0,varY=0):
        for x in range(4):
            for y in range(4):
                outoflimit=False
                outoflimit = y + piece.y + varY < 0
                if outoflimit or piece.shape[y][x] =='*':
                    continue
                if not ((x+piece.x+varX)>=0 and (x+piece.x+varX)<bw and (y+piece.y+varY)<bh):
                    return False
                if self.board[x+piece.x+varX][y+piece.y+varY]!='*':
                    return False

        return True
    def fillPiecePos(self,piece):
        for x in range(4):
            for y in range(4):
                if piece.shape[y][x]!='*':
                    self.board[x+piece.x][y+piece.y]=piece.color

    def updatescore():
        self._score=0
        self._level=int(self._score/1000)
