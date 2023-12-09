import pygame, random, sys

pygame.init()
snake_game = True


class Snake_game:
    def __init__(self):
        # Background
        self.bg = pygame.transform.scale(pygame.image.load(r'Snake_game\Picture\BG'), (1000, 800))

        # snake body
        self.body = pygame.transform.scale(pygame.image.load(r'Snake_game\Picture\Body.png'), (50, 50))
        self.body_list = []
        self.body_list.append(self.body.get_rect(topleft=(0, 0)))
        self.body_pos_x = 0
        self.body_pos_y = 0

        # food
        self.food = pygame.transform.scale(pygame.image.load(r'Snake_game\Picture\food.png'), (50, 50))
        self.food_rect = self.food.get_rect(topleft=(500, 500))
        self.food_time = 0

        self.score = 0
        self.gameover = False

        self.change = 'down'
        self.direction = 'down'

        # self.game_font = pygame.font.Font('Roboto-Black.ttf', 100)
        # self.game_font2 = pygame.font.Font('Roboto-Black.ttf', 60)
        # self.game_font3 = pygame.font.Font('Roboto-Black.ttf', 30)

        self.gameover_surface = pygame.font.Font('Snake_game/Roboto-Black.ttf', 100).render('GAME OVER !!!', True,
                                                                                            (255, 255, 255))
        self.gameover_rect = self.gameover_surface.get_rect(center=(500, 300))
        self.play_again = pygame.font.Font('Snake_game/Roboto-Black.ttf', 60).render('Tap to play again', True,
                                                                                     (255, 255, 255))
        self.play_again_rect = self.play_again.get_rect(center=(500, 500))
        self.score_display = pygame.font.Font('Snake_game/Roboto-Black.ttf', 30).render('Score:', True, (255, 255, 255))
        self.score_display_rect = self.score_display.get_rect(center=(50, 50))

        self.check_change_screen = False

        # nút exit
        self.exit_button = pygame.font.Font('Snake_game/Roboto-Black.ttf', 60).render('EXIT', True, (255, 255, 255))
        self.exit_button_rect = self.exit_button.get_rect(topleft=(850, 700))

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
        for i in range(1, len(self.body_list)):
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

    def Snake_game_play(self, screen):
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
                    self.body_list.append(self.body.get_rect(topleft=(0, 0)))
                    self.score = 0
                    self.body_pos_x = 0
                    self.body_pos_y = 0
                    self.direction = 'down'
                    self.change = 'down'
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if self.exit_button_rect.collidepoint(pos):
                    self.exit_game(screen)
        if self.gameover == False:

            self.food_time += 1
            self.food_time %= 10

            if (self.food_time < 6):
                screen.blit(self.food, self.food_rect)

            self.change_direction()

            self.change_pos()

            self.body_list.insert(0, self.body.get_rect(topleft=(self.body_pos_x, self.body_pos_y)))
            if (self.score != len(self.body_list) - 1):
                self.body_list.pop()

            self.draw_body(screen)

            self.check_collision()

            self.check_game_over()

            score_surface = pygame.font.Font('Snake_game/Roboto-Black.ttf', 30).render(str(self.score), True,
                                                                                       (255, 255, 255))
            score_rect = score_surface.get_rect(center=(120, 50))
            screen.blit(score_surface, score_rect)
            screen.blit(self.score_display, self.score_display_rect)
        else:
            screen.blit(self.gameover_surface, self.gameover_rect)
            screen.blit(self.play_again, self.play_again_rect)
        screen.blit(self.exit_button, self.exit_button_rect)

    def exit_game(self, screen):
        global snake_game
        self.check_change_screen = False
        import game


snake = Snake_game()
screen = pygame.display.set_mode((1400, 800))
clock = pygame.time.Clock()  # Dat fps cho game
bg = pygame.transform.scale(pygame.image.load('Snake_game/menugame.png'), (1400, 800))
snake_game = True

while True:
    if snake_game:
        if not snake.check_change_screen:
            screen = pygame.display.set_mode((1000, 800))
            snake.check_change_screen = True
        snake.Snake_game_play(screen)

    pygame.display.update()
