# import parameters as p
from button import *
from bird import *
from object import *
from effects import *
from images import *


class Game:
    def __init__(self):
        pygame.display.set_caption('Dinozaur')  # громкость звука 1 - 100%

        icon = pygame.image.load('../Backgrounds/icon.png')
        pygame.display.set_icon(icon)

        pygame.mixer.music.load('../Sounds/background.mp3')
        pygame.mixer.music.set_volume(0.5)

        self.cactus_option = [69, 449, 37, 410, 40, 420]
        self.img_counter = 0
        self.health = 2
        self.make_jump = False
        self.jump_counter = 30
        self.scores = 0
        self.max_scores = 0
        self.max_above = 0
        self.cooldown = 0

    def show_menu(self):
        menu_bckgr = pygame.image.load('../Backgrounds/Menu.jpg')

        pygame.mixer.music.load('../Sounds/Big_Slinker.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        show = True
        start_btn = Button(288, 70)
        quit_btn = Button(120, 70)

        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display.blit(menu_bckgr, (0, 0))
            start_btn.draw(270, 200, 'Start game.', self.start_game, 50)
            quit_btn.draw(358, 300, 'Quit', quit, 50)

            draw_mouse()

            pygame.display.update()
            clock.tick(60)

    def start_game(self):
        while self.game_cycle():
            self.scores = 0
            self.make_jump = False
            self.jump_counter = 30
            p.usr_y = p.display_height - p.usr_height - 100
            self.health = 2
            self.cooldown = 0

    def game_cycle(self):
        # Если хотим чтобы музыка играла всю игру -1, если 1 раз, то 1
        game = True
        cactus_arr = []
        self.create_cactus_arr(cactus_arr)
        land = pygame.image.load('../Backgrounds/Land.jpg')

        stone, cloud = self.open_random_objects()
        heart = Object(display_width, 280, 30, 4, health_image)

        all_btn_bullets = []
        all_ms_bullets = []

        bird1 = Bird(-80)
        bird2 = Bird(-70)

        all_birds = [bird1, bird2]

        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if keys[pygame.K_SPACE]:
                self.make_jump = True

            self.count_scores(cactus_arr)

            display.blit(land, (0, 0))
            print_text('Scores: ' + str(self.scores), 600, 10)

            self.draw_array(cactus_arr)
            self.move_obects(stone, cloud)

            self.draw_dino()

            if keys[pygame.K_ESCAPE]:
                self.pause()

            if not self.cooldown:
                if keys[pygame.K_x]:
                    pygame.mixer.Sound.play(bullet_sound)
                    all_btn_bullets.append(Bullet(p.usr_x + p.usr_width, p.usr_y + 28))
                    self.cooldown = 50
                elif click[0]:
                    pygame.mixer.Sound.play(bullet_sound)
                    add_bullet = Bullet(p.usr_x + p.usr_width, p.usr_y + 28)
                    add_bullet.find_path(mouse[0], mouse[1])
                    all_ms_bullets.append(add_bullet)
                    self.cooldown = 50

            else:
                print_text('Cooldown time:' + str(self.cooldown // 10), 482, 40)
                self.cooldown -= 1

            for bullet in all_btn_bullets:
                if not bullet.move():
                    all_btn_bullets.remove(bullet)

            for bullet in all_ms_bullets:
                if not bullet.move_to():
                    all_ms_bullets.remove(bullet)

            heart.move()
            self.hearts_plus(heart)

            if self.make_jump:
                self.jump()

            if self.check_collision(cactus_arr):
                # pygame.mixer.music.stop()
                # pygame.mixer.Sound.play(fall_sound)
                # if not check_health():
                game = False

            self.show_health()

            #  bird1.draw()
            #  bird2.draw()

            self.draw_birds(all_birds)
            self.check_birds_dmg(all_ms_bullets, all_birds)

            draw_mouse()

            pygame.display.update()
            clock.tick(80)

        return self.game_over()

    def jump(self):
        if self.jump_counter >= -30:
            if self.jump_counter == 30:
                pygame.mixer.Sound.play(jump_sound)
            if self.jump_counter == -30:
                pygame.mixer.Sound.play(fall_sound)

            p.usr_y -= self.jump_counter / 2.5
            self.jump_counter -= 1
        else:
            self.jump_counter = 30
            self.make_jump = False

        print("Y = " + str(p.usr_y))

    def create_cactus_arr(self, array):
        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_option[choice * 2]
        height = self.cactus_option[choice * 2 + 1]
        array.append(Object(display_width + 20, height, width, 4, img))

        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_option[choice * 2]
        height = self.cactus_option[choice * 2 + 1]
        array.append(Object(display_width + 300, height, width, 4, img))

        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_option[choice * 2]
        height = self.cactus_option[choice * 2 + 1]
        array.append(Object(display_width + 600, height, width, 4, img))

    @staticmethod
    def find_radius(array):
        maximum = max(array[0].x, array[1].x, array[2].x)

        if maximum < display_width:
            radius = display_width
            if radius - maximum < 50:
                radius += 280
        else:
            radius = maximum

        choise = random.randrange(0, 5)
        if choise == 0:
            radius += random.randrange(10, 15)
        else:
            radius += random.randrange(250, 400)

        return radius

    def draw_array(self, array):
        for cactus in array:
            check = cactus.move()
            if not check:
                self.object_return(array, cactus)

    def object_return(self, objects, obj):
        radius = self.find_radius(objects)

        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_option[choice * 2]
        height = self.cactus_option[choice * 2 + 1]

        obj.return_self(radius, height, width, img)


    @staticmethod
    def open_random_objects():
        choice = random.randrange(0, 2)
        img_of_stone = stone_img[choice]

        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]

        stone = Object(display_width, display_height - 80, 10, 4, img_of_stone)
        cloud = Object(display_width, 80, 70, 2, img_of_cloud)

        return stone, cloud

    @staticmethod
    def move_obects(stone, cloud):
        check = stone.move()
        if not check:
            choice = random.randrange(0, 2)
            img_of_stone = stone_img[choice]
            stone.return_self(p.display_width, 500 + random.randrange(10, 80), stone.width, img_of_stone)

        check = cloud.move()
        if not check:
            choice = random.randrange(0, 2)
            img_of_cloud = cloud_img[choice]
            cloud.return_self(p.display_width, random.randrange(10, 200), cloud.width, img_of_cloud)

    def draw_dino(self):
        if self.img_counter == 25:
            self.img_counter = 0

        display.blit(dino_img[self.img_counter // 5], (usr_x, usr_y))
        self.img_counter += 1

    @staticmethod
    def pause():
        paused = True

        pygame.mixer.music.pause()

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            print_text('Paused. Press enter to continue.', 160, 300)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                paused = False

            pygame.display.update()
            clock.tick(15)

        pygame.mixer.music.unpause()

    def check_collision(self, barriers):  # проверка на то, персонаж ли игрок с кактусом, или нет
        for barrier in self.barriers:  # проходимся по всем препятствиям, через которые должен перепрыгнуть игрок
            if barrier.y == 449:  # маленький кактус
                if not self.make_jump:  # если не делаем прыжок
                    if barrier.x <= p.usr_x + p.usr_width - 22 <= barrier.x + barrier.width:  # если выполняется это условие
                        if self.check_health():
                            self.object_return(barriers, barrier)
                        else:
                            return True

                elif self.jump_counter >= 0:  # если прыжок начинает возрастать. 1 часть параболы
                    if p.usr_y + p.usr_height - 5 >= barrier.y:  # проверяем координаты по у
                        if barrier.x <= p.usr_x + p.usr_width - 22 <= barrier.x + barrier.width:  # проверка правой координаты
                            if self.check_health():
                                self.object_return(barriers, barrier)
                            else:
                                return True
                else:  # если же вторая часть прыжка
                    if p.usr_y + p.usr_height - 10 >= barrier.y:  # проверяем координаты по у
                        if barrier.x <= p.usr_x <= barrier.x + barrier.width:  # проверка правой координаты
                            if self.check_health():
                                self.object_return(barriers, barrier)
                            else:
                                return True
            else:  # если не маленький кактус
                if not self.make_jump:  # если не делаем прыжок
                    if barrier.x <= p.usr_x + p.usr_width + 5 <= barrier.x + barrier.width:  # если выполняется это условие
                        if self.check_health():
                            self.object_return(barriers, barrier)
                            return False
                        else:
                            return True
                elif self.jump_counter == 10:  # начало прыжка
                    if p.usr_y + p.usr_height - 2 >= barrier.y:  # если есть столкновение по координате y
                        if barrier.x <= p.usr_x + 13 <= barrier.x + barrier.width:  # Если столкнулись
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                elif self.jump_counter <= 1:  # до того момента, как динозавр начнет падать вниз
                    if p.usr_y + p.usr_height - 2 >= barrier.y:  # столкновение по у
                        if barrier.x <= p.usr_x + p.usr_width + 13 <= barrier.x + barrier.width:  # по х координате
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                elif self.jump_counter >= 1:  # игрок совершает 2 часть прыжка
                    if p.usr_y + p.usr_height - 2 >= barrier.y:  # столкновение по у
                        if barrier.x <= p.usr_x + p.usr_width - 22 <= barrier.x + barrier.width:  # по х координате
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                else:
                    if p.usr_y + p.usr_height - 3 >= barrier.y:  # проверяем координаты по у
                        if barrier.x <= p.usr_x + p.usr_width + 5 <= barrier.x + barrier.width:  # проверка правой координаты
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
        return False  # если же ничего не произошло, то возвращаем false, т.е ничего не было

    def count_scores(self, barriers):
        above_cactus = 0

        if -20 < self.jump_counter < 25:
            for barrier in barriers:
                if p.usr_y + p.usr_height - 5 <= barrier.y:
                    if barrier.x <= p.usr_x <= barrier.x + barrier.width:
                        above_cactus += 1
                    elif barrier.x <= p.usr_x + p.usr_width <= barrier.x + barrier.width:
                        above_cactus += 1

            self.max_above = max(self.max_above, above_cactus)
        else:
            if self.jump_counter == -30:
                self.scores += self.max_above
                self.max_above = 0

    def game_over(self):
        if self.scores > self.max_scores:
            self.max_scores = self.scores

        stopped = True
        while stopped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            print_text('Game over. Press enter to play again, Esc to exit.', 40, 300)
            print_text('Max scores: ' + str(self.max_scores), 300, 350)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                return True

            if keys[pygame.K_ESCAPE]:
                return False

            pygame.display.update()
            clock.tick(15)

    def show_health(self):
        show = 0
        x = 20
        while show != self.health:
            display.blit(health_image, (x, 20))
            x += 40
            show += 1

    def check_health(self):
        self.health -= 1
        if self.health == 0:
            pygame.mixer.Sound.play(lose_sound)
            return False
        else:
            pygame.mixer.Sound.play(fall_sound)
            return True

    def hearts_plus(self, heart):
        if heart.x <= -heart.width:
            radius = p.display_width + random.randrange(1000, 3000)
            heart.return_self(radius, heart.y, heart.width, heart.image)

        if p.usr_x <= heart.x <= p.usr_x + p.usr_width:
            if p.usr_y <= heart.y <= p.usr_y + p.usr_height:
                pygame.mixer.Sound.play(heart_plus_sound)
                if self.health < 5:
                    self.health += 1

                radius = p.display_width + random.randrange(1000, 3000)
                heart.return_self(radius, heart.y, heart.width, heart.image)

    @staticmethod
    def draw_birds(birds):
        for bird in birds:
            action = bird.draw()
            if action == 1:
                bird.show()
            elif action == 2:
                bird.hide()
            else:
                bird.shoot()

    @staticmethod
    def check_birds_dmg(bullets, birds):
        for bird in birds:
            for bullet in bullets:
                bird.check_dmg(bullet)

    def check_dino_damage(self, bullets):
        for bullet in bullets:
            if p.usr_x <= bullet.x <= p.usr_x + p.usr_width:
                if p.usr_y <= bullet.y <= p.usr_y + p.usr_height:
                    self.health -= 1
