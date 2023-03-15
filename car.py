import pygame


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, surf):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (100, 200))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args):
        self.rect.x = args[0]
        self.rect.y = args[1]

