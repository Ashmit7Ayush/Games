#  border ciustom
#  color custom
#  position custom
#  one liner y
#  customing the boundtion
#  name custom




# music custom



import pygame
from pygame import mixer

mixer.init()

pygame.init()

win = pygame.display.set_mode((750,500))

pygame.display.set_caption('MyPong_Game')


# music
# filename = 'Treasure BGM Entrance.mp3'
# filename = 'Common 8.mp3'
# filename = '10-billion-husbands.mp3'
# mixer.music.load(filename)
# mixer.music.set_volume(0.5)
# mixer.music.play(loops=21)

# short music
def fast():
    filename2 = 'Dice 3.mp3'
    mixer.music.load(filename2)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    pygame.time.delay(100)
    mixer.music.stop()


#  variation in the color
white = (255,255, 255)
blue = (106, 90, 205)
deep = (0, 0, 255)
green = (91, 212, 0, 0.7)
black = (0,0,0)

#  giving the side border
col = (255, 99, 71)


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,75])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.points = 0
        self.speed = 10



class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = 5
        self.dx = 1
        self.dy = 1



paddle_1 = Paddle()
paddle_1.rect.x = 15
paddle_1.rect.y = 225

paddle_2 = Paddle()
paddle_2.rect.x = 725
paddle_2.rect.y = 225



pong = Ball()
pong.rect.x = 375
pong.rect.y = 250


all_ = pygame.sprite.Group()
all_.add(paddle_1, paddle_2,pong)


def redraw():
    
    win.fill(black)

    # border
    pygame.draw.rect(win, col ,(0,0,750,15))
    pygame.draw.rect(win, col ,(0,0,14,500))
    pygame.draw.rect(win, col ,(736,0,750,500))
    pygame.draw.rect(win, col ,(0,485,750,500))

    #  for the point showing
    font = pygame.font.SysFont('Comic Sans MS', 21)
    text = font.render('PING-PONG', False, green)
    textRect = text.get_rect()
    textRect.center = (750//2,50)
    win.blit(text, textRect)


    #  _Player one
    p_1_score = font.render('Pla-1 -> '+str(paddle_1.points), False, deep)
    p_1Rect = p_1_score.get_rect()
    p_1Rect.center = (100,50)
    win.blit(p_1_score, p_1Rect)

    #  _Player two
    p_2_score = font.render('Pla-2 -> '+str(paddle_2.points), False, deep)
    p_2Rect = p_2_score.get_rect()
    p_2Rect.center = (650,50)
    win.blit(p_2_score, p_2Rect)

    all_.draw(win)
    pygame.display.update()

run = True



while run:
    pygame.time.delay(21)

   
    for event in pygame.event.get():

        if event.type  == pygame.QUIT:
            run = False

    
    key = pygame.key.get_pressed()    
    if key[pygame.K_w]:
        # making changes so that boundation 15 + speed i.e 10
        if paddle_1.rect.y >= 25:
            paddle_1.rect.y +=  -paddle_1.speed
    elif key[pygame.K_s]:
        # making changes so that boundation 485 - speed i.e 10 - 75
        if paddle_1.rect.y <= 400:
            paddle_1.rect.y += paddle_1.speed

    if key[pygame.K_UP]:
        if paddle_2.rect.y >= 25:
            paddle_2.rect.y +=  -paddle_2.speed
    elif key[pygame.K_DOWN]:
        if paddle_2.rect.y <= 400:
            paddle_2.rect.y += paddle_2.speed

    
   
    pong.rect.x += pong.speed * pong.dx
    pong.rect.y += pong.speed * pong.dy

    
    if pong.rect.y >= 485 or pong.rect.y <= 15:
        pong.dy *= -1
    
    if pong.rect.x >= 735:
        
        # short music
        # fast()
        filename2 = 'Dice 3.mp3'
        mixer.music.load(filename2)
        mixer.music.set_volume(0.7)
        mixer.music.play()
        pygame.time.delay(100)
        # mixer.music.stop()
    
        
        pong.rect.x = 700
        pong.dx = -1
        paddle_1.points += 1
    if pong.rect.x <= 15:
        # short music
        # fast()
        filename2 = 'Dice 3.mp3'
        mixer.music.load(filename2)
        mixer.music.set_volume(0.7)
        mixer.music.play()
        pygame.time.delay(100)
        # mixer.music.stop()


        pong.rect.x = 50
        pong.dx = 1
        paddle_2.points +=1

    # if event.type == pygame.MOUSEBUTTONUP:
    #                 pos = pygame.mouse.get_pos() 
    #                 print(pos)
    
    if paddle_1.rect.colliderect(pong.rect) or paddle_2.rect.colliderect(pong.rect):
        pong.dx *= -1

        
    redraw()
    pygame.display.update()

pygame.quit()