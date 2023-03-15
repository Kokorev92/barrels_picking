import pygame
import random

from conus import Conus

pygame.init()
keep_going = True
screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)

timer = pygame.time.Clock()
random.seed()
FPS = 60

cone_image = 'conus.png'
cone_serf = pygame.image.load('resources/' + cone_image).convert_alpha()
cones = pygame.sprite.Group()
pygame.time.set_timer(pygame.USEREVENT, 250)


def create_Conuse(group):
    x = random.randint(0, screen.get_rect().width)
    speed = 5
    return Conus(x, speed, cone_serf, group)


create_Conuse(cones)

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.USEREVENT:
            create_Conuse(cones)
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        keep_going = False

    screen.fill([127, 127, 127])
    cones.draw(screen)

    cones.update(screen.get_rect().height)
    pygame.display.update()
    timer.tick(FPS)

pygame.quit()
