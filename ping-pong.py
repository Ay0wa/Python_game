from pygame import *
import random
dis = display.set_mode((1000,500))

game = True

background = transform.scale(
        image.load("background_blue.png"),    
        (1000, 500)
    )

class GameSprite(sprite.Sprite):
    def __init__(self, img, player_x, player_y, width, height, speed_player, speed_x, speed_y):
        super().__init__()
        self.width = width
        self.height = height
        self.imagee = transform.scale(image.load(img), (self.width,self.height))
        self.rect = self.imagee.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed_player
        self.speed_x = speed_x
        self.speed_y = speed_y
        
        
    def blit(self):
        dis.blit(self.imagee,(self.rect.x, self.rect.y))
        
class Lazer1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_RIGHT] and self.rect.y <= 400:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.y >= 0:
            self.rect.y -= self.speed
class Lazer2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y <= 400:
            self.rect.y += self.speed
        if keys[K_d] and self.rect.y >= 0:
            self.rect.y -= self.speed
lazer1 = Lazer1('laser.png', 40, 225, 20,100,5,5,1)
lazer2 = Lazer2('laser.png', 940, 225, 20,100,5,5,1)
class Ball(GameSprite):
    def update(self):
        if self.rect.y < 0 or self.rect.y > 450:
            self.speed_y *= -1
        elif self.rect.x < -100 or self.rect.x > 1050:
            self.rect.x = 450
            self.rect.y = 225
        if sprite.collide_rect(ball, lazer1) or sprite.collide_rect(ball, lazer2):
            self.speed_x *= -1
            
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        
            
clock = time.Clock()        
        
ball = Ball('ball_red_large.png', random.randint(100,900), random.randint(10,450), 50,50,1,3,3)        
while game: 
    dis.blit(background,(0,0))
    for ev in event.get():
        if ev.type == QUIT:
            game = False
    ball.update()
    ball.blit()
    lazer2.update()
    lazer2.blit()
    lazer1.update()
    lazer1.blit()
    
    clock.tick(60)
    display.update()