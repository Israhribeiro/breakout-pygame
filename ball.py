import pygame
from random import randint
preto = (0,0,0)

class Ball(pygame.sprite.Sprite):
  def __init__(self,cor,largura,altura):

    super().__init__()

    self.image = pygame.Surface([largura,altura])
    self.image.fill(preto)
    self.image.set_colorkey(preto)

    pygame.draw.rect(self.image,cor,[0,0,largura,altura])

    self.velocity = [randint(4,8),randint(-7,8)]

    self.rect = self.image.get_rect()
  def update(self):
    self.rect.x += self.velocity[0]
    self.rect.y += self.velocity[1]
  def bounce(self):
    self.velocity[0] = -self.velocity[0]
    self.velocity[1] = randint(-8,8)