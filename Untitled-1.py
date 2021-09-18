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