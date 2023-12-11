import pygame
pygame.init()


SCREEN_WIDTH = 1344
SCREEN_HEIGHT = 756
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def rule_screen(lan, rule_page):
    if lan:
        bg = pygame.transform.scale(pygame.image.load('rule' + str(rule_page) + '.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
    else:
        bg = pygame.transform.scale(pygame.image.load('rule' + str(rule_page) + 'vn.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(bg, (0,0))

def change_page(rule_page):
    pass