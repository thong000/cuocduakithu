from datetime import datetime

import pygame
import random
import sys
import time
import re

pygame.init()
write_history_active=False
def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        numbers = re.findall(r'\d+', text)
        numeric_values = [int(number) for number in numbers]
        return numeric_values[0]
with open('user.txt', 'r') as file:
    user = file.read()
def write_history(nv, result, bet, earn,nguon):
    current_date = datetime.now().date()
    formatted_date = current_date.strftime("%d/%m/%Y")
    current_time = datetime.now()
    hour = current_time.hour
    minute = current_time.minute

    time = str(hour) + "h" + str(minute) + "p" + "-" + str(formatted_date)

    stt = int(read_file("account/" + str(user) + "/stt.txt"))
    global write_history_active
    if write_history_active:
        with open('account/' + str(user) + '/stt.txt', 'w') as file:
            file.write(str(int(stt) + 1))
            write_history_active = False
    with open('account/' + str(user) + '/history.txt', 'a') as file:
        file.write(
            str(int(stt)) + ',' + str(nv) + ',' + str(result) + ',' + str(bet) + ',' + str(earn) + ',' + str(time)+','+str(nguon))
        file.write('\n')



class Flappy_bird:
    def __init__(self):
        self.gravity = 0.1
        self.bird_movement = 0
        self.game_active = False

        # chen BG va floor
        self.bg = pygame.transform.scale(pygame.image.load('Flappy_Bird/assets/background-night.png'), (500, 768))
        self.floor = pygame.transform.scale2x(pygame.image.load('Flappy_Bird/assets/floor.png'))
        self.floor_x = 0

        # kieu chu
        self.game_font = pygame.font.Font('Flappy_Bird/04B_19.TTF', 40)

        # bang diem
        self.score = 0
        self.high_score = 0

        # tao chim
        self.bird_down = pygame.transform.scale2x(pygame.image.load('Flappy_Bird/assets/yellowbird-downflap.png'))
        self.bird_up = pygame.transform.scale2x(pygame.image.load('Flappy_Bird/assets/yellowbird-upflap.png'))
        self.bird_mid = pygame.transform.scale2x(pygame.image.load('Flappy_Bird/assets/yellowbird-midflap.png'))
        self.bird_list = [self.bird_up, self.bird_mid, self.bird_down]
        self.bird_rect = self.bird_mid.get_rect(center=(100, 384))
        self.bird_index = 0

        # tao pipe
        self.pipe_surface = pygame.transform.scale2x(pygame.image.load('Flappy_Bird/assets/pipe-green.png'))
        self.pipe_list = []
        self.pipe_height = [200, 250, 300, 350, 400]

        # tao timer
        self.spawnpipe = pygame.USEREVENT
        pygame.time.set_timer(self.spawnpipe, 1200)

        # gameover
        self.game_over = pygame.image.load('Flappy_Bird/assets/begin.png')
        self.game_over_rect = self.game_over.get_rect(center=(250, 384))

        # chem am thanh
        self.flap_sound = pygame.mixer.Sound('Flappy_Bird/sound\sfx_wing.wav')
        self.hit_sound = pygame.mixer.Sound('Flappy_Bird/sound\sfx_die.wav')
        self.score_sound = pygame.mixer.Sound('Flappy_Bird/sound\sfx_point.wav')

        # nút exit
        self.exit_button = self.game_font.render('EXIT', True, (255, 255, 255))
        self.exit_button_rect = self.exit_button.get_rect(topleft=(400, 700))

        self.limit_money = 10

    def draw_floor(self, screen):
        screen.blit(self.floor, (self.floor_x, 600))
        screen.blit(self.floor, (self.floor_x + 432, 600))

    def create_pipe(self):
        random_pipe_pos = random.choice(self.pipe_height)
        bottom_pipe = self.pipe_surface.get_rect(midtop=(700, random_pipe_pos))
        top_pipe = self.pipe_surface.get_rect(midtop=(700, random_pipe_pos - 700))
        self.pipe_list.extend((bottom_pipe, top_pipe))

    def move_pipe(self):
        if self.pipe_list is not None:
            for pipe in self.pipe_list:
                pipe.centerx -= 5

    def draw_pipe(self, screen):
        for pipe in self.pipe_list:
            if pipe.bottom >= 600:
                screen.blit(self.pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(self.pipe_surface, False, True)
                screen.blit(flip_pipe, pipe)

    def check_collision(self):
        for pipe in self.pipe_list:
            if self.bird_rect.colliderect(pipe) or self.bird_rect.bottom >= 650 or self.bird_rect.top <= 0:
                self.hit_sound.play()
                return False
        return True

    def rotate_bird(self, bird):
        new_bird = pygame.transform.rotozoom(bird, self.bird_movement * -3, 1)
        return new_bird

    def score_display(self, screen, money):
        score_surface = self.game_font.render(str(self.score), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(300, 50))
        screen.blit(score_surface, score_rect)

        score_surface_1 = self.game_font.render('Score :', True, (255, 255, 255))
        score_rect.center = (140, 50)
        screen.blit(score_surface_1, score_rect)

        money_surface = self.game_font.render(str(money), True, (255, 255, 255))
        score_rect.center = (140, 100)
        screen.blit(money_surface, score_rect)

        if self.game_active == False:
            high_score_surface = self.game_font.render(str(self.high_score), True, (255, 255, 255))
            score_rect.center = (340, 700)
            screen.blit(high_score_surface, score_rect)

            high_score_surface_1 = self.game_font.render('High score :', True, (255, 255, 255))
            score_rect.center = (80, 700)
            screen.blit(high_score_surface_1, score_rect)

    def Flappy_bird_game(self, screen, money):
        screen = pygame.display.set_mode((500, 768))
        out_game = False
        while True:
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.game_active == True:
                        self.bird_movement = -5
                        self.flap_sound.play()
                    if event.key == pygame.K_SPACE and self.game_active == False:
                        self.game_active = True
                        self.bird_movement = 0
                        self.bird_rect.center = (100, 384)
                        self.score = 0
                if event.type == self.spawnpipe:
                    if (len(self.pipe_list) != 0):
                        self.score += 1
                        self.score_sound.play()
                    self.create_pipe()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.exit_button_rect.collidepoint(pos):
                        out_game = True

            if out_game:
                self.game_active = True
                self.bird_movement = 0
                self.bird_rect.center = (100, 384)
                self.score = 0
                self.pipe_list.clear()
                break

            screen.blit(self.bg, (0, 0))

            if self.game_active:
                # chim
                self.bird_index += 1
                self.bird_index %= 42
                bird = self.bird_list[int(self.bird_index / 14)]
                self.bird_movement += self.gravity
                self.bird_rect.centery += self.bird_movement
                screen.blit(self.rotate_bird(bird), self.bird_rect)
                self.game_active = self.check_collision()

                # ong
                self.move_pipe()
                self.draw_pipe(screen)
            else:
                screen.blit(self.game_over, self.game_over_rect)
                if self.pipe_list is not None:
                    self.pipe_list.clear()
                self.high_score = max(self.high_score, self.score)
                if self.limit_money > 0:
                    old_money=money
                    money += min(self.limit_money, self.score)
                    if money-old_money>0:
                        global write_history_active
                        write_history_active=True
                        write_history("-","-","-",min(self.limit_money, self.score),"Flappy Bird")
                    else:
                        write_history_active=False
                self.limit_money -= self.score
                self.score = 0
                # san
            self.floor_x -= 1
            if self.floor_x == -432:
                self.floor_x = 0
            self.draw_floor(screen)

            # bang diem
            self.score_display(screen, money)

            screen.blit(self.exit_button, self.exit_button_rect)
            pygame.display.update()

        return money


screen = pygame.display.set_mode((1400, 800))
bird = Flappy_bird()
clock = pygame.time.Clock()  # Dat fps cho game


def play(money):
    clock.tick(60)
    money = bird.Flappy_bird_game(screen, money)
    return money
