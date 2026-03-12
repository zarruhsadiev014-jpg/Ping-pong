from pygame import *
font.init()
back = (0,204,204)
window = display.set_mode((700,500))
FPS = 60
cloak = time.Clock()
game = True
window.fill(back)
finish = False
d_x = 3
d_y = 3
font1 = font.SysFont('verdana',100).render('R WIN',True,(255,22,222))
font2 = font.SysFont('verdana',100).render('L WIN',True,(255,22,222))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,player_width,player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_width,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 120:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <  500 - 120:
            self.rect.y += self.speed
racket_left = Player('racket.png',0,250,5,40,120)
racket_right = Player('racket.png',660,250,5,40,120)
ball = Player('ball.png',300,250,7,55,55)
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        ball.rect.x += d_x 
        ball.rect.y += d_y
        
        if ball.rect.y> 450 or ball.rect.y < 0:
            d_y *= -1

        if sprite.collide_rect(racket_left,ball):
            d_x *= -1
        if sprite.collide_rect(racket_right,ball):
            d_x *= -1
        
        if ball.rect.x > 700:
            print(ball.rect.x)
            window.blit(font2,(200,200))
            finish = True
        if ball.rect.x < - 55:
            print(ball.rect.x)
            window.blit(font1,(200,200))
            finish = True
        racket_right.reset()
        racket_right.update_2()
        racket_left.reset()
        racket_left.update()
        ball.reset()
    cloak.tick(FPS)
    display.update()
