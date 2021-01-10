import pygame

pygame.init()

win = pygame.display.set_mode((750,500))

pygame.display.set_caption('MyPong_Game')

white = (255,255, 255)
black = (0,0,0)


#  making classes
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0
#  speed of the paddle 
        self.speed = 14



class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = 4
        #  for the griding change
        self.dx = 1
        self.dy = 1


#  creating he objects
paddle_1 = Paddle()
paddle_1.rect.x = 25
paddle_1.rect.y = 225

paddle_2 = Paddle()
paddle_2.rect.x = 715
paddle_2.rect.y = 225



pong = Ball()
pong.rect.x = 375
pong.rect.y = 250

#  taking all the paddle1 paddle2 and pong at one place
all_ = pygame.sprite.Group()
all_.add(paddle_1, paddle_2,pong)


def redraw():
    #  makes the screen black
    win.fill(black)
    all_.draw(win)
    pygame.display.update()

run = True

while run:
    pygame.time.delay(10)


    for event in pygame.event.get():

        if event.type  == pygame.QUIT:
            run = False

        key = pygame.key.get_pressed()

        #  for paddle 1
        if key[pygame.K_w]:
            paddle_1.rect.y +=  paddle_1.speed
        elif key[pygame.K_s]:
            paddle_1.rect.y += paddle_1.speed

            #  for the paddle 2
        if key[pygame.K_UP]:
            paddle_2.rect.y +=  paddle_2.speed
        elif key[pygame.K_DOWN]:
            paddle_2.rect.y += paddle_2.speed

        
        pong.rect.x += pong.speed
        pong.rect.y += pong.speed

        
        

    redraw()
    pygame.display.update()

pygame.quit()