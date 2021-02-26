import pygame

pygame.init()

cactus_img = [pygame.image.load('Objects/Cactus0.png'), pygame.image.load('Objects/Cactus1.png'), pygame.image.load(
    'Objects/Cactus2.png')]


lvl2_bckgr = pygame.image.load('Backgrounds/Landlev.jpg')
menu_bckgr = pygame.image.load('Backgrounds/Menufon.png')
theme_fon = pygame.image.load('Backgrounds/ThemeFon.jpeg')
hero_fon = pygame.image.load('Backgrounds/Herofon.jpeg')

stone_img = [pygame.image.load('Objects/Stone0.png'), pygame.image.load('Objects/Stone1.png')]
cloud_img = [pygame.image.load('Objects/Cloud0.png'), pygame.image.load('Objects/Cloud1.png')]

dino_img = [pygame.image.load('Dino/Dino0.png'), pygame.image.load('Dino/Dino1.png'),
            pygame.image.load('Dino/Dino2.png'), pygame.image.load('Dino/Dino3.png'), pygame.image.load(
        'Dino/Dino4.png')]

bird_img = [pygame.image.load('Bird/Bird0.png'), pygame.image.load('Bird/Bird1.png'),
            pygame.image.load('Bird/Bird2.png'), pygame.image.load('Bird/Bird3.png'), pygame.image.load(
        'Bird/Bird4.png'), pygame.image.load('Bird/Bird5.png')]

health_image = pygame.image.load('Effects/heart.png')
health_image = pygame.transform.scale(health_image, (30, 30))

# bullet_img = pygame.image.load('Effects/shot.png')
# bullet_img = pygame.transform.scale(bullet_img, (30, 9))

bullet_img1 = pygame.image.load('Effects/Blood-Magic-Effect_06.png')
bullet_img1 = pygame.transform.scale(bullet_img1, (50, 50))

bullet_img2 = pygame.image.load('Effects/Blood-Magic-Effect_07.png')
bullet_img2 = pygame.transform.scale(bullet_img2, (50, 50))

bullet_img3 = pygame.image.load('Effects/Blood-Magic-Effect_08.png')
bullet_img3 = pygame.transform.scale(bullet_img3, (50, 50))

bullet_img4 = pygame.image.load('Effects/Blood-Magic-Effect_09.png')
bullet_img4 = pygame.transform.scale(bullet_img4, (50, 50))

bullet_img5 = pygame.image.load('Effects/Blood-Magic-Effect_10.png')
bullet_img5 = pygame.transform.scale(bullet_img5, (50, 50))

bullet_img6 = [bullet_img1, bullet_img2, bullet_img3, bullet_img4, bullet_img5]

light_img = [pygame.image.load('Effects/Light0.png'), pygame.image.load('Effects/Light1.png'), pygame.image.load(
    'Effects/Light2.png'),
             pygame.image.load('Effects/Light3.png'), pygame.image.load('Effects/Light4.png'), pygame.image.load(
        'Effects/Light6.png'),
             pygame.image.load('Effects/Light7.png'), pygame.image.load('Effects/Light8.png'), pygame.image.load(
        'Effects/Light9.png'),
             pygame.image.load('Effects/Light10.png')]

bullet_img7 = pygame.image.load('Effects/Blood-Magic-Effect_16.png')
bullet_img7 = pygame.transform.scale(bullet_img7, (50, 50))

bullet_img8 = pygame.image.load('Effects/Blood-Magic-Effect_17.png')
bullet_img8 = pygame.transform.scale(bullet_img8, (50, 50))

bullet_img9 = pygame.image.load('Effects/Blood-Magic-Effect_18.png')
bullet_img9 = pygame.transform.scale(bullet_img9, (50, 50))

bullet_img10 = pygame.image.load('Effects/Blood-Magic-Effect_19.png')
bullet_img10 = pygame.transform.scale(bullet_img10, (50, 50))

bullet_img11 = pygame.image.load('Effects/Blood-Magic-Effect_20.png')
bullet_img11 = pygame.transform.scale(bullet_img11, (50, 50))

bullet_img12 = [bullet_img7, bullet_img8, bullet_img9, bullet_img10, bullet_img11]


def set_theme(num):
    global land
    land = pygame.image.load(f'Backgrounds/Land{num}.jpg')


def set_hero(num):
    global dino_img

    if num == 1:
        dino_img = [pygame.image.load('Dino/Dino0.png'), pygame.image.load('Dino/Dino1.png'),
                    pygame.image.load('Dino/Dino2.png'), pygame.image.load('Dino/Dino3.png'), pygame.image.load(
                'Dino/Dino4.png')]
    else:
        dino_img = [pygame.image.load('Dino/Dino2_0.png'), pygame.image.load('Dino/Dino2_1.png'),
                    pygame.image.load('Dino/Dino2_2.png'), pygame.image.load('Dino/Dino2_3.png'), pygame.image.load(
                'Dino/Dino2_4.png')]

