import pygame
import os
import sys

pygame.mixer.init()
with open('lan.txt', 'r') as language:
    l = language.read()
    if l == "1":
        lang = True
    else:
        lang = False


class Button:
    def __init__(self, image, x, y, w, h):
        self.but_pos = (x, y)
        self.x = x
        self.y = y
        image = pygame.transform.scale(image, (w, h))
        self.image = image
        self.image_rect = self.image.get_rect(center=(x, y))

    def draw_but(self, sur):
        sur.blit(self.image, self.image_rect)


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
            return True
        else:
            return False


def after_race(pos1, pos2, pos3, pos4, pos5, chosen_set, sur, wnd_width, wnd_height, result):
    """
    đưa vào số thứ tự của thằng đứng thứ 1 -> 5, set nhân vật được chọn 
    (tao hiện tại để 1, 3, 4, 5(set zombie), cái set 2 ảnh tụi mình chả biết ăn mừng kiểu gì =)), surface, kích cỡ window 
    phần dưới đây là khai báo các ảnh vào chương trình
    """
    if chosen_set != 3:
        off_screen = 0
        main_dir = "after_race/podium_resource/set" + str(chosen_set)
        pos1_dir = main_dir + "/PNG" + str(pos1) + " Sequences/Taunt"
        pos2_dir = main_dir + "/PNG" + str(pos2) + " Sequences/Taunt"
        pos3_dir = main_dir + "/PNG" + str(pos3) + " Sequences/Taunt"
        pos4_dir = main_dir + "/PNG" + str(pos4) + " Sequences/Dying"
        pos5_dir = main_dir + "/PNG" + str(pos5) + " Sequences/Dying"

        list1 = os.listdir(pos1_dir)
        list2 = os.listdir(pos2_dir)
        list3 = os.listdir(pos3_dir)
        list4 = os.listdir(pos4_dir)
        list5 = os.listdir(pos5_dir)

        frame1 = len(list1) - 1
        frame2 = len(list2) - 1
        frame3 = len(list3) - 1
        frame4 = len(list4) - 1
        frame5 = len(list5) - 1

    bg = pygame.image.load("after_race/podium_resource/podium.png")
    bg = pygame.transform.scale(bg, (wnd_width, wnd_height))
    exit_but_image = pygame.image.load("after_race/podium_resource/exit.png")
    exit_but = Button(exit_but_image, 50, 50, 75, 50)
    next_img = pygame.image.load("Button/next.png")
    next_but = Button(next_img, 1200, 720, 100, 50)
    win = pygame.image.load("end/win.png")
    win_but = Button(win, 1344 // 2, 756 // 2, 800, 300)
    lose = pygame.image.load("end/lose.png")
    thang = pygame.image.load("end/thang.png")
    thua = pygame.image.load("end/thua.png")
    lose_but = Button(lose, 1344 // 2, 756 // 2, 800, 300)
    winvn_but = Button(thang, 1344 // 2, 756 // 2, 800, 300)
    losevn_but = Button(thua, 1344 // 2, 756 // 2, 800, 300)

    k1 = k2 = k3 = k4 = k5 = 0

    def drawf(cur_frame, max_frame, list_frame, dirt, x, y, w, h, rotate):  # hàm này để vẽ từng thằng
        cur_frame += 1
        tg = cur_frame
        if chosen_set == 5:  # fix bug của set zombie vs set 1
            w *= 0.5
            h *= 0.5
            max_frame *= 3
            x += wnd_width // 17
            y += wnd_height // 13
            tg = cur_frame // 3
        if chosen_set == 1:
            y -= wnd_height // 20
        if cur_frame > max_frame:
            cur_frame = 0
            tg = 0
        image = pygame.image.load(dirt + "/" + list_frame[tg])
        image = pygame.transform.scale(image, (w, h))
        image = pygame.transform.flip(image, rotate, False)
        sur.blit(image, (x, y))
        return cur_frame

    off_screen = 0

    start_t = pygame.time.get_ticks()
    while True and off_screen == 0:
        cur_time = pygame.time.get_ticks()
        if cur_time - start_t < 1000:
            if result:
                if lang:
                    win_but.draw_but(sur)
                else:
                    winvn_but.draw_but(sur)
            else:
                if lang:
                    lose_but.draw_but(sur)
                else:
                    losevn_but.draw_but(sur)

        else:

            if chosen_set != 3:
                sur.blit(bg, (0, 0))
                mouse_pos = pygame.mouse.get_pos()
                next_but.draw_but(sur)
                if check_press(next_but.image_rect, mouse_pos):
                    off_screen = 22

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                        # vẽ từng thằng ra, mỗi thằng có một cái k riêng check frame hiện tại
                k1 = drawf(k1, frame1, list1, pos1_dir, wnd_width // 36 * 15, wnd_height // 36 * 10,
                           wnd_width // 16 * 3,
                           wnd_height // 3, True)
                k2 = drawf(k2, frame2, list2, pos2_dir, wnd_width // 36 * 10, wnd_height // 24 * 7, wnd_width // 16 * 3,
                           wnd_height // 3, False)
                k3 = drawf(k3, frame3, list3, pos3_dir, wnd_width // 36 * 20, wnd_height // 24 * 7, wnd_width // 16 * 3,
                           wnd_height // 3, True)
                k4 = drawf(k4, frame4, list4, pos4_dir, wnd_width // 5, wnd_height // 3 * 2, wnd_width // 16 * 3,
                           wnd_height // 3, False)
                k5 = drawf(k5, frame5, list5, pos5_dir, wnd_width // 36 * 5, wnd_height // 3 * 2, wnd_width // 16 * 3,
                           wnd_height // 3, False)
            else:
                off_screen = 22

        pygame.display.update()
    return off_screen
