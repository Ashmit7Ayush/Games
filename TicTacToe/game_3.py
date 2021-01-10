#  in this we have made upto the not agin filling part 
# : in the next video we have dealt with the refreshing part


import pygame
pygame.init()

tup = (550, 550)
win = pygame.display.set_mode(tup)

name = 'TIC-TAC-TOE'
def display():
    pygame.display.set_caption(name)
display()


box_0 = pygame.draw.rect(win, (255,100,70),(25,25,150,150))
box_1 = pygame.draw.rect(win, (255,100,70),(200,25,150,150))
box_2 = pygame.draw.rect(win, (255,100,70),(375,25,150,150))
box_3 = pygame.draw.rect(win, (255,100,70),(25,200,150,150))
box_4 = pygame.draw.rect(win, (255,100,70),(200,200,150,150))
box_5 = pygame.draw.rect(win, (255,100,70),(375,200,150,150))
box_6 = pygame.draw.rect(win, (255,100,70),(25,375,150,150))
box_7 = pygame.draw.rect(win, (255,100,70),(200,375,150,150))
box_8 = pygame.draw.rect(win, (255,100,70),(375,375,150,150))


run = True

# making variable for the printing
draw = 're'

# whether filled or not
open_box_0 = True
open_box_1 = True
open_box_2 = True
open_box_3 = True
open_box_4 = True
open_box_5 = True
open_box_6 = True
open_box_7 = True
open_box_8 = True

while run:
    
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos() 
            print(pos)

            if box_0.collidepoint(pos) and open_box_0:
                if draw == 're':
                    pygame.draw.rect(win, (255, 0, 0), (50,50,100,100))
                    draw = 'ci'
                else:
                    pygame.draw.circle(win, (0, 255, 0), (100,100), 50)
                    draw = 're'
                
                open_box_0 = False

            if box_1.collidepoint(pos) and open_box_1:
                if draw == 're':
                    pygame.draw.rect(win, (255, 0, 0), (225,50,100,100))
                    draw = 'ci'
                else:
                    pygame.draw.circle(win, (0, 255, 0), (275,100), 50)
                    draw = 're'

                open_box_1 = False

            if box_2.collidepoint(pos) and open_box_2:
                if draw == 're':
                    pygame.draw.rect(win, (255, 0, 0), (400,50,100,100))
                    draw = 'ci'
                else:
                    pygame.draw.circle(win, (0, 255, 0), (450,100), 50)
                    draw = 're'

                open_box_2 =False
                 

            if box_3.collidepoint(pos) and open_box_3:
                if draw == 're':
                    pygame.draw.rect(win, (255, 0, 0), (50,225,100,100))
                    draw = 'ci'
                else:
                    pygame.draw.circle(win, (0, 255, 0), (100,275), 50)
                    draw = 're'

                open_box_3 = False

            if box_4.collidepoint(pos) and open_box_4:
                if draw == 're':
                    pygame.draw.rect(win, (255, 0, 0), (225,225,100,100))
                    draw = 'ci'
                else:
                    pygame.draw.circle(win, (0, 255, 0), (275,275), 50)
                    draw = 're'

                open_box_4 = False

            if box_5.collidepoint(pos) and open_box_5:
                if draw == 're':
                    pygame.draw.rect(win, (255, 0, 0), (400,225,100,100))
                    draw = 'ci'
                else:
                    pygame.draw.circle(win, (0, 255, 0), (450,275), 50)
                    draw = 're'
                
                open_box_5 = False

            if box_6.collidepoint(pos) and open_box_6:
                if draw == 're':
                    pygame.draw.rect(win, (255, 0, 0), (50,400,100,100))
                    draw = 'ci'
                else:
                    pygame.draw.circle(win, (0, 255, 0), (100,450), 50)
                    draw = 're'

                open_box_6 = False

            if box_7.collidepoint(pos) and open_box_7:
                if draw == 're':
                    pygame.draw.rect(win, (255, 0, 0), (225,400,100,100))
                    draw = 'ci'
                else:
                    pygame.draw.circle(win, (0, 255, 0), (275,450), 50)
                    draw = 're'

                open_box_7 = False

            if box_8.collidepoint(pos) and open_box_8:
                if draw == 're':
                    pygame.draw.rect(win, (255, 0, 0), (400,400,100,100))
                    draw = 'ci'
                else:
                    pygame.draw.circle(win, (0, 255, 0), (450,450), 50)
                    draw = 're'

                open_box_8 = False

    
    pygame.display.update()


pygame.quit()