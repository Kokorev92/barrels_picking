import pygame

pygame.init()
keep_going = True
screen = pygame.display.set_mode([700, 700])

timer = pygame.time.Clock()

FPS = 60


class Conus(pygame.sprite.Sprite):
    def __init__(self, x, speed, file_name, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] - self.rect.height:
            self.rect.y += self.speed
        else:
            self.kill


conuses = pygame.sprite.Group()

conus_1 = Conus(100, 5, "conus.png", conuses)
conus_2 = Conus(400, 10, "conus.png", conuses)
conus_3 = Conus(200, 15, "conus.png", conuses)

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        keep_going = False

    pygame.display.update()
    timer.tick(FPS)

    screen.fill([127, 127, 127])

    conuses.draw(screen)
    conuses.update(screen.get_rect().height)

pygame.quit()
