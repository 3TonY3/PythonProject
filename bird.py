from sounds import *
import random
from bullet import *
from images import *


class Bird:
    def __init__(self, away_y):
        self.x = random.randrange(750, 800)
        self.y = away_y
        self.width = 105
        self.height = 55
        self.away_y = away_y
        self.speed = 3
        self.dest_y = self.speed * random.randrange(20, 50)
        self.img_cnt = 0
        self.cd_hide = 0
        self.come = True
        self.go_away = False
        self.cd_shoot = 0
        self.all_bullets = []

    def draw(self):
        if self.img_cnt == 30:
            self.img_cnt = 0

        display.blit(bird_img[self.img_cnt // 5], (self.x, self.y))
        self.img_cnt += 1

        if self.come and self.cd_hide == 0:
            return 1

        elif self.go_away:
            return 2

        elif self.cd_hide > 0:
            self.cd_hide -= 1

        return 0

    def show(self):
        if self.y < self.dest_y:
            self.y += self.speed
            self.x -= 1
        else:
            self.come = False
            #  self.go_away = True
            self.dest_y = self.away_y

    def hide(self):
        if self.y > self.dest_y:
            self.y -= self.speed
            self.x -= 2
        else:
            self.come = True
            self.go_away = False
            self.x = random.randrange(500, 730)
            self.dest_y = self.speed * random.randrange(20, 70)
            self.cd_hide = 80

    def check_dmg(self, bullet):
        if self.x <= bullet.x <= self.x + self.width:
            if self.y <= bullet.y <= self.y + self.height:
                self.go_away = True

    # def shoot(self):
    #     if not self.cd_shoot:
    #         pygame.mixer.Sound.play(bullet_sound)
    #
    #         new_bullet = Bullet(self.x, self.y)
    #         new_bullet.find_path(usr_x + usr_width // 2, usr_y + usr_height // 2)
    #
    #         self.all_bullets.append(new_bullet)
    #         self.cd_shoot = 200
    #     else:
    #         self.cd_shoot -= 1
    #
    #     for bullet in self.all_bullets:
    #         if not bullet.move_to(reverse=True):
    #             self.all_bullets.remove(bullet)
