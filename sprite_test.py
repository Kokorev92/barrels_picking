import pygame
import random

from cone import Cone
from car import Car

pygame.init()
pygame.mouse.set_visible(False)

keep_going = True
game_over = False
screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)

timer = pygame.time.Clock()
random.seed()
FPS = 60
pygame.time.set_timer(pygame.USEREVENT, 500)
car_base_speed = 5

cone_image = 'cone.png'
cone_serf = pygame.image.load('resources/' + cone_image).convert_alpha()
cones = pygame.sprite.Group()

car_image = 'car.png'
car_serf = pygame.image.load('resources/' + car_image).convert_alpha()
car = Car(0, 0, car_base_speed, car_serf)

car_x = screen.get_rect().centerx - car.rect.centerx
car_y = screen.get_rect().centery - car.rect.centery

border_vertical = screen.get_size()[0] - car.rect.width
border_horizontal = screen.get_size()[1] - car.rect.height


def create_cone(group):
    x = random.randint(0, screen.get_rect().width)
    cone_speed = 5
    return Cone(x, cone_speed, cone_serf, group)


create_cone(cones)

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.USEREVENT:
            create_cone(cones)
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        keep_going = False

    if not game_over:
        if pygame.key.get_pressed()[pygame.K_LCTRL]:
            speed = car_base_speed * 2
        else:
            speed = car_base_speed
        if pygame.key.get_pressed()[pygame.K_UP]:
            car_y = car_y - speed if car_y > 0 else 0
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            car_y = car_y + speed if car_y < border_horizontal else border_horizontal
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            car_x = car_x - speed if car_x > 0 else 0
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            car_x = car_x + speed if car_x < border_vertical else border_vertical

        screen.fill([127, 127, 127])
        cones.draw(screen)
        screen.blit(car.image, car.rect)
        cones.update(screen.get_rect().height)
        car.update(car_x, car_y)
        if pygame.sprite.spritecollideany(car, cones, pygame.sprite.collide_mask):
            game_over = True
    else:
        f = pygame.font.Font('resources/3dumb.ttf', 78)
        game_over_text = f.render("GAME OVER", 1, (246, 198, 1))
        text_rect = game_over_text.get_rect(center=screen.get_rect().center)
        screen.blit(game_over_text, text_rect)

    pygame.display.update()
    timer.tick(FPS)
