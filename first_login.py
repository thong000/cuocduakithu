import pygame
import sys
import time
import subprocess

screen = pygame.display.set_mode((1344, 756))

with open('lan.txt', 'r') as file:
    l = file.read()
    if l == "1":
        lan = True
    if l == "0":
        lan = False


class Background:
    def __init__(self, image):
        self.bg_img = image
        self.bg_img = pygame.transform.scale(self.bg_img, (1344, 756))
        self.bg_rect = self.bg_img.get_rect(topleft=(0, 0))

    def draw_bg(self, sur):
        sur.blit(self.bg_img, self.bg_rect)


def check_press(rect, pos):
    if rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            pygame.mixer.init()
            click_music = pygame.mixer.Sound("music/click.mp3")
            click_music.play()
            time.sleep(0.4)
            return True
        else:
            return False


onevn = pygame.image.load("NPC/Vie/20.png")
twovn = pygame.image.load("NPC/Vie/21.png")
threevn = pygame.image.load("NPC/Vie/23.png")
fourvn = pygame.image.load("NPC/Vie/25.png")
fivevn = pygame.image.load("NPC/Vie/27.png")
sixvn = pygame.image.load("NPC/Vie/29.png")
A = [onevn, twovn, threevn, fourvn, fivevn,sixvn]
for i in range(0, 6, 1):
    A[i] = Background(A[i])

one = pygame.image.load("NPC/Eng/19.png")
two = pygame.image.load("NPC/Eng/22.png")
three = pygame.image.load("NPC/Eng/24.png")
four = pygame.image.load("NPC/Eng/26.png")
five = pygame.image.load("NPC/Eng/28.png")
six = pygame.image.load("NPC/Eng/30.png")
B = [one, two, three, four, five,six]
for j in range(0, 6, 1):
    B[j] = Background(B[j])


def first_login_screen(lan, i, screen):
    if lan:
        B[i].draw_bg(screen)
    else:
        A[i].draw_bg(screen)


i = 0
clock = pygame.time.Clock()
while True:
    pos = pygame.mouse.get_pos()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    first_login_screen(not lan, i, screen)
    if check_press(pygame.rect.Rect(0, 0, 1344, 756), pos):
        i += 1
        if i == 6:
            subprocess.run(["python", "gamegoc.py"])

    pygame.display.update()
    clock.tick(60)
