import pygame

pygame.init()

win = pygame.display.set_mode((750,500))

pygame.display.set_caption('MyPong_Game')

white = (255, 255, 255)
black = (0,0,0)


run = True

while run():
    pygame.time.delay(100)


    for event in pygame.event.get():

        if event.type  ==pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()