import pygame
import random
import subprocess
import sys
import time

import pygments.formatters.irc

pygame.init()
with open('lan.txt', 'r') as file:
    l = file.read()
    if l == "1":
        lan = True
    if l == "0":
        lan = False
# Thông số cơ bản
coin = 0
speed = 5
lock = False
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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cuộc đua kì thú")
# Load backgrounds
bg = pygame.image.load("background\\menugame.png")
bg0 = pygame.image.load("background\\menugamemap.png")
bg1 = pygame.image.load("background\\1.jpg")
bg2 = pygame.image.load("background\\2.jpg")
bg3 = pygame.image.load("background\\3.jpg")
bg4 = pygame.image.load("background\\4.jpg")
bg5 = pygame.image.load("background\\5.jpg")
result = pygame.image.load("background\\result.png")

# vi tri nv
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

x1 = random.uniform(0.8, 1.2)
x2 = random.uniform(0.8, 1.2)
x3 = random.uniform(0.8, 1.2)
x4 = random.uniform(0.8, 1.2)
x5 = random.uniform(0.8, 1.2)

finish = SCREEN_WIDTH // 1.3

game_font1 = pygame.font.Font("font/MuseoModerno-Bold.ttf", 40)
with open('log.txt', 'r') as file:
    content = file.read()
    if content == "1":
        lock = True
    if content == "0":
        lock = False
lan = True
set_ = True
wait = False
set1 = False
set2 = False
set3 = False
set4 = False
set5 = False
setting_bool = False
lang = False


class Background:
    def __init__(self, image, w, h):
        self.bg_img = image
        self.bg_img = pygame.transform.scale(self.bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bg_rect = self.bg_img.get_rect(topleft=(0, 0))

    def draw_bg(self, sur):
        sur.blit(self.bg_img, self.bg_rect)


class Button:
    def __init__(self, image, x, y, w, h):
        self.but_pos = (x, y)
        image = pygame.transform.scale(image, (w, h))
        self.image = image
        self.image_rect = self.image.get_rect(center=(x, y))

    def draw_but(self, sur):
        sur.blit(self.image, self.image_rect)


class Text:
    def __init__(self, font, text, r, g, b, ):
        self.font = font
        self.text = text
        self.font_but = self.font.render(text, True, (r, g, b))

    def draw_text(self, sur, x, y):
        sur.blit(self.font_but, (x, y))


# Load button
play = pygame.image.load("Button\play.png")
choose1 = pygame.image.load("Button\set_but1.png")
choose1vn = pygame.image.load("Button\set_but1vn.png")
choose2 = pygame.image.load("Button\set_but2.png")
choose2vn = pygame.image.load("Button\set_but2vn.png")
choose3 = pygame.image.load("Button\set_but3.png")
choose3vn = pygame.image.load("Button\set_but3vn.png")
choose4 = pygame.image.load("Button\set_but4.png")
choose4vn = pygame.image.load("Button\set_but4vn.png")
choose5 = pygame.image.load("Button\set_but5.png")
choose5vn = pygame.image.load("Button\set_but5vn.png")
exit = pygame.image.load("Button\exit.png")
signup = pygame.image.load("Button\signup.png")
signupvn = pygame.image.load("Button/signupvn.png")
login = pygame.image.load("Button\login.png")
loginvn = pygame.image.load("Button\loginvn.png")
setting = pygame.image.load("Button\setting.png")
logout = pygame.image.load("Button\logout.png")
logoutvn = pygame.image.load("Button/logoutvn.png")
language = pygame.image.load("Button/language.png")
languagevn = pygame.image.load("Button/languagevn.png")
vie = pygame.image.load("Button/vie.png")
eng = pygame.image.load("Button/eng.png")

# Load nv set1 1
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
    w11_name[i] = pygame.transform.scale(w11_name[i], (90, 90))

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
    w12_name[i] = pygame.transform.scale(w12_name[i], (90, 90))

# Load nv set1 3
w13_name = ["w130", "w131", "w132", "w133", "w134", "w135", "w136", "w137", "w138", "w139", "w1310", "w1311", "w1312",
            "w1313", "w1314", "w315", "w1316", "w1317", ]
w13_loca = ["set01\PNG3 Sequences\Walking\w130.png",
            "set01\PNG3 Sequences\Walking\w131.png",
            "set01\PNG3 Sequences\Walking\w132.png",
            "set01\PNG3 Sequences\Walking\w133.png",
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
    w13_name[i] = pygame.transform.scale(w13_name[i], (90, 90))

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
    w14_name[i] = pygame.transform.scale(w14_name[i], (90, 90))

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
    w15_name[i] = pygame.transform.scale(w15_name[i], (90, 90))

w21_name = ["w210", "w211", "w212", "w213", "w214", "w215", "w216", "w217", "w218", "w219", "w2110", "w2111"]

w21_loca = ["set02\PNG1 Sequences\Walking\w210.png",
            "set02\PNG1 Sequences\Walking\w211.png",
            "set02\PNG1 Sequences\Walking\w212.png",
            "set02\PNG1 Sequences\Walking\w213.png",
            "set02\PNG1 Sequences\Walking\w214.png",
            "set02\PNG1 Sequences\Walking\w211.png",
            "set02\PNG1 Sequences\Walking\w216.png",
            "set02\PNG1 Sequences\Walking\w217.png",
            "set02\PNG1 Sequences\Walking\w218.png",
            "set02\PNG1 Sequences\Walking\w219.png",
            "set02\PNG1 Sequences\Walking\w2110.png",
            "set02\PNG1 Sequences\Walking\w2111.png"]

for i in range(0, 12):
    w21_name[i] = pygame.image.load(w21_loca[i])
    w21_name[i] = pygame.transform.scale(w21_name[i], (100, 100))

w22_name = ["w220", "w221", "w222", "w223", "w224", "w225", "w226", "w227", "w228", "w229", "w2210", "w2211"]

w22_loca = ["set02\PNG2 Sequences\Walking\w220.png",
            "set02\PNG2 Sequences\Walking\w221.png",
            "set02\PNG2 Sequences\Walking\w222.png",
            "set02\PNG2 Sequences\Walking\w223.png",
            "set02\PNG2 Sequences\Walking\w224.png",
            "set02\PNG2 Sequences\Walking\w221.png",
            "set02\PNG2 Sequences\Walking\w226.png",
            "set02\PNG2 Sequences\Walking\w227.png",
            "set02\PNG2 Sequences\Walking\w228.png",
            "set02\PNG2 Sequences\Walking\w229.png",
            "set02\PNG2 Sequences\Walking\w2210.png",
            "set02\PNG2 Sequences\Walking\w2211.png"]

for i in range(0, 12):
    w22_name[i] = pygame.image.load(w22_loca[i])
    w22_name[i] = pygame.transform.scale(w22_name[i], (100, 100))
w23_name = ["w230", "w231", "w232", "w233", "w234", "w235", "w236", "w237", "w238", "w239", "w2310", "w2311"]

w23_loca = ["set02\PNG3 Sequences\Walking\w230.png",
            "set02\PNG3 Sequences\Walking\w231.png",
            "set02\PNG3 Sequences\Walking\w232.png",
            "set02\PNG3 Sequences\Walking\w233.png",
            "set02\PNG3 Sequences\Walking\w234.png",
            "set02\PNG3 Sequences\Walking\w231.png",
            "set02\PNG3 Sequences\Walking\w236.png",
            "set02\PNG3 Sequences\Walking\w237.png",
            "set02\PNG3 Sequences\Walking\w238.png",
            "set02\PNG3 Sequences\Walking\w239.png",
            "set02\PNG3 Sequences\Walking\w2310.png",
            "set02\PNG3 Sequences\Walking\w2311.png"]

for i in range(0, 12):
    w23_name[i] = pygame.image.load(w23_loca[i])
    w23_name[i] = pygame.transform.scale(w23_name[i], (100, 100))

w24_name = ["w240", "w241", "w242", "w243", "w244", "w245", "w246", "w247", "w248", "w249", "w2410", "w2411"]

w24_loca = ["set02\PNG4 Sequences\Walking\w240.png",
            "set02\PNG4 Sequences\Walking\w241.png",
            "set02\PNG4 Sequences\Walking\w242.png",
            "set02\PNG4 Sequences\Walking\w243.png",
            "set02\PNG4 Sequences\Walking\w244.png",
            "set02\PNG4 Sequences\Walking\w241.png",
            "set02\PNG4 Sequences\Walking\w246.png",
            "set02\PNG4 Sequences\Walking\w247.png",
            "set02\PNG4 Sequences\Walking\w248.png",
            "set02\PNG4 Sequences\Walking\w249.png",
            "set02\PNG4 Sequences\Walking\w2410.png",
            "set02\PNG4 Sequences\Walking\w2411.png"]

for i in range(0, 12):
    w24_name[i] = pygame.image.load(w24_loca[i])
    w24_name[i] = pygame.transform.scale(w24_name[i], (100, 100))

w25_name = ["w250", "w251", "w252", "w253", "w254", "w255", "w256", "w257", "w258", "w259", "w2510", "w2511"]

w25_loca = ["set02\PNG5 Sequences\Walking\w250.png",
            "set02\PNG5 Sequences\Walking\w251.png",
            "set02\PNG5 Sequences\Walking\w252.png",
            "set02\PNG5 Sequences\Walking\w253.png",
            "set02\PNG5 Sequences\Walking\w254.png",
            "set02\PNG5 Sequences\Walking\w251.png",
            "set02\PNG5 Sequences\Walking\w256.png",
            "set02\PNG5 Sequences\Walking\w257.png",
            "set02\PNG5 Sequences\Walking\w258.png",
            "set02\PNG5 Sequences\Walking\w259.png",
            "set02\PNG5 Sequences\Walking\w2510.png",
            "set02\PNG5 Sequences\Walking\w2511.png"]

for i in range(0, 12):
    w25_name[i] = pygame.image.load(w25_loca[i])
    w25_name[i] = pygame.transform.scale(w25_name[i], (100, 100))

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
    w41_name[i] = pygame.transform.scale(w41_name[i], (90, 90))

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
    w42_name[i] = pygame.transform.scale(w42_name[i], (90, 90))

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
    w43_name[i] = pygame.transform.scale(w43_name[i], (90, 90))

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
    w44_name[i] = pygame.transform.scale(w44_name[i], (90, 90))

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
    w45_name[i] = pygame.transform.scale(w45_name[i], (90, 90))

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
    w51_name[i] = pygame.transform.scale(w51_name[i], (100, 100))
w52_name = ["w5201", "w5202", "w5203", "w5204", "w5205", "w5206", "w5207", "w5208", "w5209", "w5210", "w5211", "w5212",
            "w5213", "w5214", "w5215", "w5216", "w5217", "w528"]
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
    "set05\PNG2 Sequences\Walking\w5218.png", ]
for i in range(0, 18):
    w52_name[i] = pygame.image.load(w52_loca[i])
    w52_name[i] = pygame.transform.scale(w52_name[i], (100, 100))

w53_name = ["w5301", "w5302", "w5303", "w5304", "w5305", "w5306", "w5307", "w5308", "w5309", "w5310", "w5311", "w5312",
            "w5313", "w5314", "w5315", "w5316", "w5317", "w538"]
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
    "set05\PNG3 Sequences\Walking\w5318.png", ]
for i in range(0, 18):
    w53_name[i] = pygame.image.load(w53_loca[i])
    w53_name[i] = pygame.transform.scale(w53_name[i], (100, 100))
w54_name = ["w5401", "w5402", "w5403", "w5404", "w5405", "w5406", "w5407", "w5408", "w5409", "w5410", "w5411", "w5412",
            "w5413", "w5414", "w5415", "w5416", "w5417", "w548"]
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
    "set05\PNG4 Sequences\Walking\w5418.png", ]
for i in range(0, 18):
    w54_name[i] = pygame.image.load(w54_loca[i])
    w54_name[i] = pygame.transform.scale(w54_name[i], (100, 100))
w55_name = ["w5501", "w5502", "w5503", "w5504", "w5505", "w5506", "w5507", "w5508", "w5509", "w5510", "w5511", "w5512",
            "w5513", "w5514", "w5515", "w5516", "w5517", "w558"]
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
    "set05\PNG5 Sequences\Walking\w5518.png", ]
for i in range(0, 18):
    w55_name[i] = pygame.image.load(w55_loca[i])
    w55_name[i] = pygame.transform.scale(w55_name[i], (100, 100))

# Set background
background = Background(bg, SCREEN_WIDTH, SCREEN_HEIGHT)
background0 = Background(bg0, SCREEN_WIDTH, SCREEN_HEIGHT)
background1 = Background(bg1, SCREEN_WIDTH, SCREEN_HEIGHT)
background2 = Background(bg2, SCREEN_WIDTH, SCREEN_HEIGHT)
background3 = Background(bg3, SCREEN_WIDTH, SCREEN_HEIGHT)
background4 = Background(bg4, SCREEN_WIDTH, SCREEN_HEIGHT)
background5 = Background(bg5, SCREEN_WIDTH, SCREEN_HEIGHT)
background6 = Background(result, SCREEN_WIDTH, SCREEN_HEIGHT)

# Set button
play_but = Button(play, int(SCREEN_WIDTH / 2.8), int(SCREEN_HEIGHT / 1.3), SCREEN_WIDTH // 10, SCREEN_HEIGHT // 5)
set1_but = Button(choose1, set_but_x, set_but_y, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)
set2_but = Button(choose2, set_but_x, set_but_y + set_but_dis, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)
set3_but = Button(choose3, set_but_x, set_but_y + 2 * set_but_dis, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)
set4_but = Button(choose4, set_but_x, set_but_y + 3 * set_but_dis, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)
set5_but = Button(choose5, set_but_x, set_but_y + 4 * set_but_dis, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)
exit_but = Button(exit, exit_but_x, exit_but_y, exit_w, exit_h)
demo_map1_but = Button(bg1, demomap_x, demomap_y, demomap_w, demomap_h)
demo_map2_but = Button(bg2, demomap_x, demomap_y, demomap_w, demomap_h)
demo_map3_but = Button(bg3, demomap_x, demomap_y, demomap_w, demomap_h)
demo_map4_but = Button(bg4, demomap_x, demomap_y, demomap_w, demomap_h)
demo_map5_but = Button(bg5, demomap_x, demomap_y, demomap_w, demomap_h)
signup_but = Button(signup, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 1.3, 250, 130)
login_but = Button(login, SCREEN_WIDTH // 2.8, SCREEN_HEIGHT // 1.3, 250, 130)
setting_but = Button(setting, SCREEN_WIDTH // 1.025, SCREEN_HEIGHT // 17, SCREEN_WIDTH // 20, SCREEN_HEIGHT // 12)
logout_but = Button(logout, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
language_but = Button(language, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)

set1vn_but = Button(choose1vn, set_but_x, set_but_y, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)
set2vn_but = Button(choose2vn, set_but_x, set_but_y + set_but_dis, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)
set3vn_but = Button(choose3vn, set_but_x, set_but_y + 2 * set_but_dis, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)
set4vn_but = Button(choose4vn, set_but_x, set_but_y + 3 * set_but_dis, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)
set5vn_but = Button(choose5vn, set_but_x, set_but_y + 4 * set_but_dis, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 4)

signupvn_but = Button(loginvn, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 1.3, 250, 130)
loginvn_but =Button(signupvn, SCREEN_WIDTH // 2.8, SCREEN_HEIGHT // 1.3, 250, 130)

logoutvn_but = Button(logoutvn, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
languagevn_but = Button(languagevn, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
vie_but = Button(vie, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
eng_but = Button(eng, SCREEN_WIDTH // 5, SCREEN_HEIGHT // 1.5, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
# Set text
chooseMap_text = Text(game_font1, "Choose the map", 255, 255, 255)
chooseMapvn_text = Text(game_font1, "Chọn bản đồ", 255, 255, 255)


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


def off_screen_except(x):
    global set_, wait, set1, set2, set3, set4, set5, setting_bool, result, lang
    set_ = False
    wait = False
    set1 = False
    set2 = False
    set3 = False
    set4 = False
    set5 = False
    result = False
    lang = False
    setting_bool = False
    if x == 0:
        set_ = True
    if x == 1:
        set1 = True
    if x == 2:
        set2 = True
    if x == 3:
        set3 = True
    if x == 4:
        set4 = True
    if x == 5:
        set5 = True
    if x == 6:
        setting_bool = True
    if x == 7:
        lang = True
    if x == 0.5:
        wait = True


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
    # global set_, wait, set1, set2, set3, set4, set5, setting_bool
    if set_ and lock == False:
        account_login()
    if lock:
        background.draw_bg(screen)
        play_but.draw_but(screen)
        setting_but.draw_but(screen)
        if check_press(play_but.image_rect, pos):
            off_screen_except(0.5)
        if check_press(setting_but.image_rect, pos):
            off_screen_except(6)
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
        set4_but.draw_but(screen)
        set5_but.draw_but(screen)
    else:
        set1vn_but.draw_but(screen)
        set2vn_but.draw_but(screen)
        set3vn_but.draw_but(screen)
        set4vn_but.draw_but(screen)
        set5vn_but.draw_but(screen)

    if set1_but.image_rect.collidepoint(pos):
        demo_map1_but.draw_but(screen)
        if pygame.mouse.get_pressed()[0] == 1:
            off_screen_except(1)
            global coin_bool
            coin_bool=True

    if set2_but.image_rect.collidepoint(pos):
        demo_map2_but.draw_but(screen)
        if pygame.mouse.get_pressed()[0] == 1:
            off_screen_except(2)
    if set3_but.image_rect.collidepoint(pos):
        demo_map3_but.draw_but(screen)
        if pygame.mouse.get_pressed()[0] == 1:
            off_screen_except(3)
    if set4_but.image_rect.collidepoint(pos):
        demo_map4_but.draw_but(screen)
        if pygame.mouse.get_pressed()[0] == 1:
            off_screen_except(4)
    if set5_but.image_rect.collidepoint(pos):
        demo_map5_but.draw_but(screen)
        if pygame.mouse.get_pressed()[0] == 1:
            off_screen_except(5)

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


def setting_screen():
    background0.draw_bg(screen)
    exit_but.draw_but(screen)
    logout_but.draw_but(screen)
    language_but.draw_but(screen)

    if check_press(logout_but.image_rect, pos):
        with open('log.txt', 'w') as file:
            file.write('0')
        off_screen_except(0)
    if check_press(exit_but.image_rect, pos):
        off_screen_except(0)
    if check_press(language_but.image_rect, pos):
        language_screen()


def exit_to_wait():
    off_screen_except(0.5)


def map1(pos):
    background1.draw_bg(screen)
    exit_but.draw_but(screen)
    if check_press(exit_but.image_rect, pos):
        off_screen_except(0.5)
        time.sleep(0.2)


def map2(pos):
    off_screen_except(2)
    background2.draw_bg(screen)
    exit_but.draw_but(screen)
    if check_press(exit_but.image_rect, pos):
        off_screen_except(0.5)
        time.sleep(0.2)


def map3(pos):
    off_screen_except(3)
    background3.draw_bg(screen)
    exit_but.draw_but(screen)
    if check_press(exit_but.image_rect, pos):
        off_screen_except(0.5)
        time.sleep(0.2)


def map4(pos):
    off_screen_except(4)
    background4.draw_bg(screen)
    exit_but.draw_but(screen)
    if check_press(exit_but.image_rect, pos):
        off_screen_except(0.5)
        time.sleep(0.2)


def map5(pos):
    off_screen_except(5)
    background5.draw_bg(screen)
    exit_but.draw_but(screen)
    if check_press(exit_but.image_rect, pos):
        off_screen_except(0.5)
        time.sleep(0.2)


clock = pygame.time.Clock()
while True:
    w11_x += x1
    w12_x += x2
    w13_x += x3
    w14_x += x4
    w15_x += x5
    wi11 += 0.5
    wi12 += 0.5
    wi14 += 0.5
    wi15 += 0.5
    if wi11 == 17: wi11 = 0
    if wi12 == 11: wi12 = 0
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
    global pos
    pos = pygame.mouse.get_pos()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if set_:
        menu_screen()
    if wait:
        wait_screen()
    if setting_bool:
        setting_screen()
    if set1:
        map1(pos)
        if check_press(exit_but.image_rect, pos):
            off_screen_except(0.5)
            time.sleep(0.2)
        nv11 = Button(w11_name[int(wi12)], w11_x, 200, 90, 90)
        nv11.draw_but(screen)
        nv12 = Button(w12_name[int(wi12)], w12_x, 325, 90, 90)
        nv12.draw_but(screen)
        nv13 = Button(w13_name[int(wi12)], w13_x, 450, 90, 90)
        nv13.draw_but(screen)
        nv14 = Button(w14_name[int(wi12)], w14_x, 550, 90, 90)
        nv14.draw_but(screen)
        nv15 = Button(w15_name[int(wi12)], w15_x, 650, 90, 90)
        nv15.draw_but(screen)
    if set2:
        map2(pos)
        if check_press(exit_but.image_rect, pos):
            off_screen_except(0.5)
            time.sleep(0.2)
        nv21 = Button(w21_name[int(wi12)], w11_x, 200, 90, 90)
        nv21.draw_but(screen)
        nv22 = Button(w22_name[int(wi12)], w12_x, 325, 90, 90)
        nv22.draw_but(screen)
        nv23 = Button(w23_name[int(wi12)], w13_x, 450, 90, 90)
        nv23.draw_but(screen)
        nv24 = Button(w24_name[int(wi12)], w14_x, 550, 90, 90)
        nv24.draw_but(screen)
        nv25 = Button(w25_name[int(wi12)], w15_x, 650, 90, 90)
        nv25.draw_but(screen)

    if set3:
        map3(pos)
        if check_press(exit_but.image_rect, pos):
            off_screen_except(0.5)
            time.sleep(0.2)
    if set4:
        map4(pos)
        if check_press(exit_but.image_rect, pos):
            off_screen_except(0.5)
            time.sleep(0.2)
        nv41 = Button(w41_name[int(wi14)], w11_x, 200, 100, 100)
        nv41.draw_but(screen)
        nv42 = Button(w42_name[int(wi14)], w12_x, 325, 100, 100)
        nv42.draw_but(screen)
        nv43 = Button(w43_name[int(wi14)], w13_x, 450, 100, 100)
        nv43.draw_but(screen)
        nv44 = Button(w44_name[int(wi14)], w14_x, 550, 100, 100)
        nv44.draw_but(screen)
        nv45 = Button(w45_name[int(wi14)], w15_x, 650, 100, 100)
        nv45.draw_but(screen)

    if set5:
        map5(pos)
        if check_press(exit_but.image_rect, pos):
            off_screen_except(0.5)
            time.sleep(0.2)
        nv51 = Button(w51_name[int(wi15)], w11_x, 200, 100, 100)
        nv51.draw_but(screen)
        nv52 = Button(w52_name[int(wi15)], w12_x, 325, 100, 100)
        nv52.draw_but(screen)
        nv53 = Button(w53_name[int(wi15)], w13_x, 450, 100, 100)
        nv53.draw_but(screen)
        nv54 = Button(w54_name[int(wi15)], w14_x, 550, 100, 100)
        nv54.draw_but(screen)
        nv55 = Button(w55_name[int(wi15)], w15_x, 650, 100, 100)
        nv55.draw_but(screen)
    if lang:
        language_screen()
    pygame.display.update()
    clock.tick(60)
