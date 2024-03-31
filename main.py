import pygame

pygame.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# load background image
bg_image = pygame.image.load(
    "assets/images/background/cherry_blossom_background.gif"
).convert_alpha()


def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# add name
pygame.display.set_caption("Spring Brawl Festa: Fist Carnival DELUXE 2024")

run = True
while run:
    # draw background
    draw_bg()
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
