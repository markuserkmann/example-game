import pygame
pygame.init()

from settings import Settings
g = Settings()

screen = pygame.display.set_mode([g.screen_width, g.screen_height])
pygame.display.set_caption(g.caption)
running = True

while running:
    screen.fill(g.bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() 