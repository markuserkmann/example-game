import pygame
pygame.init()

screen = pygame.display.set_mode([600, 500])
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() 