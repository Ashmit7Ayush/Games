#  added music
#  task menu
#  also the key task 

# using the sys to execute because in return we are getting problm
import sys
from pygame import mixer
mixer.init()
import pygame
pygame.init()

tup = (600, 600)
win = pygame.display.set_mode(tup)

name = 'TIC-TAC-TOE'
def display():
    pygame.display.set_caption(name)
display()




class TTT:
    def box(self):
        
        tup = (600, 600)
        win = pygame.display.set_mode(tup)

        name = 'TIC-TAC-TOE'
        def display():
            pygame.display.set_caption(name)
        display()
        # 



        self.box_0 = pygame.draw.rect(win, (209, 209, 212),(25,25,150,150))
        self.box_1 = pygame.draw.rect(win, (209, 209, 212),(200,25,150,150))
        self.box_2 = pygame.draw.rect(win, (209, 209, 212),(375,25,150,150))
        self.box_3 = pygame.draw.rect(win, (209, 209, 212),(25,200,150,150))
        self.box_4 = pygame.draw.rect(win, (209, 209, 212),(200,200,150,150))
        self.box_5 = pygame.draw.rect(win, (209, 209, 212),(375,200,150,150))
        self.box_6 = pygame.draw.rect(win, (209, 209, 212),(25,375,150,150))
        self.box_7 = pygame.draw.rect(win, (209, 209, 212),(200,375,150,150))
        self.box_8 = pygame.draw.rect(win, (209, 209, 212),(375,375,150,150))

        #  for the options 
        self.box_9 = pygame.draw.rect(win,(255, 255, 255), (560,25,30,124))
        self.box_10 = pygame.draw.rect(win,(255, 255, 255), (560,150,30,124))
        self.box_11 = pygame.draw.rect(win,(255, 255, 255), (560,275,30,124))
        self.box_12 = pygame.draw.rect(win,(255, 255, 255), (560,400,30,125))



        
        self.draw = 're'

        
        self.open_box_0 = True
        self.open_box_1 = True
        self.open_box_2 = True
        self.open_box_3 = True
        self.open_box_4 = True
        self.open_box_5 = True
        self.open_box_6 = True
        self.open_box_7 = True
        self.open_box_8 = True

    

        self.run = True

        self.ttt = [[0, 0, 0], [0, 0, 0 ], [0, 0, 0]] 
        self.RUN()

#  for the player win 
    def over_text(self,string):
        font = pygame.font.Font('freesansbold.ttf', 49)
        text = font.render(string, True, (183, 16, 224), (0,0,0))
        textRect = text.get_rect()  
        textRect.center = (550 // 2, 550 // 2)
        win.blit(text, textRect) 
        pygame.display.update()


#  turn of the player
    def turn(self,player):
        font = pygame.font.Font('freesansbold.ttf', 49)
        text = font.render(player, True, (252, 176, 253), None )
        textRect = text.get_rect()  
        textRect.center = (550 // 2, 575)
        win.blit(text, textRect) 
        pygame.display.update()

    def clear(self):
       

        pygame.draw.rect(win, (0, 0, 0), (0,550,550,50))
        pygame.display.update()
    

    def match_over(self):
        #  first clear
        self.clear()

        # almost turn but different clor
        font = pygame.font.Font('freesansbold.ttf', 49)
        text = font.render('Match Over', True, (255,0,0), None )
        textRect = text.get_rect()  
        textRect.center = (550 // 2, 575)
        win.blit(text, textRect) 
        pygame.display.update() 
        

    def check_1(self):
        dep = False
        # row
        if self.ttt[0][0] == self.ttt[0][1] == self.ttt[0][2] == 1:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (25,100), (525,100),21)
            pygame.display.update()

            #  who wins calling the method to display
            self.over_text('Player A WIN!!!')

        elif self.ttt[1][0] == self.ttt[1][1] == self.ttt[1][2] == 1:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (25,275), (525,275),21)
            pygame.display.update()

            self.over_text('Player A WIN!!!')

        elif self.ttt[2][0] == self.ttt[2][1] == self.ttt[2][2] == 1:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (25,450), (525,450),21)
            pygame.display.update()

            self.over_text('Player A WIN!!!')

        # column
        elif self.ttt[0][0] == self.ttt[1][0] == self.ttt[2][0] == 1:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (100,25), (100,525),21)
            pygame.display.update()

            self.over_text('Player A WIN!!!')

        elif self.ttt[0][1] == self.ttt[1][1] == self.ttt[2][1] == 1:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (275,25), (275,525),21)
            pygame.display.update()

            self.over_text('Player A WIN!!!')

        elif self.ttt[0][2] == self.ttt[1][2] == self.ttt[2][2] == 1:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (450,25), (450,525),21)
            pygame.display.update()

            self.over_text('Player A WIN!!!')

        # diagonal
        elif self.ttt[0][0] == self.ttt[1][1] == self.ttt[2][2] == 1:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (25,25), (525,525),21)
            pygame.display.update()

            self.over_text('Player A WIN!!!')

        elif self.ttt[0][2] == self.ttt[1][1] == self.ttt[2][0] == 1:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (525,25), (25,525),21)
            pygame.display.update()

            self.over_text('Player A WIN!!!')
        

        if dep == True:

            # print match over
            self.match_over()

            pygame.time.delay(3000)
            self.box()

    def check_2(self):
        dep = False
        # row
        if self.ttt[0][0] == self.ttt[0][1] == self.ttt[0][2] == 2:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (25,100), (525,100),21)
            pygame.display.update()

            self.over_text('Player B WIN!!!')

        elif self.ttt[1][0] == self.ttt[1][1] == self.ttt[1][2] == 2:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (25,275), (525,275),21)
            pygame.display.update()

            self.over_text('Player B WIN!!!')

        elif self.ttt[2][0] == self.ttt[2][1] == self.ttt[2][2] == 2:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (25,450), (525,450),21)
            pygame.display.update()

            self.over_text('Player B WIN!!!')

        # column
        elif self.ttt[0][0] == self.ttt[1][0] == self.ttt[2][0] == 2:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (100,25), (100,525),21)
            pygame.display.update()

            self.over_text('Player B WIN!!!')

        elif self.ttt[0][1] == self.ttt[1][1] == self.ttt[2][1] == 2:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (275,25), (275,525),21)
            pygame.display.update()

            self.over_text('Player B WIN!!!')

        elif self.ttt[0][2] == self.ttt[1][2] == self.ttt[2][2] == 2:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (450,25), (450,525),21)
            pygame.display.update()

            self.over_text('Player B WIN!!!')

        # diagonal
        elif self.ttt[0][0] == self.ttt[1][1] == self.ttt[2][2] == 2:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (25,25), (525,525),21)
            pygame.display.update()

            self.over_text('Player B WIN!!!')

        elif self.ttt[0][2] == self.ttt[1][1] == self.ttt[2][0] == 2:
            dep = True
            pygame.draw.line(win, (102, 101, 100), (525,25), (25,525),21)
            pygame.display.update()

            self.over_text('Player B WIN!!!')
        

        if dep == True:

            #  match over
            self.match_over()

            pygame.time.delay(3000)
            self.box()
    

    def check(self):

        self.check_1()
        self.check_2()
        
        if self.ttt[0][0] != 0 and self.ttt[0][1] != 0 and self.ttt[0][2] != 0 and self.ttt[1][0] != 0 and self.ttt[1][1] != 0 and self.ttt[1][2] != 0 and self.ttt[2][0] != 0 and self.ttt[2][1] != 0 and self.ttt[2][2] != 0:
            
            #  since it have draw so we have to make it draw
            self.over_text('Match Drawn!!!')

            #  match over also
            self.match_over()

            pygame.time.delay(3000)
            self.box()

    #  menu side
    def display(self):
        font = pygame.font.Font('freesansbold.ttf', 27)
        text = font.render('P', True, (255,0,0), None )
        textRect = text.get_rect()  
        textRect.center = (575,87.5 )
        win.blit(text, textRect) 

        text = font.render('M', True, (255,0,0), None )
        textRect = text.get_rect()  
        textRect.center = (575, 212.5)
        win.blit(text, textRect) 

        text = font.render('R', True, (255,0,0), None )
        textRect = text.get_rect()  
        textRect.center = (575,337.5 )
        win.blit(text, textRect) 

        text = font.render('S', True, (255,0,0), None )
        textRect = text.get_rect()  
        textRect.center = (575,462.5 )
        win.blit(text, textRect) 


        pygame.display.update()

    def RUN(self):

        #  default music start
        filename='filename_1.mp3'
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(loops=21, start=0.0)

        # display the side menu
        self.display()

            # at start time player 1
        self.turn('Player A Turn !')
        while self.run:
            
            

            # pygame.time.delay(100)


            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.box()

                    #  for the music to satart
                    elif event.key == pygame.K_m:
                        pygame.mixer.music.load(filename)
                        pygame.mixer.music.play(loops=21, start=0.0)
                    elif event.key == pygame.K_p:
                        pygame.mixer.music.stop()
                    elif event.key == pygame.K_s:
                        sys.exit()
                    elif event.key == pygame.K_r:
                        self.box()


                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos() 
                    print(pos)

                    if self.box_0.collidepoint(pos) and self.open_box_0:
                        if self.draw == 're':
                            # pygame.draw.rect(win, (255, 0, 0), (50,50,100,100))
                            pygame.draw.line(win, (255, 0, 0), (50, 50), (150,150), 17)
                            pygame.draw.line(win, (255, 0, 0), (150, 50), (50,150), 17)
                            self.draw = 'ci'
                            
                            self.clear()
                            self.turn('Player B Turn !')
                            
                            

                            self.ttt[0][0] = 1
                        else:
                            pygame.draw.circle(win, (17, 192, 2), (100,100), 50)
                            
                            self.draw = 're'

                            self.clear()
                            self.turn('Player A Turn !')
                            

                            self.ttt[0][0] = 2
                        
                        self.open_box_0 = False
                        # self.check()
                

                    elif self.box_1.collidepoint(pos) and self.open_box_1:
                        if self.draw == 're':
                            # pygame.draw.rect(win, (255, 0, 0), (225,50,100,100))
                            pygame.draw.line(win, (255, 0, 0), (225, 50), (325,150), 17)
                            pygame.draw.line(win, (255, 0, 0), (325, 50), (225,150), 17)
                            self.draw = 'ci'

                            self.clear()
                            self.turn('Player B Turn !')
                            

                            self.ttt[0][1] = 1
                        else:
                            pygame.draw.circle(win, (17, 192, 2), (275,100), 50)
                            self.draw = 're'

                            self.clear()
                            self.turn('Player A Turn !')
                            

                            self.ttt[0][1] = 2

                        self.open_box_1 = False
                        # self.check()
                

                    elif self.box_2.collidepoint(pos) and self.open_box_2:
                        if self.draw == 're':
                            # pygame.draw.rect(win, (255, 0, 0), (400,50,100,100))
                            pygame.draw.line(win, (255, 0, 0), (400, 50), (500,150), 17)
                            pygame.draw.line(win, (255, 0, 0), (500, 50), (400,150), 17)
                            self.draw = 'ci'

                            self.clear()
                            self.turn('Player B Turn !')
                            

                            self.ttt[0][2] = 1
                        else:
                            pygame.draw.circle(win, (17, 192, 2), (450,100), 50)
                            self.draw = 're'

                            self.clear()
                            self.turn('Player A Turn !')
                            

                            self.ttt[0][2] = 2

                        self.open_box_2 =False
                        # self.check()
                
                        

                    elif self.box_3.collidepoint(pos) and self.open_box_3:
                        if self.draw == 're':
                            # pygame.draw.rect(win, (255, 0, 0), (50,225,100,100))
                            pygame.draw.line(win, (255, 0, 0), (50, 225), (150,325), 17)
                            pygame.draw.line(win, (255, 0, 0), (150, 225), (50,325), 17)
                            self.draw = 'ci'

                            self.clear()
                            self.turn('Player B Turn !')
                            

                            self.ttt[1][0] = 1
                        else:
                            pygame.draw.circle(win, (17, 192, 2), (100,275), 50)
                            self.draw = 're'

                            self.clear()
                            self.turn('Player A Turn !')
                            

                            self.ttt[1][0] = 2

                        self.open_box_3 = False
                        # self.check()
                

                    elif self.box_4.collidepoint(pos) and self.open_box_4:
                        if self.draw == 're':
                            # pygame.draw.rect(win, (255, 0, 0), (225,225,100,100))
                            pygame.draw.line(win, (255, 0, 0), (225, 225), (325,325), 17)
                            pygame.draw.line(win, (255, 0, 0), (325, 225), (225,325), 17)
                            self.draw = 'ci'

                            self.clear()
                            self.turn('Player B Turn !')
                            

                            self.ttt[1][1] = 1
                        else:
                            pygame.draw.circle(win, (17, 192, 2), (275,275), 50)
                            self.draw = 're'

                            self.clear()
                            self.turn('Player A Turn !')
                            

                            self.ttt[1][1] = 2

                        self.open_box_4 = False
                        # self.check()
                

                    elif self.box_5.collidepoint(pos) and self.open_box_5:
                        if self.draw == 're':
                            # pygame.draw.rect(win, (255, 0, 0), (400,225,100,100))
                            pygame.draw.line(win, (255, 0, 0), (400, 225), (500,325), 17)
                            pygame.draw.line(win, (255, 0, 0), (500, 225), (400,325), 17)
                            self.draw = 'ci'

                            self.clear()
                            self.turn('Player B Turn !')
                            

                            self.ttt[1][2] = 1
                        else:
                            pygame.draw.circle(win, (17, 192, 2), (450,275), 50)
                            self.draw = 're'

                            self.clear()
                            self.turn('Player A Turn !')
                            
                        
                            self.ttt[1][2] = 2

                        self.open_box_5 = False
                        # self.check()
                

                    elif self.box_6.collidepoint(pos) and self.open_box_6:
                        if self.draw == 're':
                            # pygame.draw.rect(win, (255, 0, 0), (50,400,100,100))
                            pygame.draw.line(win, (255, 0, 0), (50, 400), (150,500), 17)
                            pygame.draw.line(win, (255, 0, 0), (150, 400), (50,500), 17)
                            self.draw = 'ci'

                            self.clear()
                            self.turn('Player B Turn !')
                            

                            self.ttt[2][0] = 1
                        else:
                            pygame.draw.circle(win, (17, 192, 2), (100,450), 50)
                            self.draw = 're'

                            self.clear()
                            self.turn('Player A Turn !')
                            

                            self.ttt[2][0] = 2

                        self.open_box_6 = False
                        # self.check()
                

                    elif self.box_7.collidepoint(pos) and self.open_box_7:
                        if self.draw == 're':
                            # pygame.draw.rect(win, (255, 0, 0), (225,400,100,100))
                            pygame.draw.line(win, (255, 0, 0), (225, 400), (325,500), 17)
                            pygame.draw.line(win, (255, 0, 0), (325, 400), (225,500), 17)
                            self.draw = 'ci'

                            self.clear()
                            self.turn('Player B Turn !')
                            

                            self.ttt[2][1] = 1
                        else:
                            pygame.draw.circle(win, (17, 192, 2), (275,450), 50)
                            self.draw = 're'

                            self.clear()
                            self.turn('Player A Turn !')
                            

                            self.ttt[2][1] = 2

                        self.open_box_7 = False
                        # self.check()
                

                    elif self.box_8.collidepoint(pos) and self.open_box_8:
                        if self.draw == 're':
                            # pygame.draw.rect(win, (255, 0, 0), (400,400,100,100))
                            pygame.draw.line(win, (255, 0, 0), (400, 400), (500,500), 17)
                            pygame.draw.line(win, (255, 0, 0), (500, 400), (400,500), 17)
                            self.draw = 'ci'

                            self.clear()
                            self.turn('Player B Turn !')
                            

                            self.ttt[2][2] = 1
                        else:
                            pygame.draw.circle(win, (17, 192, 2), (450,450), 50)
                            self.draw = 're'

                            self.clear()
                            self.turn('Player A Turn !')
                            

                            self.ttt[2][2] = 2

                        self.open_box_8 = False

# slide menu activity
                    elif self.box_9.collidepoint(pos):
                        pygame.mixer.music.stop()

                    elif self.box_10.collidepoint(pos):
                        pygame.mixer.music.load(filename)
                        pygame.mixer.music.play(loops=21, start=0.0)

                    elif self.box_11.collidepoint(pos):
                        self.box()

                    elif self.box_12.collidepoint(pos):
                        sys.exit()

                    else:
                        pass

            
            pygame.display.update()
        # self.check() for the completion   and win or drraw
            self.check()


        pygame.quit()
    
    
x = TTT()
x.box()