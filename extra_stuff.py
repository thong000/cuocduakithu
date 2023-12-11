import pygame
import store_func
import sys

pygame.init()
pygame.font.init()

class Button:
    def __init__(self, image, x, y, w, h):
        self.but_pos = (x, y)
        image = pygame.transform.scale(image, (w, h))
        self.image = image
        self.image_rect = self.image.get_rect(center=(x, y))

    def draw_but(self, sur):
        sur.blit(self.image, self.image_rect)

def check_press(rect, pos):
    if rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            return True
        else:
            return False

money = 50
wnd_width = 1366
wnd_height = 768
global mouse_pos

screen = pygame.display.set_mode((wnd_width, wnd_height))
store_img = pygame.image.load("extra_stuff/store/store.png")
store = Button(store_img, wnd_width // 15 * 13, wnd_height // 10 * 8, wnd_width // 12, wnd_height // 7)
clock = pygame.time.Clock()
race_complete = 1

while True:
    mouse_pos = pygame.mouse.get_pos()
    ''' store.draw_but(screen)'''
    if race_complete:
        new_store = store_func.Store(0, wnd_width, wnd_height)
        race_complete = 0
        buff, money = new_store.running(screen, money, wnd_width, wnd_height)
        screen = pygame.display.set_mode((wnd_width, wnd_height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()