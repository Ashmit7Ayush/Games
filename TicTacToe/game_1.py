import pygame
pygame.init()

tup = (550, 550)
win = pygame.display.set_mode(tup)

name = 'TIC-TAC-TOE'
def display():
    pygame.display.set_caption(name)
display()

# drawing a rect/square  window    color    starting x and starting y 
# last two are the dimensions
# Making_Boxes
box_0 = pygame.draw.rect(win, (255,0,0),(25,25,150,150))
box_1 = pygame.draw.rect(win, (255,0,0),(200,25,150,150))
box_2 = pygame.draw.rect(win, (255,0,0),(375,25,150,150))
box_3 = pygame.draw.rect(win, (255,0,0),(25,200,150,150))
box_4 = pygame.draw.rect(win, (255,0,0),(200,200,150,150))
box_5 = pygame.draw.rect(win, (255,0,0),(375,200,150,150))
box_6 = pygame.draw.rect(win, (255,0,0),(25,375,150,150))
box_7 = pygame.draw.rect(win, (255,0,0),(200,375,150,150))
box_8 = pygame.draw.rect(win, (255,0,0),(375,375,150,150))


run = True

while run:
    # time to be dlayed in the update
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # to display the win updated
    pygame.display.update()


pygame.quit()