import pygame

pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# add name
pygame.display.set_caption("Spring Brawl Festa: Fist Carnival DELUXE 2024")

run = True
while run:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()