from components.button import Button
from components.scaleable_image import ScaleableImage
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
bg_image = pygame.image.load(
    "assets/images/background/cherry_blossom_background.gif"
).convert_alpha()


def draw_bg(image):
    """procedure to set background image in screen

    Keyword arguments:
    image -- Surface based in a image
    """

    scaled_bg = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


def get_font(size):
    return pygame.font.Font("assets/fonts/font.ttf", size)


def get_main_menu():
    while True:
        screen.fill("black")
        draw_bg(image=bg_image)
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


def play():
    pass


def get_credits():
    pass


if __name__ == "__main__":
    get_main_menu()
