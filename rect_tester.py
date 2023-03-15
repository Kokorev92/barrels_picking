import pygame

pygame.init()

screen = pygame.display.set_mode([700, 700])
conus = pygame.image.load("resources/conus.png")
conus = pygame.transform.scale(conus, [100, 100])
conus_rect = conus.get_rect(topleft=[100,100])
print(conus_rect)

keep_going = True

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        keep_going = False

    screen.fill([127, 127, 127])
    screen.blit(conus, conus_rect)
    pygame.display.update()

pygame.quit()
