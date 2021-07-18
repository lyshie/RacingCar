import pygame
from .env import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(path.join(IMAGE_DIR,"logo.png")),coin_size)
        self.rect = self.image.get_rect()
        self.rect.center = x ,y
<<<<<<< HEAD
        self.vel = 5
=======
        self.vel = 7
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2

    def update(self, *args):
        self.rect.centerx -= self.vel
        if self.rect.centerx < 0:
            self.kill()

    def move(self):
        self.rect.centery += self.vel
<<<<<<< HEAD
=======
        if self.rect.centery > HEIGHT:
            self.kill()
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2

    def get_position(self):
        return (self.rect.left, self.rect.top)