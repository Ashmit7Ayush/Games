import pygame

pygame.init()

win = pygame.display.set_mode((550, 550))

pygame.display.set_caption('XYZ')

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()