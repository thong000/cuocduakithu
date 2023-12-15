from datetime import datetime

import pygame, random, sys,re
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


class Snake_game:
    def __init__(self):
        #Background
        self.bg = pygame.transform.scale(pygame.image.load('Snake_game/Picture/BG'), (1000, 800))

        #snake body
        self.body = pygame.transform.scale(pygame.image.load('Snake_game/Picture/body.png'), (50, 50))
        self.body_list = []
        self.body_list.append(self.body.get_rect(topleft = (0, 0)))
        self.body_pos_x = 0
        self.body_pos_y = 0
        
        #food
        self.food = pygame.transform.scale(pygame.image.load('Snake_game/Picture/food.png'), (50, 50))
        self.food_rect = self.food.get_rect(topleft = (500, 500))
        self.food_time = 0

        self.score = 0
        self.gameover = False

        self.change = 'down'
        self.direction = 'down'

        #self.game_font = pygame.font.Font('Roboto-Black.ttf', 100)
        #self.game_font2 = pygame.font.Font('Roboto-Black.ttf', 60)
        #self.game_font3 = pygame.font.Font('Roboto-Black.ttf', 30)

        self.gameover_surface =  pygame.font.Font('Snake_game/Roboto-Black.ttf', 100).render('GAME OVER !!!', True, (255, 255, 255))
        self.gameover_rect = self.gameover_surface.get_rect(center = (500, 300))
        self.play_again = pygame.font.Font('Snake_game/Roboto-Black.ttf', 60).render('Tap to play again', True, (255, 255, 255))
        self.play_again_rect = self.play_again.get_rect(center = (500, 500))
        self.score_display = pygame.font.Font('Snake_game/Roboto-Black.ttf', 30).render('Score:', True, (255, 255, 255))
        self.score_display_rect = self.score_display.get_rect(center = (50, 50))


        #nút exit
        self.exit_button = pygame.font.Font('Snake_game/Roboto-Black.ttf', 60).render('EXIT', True, (255, 255, 255))
        self.exit_button_rect = self.exit_button.get_rect(topleft = (850, 700))

        self.limit_money = 10
    
    def check_collision(self):
        for snake in self.body_list:
            if self.food_rect.colliderect(snake):
                self.score += 1
                self.new_food()

    def check_food(self, pos_x, pos_y):
        for body in self.body_list:
            if body.topleft == (pos_x, pos_y):
                return True
        return False

    def new_food(self):
        new_pos_x = random.random()
        new_pos_x *= 10000
        new_pos_x = int(new_pos_x)
        new_pos_x %= 20

        new_pos_y = random.random()
        new_pos_y *= 10000
        new_pos_y = int(new_pos_y)
        new_pos_y %= 15
        new_pos_y += 1

        while self.check_food(new_pos_x * 50, new_pos_y * 50):
            new_pos_x = random.random()
            new_pos_x *= 10000
            new_pos_x = int(new_pos_x)
            new_pos_x %= 20

            new_pos_y = random.random()
            new_pos_y *= 10000
            new_pos_y = int(new_pos_y)
            new_pos_y %= 15
            new_pos_y += 1  

        self.food_rect.topleft = (new_pos_x * 50, new_pos_y * 50)

    def check_game_over(self):
        head = self.body_list[0]
        for i in range (1, len(self.body_list)):
            if head.colliderect(self.body_list[i]):
                self.gameover = True

        for body in self.body_list:
            if body.centerx > 1000 or body.centerx < 0 or body.centery > 800 or body.centery < 0:
                self.gameover = True

    def change_direction(self):
        if self.change == 'up' and self.direction != 'down':
            self.direction = 'up'
        
        if self.change == 'down' and self.direction != 'up':
            self.direction = 'down'

        if self.change == 'left' and self.direction != 'right':
            self.direction = 'left'
        
        if self.change == 'right' and self.direction != 'left':
            self.direction = 'right'
    
    def change_pos(self):
        if self.direction == 'up':
            self.body_pos_y -= 50
        if self.direction == 'down':
            self.body_pos_y += 50
        if self.direction == 'left':
            self.body_pos_x -= 50
        if self.direction == 'right':
            self.body_pos_x += 50

    def draw_body(self, screen):
        for body_rect in self.body_list:
            screen.blit(self.body, body_rect)

    def Snake_game_play(self, screen, money):
        clock = pygame.time.Clock() #Dat fps cho game
        screen = pygame.display.set_mode((1000, 800))
        out_game = False
        while True:
            clock.tick(10)
            screen.blit(self.bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.change = 'up'
                    if event.key == pygame.K_DOWN:
                        self.change = 'down'
                    if event.key == pygame.K_LEFT:
                        self.change = 'left'
                    if event.key == pygame.K_RIGHT:
                        self.change = 'right'
                    if event.key == pygame.K_SPACE and self.gameover == True:
                        self.gameover = False
                        self.body_list = []
                        self.body_list.append(self.body.get_rect(topleft = (0, 0)))
                        self.score = 0
                        self.body_pos_x = 0
                        self.body_pos_y = 0
                        self.direction = 'down'
                        self.change = 'down'
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.exit_button_rect.collidepoint(pos):
                        out_game = True
            
            if out_game:
                self.gameover = False
                self.body_list = []
                self.body_list.append(self.body.get_rect(topleft = (0, 0)))
                self.score = 0
                self.body_pos_x = 0
                self.body_pos_y = 0
                self.direction = 'down'
                self.change = 'down'
                break

            if self.gameover == False:

                self.food_time += 1
                self.food_time %= 10

                if self.food_time < 6:
                    screen.blit(self.food, self.food_rect)

                self.change_direction()

                self.change_pos()

                self.body_list.insert(0,self.body.get_rect(topleft = (self.body_pos_x, self.body_pos_y)))
                if(self.score != len(self.body_list) - 1):
                    self.body_list.pop()

                self.draw_body(screen)

                self.check_collision()

                self.check_game_over()

                if self.gameover:
                    if self.limit_money > 0:
                        old_money = money
                        money += min(self.limit_money, self.score)
                        if money - old_money > 0:
                            global write_history_active
                            write_history_active = True
                            write_history("-", "-", "-", min(self.limit_money, self.score),"Snake Game")
                        else:
                            write_history_active = False
                    self.limit_money -= self.score
                    self.score = 0 
                
                score_surface = pygame.font.Font('Snake_game/Roboto-Black.ttf', 30).render(str(self.score), True, (255, 255, 255))
                score_rect = score_surface.get_rect(center = (120, 50))
                screen.blit(score_surface, score_rect)
                screen.blit(self.score_display, self.score_display_rect)
            else:
                screen.blit(self.gameover_surface, self.gameover_rect)
                screen.blit(self.play_again, self.play_again_rect)
            
            #ve tien
            money_surface = pygame.font.Font('Snake_game/Roboto-Black.ttf', 30).render(str(money), True, (255, 255, 255))
            score_rect = money_surface.get_rect(center = (120, 100))
            screen.blit(money_surface, score_rect)


            screen.blit(self.exit_button, self.exit_button_rect)

            pygame.display.update()
        return money

snake = Snake_game()
screen = pygame.display.set_mode((1400, 800))
def play(money):
    money = snake.Snake_game_play(screen, money)
    return money
