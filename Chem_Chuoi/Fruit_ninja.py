import pygame, random, sys

pygame.init()


class Fruit_ninja:

    def __init__(self):

        self.game_font = pygame.font.Font('Chem_Chuoi/Roboto-Black.ttf', 50)
        self.game_font2 = pygame.font.Font('Chem_Chuoi/Roboto-Black.ttf', 100)

        self.bg = pygame.transform.scale(pygame.image.load('Chem_Chuoi/picture/BG.png'), (1300, 768))

        self.game_active = True

        # trai cay
        self.watermelon = pygame.transform.scale(pygame.image.load('Chem_Chuoi/picture/watermelon2.png'), (170, 170))
        self.strawberry = pygame.transform.scale(pygame.image.load('Chem_Chuoi/picture/strawberry_2.png'), (70, 70))
        self.pear = pygame.transform.scale(pygame.image.load('Chem_Chuoi/picture/pear_2.png'), (100, 100))
        self.bomb = pygame.transform.scale(pygame.image.load('Chem_Chuoi/picture/Bomb.png'), (100, 100))

        self.fruit_list = [self.watermelon, self.strawberry, self.pear, self.bomb]
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
        self.exit_button = pygame.font.Font('Chem_Chuoi/Roboto-Black.ttf', 60).render('EXIT', True, (255, 255, 255))
        self.exit_button_rect = self.exit_button.get_rect(topleft=(1100, 700))

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

    def draw_score(self, screen):
        if self.game_active:
            score_surface = self.game_font.render(str(self.score), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(280, 50))
            screen.blit(score_surface, score_rect)

            score_surface_1 = self.game_font.render('Score :', True, (255, 255, 255))
            score_rect.center = (100, 50)
            screen.blit(score_surface_1, score_rect)

            score_surface = self.game_font.render(str(self.player_heart), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(430, 100))
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

    def fruit_ninja_game_play(self, screen):
        clock.tick(120)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.game_active == False:
                    self.game_active = True
                    self.player_heart = 3
                    self.score = 0
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if self.exit_button_rect.collidepoint(pos):
                    self.exit_game(screen)

        screen.blit(self.bg, (0, 0))

        if self.game_active:

            self.update()

            self.draw_fruit(screen)

            for i in range(0, len(self.fruits)):
                if self.fruits_active[i] == True and self.fruits_rect[i].centery >= 768 and self.fruits_fall[i] < 0 and \
                        self.fruits[i] != self.bomb:
                    self.player_heart -= 1
                    self.fruits_active[i] = False

            if self.player_heart == 0:
                self.game_active = False
                self.high_score = max(self.high_score, self.score)
        else:
            self.game_over(screen)
            self.fruits = []
            self.fruits_rect = []
            self.fruits_high = []
            self.fruits_pos_x = []
            self.fruits_active = []

        self.draw_score(screen)

        screen.blit(self.exit_button, self.exit_button_rect)

    def exit_game(self, screen):
        import game
        global fruit_game
        self.check_change_screen = False


screen = pygame.display.set_mode((1400, 800))
clock = pygame.time.Clock()  # Dat fps cho game
fruit_game = True
fruit = Fruit_ninja()
bg = pygame.transform.scale(pygame.image.load('Chem_Chuoi/menugame.png'), (1400, 800))
while True:
    """if not fruit.check_change_screen:"""
    screen = pygame.display.set_mode((1300, 768))
    fruit.check_change_screen = True
    fruit.fruit_ninja_game_play(screen)

    pygame.display.update()
