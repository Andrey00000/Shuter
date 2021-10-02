from pygame import *
font.init()
font = font.SysFont("Arial", 30)

img_back = "images.jpg"
wedth = int(700 * 1.5)
height = int(500 * 1.5)
size_ball = 50
img_hero = "bullet.png"
img_ball = "pngwing.com.png"
img_win = "space.jpg"
img_los = "blast.png"
score = 0
pobeda = 7
pobeda_2 = 7
propusk = 0
max_propusk = 10

window = display.set_mode((wedth, height))
display.set_caption("ping-pong")
background = transform.scale(image.load(img_back), (wedth, height))
clock = time.Clock()
window.blit(background,(0,0))
display.update()
print(background)
class Player(sprite.Sprite):
    def __init__(self, player_image, x, y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Racket_1(Player):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        if keys[K_DOWN] and self.rect.y <  height - 60:
            self.rect.y += 10
racket_1 = Racket_1(img_hero, wedth - 20, 250, 15, 60)
class Racket_2(Player):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys[K_s] and self.rect.y < height - 60:
            self.rect.y += 10
racket_2 = Racket_2(img_hero, 20, 230, 15, 60)
class Ball(Player):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x >= wedth - 50 or self.rect.x ==0:
            self.speed_x *= -1
        if self.rect.y >= height - 50 or self.rect.y ==0:
            self.speed_y *= -1
        if self.rect.x >= wedth - size_ball:
            global propusk
            propusk += 1    
        if self.rect.x == 0:
            global score
            score += 1 
ball = Ball(img_ball, 350, 250, size_ball, size_ball)
ball.speed_x = 10
ball.speed_y = 10
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0,0))

        text = font.render("         Игрок №1: " + str(score), 1, (255, 0, 0))
        place = text.get_rect(center = (50, 20))
        window.blit(text, place)
        text_lose = font.render("         Игрок №2: " + str(propusk), 1, (255, 0, 0))
        place = text.get_rect(center =(50, 50))
        window.blit(text_lose, place)

        racket_1.update()
        racket_2.update()
        ball.update()
        racket_1.reset()
        racket_2.reset()
        ball.reset()

        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y

    if sprite.collide_rect(ball, racket_1,) or sprite.collide_rect(ball, racket_2):
        ball.speed_x *= -1

    display.update()
    clock.tick(60)
