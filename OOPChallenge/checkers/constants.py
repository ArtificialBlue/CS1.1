import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
BIGCHUNGUS = pygame.transform.scale(pygame.image.load('assets/Chungus.png'), (70,70))
CROWNEDCHUNGUS = pygame.transform.scale(pygame.image.load('assets/SwagChungus.png'), (70,70))
CROUND = pygame.transform.scale(pygame.image.load('assets/cRound.png'), (70,70))
KROUND = pygame.transform.scale(pygame.image.load('assets/kRound.png'), (100,100))
