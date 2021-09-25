from pygame import *

img_back = "images.jpg"
wedth = 700
height = 500

window = display.set_mode((wedth, height))
display.set_caption("ping-pong")
background = transform.scale(image.load(img_back), (wedth, height))

window.blit(background,(0,0))
display.update()
print(background)
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0,0))
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
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += 10
racket_1 = Racket_1(img_hero, 680, 230, 5, 20)
class Racket_2(Player):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += 10
racket_2 = Racket_2(img_hero, 20, 230, 5, 20)
