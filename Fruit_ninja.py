import pygame, random, sys,re
from datetime import datetime
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




class Fruit_ninja:

    def __init__(self):

        self.game_font = pygame.font.Font('Chem_chuoi/Roboto-Black.ttf', 50)
        self.game_font2 = pygame.font.Font('Chem_chuoi/Roboto-Black.ttf', 100)

        self.bg = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/bg.png'), (1300, 768))

        self.game_active = True

        #trai cay
        self.watermelon = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/watermelon2.png'), (170,170))
        self.strawberry = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/strawberry_2.png'), (70, 70))
        self.pear = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/pear_2.png'), (100, 100))
        self.apple = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/app.png'), (120, 120))
        self.bomb = pygame.transform.scale(pygame.image.load('Chem_chuoi/picture/bomb.png'), (100, 100))

        self.fruit_list = [self.watermelon, self.strawberry, self.pear, self.bomb, self.apple, self.bomb]
        self.fruit_high = [50 , 100, 150, 200]
        self.fruits = []
        self.fruits_rect = []
        self.fruits_fall = []
        self.fruits_direction = []
        self.fruits_active = []
        self.fruits_rotate = []
        self.fruits_limit = []

        #tao timer
        self.spawn_fruit = pygame.USEREVENT
        pygame.time.set_timer(self.spawn_fruit, 1000)

        #tao score
        self.score = 0
        self.high_score = 0

        self.player_heart = 3

        self.check_change_screen = False

        #nut exit
        self.exit_button = pygame.font.Font('Chem_chuoi/Roboto-Black.ttf', 60).render('EXIT', True, (255, 255, 255))
        self.exit_button_rect = self.exit_button.get_rect(topleft = (1100, 700))

        #tao vet nuoc
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
        fruit_rect = fruit.get_rect(center = (pos_x, 800))
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
        for i in range (1, len(self.fruits)):
            if self.fruits_active[i]:
                screen.blit(self.rotate_fruit(i), self.fruits_rect[i])

    def rotate_fruit(self, i):
        new_fruit = pygame.transform.rotozoom(self.fruits[i], -3 * self.fruits_rotate[i], 1)
        return new_fruit

    def update(self):
        for i in range (1, len(self.fruits_rect)):
            self.fruits_rect[i].centery -= 10 * self.fruits_fall[i]
            if self.fruits_rect[i].centery <= self.fruits_limit[i]:
                self.fruits_fall[i] = -1
            self.fruits_rect[i].centerx += self.fruits_direction[i]
            self.fruits_rotate[i] += 1

    def game_over(self, screen):
        lose = self.game_font2.render('GAME OVER!', True, (255, 255, 255))
        lose_rect = lose.get_rect(center = (650, 384))
        screen.blit(lose, lose_rect)
    
    def draw_score(self, screen, money):
        if self.game_active:
            score_surface = self.game_font.render(str(self.score), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center = (280, 50))
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
            score_rect = score_surface.get_rect(center = (380, 50))
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
                    for i in range (0, len(self.fruits)):
                        if self.fruits_rect[i].collidepoint(pos) and self.fruits_active[i] == True:
                            if self.fruits[i] != self.bomb:
                                self.fruits_active[i] = False
                                self.score += 1
                            else:
                                self.player_heart -= 1
                                self.fruits_active[i] = False
                            self.choose_scrath(i)
                            self.scrath_rect.append(self.scrath_red.get_rect(center = pos))
                            self.scrath_timer.append(1)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.game_active == False:
                        self.game_active = True
                        self.player_heart = 3
                        self.score = 0
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.exit_button_rect.collidepoint(pos):
                        out_game = True
                        
            if out_game:
                self.fruits = []
                self.fruits_rect = []
                self.fruits_fall = []
                self.fruits_direction = []
                self.fruits_active = []
                self.fruits_rotate = []
                self.fruits_limit = []
                self.player_heart = 3
                self.score = 0
                break

            screen.blit(self.bg, (0,0))

            if self.game_active:
        
                self.update()

                self.draw_fruit(screen)

                for i in range (0, len(self.fruits)):
                    if self.fruits_active[i] == True and self.fruits_rect[i].centery >= 768 and self.fruits_fall[i] < 0 and self.fruits[i] != self.bomb:
                        self.player_heart -= 1
                        self.fruits_active[i] = False
                
                if self.player_heart == 0:
                    self.game_active = False
                    self.high_score = max(self.high_score, self.score)
                    if self.limit_money > 0:
                        old_money = money
                        money += min(self.limit_money, self.score)
                        if money - old_money > 0:
                            global write_history_active
                            write_history_active = True
                            write_history("-", "-", "-", min(self.limit_money, self.score),"Fruit Ninja")
                        else:
                            write_history_active = False
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

screen = pygame.display.set_mode((1400, 800))
clock = pygame.time.Clock() #Dat fps cho game
fruit = Fruit_ninja()
def play(money):
    money = fruit.fruit_ninja_game_play(screen, money)
    return money
