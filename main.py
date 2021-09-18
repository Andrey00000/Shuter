from pygame import *
from random import randint
font.init()
font = font.SysFont("Arial", 30)
img_bullet = "rocket1.png"
img_bullet1 = "rocket1.png"
img_back = "images.jpg"
img_win = "space.jpg"
img_hero = "rocket2.png"
img_hero1 = "enemy3.png"
img_los = "blast.png"
img_enemy = "enemy1.png"
img_enemy1 = "enemy2.png"
score = 0
pobeda = 10
propusk = 0
max_propusk = 10
enemy_speed = 3
speed = 10
class Player(sprite.Sprite):
    def __init__(self, player_image, x, y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Hero(Player):
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x < 620:
            self.rect.x += speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20)
        bullets.add(bullet)
ship = Hero(img_hero, 300, 400, 80, 100)

class Enemy(Player):
    def update(self):
        self.rect.y += enemy_speed
        if self.rect.y > 500:
            global propusk
            propusk += 1
            self.rect.x = randint(80, 620)
            self.rect.y = 0
monsters = sprite.Group()
for i in range(4):
    monster = Enemy(img_enemy, randint(80, 620), -40, 80, 50)                
    monsters.add(monster)
class Bullet(Player):
    def update(self):
        self.rect.y -= speed
        if self.rect.y < 0:
            self.kill()            
bullets = sprite.Group()

window = display.set_mode((700, 500))
display.set_caption("Космонавты против Пришельцев.")
background = transform.scale(image.load(img_back), (700, 500))
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire() 
            elif e.key == K_1:
                finish = True
            elif e.key == K_2:
                finish = False 



    if not finish:
        window.blit(background,(0,0))
        text = font.render("Счет: " + str(score), 1, (255, 0, 0))
        place = text.get_rect(center = (50, 20))
        window.blit(text, place)
        text_lose = font.render("Пропущено: " + str(propusk), 1, (255, 0, 0))
        place = text.get_rect(center =(50, 50))
        window.blit(text_lose, place)
        ship.update()
        bullets.update()
        monsters.update()
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy(img_enemy, randint(80, 620), -40, 80, 50)
            monsters.add(monster)
            
        if sprite.spritecollide(ship, monsters, True) or propusk >= max_propusk:
            window.fill((255, 255, 255))
            img = image.load(img_los)
            window.blit(transform.scale(img, (700, 500)), (0, 0))
            text_lose2 = font.render("ПОРАЖЕНИЕ *_* ", 1, (255, 0, 0))
            place = text.get_rect(center =(300, 250))
            window.blit(text_lose2, place)
            time.delay(50)
            finish = True
        if score >= pobeda:
            window.fill((255, 255, 255))
            img_1 = image.load(img_win)
            window.blit(transform.scale(img_1, (700, 500)), (0, 0))
            text_lose1 = font.render("ПОБЕДА!!!", 1, (255, 0, 0))
            place = text.get_rect(center =(300, 250))
            window.blit(text_lose1, place)
            finish = True 
        display.update()
    time.delay(50)