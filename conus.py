import pygame

class Conus(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(x, -100))
        self.speed = speed
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0]:
            self.rect.y += self.speed
        else:
            self.kill()