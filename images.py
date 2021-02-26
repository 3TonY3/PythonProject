import pygame

pygame.init()

cactus_img = [pygame.image.load('resources/Objects/Cactus0.png'), pygame.image.load('resources/Objects/Cactus1.png'), pygame.image.load(
    'resources/Objects/Cactus2.png')]


lvl2_bckgr = pygame.image.load('resources/Backgrounds/Landlev.jpg')
menu_bckgr = pygame.image.load('resources/Backgrounds/Menufon.png')
theme_fon = pygame.image.load('resources/Backgrounds/ThemeFon.jpeg')
hero_fon = pygame.image.load('resources/Backgrounds/Herofon.jpeg')

stone_img = [pygame.image.load('resources/Objects/Stone0.png'), pygame.image.load('resources/Objects/Stone1.png')]
cloud_img = [pygame.image.load('resources/Objects/Cloud0.png'), pygame.image.load('resources/Objects/Cloud1.png')]

dino_img = [pygame.image.load('resources/Dino/Dino0.png'), pygame.image.load('resources/Dino/Dino1.png'),
            pygame.image.load('resources/Dino/Dino2.png'), pygame.image.load('resources/Dino/Dino3.png'), pygame.image.load(
        'resources/Dino/Dino4.png')]

bird_img = [pygame.image.load('resources/Bird/Bird0.png'), pygame.image.load('resources/Bird/Bird1.png'),
            pygame.image.load('resources/Bird/Bird2.png'), pygame.image.load('resources/Bird/Bird3.png'), pygame.image.load(
        'resources/Bird/Bird4.png'), pygame.image.load('resources/Bird/Bird5.png')]

health_image = pygame.image.load('resources/Effects/heart.png')
health_image = pygame.transform.scale(health_image, (30, 30))

bullet_img = pygame.image.load('resources/Effects/shot.png')
bullet_img = pygame.transform.scale(bullet_img, (30, 9))

light_img = [pygame.image.load('resources/Effects/Light0.png'), pygame.image.load('resources/Effects/Light1.png'), pygame.image.load(
    'resources/Effects/Light2.png'),
             pygame.image.load('resources/Effects/Light3.png'), pygame.image.load('resources/Effects/Light4.png'), pygame.image.load(
        'resources/Effects/Light6.png'),
             pygame.image.load('resources/Effects/Light7.png'), pygame.image.load('resources/Effects/Light8.png'), pygame.image.load(
        'resources/Effects/Light9.png'),
             pygame.image.load('resources/Effects/Light10.png')]


def set_theme(num):
    global land
    land = pygame.image.load(f'resources/Backgrounds/Land{num}.jpg')


def set_hero(num):
    global dino_img

    if num == 1:
        dino_img = [pygame.image.load('resources/Dino/Dino0.png'), pygame.image.load('resources/Dino/Dino1.png'),
                    pygame.image.load('resources/Dino/Dino2.png'), pygame.image.load('resources/Dino/Dino3.png'), pygame.image.load(
                'resources/Dino/Dino4.png')]
    else:
        dino_img = [pygame.image.load('resources/Dino/Dino2_0.png'), pygame.image.load('resources/Dino/Dino2_1.png'),
                    pygame.image.load('resources/Dino/Dino2_2.png'), pygame.image.load('resources/Dino/Dino2_3.png'), pygame.image.load(
                'resources/Dino/Dino2_4.png')]

