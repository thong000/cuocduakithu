import pygame
import random
import subprocess
import sys
import time
import Fruit_ninja

pygame.init()

# Mở file lan để xác định ngôn ngữ
with open('lan.txt', 'r') as file:
    l = file.read()
    if l == "1":
        lan = True
    if l == "0":
        lan = False

# mở file log dể biết tình trạng đăng nhập
with open('log.txt', 'r') as file:
    content = file.read()
    if content == "1":
        lock = True
    if content == "0":
        lock = False

# Thông số cơ bản

coin = 0
speed = 5

SCREEN_WIDTH = 1344
SCREEN_HEIGHT = 756

set_but_dis = SCREEN_WIDTH // 10
set_but_x = SCREEN_WIDTH // 10
set_but_y = SCREEN_HEIGHT // 5

exit_but_x = SCREEN_WIDTH // 40
exit_but_y = SCREEN_HEIGHT // 25
exit_w = SCREEN_WIDTH // 20
exit_h = SCREEN_HEIGHT // 10

choose_map_x = SCREEN_WIDTH // 2.5
choose_map_y = SCREEN_HEIGHT // 50

demomap_x = SCREEN_WIDTH * 2 // 3.2
demomap_y = SCREEN_HEIGHT // 2
demomap_w = SCREEN_WIDTH // 1.5
demomap_h = SCREEN_HEIGHT // 1.5

finish = SCREEN_WIDTH // 1.2

random_x1 = random.randrange(SCREEN_WIDTH // 3, SCREEN_WIDTH // 2)
random_x2 = random.randrange(SCREEN_WIDTH // 3, SCREEN_WIDTH // 2)
random_x3 = random.randrange(SCREEN_WIDTH // 3, SCREEN_WIDTH // 2)
random_x4 = random.randrange(SCREEN_WIDTH // 3, SCREEN_WIDTH // 2)
random_x5 = random.randrange(SCREEN_WIDTH // 3, SCREEN_WIDTH // 2)

# biến ngôn ngữ
lan = True

# Khởi tạo các biến logic để biết màn hình nào đang chạy (một lúc có 1)
set_ = True
wait = False
set1 = False
set2 = False
set3 = False
setting_bool = False
lang = False
start_bool = False
minigame_bool = False
rule_bool = False
choosenv_bool1 = False
choosenv_bool2 = False
setnv11 = False
setnv21 = False
setnv12 = False
setnv22 = False
flap = False

import pygame, random, sys

pygame.init()


class Fruit_ninja:

    def __init__(self):

        self.game_font = pygame.font.Font('Chem_chuoi/Roboto-Black.ttf', 50)
        self.game_font2 = pygame.font.Font('Chem_chuoi/Roboto-Black.ttf', 100)

        self.bg = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/bg.png'), (1300, 768))

        self.game_active = True

        # trai cay
        self.watermelon = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/watermelon2.png'), (170, 170))
        self.strawberry = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/strawberry_2.png'), (70, 70))
        self.pear = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/pear_2.png'), (100, 100))
        self.apple = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/app.png'), (120, 120))
        self.bomb = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/bomb.png'), (100, 100))

        self.fruit_list = [self.watermelon, self.strawberry, self.pear, self.bomb, self.apple, self.bomb]
        self.fruit_high = [50, 100, 150, 200]
        self.fruits = []
        self.fruits_rect = []
        self.fruits_fall = []
        self.fruits_direction = []
        self.fruits_active = []
        self.fruits_rotate = []
        self.fruits_limit = []

        # tao timer
        self.spawn_fruit = pygame.USEREVENT
        pygame.time.set_timer(self.spawn_fruit, 1000)

        # tao score
        self.score = 0
        self.high_score = 0

        self.player_heart = 3

        self.check_change_screen = False

        # nut exit
        self.exit_button = pygame.font.Font('Chem_chuoi/Roboto-Black.ttf', 60).render('EXIT', True, (255, 255, 255))
        self.exit_button_rect = self.exit_button.get_rect(topleft=(1100, 700))

        # tao vet nuoc
        self.scrath_red = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/red.png'), (170, 170))
        self.scrath_pink = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/pink.png'), (150, 150))
        self.scrath_da = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/da.png'), (150, 150))
        self.scrath_green = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/xanh.png'), (150, 150))
        self.scrath_boom = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/boom.png'), (150, 150))
        self.list_scrath = []
        self.scrath_timer = []
        self.scrath_rect = []

        self.limit_money = 10

    def create_fruit(self):
        pos_x = random.random()
        pos_x *= 10000
        pos_x = int(pos_x)
        pos_x %= 1100
        pos_x += 100
        fruit = random.choice(self.fruit_list)
        fruit_rect = fruit.get_rect(center=(pos_x, 800))
        self.fruits.append(fruit)
        self.fruits_rect.append(fruit_rect)
        self.fruits_fall.append(1)
        if pos_x > 650:
            self.fruits_direction.append(-3)
        else:
            self.fruits_direction.append(3)
        self.fruits_active.append(True)
        self.fruits_rotate.append(0)
        self.fruits_limit.append(random.choice(self.fruit_high))

    def draw_fruit(self, screen):
        for i in range(1, len(self.fruits)):
            if self.fruits_active[i]:
                screen.blit(self.rotate_fruit(i), self.fruits_rect[i])

    def rotate_fruit(self, i):
        new_fruit = pygame.transform.rotozoom(self.fruits[i], -3 * self.fruits_rotate[i], 1)
        return new_fruit

    def update(self):
        for i in range(1, len(self.fruits_rect)):
            self.fruits_rect[i].centery -= 10 * self.fruits_fall[i]
            if self.fruits_rect[i].centery <= self.fruits_limit[i]:
                self.fruits_fall[i] = -1
            self.fruits_rect[i].centerx += self.fruits_direction[i]
            self.fruits_rotate[i] += 1

    def game_over(self, screen):
        lose = self.game_font2.render('GAME OVER!', True, (255, 255, 255))
        lose_rect = lose.get_rect(center=(650, 384))
        screen.blit(lose, lose_rect)

    def draw_score(self, screen, money):
        if self.game_active:
            score_surface = self.game_font.render(str(self.score), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(280, 50))
            screen.blit(score_surface, score_rect)

            score_surface_1 = self.game_font.render('Score :', True, (255, 255, 255))
            score_rect.center = (100, 50)
            screen.blit(score_surface_1, score_rect)

            score_surface = self.game_font.render(str(self.player_heart), True, (255, 255, 255))
            score_rect.center = (430, 100)
            screen.blit(score_surface, score_rect)

            score_surface_1 = self.game_font.render('Player hearts: ', True, (255, 255, 255))
            score_rect.center = (100, 100)
            screen.blit(score_surface_1, score_rect)
        else:
            score_surface = self.game_font.render(str(self.high_score), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(380, 50))
            screen.blit(score_surface, score_rect)

            score_surface_1 = self.game_font.render('High score :', True, (255, 255, 255))
            score_rect.center = (100, 50)
            screen.blit(score_surface_1, score_rect)

        money_surface = self.game_font.render(str(money), True, (255, 255, 255))
        score_rect.center = (100, 150)
        screen.blit(money_surface, score_rect)

    def draw_scrath(self, screen):
        for i in range(len(self.list_scrath)):
            if self.scrath_timer[i] <= 10:
                screen.blit(self.list_scrath[i], self.scrath_rect[i])
                self.scrath_timer[i] += 1

    def choose_scrath(self, i):
        if self.fruits[i] == self.watermelon:
            self.list_scrath.append(self.scrath_red)
        elif self.fruits[i] == self.apple:
            self.list_scrath.append(self.scrath_da)
        elif self.fruits[i] == self.strawberry:
            self.list_scrath.append(self.scrath_pink)
        elif self.fruits[i] == self.pear:
            self.list_scrath.append(self.scrath_green)
        elif self.fruits[i] == self.bomb:
            self.list_scrath.append(self.scrath_boom)

    def fruit_ninja_game_play(self, screen, money):
        clock = pygame.time.Clock()
        clock.tick(120)
        screen = pygame.display.set_mode((1300, 768))
        out_game = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == self.spawn_fruit:
                    self.create_fruit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for i in range(0, len(self.fruits)):
                        if self.fruits_rect[i].collidepoint(pos) and self.fruits_active[i] == True:
                            if self.fruits[i] != self.bomb:
                                self.fruits_active[i] = False
                                self.score += 1
                            else:
                                self.player_heart -= 1
                                self.fruits_active[i] = False
                            self.choose_scrath(i)
                            self.scrath_rect.append(self.scrath_red.get_rect(center=pos))
                            self.scrath_timer.append(1)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.game_active == False:
                        self.game_active = True
                        self.player_heart = 3
                        self.score = 0
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.exit_button_rect.collidepoint(pos):
                        self.exit_game(screen)
                        out_game = True

            if out_game:
                break

            screen.blit(self.bg, (0, 0))

            if self.game_active:

                self.update()

                self.draw_fruit(screen)

                for i in range(0, len(self.fruits)):
                    if self.fruits_active[i] == True and self.fruits_rect[i].centery >= 768 and self.fruits_fall[
                        i] < 0 and self.fruits[i] != self.bomb:
                        self.player_heart -= 1
                        self.fruits_active[i] = False

                if self.player_heart == 0:
                    self.game_active = False
                    self.high_score = max(self.high_score, self.score)
                    if self.limit_money > 0:
                        money += min(self.limit_money, self.score)
                    self.limit_money -= self.score
                    self.score = 0
            else:
                self.game_over(screen)
                self.fruits = []
                self.fruits_rect = []
                self.fruits_fall = []
                self.fruits_direction = []
                self.fruits_active = []
                self.fruits_rotate = []
                self.fruits_limit = []

            self.draw_score(screen, money)
            self.draw_scrath(screen)

            screen.blit(self.exit_button, self.exit_button_rect)
            pygame.display.update()
        return money

    def exit_game(self, screen):
        global fruit_game
        screen = pygame.display.set_mode((1400, 800))
        fruit_game = False


fruit=Fruit_ninja()
# thiết lập màn hình
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cuộc đua kì thú")
pygame.display.set_icon(pygame.image.load("SPEED RACE.png"))

# vị trí của nhân vật và các chỉ số chạy mảng
w11_x = 0
w12_x = 0
w13_x = 0
w14_x = 0
w15_x = 0
wi11 = 0
wi12 = 0
wi13 = 0
wi14 = 0
wi15 = 0

# random tốc độ nhân vật
x1 = random.uniform(0.8, 1.2)
x2 = random.uniform(0.8, 1.2)
x3 = random.uniform(0.8, 1.2)
x4 = random.uniform(0.8, 1.2)
x5 = random.uniform(0.8, 1.2)

# font chữ ở nhiều kích thước khác nhau
game_font1 = pygame.font.Font("font/DVN-Fredoka-Bold.ttf", 40)
game_font2 = pygame.font.Font("font/DVN-Fredoka-Bold.ttf", 25)
game_font3 = pygame.font.Font("font/DVN-Fredoka-Bold.ttf", 70)
game_font4 = pygame.font.Font("font/DVN-Fredoka-Bold.ttf", 80)
game_font_mini = pygame.font.Font("font/DVN-Fredoka-Bold.ttf", 10)

# Các Class

'''Background full màn hình'''


class Background:
    def __init__(self, image):
        self.bg_img = image
        self.bg_img = pygame.transform.scale(self.bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bg_rect = self.bg_img.get_rect(topleft=(0, 0))

    def draw_bg(self, sur):
        sur.blit(self.bg_img, self.bg_rect)


'''Button có chiều dài w, chiều rộng h, trung tâm của ảnh có tọa độ (x,y)'''


class Button:
    def __init__(self, image, x, y, w, h):
        self.but_pos = (x, y)
        self.x = x
        self.y = y
        image = pygame.transform.scale(image, (w, h))
        self.image = image
        self.image_rect = self.image.get_rect(center=(x, y))

    '''Ve hinh ở (x,y)'''

    def draw_but(self, sur):
        sur.blit(self.image, self.image_rect)


'''một đoạn text có font là "font" nội dung là "text" có màu (r,g,b)'''


class Text:
    def __init__(self, font, text, r, g, b, ):
        self.font = font
        self.text = text
        self.font_but = self.font.render(text, True, (r, g, b))

    '''Ve hinh ở (x,y)'''

    def draw_text(self, sur, x, y):
        sur.blit(self.font_but, (x, y))


'''Tao nhan vat'''


class nhanVat:
    def __init__(self, name, img_array, x, y, w, h):
        self.name = name
        self.img_array = img_array
        self.x = x
        self.y = y
        self.name = Button(img_array, x, y, w, h)

    def draw_nv(self):
        self.name.draw_but(screen)

    '''check va cham voi "sur" (box,vạch đích,...)'''

    def check_vc(self, sur):
        if self.name.image_rect.colliderect(sur.image_rect):
            return True
        else:
            return False

    '''Cac hieu ứng khi chạm box'''

    def buff_speed(self, i):
        bonus1 = random.randrange(1, 100)
        bonus2 = random.randrange(1, 100)
        bonus3 = random.randrange(1, 100)
        bonus4 = random.randrange(1, 100)
        bonus5 = random.randrange(1, 100)

        bonus_tuple = (bonus1, bonus2, bonus3, bonus4, bonus5)
        if 1 <= bonus_tuple[i] <= 50:
            return 2
        if 50 <= bonus_tuple[i] <= 100:
            return 1.2


'''Load set 1(cho map1)'''
w11_name = ["w110", "w111", "w112", "w113", "w114", "w115", "w116", "w117", "w118", "w119", "w1110", "w1111", "w1112",
            "w1113", "w1114", "w1115", "w1116", "w1117", ]
w11_loca = ["set01\PNG1 Sequences\Walking\w110.png",
            "set01\PNG1 Sequences\Walking\w111.png",
            "set01\PNG1 Sequences\Walking\w112.png",
            "set01\PNG1 Sequences\Walking\w113.png",
            "set01\PNG1 Sequences\Walking\w114.png",
            "set01\PNG1 Sequences\Walking\w115.png",
            "set01\PNG1 Sequences\Walking\w116.png",
            "set01\PNG1 Sequences\Walking\w117.png",
            "set01\PNG1 Sequences\Walking\w118.png",
            "set01\PNG1 Sequences\Walking\w119.png",
            "set01\PNG1 Sequences\Walking\w1110.png",
            "set01\PNG1 Sequences\Walking\w1111.png",
            "set01\PNG1 Sequences\Walking\w1112.png",
            "set01\PNG1 Sequences\Walking\w1113.png",
            "set01\PNG1 Sequences\Walking\w1114.png",
            "set01\PNG1 Sequences\Walking\w1115.png",
            "set01\PNG1 Sequences\Walking\w1116.png",
            "set01\PNG1 Sequences\Walking\w1117.png"]
for i in range(0, 18):
    w11_name[i] = pygame.image.load(w11_loca[i])
for i in range(0, 18):
    w11_name[i] = pygame.transform.scale(w11_name[i], (1400, 1400))

# Load nv set1 2
w12_name = ["w120", "w121", "w122", "w123", "w124", "w125", "w126", "w127", "w128", "w129", "w1210", "w1211", "w1212",
            "w1213", "w1214", "w1215", "w1216", "w1217", ]
w12_loca = ["set01\PNG2 Sequences\Walking\w120.png",
            "set01\PNG2 Sequences\Walking\w121.png",
            "set01\PNG2 Sequences\Walking\w122.png",
            "set01\PNG2 Sequences\Walking\w123.png",
            "set01\PNG2 Sequences\Walking\w124.png",
            "set01\PNG2 Sequences\Walking\w125.png",
            "set01\PNG2 Sequences\Walking\w126.png",
            "set01\PNG2 Sequences\Walking\w127.png",
            "set01\PNG2 Sequences\Walking\w128.png",
            "set01\PNG2 Sequences\Walking\w129.png",
            "set01\PNG2 Sequences\Walking\w1210.png",
            "set01\PNG2 Sequences\Walking\w1211.png",
            "set01\PNG2 Sequences\Walking\w1212.png",
            "set01\PNG2 Sequences\Walking\w1213.png",
            "set01\PNG2 Sequences\Walking\w1214.png",
            "set01\PNG2 Sequences\Walking\w1215.png",
            "set01\PNG2 Sequences\Walking\w1216.png",
            "set01\PNG2 Sequences\Walking\w1217.png"]
for i in range(0, 18):
    w12_name[i] = pygame.image.load(w12_loca[i])
    w12_name[i] = pygame.transform.scale(w12_name[i], (140, 140))

# Load nv set1 3
w13_name = ["w130", "w131", "w132", "w133", "w134", "w135", "w136", "w137", "w138", "w139", "w1310", "w1311", "w1312",
            "w1313", "w1314", "w315", "w1316", "w1317", ]
w13_loca = ["set01\PNG3 Sequences\Walking\w130.png",
            "set01\PNG3 Sequences\Walking\w131.png",
            "set01\PNG3 Sequences\Walking\w132.png",
            'set01\PNG3 Sequences\Walking\w133.png',
            "set01\PNG3 Sequences\Walking\w134.png",
            "set01\PNG3 Sequences\Walking\w135.png",
            "set01\PNG3 Sequences\Walking\w136.png",
            "set01\PNG3 Sequences\Walking\w137.png",
            "set01\PNG3 Sequences\Walking\w138.png",
            "set01\PNG3 Sequences\Walking\w139.png",
            "set01\PNG3 Sequences\Walking\w1310.png",
            "set01\PNG3 Sequences\Walking\w1311.png",
            "set01\PNG3 Sequences\Walking\w1312.png",
            "set01\PNG3 Sequences\Walking\w1313.png",
            "set01\PNG3 Sequences\Walking\w1314.png",
            "set01\PNG3 Sequences\Walking\w1315.png",
            "set01\PNG3 Sequences\Walking\w1316.png",
            "set01\PNG3 Sequences\Walking\w1317.png"]
for i in range(0, 18):
    w13_name[i] = pygame.image.load(w13_loca[i])
    w13_name[i] = pygame.transform.scale(w13_name[i], (140, 140))

w14_name = ["w140", "w141", "w142", "w143", "w144", "w145", "w146", "w147", "w148", "w149", "w1410", "w1411", "w1412",
            "w1413", "w1414", "w1415", "w1416", "w1417", ]
w14_loca = ["set01\PNG4 Sequences\Walking\w140.png",
            "set01\PNG4 Sequences\Walking\w141.png",
            "set01\PNG4 Sequences\Walking\w142.png",
            "set01\PNG4 Sequences\Walking\w143.png",
            "set01\PNG4 Sequences\Walking\w144.png",
            "set01\PNG4 Sequences\Walking\w145.png",
            "set01\PNG4 Sequences\Walking\w146.png",
            "set01\PNG4 Sequences\Walking\w147.png",
            "set01\PNG4 Sequences\Walking\w148.png",
            "set01\PNG4 Sequences\Walking\w149.png",
            "set01\PNG4 Sequences\Walking\w1410.png",
            "set01\PNG4 Sequences\Walking\w1411.png",
            "set01\PNG4 Sequences\Walking\w1412.png",
            "set01\PNG4 Sequences\Walking\w1413.png",
            "set01\PNG4 Sequences\Walking\w1414.png",
            "set01\PNG4 Sequences\Walking\w1415.png",
            "set01\PNG4 Sequences\Walking\w1416.png",
            "set01\PNG4 Sequences\Walking\w1417.png"]
for i in range(0, 18):
    w14_name[i] = pygame.image.load(w14_loca[i])
    w14_name[i] = pygame.transform.scale(w14_name[i], (140, 140))

w15_name = ["w150", "w151", "w152", "w153", "w154", "w155", "w156", "w157", "w158", "w159", "w1510", "w1511", "w1512",
            "w1513", "w1514", "w1515", "w1516", "w1517", ]
w15_loca = ["set01\PNG5 Sequences\Walking\w150.png",
            "set01\PNG5 Sequences\Walking\w151.png",
            "set01\PNG5 Sequences\Walking\w152.png",
            "set01\PNG5 Sequences\Walking\w153.png",
            "set01\PNG5 Sequences\Walking\w154.png",
            "set01\PNG5 Sequences\Walking\w155.png",
            "set01\PNG5 Sequences\Walking\w156.png",
            "set01\PNG5 Sequences\Walking\w157.png",
            "set01\PNG5 Sequences\Walking\w158.png",
            "set01\PNG5 Sequences\Walking\w159.png",
            "set01\PNG5 Sequences\Walking\w1510.png",
            "set01\PNG5 Sequences\Walking\w1511.png",
            "set01\PNG5 Sequences\Walking\w1512.png",
            "set01\PNG5 Sequences\Walking\w1513.png",
            "set01\PNG5 Sequences\Walking\w1514.png",
            "set01\PNG5 Sequences\Walking\w1515.png",
            "set01\PNG5 Sequences\Walking\w1516.png",
            "set01\PNG5 Sequences\Walking\w1517.png"]
for i in range(0, 18):
    w15_name[i] = pygame.image.load(w15_loca[i])
    w15_name[i] = pygame.transform.scale(w15_name[i], (140, 140))

'''Load set 2 (cho map2)'''
w21_name = ["w210", "w211", "w212", "w213", "w214", "w215", "w216", "w217", "w218", "w219", "w2110", "w2111"]

w21_loca = ["set02\PNG1 Sequences\Walking\w210.png",
            "set02\PNG1 Sequences\Walking\w211.png",
            "set02\PNG1 Sequences\Walking\w212.png",
            "set02\PNG1 Sequences\Walking\w213.png",
            "set02\PNG1 Sequences\Walking\w214.png",
            "set02\PNG1 Sequences\Walking\w215.png",
            "set02\PNG1 Sequences\Walking\w216.png",
            "set02\PNG1 Sequences\Walking\w217.png",
            "set02\PNG1 Sequences\Walking\w218.png",
            "set02\PNG1 Sequences\Walking\w219.png",
            "set02\PNG1 Sequences\Walking\w2110.png",
            "set02\PNG1 Sequences\Walking\w2111.png"]

for i in range(0, 12):
    w21_name[i] = pygame.image.load(w21_loca[i])
    w21_name[i] = pygame.transform.scale(w21_name[i], (140, 140))

w22_name = ["w220", "w221", "w222", "w223", "w224", "w225", "w226", "w227", "w228", "w229", "w2210", "w2211"]

w22_loca = ["set02\PNG2 Sequences\Walking\w220.png",
            "set02\PNG2 Sequences\Walking\w221.png",
            "set02\PNG2 Sequences\Walking\w222.png",
            "set02\PNG2 Sequences\Walking\w223.png",
            "set02\PNG2 Sequences\Walking\w224.png",
            "set02\PNG2 Sequences\Walking\w225.png",
            "set02\PNG2 Sequences\Walking\w226.png",
            "set02\PNG2 Sequences\Walking\w227.png",
            "set02\PNG2 Sequences\Walking\w228.png",
            "set02\PNG2 Sequences\Walking\w229.png",
            "set02\PNG2 Sequences\Walking\w2210.png",
            "set02\PNG2 Sequences\Walking\w2211.png"]

for i in range(0, 12):
    w22_name[i] = pygame.image.load(w22_loca[i])
    w22_name[i] = pygame.transform.scale(w22_name[i], (140, 140))
w23_name = ["w230", "w231", "w232", "w233", "w234", "w235", "w236", "w237", "w238", "w239", "w2310", "w2311"]

w23_loca = ["set02\PNG3 Sequences\Walking\w230.png",
            "set02\PNG3 Sequences\Walking\w231.png",
            "set02\PNG3 Sequences\Walking\w232.png",
            "set02\PNG3 Sequences\Walking\w233.png",
            "set02\PNG3 Sequences\Walking\w234.png",
            "set02\PNG3 Sequences\Walking\w235.png",
            "set02\PNG3 Sequences\Walking\w236.png",
            "set02\PNG3 Sequences\Walking\w237.png",
            "set02\PNG3 Sequences\Walking\w238.png",
            "set02\PNG3 Sequences\Walking\w239.png",
            "set02\PNG3 Sequences\Walking\w2310.png",
            "set02\PNG3 Sequences\Walking\w2311.png"]

for i in range(0, 12):
    w23_name[i] = pygame.image.load(w23_loca[i])
    w23_name[i] = pygame.transform.scale(w23_name[i], (140, 140))

w24_name = ["w240", "w241", "w242", "w243", "w244", "w245", "w246", "w247", "w248", "w249", "w2410", "w2411"]

w24_loca = ["set02\PNG4 Sequences\Walking\w240.png",
            "set02\PNG4 Sequences\Walking\w241.png",
            "set02\PNG4 Sequences\Walking\w242.png",
            "set02\PNG4 Sequences\Walking\w243.png",
            "set02\PNG4 Sequences\Walking\w244.png",
            "set02\PNG4 Sequences\Walking\w245.png",
            "set02\PNG4 Sequences\Walking\w246.png",
            "set02\PNG4 Sequences\Walking\w247.png",
            "set02\PNG4 Sequences\Walking\w248.png",
            "set02\PNG4 Sequences\Walking\w249.png",
            "set02\PNG4 Sequences\Walking\w2410.png",
            "set02\PNG4 Sequences\Walking\w2411.png"]

for i in range(0, 12):
    w24_name[i] = pygame.image.load(w24_loca[i])
    w24_name[i] = pygame.transform.scale(w24_name[i], (140, 140))

w25_name = ["w250", "w251", "w252", "w253", "w254", "w255", "w256", "w257", "w258", "w259", "w2510", "w2511"]

w25_loca = ["set02\PNG5 Sequences\Walking\w250.png",
            "set02\PNG5 Sequences\Walking\w251.png",
            "set02\PNG5 Sequences\Walking\w252.png",
            "set02\PNG5 Sequences\Walking\w253.png",
            "set02\PNG5 Sequences\Walking\w254.png",
            "set02\PNG5 Sequences\Walking\w255.png",
            "set02\PNG5 Sequences\Walking\w256.png",
            "set02\PNG5 Sequences\Walking\w257.png",
            "set02\PNG5 Sequences\Walking\w258.png",
            "set02\PNG5 Sequences\Walking\w259.png",
            "set02\PNG5 Sequences\Walking\w2510.png",
            "set02\PNG5 Sequences\Walking\w2511.png"]

for i in range(0, 12):
    w25_name[i] = pygame.image.load(w25_loca[i])
    w25_name[i] = pygame.transform.scale(w25_name[i], (140, 140))

'''Load set 4 (cho map2)'''
w41_name = ["w410", "w411", "w412", "w413", "w414", "w415", "w416", "w417", "w418", "w419", "w4110", "w4111", "w4112",
            "w4113", "w4114", "w4115", "w4116", "w4117", ]
w41_loca = ["set04\PNG1 Sequences\Walking\w410.png",
            "set04\PNG1 Sequences\Walking\w411.png",
            "set04\PNG1 Sequences\Walking\w412.png",
            "set04\PNG1 Sequences\Walking\w413.png",
            "set04\PNG1 Sequences\Walking\w414.png",
            "set04\PNG1 Sequences\Walking\w415.png",
            "set04\PNG1 Sequences\Walking\w416.png",
            "set04\PNG1 Sequences\Walking\w417.png",
            "set04\PNG1 Sequences\Walking\w418.png",
            "set04\PNG1 Sequences\Walking\w419.png",
            "set04\PNG1 Sequences\Walking\w4110.png",
            "set04\PNG1 Sequences\Walking\w4111.png",
            "set04\PNG1 Sequences\Walking\w4112.png",
            "set04\PNG1 Sequences\Walking\w4113.png",
            "set04\PNG1 Sequences\Walking\w4114.png",
            "set04\PNG1 Sequences\Walking\w4115.png",
            "set04\PNG1 Sequences\Walking\w4116.png",
            "set04\PNG1 Sequences\Walking\w4117.png"]
for i in range(0, 18):
    w41_name[i] = pygame.image.load(w41_loca[i])
    w41_name[i] = pygame.transform.scale(w41_name[i], (140, 140))

# Load nv set1 2
w42_name = ["w420", "w421", "w422", "w423", "w424", "w425", "w426", "w427", "w428", "w429", "w4210", "w4211", "w4212",
            "w4213", "w4214", "w4215", "w4216", "w4217", ]
w42_loca = ["set04\PNG2 Sequences\Walking\w420.png",
            "set04\PNG2 Sequences\Walking\w421.png",
            "set04\PNG2 Sequences\Walking\w422.png",
            "set04\PNG2 Sequences\Walking\w423.png",
            "set04\PNG2 Sequences\Walking\w424.png",
            "set04\PNG2 Sequences\Walking\w425.png",
            "set04\PNG2 Sequences\Walking\w426.png",
            "set04\PNG2 Sequences\Walking\w427.png",
            "set04\PNG2 Sequences\Walking\w428.png",
            "set04\PNG2 Sequences\Walking\w429.png",
            "set04\PNG2 Sequences\Walking\w4210.png",
            "set04\PNG2 Sequences\Walking\w4211.png",
            "set04\PNG2 Sequences\Walking\w4212.png",
            "set04\PNG2 Sequences\Walking\w4213.png",
            "set04\PNG2 Sequences\Walking\w4214.png",
            "set04\PNG2 Sequences\Walking\w4215.png",
            "set04\PNG2 Sequences\Walking\w4216.png",
            "set04\PNG2 Sequences\Walking\w4217.png"]
for i in range(0, 18):
    w42_name[i] = pygame.image.load(w42_loca[i])
    w42_name[i] = pygame.transform.scale(w42_name[i], (140, 140))

# Load nv set1 3
w43_name = ["w430", "w431", "w432", "w433", "w434", "w435", "w436", "w437", "w438", "w439", "w4310", "w4311", "w4312",
            "w4313", "w4314", "w315", "w4316", "w4317", ]
w43_loca = ["set04\PNG3 Sequences\Walking\w430.png",
            "set04\PNG3 Sequences\Walking\w431.png",
            "set04\PNG3 Sequences\Walking\w432.png",
            "set04\PNG3 Sequences\Walking\w433.png",
            "set04\PNG3 Sequences\Walking\w434.png",
            "set04\PNG3 Sequences\Walking\w435.png",
            "set04\PNG3 Sequences\Walking\w436.png",
            "set04\PNG3 Sequences\Walking\w437.png",
            "set04\PNG3 Sequences\Walking\w438.png",
            "set04\PNG3 Sequences\Walking\w439.png",
            "set04\PNG3 Sequences\Walking\w4310.png",
            "set04\PNG3 Sequences\Walking\w4311.png",
            "set04\PNG3 Sequences\Walking\w4312.png",
            "set04\PNG3 Sequences\Walking\w4313.png",
            "set04\PNG3 Sequences\Walking\w4314.png",
            "set04\PNG3 Sequences\Walking\w4315.png",
            "set04\PNG3 Sequences\Walking\w4316.png",
            "set04\PNG3 Sequences\Walking\w4317.png"]
for i in range(0, 18):
    w43_name[i] = pygame.image.load(w43_loca[i])
    w43_name[i] = pygame.transform.scale(w43_name[i], (140, 140))

w44_name = ["w440", "w441", "w442", "w443", "w444", "w445", "w446", "w447", "w448", "w449", "w4410", "w4411", "w4412",
            "w4413", "w4414", "w4415", "w4416", "w4417", ]
w44_loca = ["set04\PNG4 Sequences\Walking\w440.png",
            "set04\PNG4 Sequences\Walking\w441.png",
            "set04\PNG4 Sequences\Walking\w442.png",
            "set04\PNG4 Sequences\Walking\w443.png",
            "set04\PNG4 Sequences\Walking\w444.png",
            "set04\PNG4 Sequences\Walking\w445.png",
            "set04\PNG4 Sequences\Walking\w446.png",
            "set04\PNG4 Sequences\Walking\w447.png",
            "set04\PNG4 Sequences\Walking\w448.png",
            "set04\PNG4 Sequences\Walking\w449.png",
            "set04\PNG4 Sequences\Walking\w4410.png",
            "set04\PNG4 Sequences\Walking\w4411.png",
            "set04\PNG4 Sequences\Walking\w4412.png",
            "set04\PNG4 Sequences\Walking\w4413.png",
            "set04\PNG4 Sequences\Walking\w4414.png",
            "set04\PNG4 Sequences\Walking\w4415.png",
            "set04\PNG4 Sequences\Walking\w4416.png",
            "set04\PNG4 Sequences\Walking\w4417.png"]
for i in range(0, 18):
    w44_name[i] = pygame.image.load(w44_loca[i])
    w44_name[i] = pygame.transform.scale(w44_name[i], (140, 140))

w45_name = ["w450", "w451", "w452", "w453", "w454", "w455", "w456", "w457", "w458", "w459", "w4510", "w4511", "w4512",
            "w4513", "w4514", "w4515", "w4516", "w4517", ]
w45_loca = ["set04\PNG5 Sequences\Walking\w450.png",
            "set04\PNG5 Sequences\Walking\w451.png",
            "set04\PNG5 Sequences\Walking\w452.png",
            "set04\PNG5 Sequences\Walking\w453.png",
            "set04\PNG5 Sequences\Walking\w454.png",
            "set04\PNG5 Sequences\Walking\w455.png",
            "set04\PNG5 Sequences\Walking\w456.png",
            "set04\PNG5 Sequences\Walking\w457.png",
            "set04\PNG5 Sequences\Walking\w458.png",
            "set04\PNG5 Sequences\Walking\w459.png",
            "set04\PNG5 Sequences\Walking\w4510.png",
            "set04\PNG5 Sequences\Walking\w4511.png",
            "set04\PNG5 Sequences\Walking\w4512.png",
            "set04\PNG5 Sequences\Walking\w4513.png",
            "set04\PNG5 Sequences\Walking\w4514.png",
            "set04\PNG5 Sequences\Walking\w4515.png",
            "set04\PNG5 Sequences\Walking\w4516.png",
            "set04\PNG5 Sequences\Walking\w4517.png"]
for i in range(0, 18):
    w45_name[i] = pygame.image.load(w45_loca[i])
    w45_name[i] = pygame.transform.scale(w45_name[i], (140, 140))

'''Load set 5 (cho map2)'''
w51_name = ["w5101", "w5102", "w5103", "w5104", "w5105", "w5106", "w5107", "w5108", "w5109", "w5110", "w5111", "w5112",
            "w5113", "w5114", "w5115", "w5116", "w5117", "w518"]
w51_loca = [
    "set05\PNG1 Sequences\Walking\w5101.png",
    "set05\PNG1 Sequences\Walking\w5102.png",
    "set05\PNG1 Sequences\Walking\w5103.png",
    "set05\PNG1 Sequences\Walking\w5104.png",
    "set05\PNG1 Sequences\Walking\w5105.png",
    "set05\PNG1 Sequences\Walking\w5106.png",
    "set05\PNG1 Sequences\Walking\w5107.png",
    "set05\PNG1 Sequences\Walking\w5108.png",
    "set05\PNG1 Sequences\Walking\w5109.png",
    "set05\PNG1 Sequences\Walking\w5110.png",
    "set05\PNG1 Sequences\Walking\w5111.png",
    "set05\PNG1 Sequences\Walking\w5112.png",
    "set05\PNG1 Sequences\Walking\w5113.png",
    "set05\PNG1 Sequences\Walking\w5114.png",
    "set05\PNG1 Sequences\Walking\w5115.png",
    "set05\PNG1 Sequences\Walking\w5116.png",
    "set05\PNG1 Sequences\Walking\w5117.png",
    "set05\PNG1 Sequences\Walking\w5118.png", ]
for i in range(0, 18):
    w51_name[i] = pygame.image.load(w51_loca[i])
    w51_name[i] = pygame.transform.scale(w51_name[i], (120, 120))
w52_name = ["w5201", "w5202", "w5203", "w5204", "w5205", "w5206", "w5207", "w5208", "w5209", "w5210", "w5211", "w5212",
            "w5213", "w5214", "w5215", "w5216", "w5217", "w5218"]
w52_loca = [
    "set05\PNG2 Sequences\Walking\w5201.png",
    "set05\PNG2 Sequences\Walking\w5202.png",
    "set05\PNG2 Sequences\Walking\w5203.png",
    "set05\PNG2 Sequences\Walking\w5204.png",
    "set05\PNG2 Sequences\Walking\w5205.png",
    "set05\PNG2 Sequences\Walking\w5206.png",
    "set05\PNG2 Sequences\Walking\w5207.png",
    "set05\PNG2 Sequences\Walking\w5208.png",
    "set05\PNG2 Sequences\Walking\w5209.png",
    "set05\PNG2 Sequences\Walking\w5210.png",
    "set05\PNG2 Sequences\Walking\w5211.png",
    "set05\PNG2 Sequences\Walking\w5212.png",
    "set05\PNG2 Sequences\Walking\w5213.png",
    "set05\PNG2 Sequences\Walking\w5214.png",
    "set05\PNG2 Sequences\Walking\w5215.png",
    "set05\PNG2 Sequences\Walking\w5216.png",
    "set05\PNG2 Sequences\Walking\w5217.png",
    "set05\PNG2 Sequences\Walking\w5218.png"]
for i in range(0, 18):
    w52_name[i] = pygame.image.load(w52_loca[i])
    w52_name[i] = pygame.transform.scale(w52_name[i], (120, 120))

w53_name = ["w5301", "w5302", "w5303", "w5304", "w5305", "w5306", "w5307", "w5308", "w5309", "w5310", "w5311", "w5312",
            "w5313", "w5314", "w5315", "w5316", "w5317", "w5318"]
w53_loca = [
    "set05\PNG3 Sequences\Walking\w5301.png",
    "set05\PNG3 Sequences\Walking\w5302.png",
    "set05\PNG3 Sequences\Walking\w5303.png",
    "set05\PNG3 Sequences\Walking\w5304.png",
    "set05\PNG3 Sequences\Walking\w5305.png",
    "set05\PNG3 Sequences\Walking\w5306.png",
    "set05\PNG3 Sequences\Walking\w5307.png",
    "set05\PNG3 Sequences\Walking\w5308.png",
    "set05\PNG3 Sequences\Walking\w5309.png",
    "set05\PNG3 Sequences\Walking\w5310.png",
    "set05\PNG3 Sequences\Walking\w5311.png",
    "set05\PNG3 Sequences\Walking\w5312.png",
    "set05\PNG3 Sequences\Walking\w5313.png",
    "set05\PNG3 Sequences\Walking\w5314.png",
    "set05\PNG3 Sequences\Walking\w5315.png",
    "set05\PNG3 Sequences\Walking\w5316.png",
    "set05\PNG3 Sequences\Walking\w5317.png",
    "set05\PNG3 Sequences\Walking\w5318.png"]
for i in range(0, 18):
    w53_name[i] = pygame.image.load(w53_loca[i])
    w53_name[i] = pygame.transform.scale(w53_name[i], (120, 120))
w54_name = ["w5401", "w5402", "w5403", "w5404", "w5405", "w5406", "w5407", "w5408", "w5409", "w5410", "w5411", "w5412",
            "w5413", "w5414", "w5415", "w5416", "w5417", "w5418"]
w54_loca = [
    "set05\PNG4 Sequences\Walking\w5401.png",
    "set05\PNG4 Sequences\Walking\w5402.png",
    "set05\PNG4 Sequences\Walking\w5403.png",
    "set05\PNG4 Sequences\Walking\w5404.png",
    "set05\PNG4 Sequences\Walking\w5405.png",
    "set05\PNG4 Sequences\Walking\w5406.png",
    "set05\PNG4 Sequences\Walking\w5407.png",
    "set05\PNG4 Sequences\Walking\w5408.png",
    "set05\PNG4 Sequences\Walking\w5409.png",
    "set05\PNG4 Sequences\Walking\w5410.png",
    "set05\PNG4 Sequences\Walking\w5411.png",
    "set05\PNG4 Sequences\Walking\w5412.png",
    "set05\PNG4 Sequences\Walking\w5413.png",
    "set05\PNG4 Sequences\Walking\w5414.png",
    "set05\PNG4 Sequences\Walking\w5415.png",
    "set05\PNG4 Sequences\Walking\w5416.png",
    "set05\PNG4 Sequences\Walking\w5417.png",
    "set05\PNG4 Sequences\Walking\w5418.png"]
for i in range(0, 18):
    w54_name[i] = pygame.image.load(w54_loca[i])
    w54_name[i] = pygame.transform.scale(w54_name[i], (120, 120))
w55_name = ["w5501", "w5502", "w5503", "w5504", "w5505", "w5506", "w5507", "w5508", "w5509", "w5510", "w5511", "w5512",
            "w5513", "w5514", "w5515", "w5516", "w5517", "w5518"]
w55_loca = [
    "set05\PNG5 Sequences\Walking\w5501.png",
    "set05\PNG5 Sequences\Walking\w5502.png",
    "set05\PNG5 Sequences\Walking\w5503.png",
    "set05\PNG5 Sequences\Walking\w5504.png",
    "set05\PNG5 Sequences\Walking\w5505.png",
    "set05\PNG5 Sequences\Walking\w5506.png",
    "set05\PNG5 Sequences\Walking\w5507.png",
    "set05\PNG5 Sequences\Walking\w5508.png",
    "set05\PNG5 Sequences\Walking\w5509.png",
    "set05\PNG5 Sequences\Walking\w5510.png",
    "set05\PNG5 Sequences\Walking\w5511.png",
    "set05\PNG5 Sequences\Walking\w5512.png",
    "set05\PNG5 Sequences\Walking\w5513.png",
    "set05\PNG5 Sequences\Walking\w5514.png",
    "set05\PNG5 Sequences\Walking\w5515.png",
    "set05\PNG5 Sequences\Walking\w5516.png",
    "set05\PNG5 Sequences\Walking\w5517.png",
    "set05\PNG5 Sequences\Walking\w5518.png"]
for i in range(0, 18):
    w55_name[i] = pygame.image.load(w55_loca[i])
    w55_name[i] = pygame.transform.scale(w55_name[i], (120, 120))

# Background

'''menu chính'''
bgvn = pygame.image.load("background\menugame.png")
bg = pygame.image.load("background\menugamevn.png")
background = Background(bg)
backgroundvn = Background(bgvn)

'''màn hình chọn nhân vật'''
bg0 = pygame.image.load("background\menugamemap.png")
background0 = Background(bg0)

'''các level của map1'''
bg1 = pygame.image.load("background\\1.jpg")
bg1_lv2 = pygame.image.load("background\\1.2.jpg")
bg1_lv3 = pygame.image.load("background\\1.3.jpg")
background1 = Background(bg1_lv2)
background1_lv2 = Background(bg1_lv2)
background1_lv3 = Background(bg1_lv3)
'''các level của map2'''
bg2 = pygame.image.load("background\\2.jpg")
bg2_lv2 = pygame.image.load("background\\2.2.jpg")
bg2_lv3 = pygame.image.load("background\\2.3.jpg")
background2 = Background(bg2)
background2_lv2 = Background(bg2_lv2)
background2_lv3 = Background(bg2_lv3)

'''các level của map3'''
bg3 = pygame.image.load("background\\3.jpg")
bg3_lv2 = pygame.image.load("background\\3.2.jpg")
bg3_lv3 = pygame.image.load("background\\3.3.jpg")
background3 = Background(bg3)
background3_lv2 = Background(bg3_lv2)
background3_lv3 = Background(bg3_lv3)
'''kết quả'''
result = pygame.image.load("background\\result.png")
background6 = Background(result)

'''luật chơi'''
rule_bg = pygame.image.load("background\\rulebg.png")
background7 = Background(rule_bg)

# Load button
'''nút play'''
play = pygame.image.load("Button\play1.png")
play_but = Button(play, 100, 700, 105, 85)

choose1 = pygame.image.load("Button\set_but1.png")
choose1vn = pygame.image.load("Button\set_but1vn.png")

choose2 = pygame.image.load("Button\set_but2.png")
choose2vn = pygame.image.load("Button\set_but2vn.png")

choose3 = pygame.image.load("Button\set_but3.png")
choose3vn = pygame.image.load("Button\set_but3vn.png")
set1vn_but = Button(choose1vn, set_but_x, set_but_y, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)
set2vn_but = Button(choose2vn, set_but_x, set_but_y + set_but_dis, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)
set3vn_but = Button(choose3vn, set_but_x, set_but_y + 2 * set_but_dis, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)

set1_but = Button(choose1, set_but_x, set_but_y, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)
set2_but = Button(choose2, set_but_x, set_but_y + set_but_dis, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)
set3_but = Button(choose3, set_but_x, set_but_y + 2 * set_but_dis, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)

exit = pygame.image.load("Button\exit.png")
exit_but = Button(exit, exit_but_x, exit_but_y, exit_w, exit_h)

signup = pygame.image.load("Button\signup.png")
signupvn = pygame.image.load("Button/signupvn.png")
login = pygame.image.load("Button\login.png")
loginvn = pygame.image.load("Button\loginvn.png")
logout = pygame.image.load("Button\logout.png")
logoutvn = pygame.image.load("Button\logoutvn.png")
signup_but = Button(signup, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 1.3, 250, 130)
login_but = Button(login, SCREEN_WIDTH // 2.8, SCREEN_HEIGHT // 1.3, 250, 130)
signupvn_but = Button(signupvn, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 1.3, 250, 130)
logout_but = Button(logout, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
loginvn_but = Button(loginvn, SCREEN_WIDTH // 2.8, SCREEN_HEIGHT // 1.3, 250, 130)
logoutvn_but = Button(logoutvn, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)

setting = pygame.image.load("Button\setting.png")
setting_but = Button(setting, SCREEN_WIDTH // 1.025, SCREEN_HEIGHT // 17, SCREEN_WIDTH // 20, SCREEN_HEIGHT // 12)

language = pygame.image.load("Button\language.png")
languagevn = pygame.image.load("Button\languagevn.png")
vie = pygame.image.load("Button\\vie.png")
eng = pygame.image.load("Button\eng.png")
language_but = Button(language, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
languagevn_but = Button(languagevn, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
vie_but = Button(vie, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
eng_but = Button(eng, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 1.5, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)

box = pygame.image.load("Button\\box.png")

car1 = pygame.image.load("setbg3\set03\car1.png")
car2 = pygame.image.load("setbg3\set03\car2.png")
car3 = pygame.image.load("setbg3\set03\car3.png")
car4 = pygame.image.load("setbg3\set03\car4.png")
car5 = pygame.image.load("setbg3\set03\car5.png")
plane = pygame.image.load("setbg3\set03\plane.png")

banhxe = pygame.image.load("setbg3\set03\\banhxe2.png")

start = pygame.image.load("start\start.png")
startvn = pygame.image.load("start\startvn.png")
start_but = Button(start, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 200, 200)
startvn_but = Button(startvn, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 200, 200)

three = pygame.image.load("start\\3.png")
two = pygame.image.load("start\\2.png")
one = pygame.image.load("start\\1.png")
three_but = Button(three, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 200, 200)
two_but = Button(two, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 200, 200)
one_but = Button(one, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 200, 200)

choose_set1 = pygame.image.load("Button\set1.png")
choose_set1vn = pygame.image.load("Button\set1vn.png")
choose_set2 = pygame.image.load("Button\set2.png")
choose_set2vn = pygame.image.load("Button\set2vn.png")
choose_set1_but = Button(choose_set1, SCREEN_WIDTH // 2, 50, 250, 130)
choose_set1vn_but = Button(choose_set1vn, SCREEN_WIDTH // 2, 50, 250, 130)
choose_set2_but = Button(choose_set2, SCREEN_WIDTH // 5, 50, 250, 130)
choose_set2vn_but = Button(choose_set1vn, SCREEN_WIDTH // 5, 50, 250, 130)


minigame = pygame.image.load("Button\minigame.png")
minigame_but = Button(minigame, 300, 712, 160, 60)

snake = pygame.image.load("Button\snake.png")
fruit = pygame.image.load("Button\\fruit.png")
flappy_bird = pygame.image.load("Button\\bird.png")
flappy_bird_but = Button(flappy_bird, 200, 600, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 15)
fruit_but = Button(fruit, 660, 600, SCREEN_WIDTH // 10, SCREEN_HEIGHT // 15)
snake_but = Button(snake, 1100, 600, SCREEN_WIDTH // 10, SCREEN_HEIGHT // 15)

rule = pygame.image.load("Button\\rule.png")
rule_info = pygame.image.load("Button\\rules.png")
rule_info = pygame.transform.scale(rule_info, (1920 / 2, 1080 / 2))
rule_but = Button(rule, 500, 712, 100, 55)

coin_img = pygame.image.load("Button/coin.png")
coin_but = Button(coin_img, 1230, 18, 50, 50)

demo_map1_but = Button(bg1, demomap_x, demomap_y, demomap_w, demomap_h)
demo_map2_but = Button(bg2, demomap_x, demomap_y, demomap_w, demomap_h)
demo_map3_but = Button(bg3, demomap_x, demomap_y, demomap_w, demomap_h)

# Head
head11 = pygame.image.load("head/Dau nv/Set1/PNG1.png")
head12 = pygame.image.load("head/Dau nv/Set1/PNG2.png")
head13 = pygame.image.load("head/Dau nv/Set1/PNG3.png")
head14 = pygame.image.load("head/Dau nv/Set1/PNG4.png")
head15 = pygame.image.load("head/Dau nv/Set1/PNG5.png")

'''
head11=pygame.transform.scale(head11,(210,210))
head12=pygame.transform.scale(head12,(280,280))
head13=pygame.transform.scale(head13,(200,200))
head14=pygame.transform.scale(head14,(200,200))
head15=pygame.transform.scale(head15,(190,200))'''

head21 = pygame.image.load("head/Dau nv/Set 2/1.png")
head22 = pygame.image.load("head/Dau nv/Set 2/2.png")
head23 = pygame.image.load("head/Dau nv/Set 2/3.png")
head24 = pygame.image.load("head/Dau nv/Set 2/4.png")
head25 = pygame.image.load("head/Dau nv/Set 2/5.png")

head31 = pygame.image.load("head/Dau nv/Set3/nv1.png")
head32 = pygame.image.load("head/Dau nv/Set3/nv2.png")
head33 = pygame.image.load("head/Dau nv/Set3/nv3.png")
head34 = pygame.image.load("head/Dau nv/Set3/nv4.png")
head35 = pygame.image.load("head/Dau nv/Set3/nv5.png")

head41 = pygame.image.load("head/Dau nv/Set4/nv1.png")
head42 = pygame.image.load("head/Dau nv/Set4/nv2.png")
head43 = pygame.image.load("head/Dau nv/Set4/nv3.png")
head44 = pygame.image.load("head/Dau nv/Set4/nv4.png")
head45 = pygame.image.load("head/Dau nv/Set4/nv5.png")

head51 = pygame.image.load("head/Dau nv/Set5/nv1.png")
head52 = pygame.image.load("head/Dau nv/Set5/nv2.png")
head53 = pygame.image.load("head/Dau nv/Set5/nv3.png")
head54 = pygame.image.load("head/Dau nv/Set5/nv4.png")
head55 = pygame.image.load("head/Dau nv/Set5/nv5.png")

# Set text
chooseMap_text = Text(game_font1, "Choose the map", 255, 255, 255)
chooseMapvn_text = Text(game_font1, "Chọn bản đồ", 255, 255, 255)
set1_text = Text(game_font4, "SET 1", 0, 0, 0)

set2_text = Text(game_font4, "SET 2", 0, 0, 0)
choosenv = Text(game_font3, "Choose your set of character", 0, 0, 0)

S_nv1 = Text(game_font2, str(int((w11_x) / 3)), 0, 0, 0)
S_nv2 = Text(game_font2, str(int((w12_x) / 3)), 0, 0, 0, )
S_nv3 = Text(game_font2, str(int((w13_x) / 3)), 0, 0, 0)
S_nv4 = Text(game_font2, str(int((w14_x) / 3)), 0, 0, 0)
S_nv5 = Text(game_font2, str(int((w15_x) / 3)), 0, 0, 0)


# Các hàm
def check_press(rect, pos):
    if rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            return True
        else:
            return False


def check_hover(rect, pos):
    if rect.collidepoint(pos):
        return True
    else:
        return False


coin_bool = False

'''Tắt hết các màn hình còn lại'''


def off_screen_except(x):
    global set_, wait, set1, set2, set3, setting_bool, result, lang, start_bool, minigame_bool, rule_bool, choosenv_bool1
    global setnv11, setnv21, choosenv_bool2, setnv12, setnv22, flap
    set_ = False  # menu
    wait = False  # chon map
    set1 = False  # map1
    set2 = False  # map2
    set3 = False  # map3
    result = False  # ket qua
    lang = False  # ngon ngu
    start_bool = False  # bat dau tran
    setting_bool = False  # setting
    minigame_bool = False  # minigame
    rule_bool = False
    flap = False  # game flappy bird
    choosenv_bool1 = choosenv_bool2 = False  # chon set truoc khi vao
    setnv11 = False  # set 1 của map1
    setnv21 = False  # set 2 của map1
    setnv12 = False  # set 1 của map2
    setnv22 = False  # set 2 của map2

    if x == 0: set_ = True
    if x == 1: set1 = True
    if x == 2: set2 = True
    if x == 3: set3 = True
    if x == 4: set4 = True  # đã bỏ không xài
    if x == 5: set5 = True  # đã bỏ không xài
    if x == 6: setting_bool = True
    if x == 7: lang = True
    if x == 8: result = True
    if x == 9: start_bool = True
    if x == 10: minigame_bool = True
    if x == 11: rule_bool = True
    if x == 12: choosenv_bool1 = True
    if x == 13: setnv12 = True
    if x == 14: setnv22 = True
    if x == 15: choosenv_bool2 = True
    if x == 16: flap = True
    if x == 0.5: wait = True


def language_screen():
    background0.draw_bg(screen)
    off_screen_except(7)
    vie_but.draw_but(screen)
    eng_but.draw_but(screen)
    if check_press(vie_but.image_rect, pos):
        with open('lan.txt', 'w') as file:
            file.write(str(0))
        off_screen_except(0)
    if check_press(eng_but.image_rect, pos):
        with open('lan.txt', 'w') as file:
            file.write(str(1))
        off_screen_except(0)
    if check_press(exit_but.image_rect, pos):
        off_screen_except(6)
        time.sleep(0.1)


def account_login():
    if lock:
        background.draw_bg(screen)
        play_but.draw_but(screen)
        setting_but.draw_but(screen)
    else:
        background.draw_bg(screen)
        if lan:
            signup_but.draw_but(screen)
            login_but.draw_but(screen)

        else:
            signupvn_but.draw_but(screen)
            loginvn_but.draw_but(screen)

        if check_press(signup_but.image_rect, pos):
            subprocess.run(["python", "RegistrationApp.py"])
        if check_press(login_but.image_rect, pos):
            subprocess.run(["python", "LoginApp.py"])


def menu_screen():
    if set_ and lock == False:
        account_login()
    if lock:
        if lan:
            background.draw_bg(screen)
        else:
            backgroundvn.draw_bg(screen)

        play_but.draw_but(screen)
        setting_but.draw_but(screen)
        minigame_but.draw_but(screen)
        rule_but.draw_but(screen)

        if check_press(play_but.image_rect, pos):
            off_screen_except(0.5)
        if check_press(setting_but.image_rect, pos):
            off_screen_except(6)
        if check_press(minigame_but.image_rect, pos):
            off_screen_except(10)
            minigame_screen()
        if check_press(rule_but.image_rect, pos):
            rule_screen()
            off_screen_except(11)




    else:
        background.draw_bg(screen)
        if lan:
            signup_but.draw_but(screen)
            login_but.draw_but(screen)
        else:
            signupvn_but.draw_but(screen)
            loginvn_but.draw_but(screen)
        setting_but.draw_but(screen)

    global w11_x, w12_x, w13_x, w14_x, w15_x, wi11, wi12, wi13, wi14, wi15
    w11_x = 0
    w12_x = 0
    w13_x = 0
    w14_x = 0
    w15_x = 0
    wi11 = 0
    wi12 = 0
    wi13 = 0
    wi14 = 0
    wi15 = 0

    random_x1 = random.randrange(SCREEN_WIDTH // 3, SCREEN_WIDTH // 2)
    random_x2 = random.randrange(SCREEN_WIDTH // 3, SCREEN_WIDTH // 2)
    random_x3 = random.randrange(SCREEN_WIDTH // 3, SCREEN_WIDTH // 2)
    random_x4 = random.randrange(SCREEN_WIDTH // 3, SCREEN_WIDTH // 2)
    random_x5 = random.randrange(SCREEN_WIDTH // 3, SCREEN_WIDTH // 2)


def minigame_screen():
    global screen, coin, fruit
    off_screen_except(10)
    background0.draw_bg(screen)
    fruit_but.draw_but(screen)
    snake_but.draw_but(screen)
    flappy_bird_but.draw_but(screen)

    if check_press(flappy_bird_but.image_rect, pos):
        #subprocess.run(["python", "PlappyBird.py"])
        pass

    if check_press(snake_but.image_rect, pos):
        pass #bỏ đoạn code các minigame vào
    if check_press(fruit_but.image_rect, pos):
        coin=fruit.fruit_ninja_game_play(screen, coin)
    exit_but.draw_but(screen)
    if check_press(exit_but.image_rect, pos):
        off_screen_except(0)


global y
y = 0


def rule_screen():
    off_screen_except(11)
    background7.draw_bg(screen)

    if check_press(exit_but.image_rect, pos):
        menu_screen()
        off_screen_except(0)


def wait_screen():
    background0.draw_bg(screen)
    if lan:
        chooseMap_text.draw_text(screen, choose_map_x, choose_map_y)
    else:
        chooseMapvn_text.draw_text(screen, choose_map_x, choose_map_y)
    exit_but.draw_but(screen)
    if lan:
        set1_but.draw_but(screen)
        set2_but.draw_but(screen)
        set3_but.draw_but(screen)


    else:
        set1vn_but.draw_but(screen)
        set2vn_but.draw_but(screen)
        set3vn_but.draw_but(screen)

    if set1_but.image_rect.collidepoint(pos):
        demo_map1_but.draw_but(screen)
        if pygame.mouse.get_pressed()[0] == 1:
            off_screen_except(12)
            choose_nv_screen1()

    if set2_but.image_rect.collidepoint(pos):
        demo_map2_but.draw_but(screen)
        if pygame.mouse.get_pressed()[0] == 1:
            off_screen_except(15)
            choose_nv_screen2()

    if set3_but.image_rect.collidepoint(pos):
        demo_map3_but.draw_but(screen)
        if pygame.mouse.get_pressed()[0] == 1:
            off_screen_except(3)

    if check_press(exit_but.image_rect, pos):
        off_screen_except(0)

    global w11_x, w12_x, w13_x, w14_x, w15_x, wi11, wi12, wi13, wi14, wi15
    w11_x = 0
    w12_x = 0
    w13_x = 0
    w14_x = 0
    w15_x = 0
    wi11 = 0
    wi12 = 0
    wi13 = 0
    wi14 = 0
    wi15 = 0

    global x1, x2, x3, x4, x5
    x1 = random.uniform(0.8, 1.2)
    x2 = random.uniform(0.8, 1.2)
    x3 = random.uniform(0.8, 1.2)
    x4 = random.uniform(0.8, 1.2)
    x5 = random.uniform(0.8, 1.2)

    global lucky1, lucky2, lucky3, lucky4, lucky5
    lucky1 = random.randrange(1, 100)
    lucky2 = random.randrange(1, 100)
    lucky3 = random.randrange(1, 100)
    lucky4 = random.randrange(1, 100)
    lucky5 = random.randrange(1, 100)


def setting_screen():
    background0.draw_bg(screen)
    exit_but.draw_but(screen)
    if lan:
        logout_but.draw_but(screen)
        language_but.draw_but(screen)
    else:
        logoutvn_but.draw_but(screen)
        languagevn_but.draw_but(screen)

    if check_press(logout_but.image_rect, pos):
        with open('log.txt', 'w') as file:
            file.write('0')
        off_screen_except(0)
    if check_press(exit_but.image_rect, pos):
        off_screen_except(0)
    if check_press(language_but.image_rect, pos):
        language_screen()


bet = ""


def choose_nv_screen1():
    global bet
    background0.draw_bg(screen)
    choosenv.draw_text(screen, 300, 10)
    set1_text.draw_text(screen, 50, 200)
    set2_text.draw_text(screen, 50, 400)
    if check_press(pygame.Rect(50, 200, 200, 80), pos):
        global setnv11
        off_screen_except(1)
        setnv11 = True
    if check_press(pygame.Rect(50, 400, 200, 80), pos):
        global setnv21
        off_screen_except(1)
        setnv21 = True
    white = pygame.image.load("background/white.png")
    white = pygame.transform.scale(white, (80, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:

                # Khi nhấn Enter, in giá trị và đặt lại biến coin
                print("Coin value:", bet)
                bet = ""
            elif event.key == pygame.K_BACKSPACE:

                bet = bet[:-1]
            else:
                bet += event.unicode

    pygame.draw.rect(screen, (0, 0, 0), (600, 600, 300, 50), 2)

    text_surface = game_font1.render(bet, True, (255, 255, 255))
    screen.blit(text_surface, (600, 600))
    pygame.display.flip()
    exit_but.draw_but(screen)
    if check_press(exit_but.image_rect, pos):
        off_screen_except(0.5)


def choose_nv_screen2():
    global bet
    background0.draw_bg(screen)
    choosenv.draw_text(screen, 300, 10)
    set1_text.draw_text(screen, 50, 200)
    set2_text.draw_text(screen, 50, 400)
    if check_press(pygame.Rect(50, 200, 200, 80), pos):
        off_screen_except(2)
        global setnv12
        setnv12 = True
    if check_press(pygame.Rect(50, 400, 200, 80), pos):
        off_screen_except(2)
        global setnv22
        setnv22 = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:

                # Khi nhấn Enter, in giá trị và đặt lại biến coin
                print("Coin value:", bet)
                bet = ""
            elif event.key == pygame.K_BACKSPACE:

                bet = bet[:-1]
            else:
                bet += event.unicode

    pygame.draw.rect(screen, (0, 0, 0), (600, 600, 300, 50), 2)

    text_surface = game_font1.render(bet, True, (255, 255, 255))
    screen.blit(text_surface, (600, 600))
    pygame.display.flip()
    exit_but.draw_but(screen)
    if check_press(exit_but.image_rect, pos):
        off_screen_except(0.5)


box_but1 = Button(box, random_x1, 235, 50, 50)
box_but2 = Button(box, random_x2, 350, 50, 50)
box_but3 = Button(box, random_x3, 460, 50, 50)
box_but4 = Button(box, random_x4, 575, 50, 50)
box_but5 = Button(box, random_x5, 675, 50, 50)


def map1(pos):
    background1.draw_bg(screen)
    exit_but.draw_but(screen)
    if check_press(exit_but.image_rect, pos):
        off_screen_except(0.5)
        time.sleep(0.2)

    S_nv1.draw_text(screen, 100, 20)
    S_nv2.draw_text(screen, 100, 45)
    S_nv3.draw_text(screen, 100, 70)
    S_nv4.draw_text(screen, 100, 95)
    S_nv5.draw_text(screen, 100, 120)
    if setnv11:
        head11_but = Button(head11, 80, 35, 26, 26)
        head12_but = Button(head12, 80, 60, 29, 29)
        head13_but = Button(head13, 80, 85, 25, 25)
        head14_but = Button(head14, 80, 110, 24, 22)
        head15_but = Button(head15, 80, 135, 24, 22)

        head11_but.draw_but(screen)
        head12_but.draw_but(screen)
        head13_but.draw_but(screen)
        head14_but.draw_but(screen)
        head15_but.draw_but(screen)
    if setnv21:
        head41_but = Button(head41, 80, 35, 26, 26)
        head42_but = Button(head42, 80, 60, 29, 29)
        head43_but = Button(head43, 80, 85, 25, 25)
        head44_but = Button(head44, 80, 110, 24, 22)
        head45_but = Button(head45, 80, 135, 24, 22)

        head41_but.draw_but(screen)
        head42_but.draw_but(screen)
        head43_but.draw_but(screen)
        head44_but.draw_but(screen)
        head45_but.draw_but(screen)

    box_but1 = Button(box, random_x1, 235, 50, 50)
    box_but2 = Button(box, random_x2, 350, 50, 50)
    box_but3 = Button(box, random_x3, 460, 50, 50)
    box_but4 = Button(box, random_x4, 575, 50, 50)
    box_but5 = Button(box, random_x5, 675, 50, 50)
    if random_x1 > w11_x:
        box_but1.draw_but(screen)
    if random_x2 > w12_x:
        box_but2.draw_but(screen)
    if random_x3 > w13_x:
        box_but3.draw_but(screen)
    if random_x4 > w14_x:
        box_but4.draw_but(screen)
    if random_x5 > w15_x:
        box_but5.draw_but(screen)


def map2(pos):
    background2.draw_bg(screen)
    exit_but.draw_but(screen)
    if check_press(exit_but.image_rect, pos):
        off_screen_except(0.5)
        time.sleep(0.2)
    S_nv1.draw_text(screen, 100, 20)
    S_nv2.draw_text(screen, 100, 40)
    S_nv3.draw_text(screen, 100, 60)
    S_nv4.draw_text(screen, 100, 80)
    S_nv5.draw_text(screen, 100, 100)

    box_but1 = Button(box, random_x1, 235, 50, 50)
    box_but2 = Button(box, random_x2, 350, 50, 50)
    box_but3 = Button(box, random_x3, 460, 50, 50)
    box_but4 = Button(box, random_x4, 575, 50, 50)
    box_but5 = Button(box, random_x5, 675, 50, 50)

    if setnv12:
        head31_but = Button(head31, 80, 35, 26, 26)
        head32_but = Button(head32, 80, 60, 29, 29)
        head33_but = Button(head33, 80, 85, 25, 25)
        head34_but = Button(head34, 80, 110, 24, 22)
        head35_but = Button(head35, 80, 135, 24, 22)

        head31_but.draw_but(screen)
        head32_but.draw_but(screen)
        head33_but.draw_but(screen)
        head34_but.draw_but(screen)
        head35_but.draw_but(screen)

    if setnv22:
        head51_but = Button(head51, 80, 35, 26, 26)
        head52_but = Button(head52, 80, 60, 29, 29)
        head53_but = Button(head53, 80, 85, 25, 25)
        head54_but = Button(head54, 80, 110, 24, 22)
        head55_but = Button(head55, 80, 135, 24, 22)

        head51_but.draw_but(screen)
        head52_but.draw_but(screen)
        head53_but.draw_but(screen)
        head54_but.draw_but(screen)
        head55_but.draw_but(screen)

    if random_x1 > w11_x:
        box_but1.draw_but(screen)
    if random_x2 > w12_x:
        box_but2.draw_but(screen)
    if random_x3 > w13_x:
        box_but3.draw_but(screen)
    if random_x4 > w14_x:
        box_but4.draw_but(screen)
    if random_x5 > w15_x:
        box_but5.draw_but(screen)


def map3(pos):
    off_screen_except(3)
    background3.draw_bg(screen)
    exit_but.draw_but(screen)

    if check_press(exit_but.image_rect, pos):
        off_screen_except(0.5)
        time.sleep(0.2)

    S_nv1.draw_text(screen, 100, 20)
    S_nv2.draw_text(screen, 100, 40)
    S_nv3.draw_text(screen, 100, 60)
    S_nv4.draw_text(screen, 100, 80)
    S_nv5.draw_text(screen, 100, 100)

    box_but1 = Button(box, random_x1, 235, 50, 50)
    box_but2 = Button(box, random_x2, 350, 50, 50)
    box_but3 = Button(box, random_x3, 460, 50, 50)
    box_but4 = Button(box, random_x4, 575, 50, 50)
    box_but5 = Button(box, random_x5, 675, 50, 50)

    if random_x1 > w11_x:
        box_but1.draw_but(screen)
    if random_x2 > w12_x:
        box_but2.draw_but(screen)
    if random_x3 > w13_x:
        box_but3.draw_but(screen)
    if random_x4 > w14_x:
        box_but4.draw_but(screen)
    if random_x5 > w15_x:
        box_but5.draw_but(screen)


i = 1
coin = 100
coin_text = Text(game_font1, "COIN: " + str(coin), 0, 0, 0)
clock = pygame.time.Clock()
while True:

    global pos
    pos = pygame.mouse.get_pos()

    S_nv1 = Text(game_font2, str(int(w11_x / 5)), 0, 0, 0)
    S_nv2 = Text(game_font2, str(int(w12_x / 5)), 0, 0, 0, )
    S_nv3 = Text(game_font2, str(int(w13_x / 5)), 0, 0, 0)
    S_nv4 = Text(game_font2, str(int(w14_x / 5)), 0, 0, 0)
    S_nv5 = Text(game_font2, str(int(w15_x / 5)), 0, 0, 0)

    if w11_x < finish + 10:
        w11_x += x1

    if w12_x < finish + 10:
        w12_x += x2

    if w13_x < finish + 10:
        w13_x += x3

    if w14_x < finish + 10:
        w14_x += x4

    if w15_x < finish + 10:
        w15_x += x5

    wi11 += 0.5
    wi12 += 0.5
    wi13 += 0.5
    wi14 += 0.5
    wi15 += 0.125
    if wi11 == 17: wi11 = 0
    if wi12 == 11: wi12 = 0
    if wi13 == 17: wi13 = 0
    if wi14 == 17: wi14 = 0
    if wi15 == 17: wi15 = 0

    with open('log.txt', 'r') as file:
        content = file.read()
        if content == "1":
            lock = True
        if content == "0":
            lock = False

    with open('lan.txt', 'r') as file:
        l = file.read()
        if l == "1":
            lan = True
        if l == "0":
            lan = False

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if set_:
        menu_screen()
        coin_text = Text(game_font1, str(int(coin)), 255, 200, 60)
        coin_text.draw_text(screen, 1150, -6)
        coin_but.draw_but(screen)
    if wait:
        wait_screen()

    if setting_bool:
        setting_screen()
    if set2:
        map2(pos)
        if check_press(exit_but.image_rect, pos):
            off_screen_except(0.5)
            time.sleep(0.2)
        if setnv12:
            nv21 = nhanVat("nv21", w21_name[int(wi12)], w11_x, 200, 120, 120)
            nv21.draw_nv()
            if nv21.check_vc(box_but1):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x1 = nv21.buff_speed(0)
                if 50 < lucky <= 100:
                    w11_x = finish

            nv22 = nhanVat("nv22", w22_name[int(wi12)], w12_x, 325, 120, 120)
            nv22.draw_nv()
            if nv22.check_vc(box_but2):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x2 = nv22.buff_speed(0)
                if 50 < lucky <= 100:
                    w12_x = finish

            nv23 = nhanVat("nv23", w23_name[int(wi12)], w13_x, 450, 120, 120)
            nv23.draw_nv()
            if nv23.check_vc(box_but3):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x3 = nv23.buff_speed(0)
                if 50 < lucky <= 100:
                    w13_x = finish

            nv24 = nhanVat("nv24", w24_name[int(wi12)], w14_x, 550, 120, 120)
            nv24.draw_nv()
            if nv24.check_vc(box_but4):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x4 = nv24.buff_speed(0)
                if 50 < lucky <= 100:
                    w14_x = finish

            nv25 = nhanVat("nv25", w25_name[int(wi12)], w15_x, 650, 120, 120)
            nv25.draw_nv()
            if nv25.check_vc(box_but5):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x5 = nv25.buff_speed(0)
                if 50 < lucky <= 100:
                    w15_x = finish
            if min(w11_x, w12_x, w13_x, w14_x, w15_x) > finish + 10:
                off_screen_except(8)
                background6.draw_bg(screen)
                exit_but.draw_but(screen)
                if check_press(exit_but.image_rect, pos):
                    off_screen_except(0.5)
        if setnv22:
            nv51 = nhanVat("nv51", w51_name[int(wi15)], w11_x, 200, 100, 100)
            nv51.draw_nv()
            if nv51.check_vc(box_but1):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x1 = nv51.buff_speed(0)
                if 50 < lucky <= 100:
                    w11_x = finish

            nv52 = nhanVat("nv52", w52_name[int(wi15)], w12_x, 325, 100, 100)
            nv52.draw_nv()
            if nv52.check_vc(box_but2):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x2 = nv52.buff_speed(0)
                if 50 < lucky <= 100:
                    w12_x = finish

            nv53 = nhanVat("nv53", w53_name[int(wi15)], w13_x, 450, 100, 100)
            nv53.draw_nv()
            if nv53.check_vc(box_but3):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x3 = nv53.buff_speed(0)
                if 50 < lucky <= 100:
                    w13_x = finish

            nv54 = nhanVat("nv54", w54_name[int(wi15)], w14_x, 550, 100, 100)
            nv54.draw_nv()
            if nv54.check_vc(box_but4):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x4 = nv54.buff_speed(0)
                if 50 < lucky <= 100:
                    w14_x = finish

            nv55 = nhanVat("nv55", w55_name[int(wi15)], w15_x, 650, 100, 100)
            nv55.draw_nv()
            if nv55.check_vc(box_but5):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x5 = nv55.buff_speed(0)
                if 50 < lucky <= 100:
                    w15_x = finish
            if min(w11_x, w12_x, w13_x, w14_x, w15_x) > finish + 10:
                off_screen_except(8)
                background6.draw_bg(screen)
                exit_but.draw_but(screen)
                if check_press(exit_but.image_rect, pos):
                    off_screen_except(0.5)
        if min(w11_x, w12_x, w13_x, w14_x, w15_x) > finish + 10:
            off_screen_except(8)
            background6.draw_bg(screen)
            exit_but.draw_but(screen)
            if check_press(exit_but.image_rect, pos):
                off_screen_except(0.5)
    if set1:
        boom_but1 = Button(boom, w11_x, 208, 90, 90)
        boom_but2 = Button(boom, w12_x, 325, 90, 90)
        boom_but3 = Button(boom, w13_x, 450, 90, 90)
        boom_but4 = Button(boom, w14_x, 550, 90, 90)
        boom_but5 = Button(boom, w15_x, 650, 90, 90)
        map1(pos)
        if check_press(exit_but.image_rect, pos):
            off_screen_except(0.5)
            time.sleep(0.2)
        if setnv21:
            nv41 = nhanVat("nv41", w41_name[int(wi14)], w11_x, 200, 120, 120)
            nv41.draw_nv()
            if nv41.check_vc(box_but1):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x1 = nv41.buff_speed(0)
                if 50 < lucky <= 100:
                    w11_x = finish

            nv42 = nhanVat("nv42", w42_name[int(wi14)], w12_x, 325, 120, 120)
            nv42.draw_nv()
            if nv42.check_vc(box_but2):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x2 = nv42.buff_speed(0)
                if 50 < lucky <= 100:
                    w12_x = finish

            nv43 = nhanVat("nv43", w43_name[int(wi14)], w13_x, 450, 120, 120)
            nv43.draw_nv()
            if nv43.check_vc(box_but3):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x3 = nv43.buff_speed(0)
                if 50 < lucky <= 100:
                    w13_x = finish

            nv44 = nhanVat("nv44", w44_name[int(wi14)], w14_x, 550, 120, 120)
            nv44.draw_nv()
            if nv44.check_vc(box_but4):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x4 = nv44.buff_speed(0)
                if 50 < lucky <= 100:
                    w14_x = finish

            nv45 = nhanVat("nv45", w45_name[int(wi14)], w15_x, 650, 120, 120)
            nv45.draw_nv()
            if nv45.check_vc(box_but5):
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 50:
                    x5 = nv45.buff_speed(0)
                if 50 < lucky <= 100:
                    w15_x = finish

            if min(w11_x, w12_x, w13_x, w14_x, w15_x) > finish + 10:
                off_screen_except(8)
                background6.draw_bg(screen)
                exit_but.draw_but(screen)
                if check_press(exit_but.image_rect, pos):
                    off_screen_except(0.5)
        if setnv11:
            nv11 = nhanVat("nv11", w11_name[int(wi11)], w11_x, 200, 120, 120)
            nv11.draw_nv()
            if nv11.check_vc(box_but1):
                boom_but1.draw_but(screen)
                if 1 <= lucky1 <= 90:
                    x1 = nv11.buff_speed(0)
                if 90 < lucky1 <= 100:
                    w11_x = finish

            nv12 = nhanVat("nv12", w12_name[int(wi11)], w12_x, 325, 120, 120)
            nv12.draw_nv()
            if nv12.check_vc(box_but2):
                boom_but2.draw_but(screen)
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 90:
                    x2 = nv12.buff_speed(1)
                if 90 < lucky <= 100:
                    w12_x = finish

            nv13 = nhanVat("nv13", w13_name[int(wi11)], w13_x, 450, 120, 120)
            nv13.draw_nv()
            if nv13.check_vc(box_but3):
                boom_but3.draw_but(screen)
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 90:
                    x3 = nv13.buff_speed(2)
                if 90 < lucky <= 100:
                    w13_x = finish

            nv14 = nhanVat("nv14", w14_name[int(wi11)], w14_x, 550, 120, 120)
            nv14.draw_nv()
            if nv14.check_vc(box_but4):
                boom_but4.draw_but(screen)
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 90:
                    x4 = nv14.buff_speed(3)
                if 90 < lucky <= 100:
                    w14_x = finish

            nv15 = nhanVat("nv15", w15_name[int(wi11)], w15_x, 650, 120, 120)
            nv15.draw_nv()
            if nv15.check_vc(box_but5):
                boom_but5.draw_but(screen)
                lucky = random.randrange(1, 100)
                if 1 <= lucky <= 90:
                    x5 = nv15.buff_speed(4)
                if 90 < lucky <= 100:
                    w15_x = finish

        if min(w11_x, w12_x, w13_x, w14_x, w15_x) > finish + 10:
            off_screen_except(8)
            background6.draw_bg(screen)
            exit_but.draw_but(screen)
            if check_press(exit_but.image_rect, pos):
                off_screen_except(0.5)

    if set3:
        map3(pos)
        if check_press(exit_but.image_rect, pos):
            off_screen_except(0.5)
            time.sleep(0.2)

        car1_but = Button(car1, w11_x, 225, 140, 90)
        car2_but = Button(car2, w12_x, 325, 160, 90)
        car3_but = Button(car3, w13_x, 450, 160, 90)
        car4_but = Button(car4, w14_x, 550, 160, 90)
        car5_but = Button(car5, w15_x, 675, 160, 90)

        car1_but.draw_but(screen)
        car2_but.draw_but(screen)
        car3_but.draw_but(screen)
        car4_but.draw_but(screen)
        car5_but.draw_but(screen)

        if car1_but.image_rect.colliderect(box_but1.image_rect):
            bonus = random.randrange(1, 100)
            if 1 < bonus < 70:
                x1 = 1.2  # max speed
            if 70 < bonus < 100:
                x1 = 3
        if car2_but.image_rect.colliderect(box_but2.image_rect):
            bonus = random.randrange(1, 100)
            if 1 < bonus < 70:
                x2 = 1.2  # max speed
            if 70 < bonus < 100:
                x2 = 3

        if car3_but.image_rect.colliderect(box_but3.image_rect):
            bonus = random.randrange(1, 100)
            if 1 < bonus < 70:
                x3 = 1.2  # max speed
            if 70 < bonus < 100:
                x3 = 3

        if car4_but.image_rect.colliderect(box_but4.image_rect):
            bonus = random.randrange(1, 100)
            if 1 < bonus < 70:
                x4 = 1.2  # max speed
            if 70 < bonus < 100:
                x4 = 3

        if car5_but.image_rect.colliderect(box_but5.image_rect):
            bonus = random.randrange(1, 100)
            if 1 < bonus < 70:
                x5 = 1.2  # max speed
            if 70 < bonus < 100:
                x5 = 3

        if min(w11_x, w12_x, w13_x, w14_x, w15_x) > finish + 10:
            off_screen_except(8)
            background6.draw_bg(screen)
            exit_but.draw_but(screen)
            if check_press(exit_but.image_rect, pos):
                off_screen_except(0.5)
    if lang:
        language_screen()
    if minigame_bool:
        minigame_screen()
    if rule_bool:
        rule_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 4:
                    y += 50
                elif event.button == 5:
                    if y >= 10:
                        y -= 50
        crop_rect = pygame.Rect(220, y, 550, 400)
        screen.blit(rule_info, (350, 260), crop_rect)

    if choosenv_bool1:
        choose_nv_screen1()
    if choosenv_bool2:
        choose_nv_screen2()
    if flap:
        pass
    pygame.display.update()
    clock.tick(60)
