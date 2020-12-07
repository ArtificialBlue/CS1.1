from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN, BIGCHUNGUS, CROUND, KROUND, CROWNEDCHUNGUS
import pygame

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True
    
    def draw(self, win):
        if self.color == (255,0,0):#Red
            win.blit(CROUND, (self.x - CROUND.get_width()//2, self.y - CROUND.get_height()//2))
            if self.king:
                win.blit(KROUND, (self.x - KROUND.get_width()//2, self.y - KROUND.get_height()//2))
        else: #White
            win.blit(BIGCHUNGUS, (self.x - BIGCHUNGUS.get_width()//2, self.y - BIGCHUNGUS.get_height()//2))
            if self.king:
                win.blit(CROWNEDCHUNGUS, (self.x - CROWNEDCHUNGUS.get_width()//2, self.y - CROWNEDCHUNGUS.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)