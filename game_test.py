import pygame

pygame.init()
keep_going = True
base_speed = 4

screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
screen_rect = screen.get_rect()

timer = pygame.time.Clock()

car = pygame.image.load("resources/car.png")
car = pygame.transform.scale(car, (100, 200))
car_rect = car.get_rect()

conus = pygame.image.load("resources/cone.png")
conus = pygame.transform.scale(conus, (50, 50))
conus_rect = conus.get_rect()

x = screen_rect.centerx - car_rect.centerx
y = screen_rect.centery - car_rect.centery

win_w = screen.get_size()[0]
win_h = screen.get_size()[1]

border_vertical = win_w - car.get_size()[0]
border_horizontal = win_h - car.get_size()[1]

conus_rect.x = 500
conus_rect.y = 100

pygame.mouse.set_visible(False)

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    if pygame.key.get_pressed()[pygame.K_LCTRL]:
        speed = base_speed * 2
    else:
        speed = base_speed
    if pygame.key.get_pressed()[pygame.K_UP]:
        y = y - speed if y > 0 else 0
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        y = y + speed if y < border_horizontal else border_horizontal
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        x = x - speed if x > 0 else 0
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        x = x + speed if x < border_vertical else border_vertical
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        keep_going = False

    car_rect.x = x
    car_rect.y = y

    # if car_rect.colliderect(conus_rect):
    #     conus_rect.x = 4000
    #     conus_rect.y = 4000

    screen.fill((80, 80, 80))
    screen.blit(conus, conus_rect)
    screen.blit(car, car_rect)

    pygame.display.update()
    timer.tick(60)

pygame.quit()
