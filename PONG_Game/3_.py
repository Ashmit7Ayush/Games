import pygame

pygame.init()

win = pygame.display.set_mode((750,500))

pygame.display.set_caption('MyPong_Game')

white = (255,255, 255)
black = (0,0,0)



class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0
        self.speed = 14



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

    #  for the point showing
    font = pygame.font.SysFont('Comic Sans MS', 21)
    text = font.render('PONG', False, white)
    textRect = text.get_rect()
    textRect.center = (750//2,25)
    win.blit(text, textRect)


    #  _Player one
    p_1_score = font.render(str(paddle_1.points), False, white)
    p_1Rect = p_1_score.get_rect()
    p_1Rect.center = (50,50)
    win.blit(p_1_score, p_1Rect)

    #  _Player two
    p_2_score = font.render(str(paddle_2.points), False, white)
    p_2Rect = p_2_score.get_rect()
    p_2Rect.center = (700,50)
    win.blit(p_2_score, p_2Rect)

    all_.draw(win)
    pygame.display.update()

run = True

while run:
    pygame.time.delay(21)


    for event in pygame.event.get():

        if event.type  == pygame.QUIT:
            run = False

    #  if out from there work more efficiently
    #  like below
    key = pygame.key.get_pressed()

        
    if key[pygame.K_w]:
        paddle_1.rect.y +=  -paddle_1.speed
    elif key[pygame.K_s]:
        paddle_1.rect.y += paddle_1.speed

            
    if key[pygame.K_UP]:
        paddle_2.rect.y +=  -paddle_2.speed
    elif key[pygame.K_DOWN]:
        paddle_2.rect.y += paddle_2.speed

    
    #  for the dirn
    pong.rect.x += pong.speed * pong.dx
    pong.rect.y += pong.speed * pong.dy

    #  change dirn when hit the end
    if pong.rect.y >= 485:
        pong.dy = -1
    if pong.rect.x >= 735:
        pong.rect.x = 700
        pong.dx = -1
        paddle_1.points += 1
    if pong.rect.y <= 15:
        pong.dy = 1
    if pong.rect.x <= 15:
        pong.rect.x = 50
        pong.dx = 1
        paddle_2.points +=1

        
    # oe line change x
    if paddle_1.rect.colliderect(pong.rect) or paddle_2.rect.colliderect(pong.rect):
        pong.dx *= -1

        
    redraw()
    pygame.display.update()

pygame.quit()