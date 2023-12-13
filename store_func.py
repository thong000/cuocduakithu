import time

import pygame
import sys
pygame.init()
pygame.mixer.init()
global mouse_pos
click_music = pygame.mixer.Sound("music/click.mp3")
muado=pygame.mixer.Sound("music/mua do.mp3")


class Button:
    def __init__(self, image, x, y, w, h):
        self.but_pos = (x, y)
        image = pygame.transform.scale(image, (w, h))
        self.image = image
        self.image.set_colorkey((246, 246, 246))
        self.image_rect = self.image.get_rect(center=(x, y))

    def draw_but(self, sur):
        sur.blit(self.image, self.image_rect)


def check_press(rect, pos):
    if rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:

            time.sleep(0.1)
            return True
        else:
            return False


def check_hover(rect, pos):
    if rect.collidepoint(pos):
        return True
    else:
        return False


class Text:
    def __init__(self, font, text, r, g, b, ):
        self.font = font
        self.text = text
        self.font_but = self.font.render(text, True, (r, g, b))

    def draw_text(self, sur, x, y):
        sur.blit(self.font_but, (x, y))


class Store:
    def __init__(self, lan, wnd_width, wnd_height):
        if lan:
            lang = "eng"
        else:
            lang = "vn"

        link = "store/" + str(lang);
        self.potion1_img = pygame.image.load("extra_stuff/store/10%.png")
        self.potion2_img = pygame.image.load("extra_stuff/store/20%.png")
        self.potion3_img = pygame.image.load("extra_stuff/store/30%.png")
        self.p1_desc_img = pygame.image.load("extra_stuff/" + link + "/desc10.png")
        self.p2_desc_img = pygame.image.load("extra_stuff/" + link + "/desc20.png")
        self.p3_desc_img = pygame.image.load("extra_stuff/" + link + "/desc30.png")
        self.shop_bg_img = pygame.image.load("extra_stuff/" + link + "/shop.png")
        self.buy_img = pygame.image.load("extra_stuff/store/buy.png")
        self.close_img = pygame.image.load("extra_stuff/store/close.png")

        self.p1_desc_img.set_colorkey((246, 246, 246))
        self.p2_desc_img.set_colorkey((246, 246, 246))
        self.p3_desc_img.set_colorkey((246, 246, 246))

        self.potion1 = Button(self.potion1_img, wnd_width // 7 * 2, wnd_height // 16 * 3, wnd_width // 15,
                              wnd_height // 5)
        self.potion2 = Button(self.potion2_img, wnd_width // 7 * 2, wnd_height // 32 * 15, wnd_width // 15,
                              wnd_height // 5)
        self.potion3 = Button(self.potion3_img, wnd_width // 7 * 2, wnd_height // 16 * 12, wnd_width // 15,
                              wnd_height // 5)
        self.close = Button(self.close_img, wnd_width // 20 * 19, wnd_height // 20 * 1, wnd_width // 192 * 10,
                            wnd_height // 108 * 10)
        self.buy = Button(self.buy_img, wnd_width // 7 * 2, wnd_height // 16 * 15, wnd_width // 17, wnd_height // 17)
        self.p1_desc = Button(self.p1_desc_img, wnd_width // 32 * 19, wnd_height // 14 * 9, wnd_width // 4,
                              wnd_height // 16 * 7)
        self.p2_desc = Button(self.p2_desc_img, wnd_width // 32 * 19, wnd_height // 14 * 9, wnd_width // 4,
                              wnd_height // 16 * 7)
        self.p3_desc = Button(self.p3_desc_img, wnd_width // 32 * 19, wnd_height // 14 * 9, wnd_width // 4,
                              wnd_height // 16 * 7)

        self.shop_bg_img = pygame.transform.scale(self.shop_bg_img, (wnd_width, wnd_height))

        self.buy1 = True
        self.buy2 = True
        self.buy3 = True

    def running(self, surface, money, wnd_width, wnd_height):

        k1 = k2 = k3 = 0
        run = True
        buff = 1.0

        while run:
            mouse_pos = pygame.mouse.get_pos()
            surface.blit(self.shop_bg_img, (0, 0))
            self.buy.draw_but(surface)
            self.close.draw_but(surface)

            money_text = Text(pygame.font.SysFont('comicsans', 40), str(money), 255, 255, 255)
            money_text.draw_text(surface, wnd_width // 2, wnd_height // 32 * 29)

            if self.buy1:
                self.potion1.draw_but(surface)
            if self.buy2:
                self.potion2.draw_but(surface)
            if self.buy3:
                self.potion3.draw_but(surface)

            if check_press(self.potion1.image_rect, mouse_pos):

                click_music.play()
                k1 = 1
                k2 = k3 = 0
            elif check_press(self.potion2.image_rect, mouse_pos):
                click_music.play()
                k2 = 1
                k1 = k3 = 0
            elif check_press(self.potion3.image_rect, mouse_pos):
                click_music.play()
                k3 = 1
                k1 = k2 = 0
            # else: k1 = k2 = k3 = 0

            if k1:
                self.p1_desc.draw_but(surface)
                pygame.draw.rect(surface, (155, 0, 0), self.potion1.image_rect, 3)
            elif k2:
                self.p2_desc.draw_but(surface)
                pygame.draw.rect(surface, (155, 0, 0), self.potion2.image_rect, 3)
            elif k3:
                self.p3_desc.draw_but(surface)
                pygame.draw.rect(surface, (155, 0, 0), self.potion3.image_rect, 3)

            if check_press(self.buy.image_rect, mouse_pos):

                if k1 and self.buy1 and int(money) >= 20:
                    self.buy1 = False
                    money -= 20
                    buff += 0.1
                elif k2 and self.buy2 and int(money) >= 35:
                    self.buy2 = False
                    money -= 35
                    buff += 0.2
                elif k3 and self.buy3 and int(money) >= 45:
                    self.buy3 = False
                    money -= 45
                    buff += 0.3
                muado.play()

            if check_press(self.close.image_rect, mouse_pos):
                click_music.play()
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

        return buff, money
