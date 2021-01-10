#  done refreshing with the OOP

import pygame
pygame.init()

tup = (550, 550)
win = pygame.display.set_mode(tup)

name = 'TIC-TAC-TOE'
def display():
    pygame.display.set_caption(name)
display()


class TTT:
    def box(self):
        self.box_0 = pygame.draw.rect(win, (255,100,70),(25,25,150,150))
        self.box_1 = pygame.draw.rect(win, (255,100,70),(200,25,150,150))
        self.box_2 = pygame.draw.rect(win, (255,100,70),(375,25,150,150))
        self.box_3 = pygame.draw.rect(win, (255,100,70),(25,200,150,150))
        self.box_4 = pygame.draw.rect(win, (255,100,70),(200,200,150,150))
        self.box_5 = pygame.draw.rect(win, (255,100,70),(375,200,150,150))
        self.box_6 = pygame.draw.rect(win, (255,100,70),(25,375,150,150))
        self.box_7 = pygame.draw.rect(win, (255,100,70),(200,375,150,150))
        self.box_8 = pygame.draw.rect(win, (255,100,70),(375,375,150,150))



        # making variable for the printing
        self.draw = 're'

        # whether filled or not
        self.open_box_0 = True
        self.open_box_1 = True
        self.open_box_2 = True
        self.open_box_3 = True
        self.open_box_4 = True
        self.open_box_5 = True
        self.open_box_6 = True
        self.open_box_7 = True
        self.open_box_8 = True

    # running when calling the function

        self.run = True

        self.RUN()

    def RUN(self):
        while self.run:
            
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.box()


                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos() 
                    print(pos)

                    if self.box_0.collidepoint(pos) and self.open_box_0:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (50,50,100,100))
                            self.draw = 'ci'
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (100,100), 50)
                            self.draw = 're'
                        
                        self.open_box_0 = False

                    if self.box_1.collidepoint(pos) and self.open_box_1:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (225,50,100,100))
                            self.draw = 'ci'
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (275,100), 50)
                            self.draw = 're'

                        self.open_box_1 = False

                    if self.box_2.collidepoint(pos) and self.open_box_2:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (400,50,100,100))
                            self.draw = 'ci'
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (450,100), 50)
                            self.draw = 're'

                        self.open_box_2 =False
                        

                    if self.box_3.collidepoint(pos) and self.open_box_3:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (50,225,100,100))
                            self.draw = 'ci'
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (100,275), 50)
                            self.draw = 're'

                        self.open_box_3 = False

                    if self.box_4.collidepoint(pos) and self.open_box_4:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (225,225,100,100))
                            self.draw = 'ci'
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (275,275), 50)
                            self.draw = 're'

                        self.open_box_4 = False

                    if self.box_5.collidepoint(pos) and self.open_box_5:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (400,225,100,100))
                            self.draw = 'ci'
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (450,275), 50)
                            self.draw = 're'
                        
                        self.open_box_5 = False

                    if self.box_6.collidepoint(pos) and self.open_box_6:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (50,400,100,100))
                            self.draw = 'ci'
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (100,450), 50)
                            self.draw = 're'

                        self.open_box_6 = False

                    if self.box_7.collidepoint(pos) and self.open_box_7:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (225,400,100,100))
                            self.draw = 'ci'
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (275,450), 50)
                            self.draw = 're'

                        self.open_box_7 = False

                    if self.box_8.collidepoint(pos) and self.open_box_8:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (400,400,100,100))
                            self.draw = 'ci'
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (450,450), 50)
                            self.draw = 're'

                        self.open_box_8 = False

            
            pygame.display.update()


        pygame.quit()
    
    
x = TTT()
x.box()