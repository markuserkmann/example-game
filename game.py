import pygame
import math
from settings import Settings

pygame.init()
g = Settings()

screen = pygame.display.set_mode([g.screen_width, g.screen_height])
pygame.display.set_caption(g.caption)

bg = pygame.image.load(g.bgpath).convert()
scroll = 0
clock = pygame.time.Clock()
tiles = math.ceil(g.screen_width / bg.get_width()) + 1
running = True

while running:
    clock.tick(35)

    i = 0
    while(i < tiles):
        screen.blit(bg, (bg.get_width() *i + scroll, 0))
        i += 1

    scroll -= g.scroll_speed

    if abs(scroll) > bg.get_width():
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()