from components.button import Button
from components.scaleable_image import ScaleableImage
from components.hp_bar import HpBar
from components.character import Character
import pygame, sys


pygame.init()

# General Settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

COLORS = {
    "white": (255, 255, 255),
    "yellow": (241, 196, 15),
    "red": (255, 0, 0),
    "blue": (0, 255, 0),
    "green": (0, 0, 255),
}

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# add name
pygame.display.set_caption("Spring Brawl Festa: Fist Carnival DELUXE 2024")

# load background image for menu
bg_image_menu = pygame.image.load(
    "assets/images/background/cherry_blossom_background.gif"
).convert_alpha()

img_bckgnd_coordinate = (0, 0)

# create game screen
img_stage_1 = pygame.image.load("assets/images/background/stage_1.jpg")
img_stage_1_coordinate = (0, 0)

hpbar_player1 = HpBar(
    pygame.image.load(
        "assets/images/icons/hp_bar.png"), (30, 50), (300, 46), pygame.image.load("assets/images/icons/hp.png"))
hpbar_player2 = HpBar(
    pygame.image.load(
        "assets/images/icons/hp_bar.png"), (460, 50), (300, 46), pygame.image.load("assets/images/icons/hp.png"))

clock = pygame.time.Clock()

def res_hp():
    global hpbar_player1
    global hpbar_player2

    hpbar_player1_res = HpBar(
        pygame.image.load(
            "assets/images/icons/hp_bar.png"), (30, 50), (300, 46), pygame.image.load("assets/images/icons/hp.png"))

    hpbar_player2_res = HpBar(
        pygame.image.load(
            "assets/images/icons/hp_bar.png"), (460, 50), (300, 46), pygame.image.load("assets/images/icons/hp.png"))
    hpbar_player1 = hpbar_player1_res
    hpbar_player2 = hpbar_player2_res

def scale_images(images, constant):
    for i, image in enumerate(images):
        images[i] = pygame.transform.scale(
            image, (image.get_rect().width*constant, image.get_rect().height*constant))


def reverse_images(images):
    for i, image in enumerate(images):
        images[i] = pygame.transform.flip(image, True, False)



def draw_bg(image):
    """procedure to set background image in screen

    Keyword arguments:
    image -- Surface based in a image
    """

    scaled_bg = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


def get_font(size):
    return pygame.font.Font("assets/fonts/font.ttf", size)

# assets/characters/
# Character animation
ryu_idle = [pygame.image.load("assets/characters/ryu/idle/idle_0.png").convert_alpha(),
            pygame.image.load(
                "assets/characters/ryu/idle/idle_1.png").convert_alpha(),
            pygame.image.load(
                "assets/characters/ryu/idle/idle_2.png").convert_alpha(),
            pygame.image.load("assets/characters/ryu/idle/idle_3.png").convert_alpha()]

ryu_move = [pygame.image.load("assets/characters/ryu/move/move_0.png").convert_alpha(),
            pygame.image.load(
                "assets/characters/ryu/move/move_1.png").convert_alpha(),
            pygame.image.load(
                "assets/characters/ryu/move/move_2.png").convert_alpha(),
            pygame.image.load(
                "assets/characters/ryu/move/move_3.png").convert_alpha(),
            pygame.image.load("assets/characters/ryu/move/move_4.png").convert_alpha()]

ryu_jump = [pygame.image.load("assets/characters/ryu/jump/jump_0.png").convert_alpha(),
            pygame.image.load(
                "assets/characters/ryu/jump/jump_1.png").convert_alpha(),
            pygame.image.load(
                "assets/characters/ryu/jump/jump_2.png").convert_alpha(),
            pygame.image.load(
                "assets/characters/ryu/jump/jump_3.png").convert_alpha(),
            pygame.image.load(
                "assets/characters/ryu/jump/jump_4.png").convert_alpha(),
            pygame.image.load(
                "assets/characters/ryu/jump/jump_5.png").convert_alpha(),
            pygame.image.load("assets/characters/ryu/jump/jump_6.png").convert_alpha()]

ryu_punch = [pygame.image.load("assets/characters/ryu/punch/punch_0.png").convert_alpha(),
             pygame.image.load(
                 "assets/characters/ryu/punch/punch_1.png").convert_alpha(),
             pygame.image.load(
                 "assets/characters/ryu/punch/punch_2.png").convert_alpha(),
             pygame.image.load(
                 "assets/characters/ryu/punch/punch_3.png").convert_alpha(),
             pygame.image.load("assets/characters/ryu/punch/punch_4.png").convert_alpha()]

ryu_airpunch = [pygame.image.load("assets/characters/ryu/air_punch/air_punch_0.png").convert_alpha(),
                pygame.image.load(
                    "assets/characters/ryu/air_punch/air_punch_1.png").convert_alpha(),
                pygame.image.load("assets/characters/ryu/air_punch/air_punch_2.png").convert_alpha()]

ryu_kick = [pygame.image.load("assets/characters/ryu/kick/kick_0.png").convert_alpha(),
            pygame.image.load(
                "assets/characters/ryu/kick/kick_1.png").convert_alpha(),
            pygame.image.load(
                "assets/characters/ryu/kick/kick_2.png").convert_alpha(),
            pygame.image.load(
                "assets/characters/ryu/kick/kick_3.png").convert_alpha(),
            pygame.image.load("assets/characters/ryu/kick/kick_4.png").convert_alpha()]

ryu_airkick = [pygame.image.load("assets/characters/ryu/air_kick/airkick_0.png").convert_alpha(),
               pygame.image.load(
                   "assets/characters/ryu/air_kick/airkick_1.png").convert_alpha(),
               pygame.image.load(
                   "assets/characters/ryu/air_kick/airkick_2.png").convert_alpha(),
               pygame.image.load("assets/characters/ryu/air_kick/airkick_3.png").convert_alpha()]
ryu_hit = [pygame.image.load("assets/characters/ryu/hit/hit_0.png").convert_alpha(),
           pygame.image.load(
    "assets/characters/ryu/hit/hit_1.png").convert_alpha(),
    pygame.image.load(
    "assets/characters/ryu/hit/hit_2.png").convert_alpha(),
    pygame.image.load("assets/characters/ryu/hit/hit_3.png").convert_alpha()]
ken_idle = [pygame.image.load("assets/characters/ken/idle/idle_0.png").convert_alpha(),
            pygame.image.load(
    "assets/characters/ken/idle/idle_1.png").convert_alpha(),
    pygame.image.load(
    "assets/characters/ken/idle/idle_2.png").convert_alpha(),
    pygame.image.load("assets/characters/ken/idle/idle_3.png").convert_alpha()]


ken_move = [pygame.image.load("assets/characters/ken/move/move_0.png").convert_alpha(),
            pygame.image.load(
    "assets/characters/ken/move/move_1.png").convert_alpha(),
    pygame.image.load(
    "assets/characters/ken/move/move_2.png").convert_alpha(),
    pygame.image.load(
    "assets/characters/ken/move/move_3.png").convert_alpha(),
    pygame.image.load("assets/characters/ken/move/move_4.png").convert_alpha()]

ken_jump = [pygame.image.load("assets/characters/ken/jump/jump_0.png").convert_alpha(),
            pygame.image.load(
    "assets/characters/ken/jump/jump_1.png").convert_alpha(),
    pygame.image.load(
    "assets/characters/ken/jump/jump_2.png").convert_alpha(),
    pygame.image.load(
    "assets/characters/ken/jump/jump_3.png").convert_alpha(),
    pygame.image.load(
    "assets/characters/ken/jump/jump_4.png").convert_alpha(),
    pygame.image.load(
    "assets/characters/ken/jump/jump_5.png").convert_alpha(),
    pygame.image.load("assets/characters/ken/jump/jump_6.png").convert_alpha()]

ken_punch = [pygame.image.load("assets/characters/ken/punch/punch_0.png").convert_alpha(),
             pygame.image.load(
    "assets/characters/ken/punch/punch_1.png").convert_alpha(),
    pygame.image.load(
    "assets/characters/ken/punch/punch_2.png").convert_alpha(),
    pygame.image.load(
    "assets/characters/ken/punch/punch_3.png").convert_alpha(),
    pygame.image.load("assets/characters/ken/punch/punch_4.png").convert_alpha()]

ken_airpunch = [pygame.image.load("assets/characters/ken/air_punch/airpunch_0.png").convert_alpha(),
                pygame.image.load(
    "assets/characters/ken/air_punch/airpunch_1.png").convert_alpha(),
    pygame.image.load("assets/characters/ken/air_punch/airpunch_2.png").convert_alpha()]

ken_kick = [pygame.image.load("assets/characters/ken/kick/kick_0.png").convert_alpha(),
            pygame.image.load(
    "assets/characters/ken/kick/kick_1.png").convert_alpha(),
    pygame.image.load(
    "assets/characters/ken/kick/kick_2.png").convert_alpha(),
    pygame.image.load(
    "assets/characters/ken/kick/kick_3.png").convert_alpha(),
    pygame.image.load("assets/characters/ken/kick/kick_4.png").convert_alpha()]

ken_airkick = [pygame.image.load("assets/characters/ken/air_kick/airkick_0.png").convert_alpha(),
               pygame.image.load(
    "assets/characters/ken/air_kick/airkick_1.png").convert_alpha(),
    pygame.image.load(
    "assets/characters/ken/air_kick/airkick_2.png").convert_alpha(),
    pygame.image.load("assets/characters/ken/air_kick/airkick_3.png").convert_alpha()]
ken_hit = [pygame.image.load("assets/characters/ken/hit/hit_0.png").convert_alpha(),
           pygame.image.load(
    "assets/characters/ken/hit/hit_1.png").convert_alpha(),
    pygame.image.load(
    "assets/characters/ken/hit/hit_2.png").convert_alpha(),
    pygame.image.load("assets/characters/ken/hit/hit_3.png").convert_alpha()]

scale_images(ryu_idle, 3)
scale_images(ryu_move, 3)
scale_images(ryu_jump, 3)
scale_images(ryu_punch, 3)
scale_images(ryu_airpunch, 3)
scale_images(ryu_kick, 2.6)
scale_images(ryu_airkick, 3)
scale_images(ryu_hit, 3)

scale_images(ken_idle, 3)
scale_images(ken_move, 3)
scale_images(ken_jump, 3)
scale_images(ken_punch, 3)
scale_images(ken_airpunch, 3)
scale_images(ken_kick, 3)
scale_images(ken_airkick, 3)
scale_images(ken_hit, 3)

ani_ryu = [ryu_idle, ryu_move, ryu_jump,
           ryu_punch, ryu_airpunch, ryu_kick, ryu_airkick, ryu_hit]
ani_ryu2 = [ken_idle, ken_move, ken_jump,
            ken_punch, ken_airpunch, ken_kick, ken_airkick, ken_hit]
ryu = Character(ani_ryu, 20, 500)
ken = Character(ani_ryu2, 640, 500)
player = ryu
player2 = ken
players = [ryu, ken]
chrc_group = pygame.sprite.Group(ryu)
chrc_group.add(ken)


def get_main_menu():
    while True:
        screen.fill("black")
        draw_bg(image=bg_image_menu)
        menu_mouse_position = pygame.mouse.get_pos()
        # main title
        img_bckgnd_text = pygame.image.load("assets/images/icons/main_title.png")
        img_bckgnd_text = pygame.transform.scale(img_bckgnd_text, (900, 600))
        img_bckgnd_text_rect = img_bckgnd_text.get_rect(x=200, y=20)
        scl_img_bckgnd_text = ScaleableImage(
            img_bckgnd_text_rect.center, img_bckgnd_text
        )
        scl_group = pygame.sprite.Group(scl_img_bckgnd_text)

        # button play
        play_pos = (screen.get_rect().centerx, screen.get_rect().centery + 50)
        play_button = Button(
            None, play_pos, "Play", get_font(50), COLORS["white"], COLORS["yellow"]
        )
        # credit button
        credit_pos = (screen.get_rect().centerx, screen.get_rect().centery + 100)
        credits_button = Button(
            None, credit_pos, "Credits", get_font(50), COLORS["white"], COLORS["yellow"]
        )
        # quit button
        quit_pos = (screen.get_rect().centerx, screen.get_rect().centery + 150)
        quit_button = Button(
            None, quit_pos, "Quit", get_font(50), COLORS["white"], COLORS["yellow"]
        )
        for button in [play_button, credits_button, quit_button]:
            button.changeColor(menu_mouse_position)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_position):
                    play()
                if credits_button.checkForInput(menu_mouse_position):
                    get_credits()
                if quit_button.checkForInput(menu_mouse_position):
                    pygame.quit()
                    sys.exit()
        scl_group.update()
        scl_group.draw(screen)
        pygame.display.update()

def collisionDetection(self, other_player):
    tollerance_collision = 10
    if self.hitbox_attack_rect.colliderect(other_player.hitbox_body_rect) or self.hitbox_attack_rect.colliderect(other_player.hitbox_head_rect) and self.is_punching:
        if(self.is_hitted == False and self.is_attacking):
            if self.is_punching:
                other_player.hp = other_player.hp - 0.05
                other_player.is_hitted_animate = True
                hpbar_player1.setHp(player.hp, True)
                hpbar_player2.setHp(player2.hp, True)

            self.is_hitted = True
    if self.hitbox_attack_kick_rect.colliderect(other_player.hitbox_body_rect) or self.hitbox_attack_kick_rect.colliderect(other_player.hitbox_head_rect) and self.is_kicking:
        if(self.is_hitted == False and self.is_attacking):
            if self.is_kicking:
                other_player.hp = other_player.hp - 0.05
                other_player.is_hitted_animate = True
                hpbar_player1.setHp(player.hp, True)
                hpbar_player2.setHp(player2.hp, True)

            self.is_hitted = True
    if(self.is_attacking == False):
        self.is_hitted = False


def play():
    # player2 is made reverse
    for images in player2.sprites:
        reverse_images(images)
    player2.reverseHitBox()

    # statements
    walk_right = False
    walk_left = False
    walk_up = False
    is_punching = False
    is_kicking = False
    is_air_attack = False
    flip_rev = False
    flip_str = True
    # check if player push button constantly when try to move right or left
    is_continues = False

    walk_right2 = False
    walk_left2 = False
    walk_up2 = False
    is_punching2 = False
    is_kicking2 = False
    is_air_attack2 = False
    is_continues2 = False

    jump_coef = 50
    jump_coef2 = 30

    ani_num2 = 0
    speed2 = 0.1
    situation = True
    speed = 0.1
    ani_num = 0
    counter, text = 100, '100'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    tempfont = pygame.font.SysFont('Consolas', 30)
    while True:
        screen.fill("black")
        draw_bg(image=img_stage_1)
        events = pygame.event.get()
        user_input = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and (user_input[pygame.K_d] or user_input[pygame.K_c] or user_input[pygame.K_UP] or user_input[pygame.K_DOWN] or user_input[pygame.K_RIGHT] or user_input[pygame.K_LEFT]):
                player.animate()
            if event.type == pygame.KEYDOWN and (user_input[pygame.K_h] or user_input[pygame.K_n] or user_input[pygame.K_o] or user_input[pygame.K_k] or user_input[pygame.K_l] or user_input[pygame.K_j]):
                player2.animate()
            if event.type == pygame.KEYUP and not((user_input[pygame.K_d] and user_input[pygame.K_c] and user_input[pygame.K_UP] and user_input[pygame.K_DOWN] and user_input[pygame.K_RIGHT] and user_input[pygame.K_LEFT])):
                is_continues = False
            if event.type == pygame.KEYUP and not((user_input[pygame.K_h] and user_input[pygame.K_n] and user_input[pygame.K_o] and user_input[pygame.K_k] and user_input[pygame.K_l] and user_input[pygame.K_j])):
                is_continues2 = False
            if event.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'Game Over!'
        if not player.is_hitted_animate:
            if player.current_index == 0 and is_continues == False:
                ani_num = 0
                speed = 0.1
                is_punching = False
                is_kicking = False
                if not walk_up:
                    walk_left = False
                    walk_right = False

            if user_input[pygame.K_RIGHT] and not (walk_up):

                ani_num = 1
                speed = 0.25
                walk_right = True
                is_continues = True
                if user_input[pygame.K_LEFT]:
                    ani_num = 0
                    walk_right = False
                    walk_left = False
                    is_continues = False
                if user_input[pygame.K_d] or is_punching:
                    if not is_kicking:
                        ani_num = 3
                        speed = 0.1
                    walk_right = False
                    walk_left = False
                    is_continues = False
                if user_input[pygame.K_c] or is_kicking:
                    if not is_punching:
                        ani_num = 5
                        speed = 0.2
                    walk_right = False
                    walk_left = False
                    is_continues = False

            if user_input[pygame.K_LEFT] and not (walk_up):
                ani_num = 1
                speed = 0.25

                walk_left = True
                is_continues = True
                if user_input[pygame.K_RIGHT]:
                    ani_num = 0
                    walk_right = False
                    walk_left = False
                    is_continues = False
                if user_input[pygame.K_d] or is_punching:
                    if not is_kicking:
                        ani_num = 3
                        speed = 0.1
                    walk_right = False
                    walk_left = False
                    is_continues = False
                if user_input[pygame.K_c] or is_kicking:
                    if not is_punching:
                        ani_num = 5
                        speed = 0.2
                    walk_right = False
                    walk_left = False
                    is_continues = False

            if user_input[pygame.K_d] and not (walk_up):

                if not is_kicking:
                    ani_num = 3
                    speed = 0.1
                    is_punching = True
                    walk_right = False
                    walk_left = False
                    player.is_attacking = True
                    player.is_punching = True

            if user_input[pygame.K_d] and walk_up:
                ani_num = 4
                speed = 0.05
                is_punching = True
                player.is_attacking = True
                player.is_kicking = True

            if user_input[pygame.K_c] and not (walk_up):

                if not is_punching:
                    ani_num = 5
                    speed = 0.2
                    is_kicking = True
                    walk_right = False
                    walk_left = False
                    player.is_attacking = True
                    player.is_punching = True

            if user_input[pygame.K_c] and walk_up:
                ani_num = 6
                speed = 0.165
                is_kicking = True
                player.is_attacking = True
                player.is_kicking = True

            if walk_up is False and user_input[pygame.K_UP] and is_punching is False and is_kicking is False:
                ani_num = 2
                speed = 0.15
                walk_up = True

            if walk_up:
                player.jumping(jump_coef)
                jump_coef -= 1

                if user_input[pygame.K_RIGHT] and user_input[pygame.K_UP] and user_input[pygame.K_d]:
                    ani_num = 4
                    speed = 0.05
                    is_punching = True
                    walk_right = True
                    player.is_attacking = True
                    player.is_kicking = True
                if user_input[pygame.K_LEFT] and user_input[pygame.K_UP] and user_input[pygame.K_d]:
                    ani_num = 4
                    speed = 0.05
                    is_punching = True
                    walk_left = True
                    player.is_attacking = True
                    player.is_kicking = True
                if user_input[pygame.K_RIGHT] and user_input[pygame.K_UP] and user_input[pygame.K_c]:
                    ani_num = 6
                    speed = 0.05
                    is_kicking = True
                    walk_right = True
                    player.is_attacking = True
                    player.is_kicking = True
                if user_input[pygame.K_LEFT] and user_input[pygame.K_UP] and user_input[pygame.K_c]:
                    ani_num = 6
                    speed = 0.05
                    is_kicking = True
                    walk_left = True
                    player.is_attacking = True
                    player.is_kicking = True
                if is_kicking:
                    if not is_air_attack:
                        player.current_index = 0
                        is_air_attack = True
                    ani_num = 6
                    speed = 0.165
                    is_kicking = True
                    player.is_attacking = True
                    player.is_kicking = True
                    if(1 < player.current_index < 2):
                        speed = 0.05
                if is_punching:
                    if not is_air_attack:
                        player.current_index = 0
                        is_air_attack = True
                    ani_num = 4
                    speed = 0.05
                    is_punching = True
                    player.is_attacking = True
                    player.is_kicking = True
                if jump_coef < -50:
                    player.is_animate = False
                    player.is_idle = True
                    player.current_index = 0
                    jump_coef = 50
                    walk_up = False
                    ani_num = 0
                    walk_left = False
                    walk_right = False
                    is_kicking = False
                    is_punching = False
                    is_air_attack = False
                    player.is_kicking = False
# PLAYER 2
        if not player2.is_hitted_animate:
            if player2.current_index == 0 and is_continues2 == False:
                ani_num2 = 0
                speed2 = 0.1
                is_punching2 = False
                is_kicking2 = False
                if not walk_up2:
                    walk_left2 = False
                    walk_right2 = False

            if user_input[pygame.K_l] and not (walk_up2):

                ani_num2 = 1
                speed2 = 0.25
                walk_right2 = True
                is_continues2 = True
                if user_input[pygame.K_j]:
                    ani_num2 = 0
                    walk_right2 = False
                    walk_left2 = False
                    is_continues2 = False
                if user_input[pygame.K_h] or is_punching2:
                    if not is_kicking2:
                        ani_num2 = 3
                        speed2 = 0.1
                    walk_right2 = False
                    walk_left2 = False
                    is_continues2 = False
                if user_input[pygame.K_n] or is_kicking2:
                    if not is_punching2:
                        ani_num2 = 5
                        speed2 = 0.2
                    walk_right2 = False
                    walk_left2 = False
                    is_continues2 = False

            if user_input[pygame.K_j] and not (walk_up2):
                ani_num2 = 1
                speed2 = 0.25

                walk_left2 = True
                is_continues2 = True
                if user_input[pygame.K_l]:
                    ani_num2 = 0
                    walk_right2 = False
                    walk_left2 = False
                    is_continues2 = False
                if user_input[pygame.K_h] or is_punching2:
                    if not is_kicking2:
                        ani_num2 = 3
                        speed2 = 0.1
                    walk_right2 = False
                    walk_left2 = False
                    is_continues2 = False
                if user_input[pygame.K_h] or is_kicking2:
                    if not is_punching2:
                        ani_num2 = 5
                        speed2 = 0.2
                    walk_right2 = False
                    walk_left2 = False
                    is_continues2 = False

            if user_input[pygame.K_h] and not (walk_up2):

                if not is_kicking2:
                    ani_num2 = 3
                    speed2 = 0.1
                    is_punching2 = True
                    walk_right2 = False
                    walk_left2 = False
                    player2.is_attacking = True
                    player2.is_punching = True

            if user_input[pygame.K_h] and walk_up2:
                ani_num2 = 4
                speed2 = 0.05
                is_punching2 = True
                player2.is_attacking = True
                player2.is_kicking = True

            if user_input[pygame.K_n] and not (walk_up2):

                if not is_punching2:
                    ani_num2 = 5
                    speed2 = 0.2
                    is_kicking2 = True
                    walk_right2 = False
                    walk_left2 = False
                    player2.is_attacking = True
                    player2.is_punching = True

            if user_input[pygame.K_n] and walk_up2:
                ani_num2 = 6
                speed2 = 0.165
                is_kicking2 = True
                player2.is_attacking = True
                player2.is_kicking = True

            if walk_up2 is False and user_input[pygame.K_o] and is_punching2 is False and is_kicking2 is False:
                ani_num2 = 2
                speed2 = 0.15
                walk_up2 = True

            if walk_up2:
                player2.jumping(jump_coef2)
                jump_coef2 -= 1

                if user_input[pygame.K_l] and user_input[pygame.K_o] and user_input[pygame.K_h]:
                    ani_num2 = 4
                    speed2 = 0.05
                    is_punching2 = True
                    walk_right2 = True
                    player2.is_attacking = True
                    player2.is_kicking = True
                if user_input[pygame.K_j] and user_input[pygame.K_o] and user_input[pygame.K_h]:
                    ani_num2 = 4
                    speed2 = 0.05
                    is_punching2 = True
                    walk_left2 = True
                    player2.is_attacking = True
                    player2.is_kicking = True
                if user_input[pygame.K_l] and user_input[pygame.K_o] and user_input[pygame.K_n]:
                    ani_num2 = 6
                    speed2 = 0.05
                    is_kicking2 = True
                    walk_right2 = True
                    player2.is_attacking = True
                    player2.is_kicking = True
                if user_input[pygame.K_j] and user_input[pygame.K_o] and user_input[pygame.K_n]:
                    ani_num2 = 6
                    speed2 = 0.05
                    is_kicking2 = True
                    walk_left2 = True
                    player2.is_attacking = True
                    player2.is_kicking = True
                if is_kicking2:
                    if not is_air_attack2:
                        player2.current_index = 0
                        is_air_attack2 = True
                    ani_num2 = 6
                    speed2 = 0.165
                    is_kicking2 = True
                    player2.is_attacking = True
                    player2.is_kicking = True
                    if(1 < player2.current_index < 2):
                        speed2 = 0.05
                if is_punching2:
                    if not is_air_attack2:
                        player2.current_index = 0
                        is_air_attack2 = True
                    ani_num2 = 4
                    speed2 = 0.05
                    is_punching2 = True
                    player2.is_attacking = True
                    player2.is_kicking = True
                if jump_coef2 < -25:
                    player2.is_animate = False
                    player2.is_idle = True
                    player2.current_index = 0
                    jump_coef2 = 50
                    walk_up2 = False
                    ani_num2 = 0
                    walk_left2 = False
                    walk_right2 = False
                    is_kicking2 = False
                    is_punching2 = False
                    is_air_attack2 = False
                    player2.is_kicking = False
        if walk_left2:
            player2.movement(-2)
        if walk_right2:
            player2.movement(2)
#########
        if walk_left:
            player.movement(-2)
        if walk_right:
            player.movement(2)

        if player.rect.topleft[0] > player2.rect.topleft[0] and not flip_rev:
            flip_rev = True
            flip_str = False
            player.reverseHitBox()
            player2.reverseHitBox()
            for images in player.sprites:
                reverse_images(images)
            for images in player2.sprites:
                reverse_images(images)

        if player.rect.topleft[0] < player2.rect.topleft[0] and not flip_str:
            flip_str = True
            flip_rev = False
            player.reverseHitBox()
            player2.reverseHitBox()
            for images in player.sprites:
                reverse_images(images)
            for images in player2.sprites:
                reverse_images(images)

        collisionDetection(player, player2)
        collisionDetection(player2, player)

        if player.is_hitted_animate:
            player.update(0.1, 7, flip_rev)
            player2.update(speed2, ani_num2, flip_str)
        elif player2.is_hitted_animate:
            player.update(speed, ani_num, flip_rev)
            player2.update(0.1, 7, flip_str)
        else:
            player.update(speed, ani_num, flip_rev)
            player2.update(speed2, ani_num2, flip_str)
        hpbar_player1.update()
        hpbar_player2.update()  # ustteki 5li blitlerin altina gidebilir.

        screen.blit(player.image, player.rect.topleft)
        screen.blit(player2.image, player2.rect.topleft)
        screen.blit(hpbar_player1.image, hpbar_player1.rect.topleft)
        screen.blit(hpbar_player1.hpImage, hpbar_player1.hpImage_rect.topleft)
        screen.blit(hpbar_player2.image, hpbar_player2.rect.topleft)
        screen.blit(hpbar_player2.hpImage, hpbar_player2.hpImage_rect.topleft)
        text_rec = tempfont.render(text, True, COLORS["red"], COLORS["green"])
        screen.blit(text_rec, (370, 55))
        if(player.hp < 0 or player2.hp < 0):
            break
        if counter < 0:
            break

        clock.tick(60)
        pygame.display.update()



def get_credits():
    while True:
        mouse_position = pygame.mouse.get_pos()
        screen.fill("black")
        draw_bg(image=bg_image_menu)
        img_bckgnd_text = pygame.image.load("assets/images/icons/credits_title.png")
        img_bckgnd_text = pygame.transform.scale(img_bckgnd_text, (900, 600))
        img_bckgnd_text_rect = img_bckgnd_text.get_rect(x=200, y=20)
        scl_img_bckgnd_text = ScaleableImage(
            img_bckgnd_text_rect.center, img_bckgnd_text
        )
        scl_group = pygame.sprite.Group(scl_img_bckgnd_text)

        exit_pos = (screen.get_rect().centerx - 20, screen.get_rect().centery + 175)
        btn_exit = Button(
            None,
            exit_pos,
            "Exit",
            pygame.font.SysFont("calibri", 36),
            COLORS["white"],
            COLORS["yellow"],
        )
        for respond in [btn_exit]:
            respond.changeColor(mouse_position)
            respond.update(screen)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_exit.checkForInput(mouse_position):
                    get_main_menu()

        scl_group.update()
        scl_group.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    get_main_menu()
