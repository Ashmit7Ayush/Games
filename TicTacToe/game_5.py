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
        # for not having the back phase color
        tup = (550, 550)
        win = pygame.display.set_mode(tup)

        name = 'TIC-TAC-TOE'
        def display():
            pygame.display.set_caption(name)
        display()
        # 



        self.box_0 = pygame.draw.rect(win, (177, 8, 213),(25,25,150,150))
        self.box_1 = pygame.draw.rect(win, (177, 8, 213),(200,25,150,150))
        self.box_2 = pygame.draw.rect(win, (177, 8, 213),(375,25,150,150))
        self.box_3 = pygame.draw.rect(win, (177, 8, 213),(25,200,150,150))
        self.box_4 = pygame.draw.rect(win, (177, 8, 213),(200,200,150,150))
        self.box_5 = pygame.draw.rect(win, (177, 8, 213),(375,200,150,150))
        self.box_6 = pygame.draw.rect(win, (177, 8, 213),(25,375,150,150))
        self.box_7 = pygame.draw.rect(win, (177, 8, 213),(200,375,150,150))
        self.box_8 = pygame.draw.rect(win, (177, 8, 213),(375,375,150,150))



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

        self.ttt = [[0, 0, 0], [0, 0, 0 ], [0, 0, 0]] 
        self.RUN()

    def check_1(self):
        dep = False
        # row
        if self.ttt[0][0] == self.ttt[0][1] == self.ttt[0][2] == 1:
            dep = True
            pygame.draw.line(win, (22,22,22), (25,100), (525,100),21)
            pygame.display.update()

        elif self.ttt[1][0] == self.ttt[1][1] == self.ttt[1][2] == 1:
            dep = True
            pygame.draw.line(win, (22,22,22), (25,275), (525,275),21)
            pygame.display.update()

        elif self.ttt[2][0] == self.ttt[2][1] == self.ttt[2][2] == 1:
            dep = True
            pygame.draw.line(win, (22,22,22), (25,450), (525,450),21)
            pygame.display.update()

        # column
        elif self.ttt[0][0] == self.ttt[1][0] == self.ttt[2][0] == 1:
            dep = True
            pygame.draw.line(win, (22,22,22), (100,25), (100,525),21)
            pygame.display.update()
        elif self.ttt[0][1] == self.ttt[1][1] == self.ttt[2][1] == 1:
            dep = True
            pygame.draw.line(win, (22,22,22), (275,25), (275,525),21)
            pygame.display.update()
        elif self.ttt[0][2] == self.ttt[1][2] == self.ttt[2][2] == 1:
            dep = True
            pygame.draw.line(win, (22,22,22), (450,25), (450,525),21)
            pygame.display.update()

        # diagonal
        elif self.ttt[0][0] == self.ttt[1][1] == self.ttt[2][2] == 1:
            dep = True
            pygame.draw.line(win, (22,22,22), (25,25), (525,525),21)
            pygame.display.update()
        elif self.ttt[0][2] == self.ttt[1][1] == self.ttt[2][0] == 1:
            dep = True
            pygame.draw.line(win, (22,22,22), (525,25), (25,525),21)
            pygame.display.update()
        

        if dep == True:
            pygame.time.delay(3000)
            self.box()

    def check_2(self):
        dep = False
        # row
        if self.ttt[0][0] == self.ttt[0][1] == self.ttt[0][2] == 2:
            dep = True
            pygame.draw.line(win, (22,22,22), (25,100), (525,100),21)
            pygame.display.update()

        elif self.ttt[1][0] == self.ttt[1][1] == self.ttt[1][2] == 2:
            dep = True
            pygame.draw.line(win, (22,22,22), (25,275), (525,275),21)
            pygame.display.update()

        elif self.ttt[2][0] == self.ttt[2][1] == self.ttt[2][2] == 2:
            dep = True
            pygame.draw.line(win, (22,22,22), (25,450), (525,450),21)
            pygame.display.update()

        # column
        elif self.ttt[0][0] == self.ttt[1][0] == self.ttt[2][0] == 2:
            dep = True
            pygame.draw.line(win, (22,22,22), (100,25), (100,525),21)
            pygame.display.update()
        elif self.ttt[0][1] == self.ttt[1][1] == self.ttt[2][1] == 2:
            dep = True
            pygame.draw.line(win, (22,22,22), (275,25), (275,525),21)
            pygame.display.update()
        elif self.ttt[0][2] == self.ttt[1][2] == self.ttt[2][2] == 2:
            dep = True
            pygame.draw.line(win, (22,22,22), (450,25), (450,525),21)
            pygame.display.update()

        # diagonal
        elif self.ttt[0][0] == self.ttt[1][1] == self.ttt[2][2] == 2:
            dep = True
            pygame.draw.line(win, (22,22,22), (25,25), (525,525),21)
            pygame.display.update()
        elif self.ttt[0][2] == self.ttt[1][1] == self.ttt[2][0] == 2:
            dep = True
            pygame.draw.line(win, (22,22,22), (525,25), (25,525),21)
            pygame.display.update()
        

        if dep == True:
            pygame.time.delay(3000)
            self.box()
    

    def check(self):

        self.check_1()
        self.check_2()
        # now checking that it is fulled and needed to be get new page
        if self.ttt[0][0] != 0 and self.ttt[0][1] != 0 and self.ttt[0][2] != 0 and self.ttt[1][0] != 0 and self.ttt[1][1] != 0 and self.ttt[1][2] != 0 and self.ttt[2][0] != 0 and self.ttt[2][1] != 0 and self.ttt[2][2] != 0:
            pygame.time.delay(3000)
            self.box()

    def RUN(self):
        while self.run:
            
            # creating an list of the 9 box

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

                            self.ttt[0][0] = 1
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (100,100), 50)
                            self.draw = 're'

                            self.ttt[0][0] = 2
                        
                        self.open_box_0 = False
                        # self.check()
                

                    if self.box_1.collidepoint(pos) and self.open_box_1:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (225,50,100,100))
                            self.draw = 'ci'

                            self.ttt[0][1] = 1
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (275,100), 50)
                            self.draw = 're'

                            self.ttt[0][1] = 2

                        self.open_box_1 = False
                        # self.check()
                

                    if self.box_2.collidepoint(pos) and self.open_box_2:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (400,50,100,100))
                            self.draw = 'ci'

                            self.ttt[0][2] = 1
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (450,100), 50)
                            self.draw = 're'

                            self.ttt[0][2] = 2

                        self.open_box_2 =False
                        # self.check()
                
                        

                    if self.box_3.collidepoint(pos) and self.open_box_3:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (50,225,100,100))
                            self.draw = 'ci'

                            self.ttt[1][0] = 1
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (100,275), 50)
                            self.draw = 're'

                            self.ttt[1][0] = 2

                        self.open_box_3 = False
                        # self.check()
                

                    if self.box_4.collidepoint(pos) and self.open_box_4:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (225,225,100,100))
                            self.draw = 'ci'

                            self.ttt[1][1] = 1
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (275,275), 50)
                            self.draw = 're'

                            self.ttt[1][1] = 2

                        self.open_box_4 = False
                        # self.check()
                

                    if self.box_5.collidepoint(pos) and self.open_box_5:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (400,225,100,100))
                            self.draw = 'ci'

                            self.ttt[1][2] = 1
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (450,275), 50)
                            self.draw = 're'
                        
                            self.ttt[1][2] = 2

                        self.open_box_5 = False
                        # self.check()
                

                    if self.box_6.collidepoint(pos) and self.open_box_6:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (50,400,100,100))
                            self.draw = 'ci'

                            self.ttt[2][0] = 1
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (100,450), 50)
                            self.draw = 're'

                            self.ttt[2][0] = 2

                        self.open_box_6 = False
                        # self.check()
                

                    if self.box_7.collidepoint(pos) and self.open_box_7:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (225,400,100,100))
                            self.draw = 'ci'

                            self.ttt[2][1] = 1
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (275,450), 50)
                            self.draw = 're'

                            self.ttt[2][1] = 2

                        self.open_box_7 = False
                        # self.check()
                

                    if self.box_8.collidepoint(pos) and self.open_box_8:
                        if self.draw == 're':
                            pygame.draw.rect(win, (255, 0, 0), (400,400,100,100))
                            self.draw = 'ci'

                            self.ttt[2][2] = 1
                        else:
                            pygame.draw.circle(win, (0, 255, 0), (450,450), 50)
                            self.draw = 're'

                            self.ttt[2][2] = 2

                        self.open_box_8 = False
                        # self.check()

            
            pygame.display.update()
            self.check()


        pygame.quit()
    
    
x = TTT()
x.box()