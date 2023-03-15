import pygame
import random

from conus import Conus

pygame.init()
keep_going = True
screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)

timer = pygame.time.Clock()
random.seed()
FPS = 60

conuses_images = ['conus.png', 'conus.png', 'conus.png']
conuses_serf = [pygame.image.load(path).convert_alpha() for path in conuses_images]
conuses = pygame.sprite.Group()
pygame.time.set_timer(pygame.USEREVENT, 500)

def create_Conuse(group):
    i = random.randint(0, len(conuses_serf) - 1)
    x = random.randint(0, screen.get_rect().width)
    speed = random.randint(1, 5)

    return Conus(x, speed, conuses_serf[i], group)


create_Conuse(conuses)

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.USEREVENT:
            create_Conuse(conuses)
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        keep_going = False

    screen.fill([127, 127, 127])
    conuses.draw(screen)


    conuses.update(screen.get_rect().height)
    pygame.display.update()
    timer.tick(FPS)
    print(len(conuses))

pygame.quit()
