import pygame
preto = (0,0,0)

class Paddle(pygame.sprite.Sprite):
  def __init__(self,cor,largura,altura):
    super().__init__()

    self.image = pygame.Surface([largura,altura])
    self.image.fill(preto)
    self.image.set_colorkey(preto)

    pygame.draw.rect(self.image,cor,[0,0,largura,altura])

    self.rect = self.image.get_rect()
  def moverParaEsquerda(self,pixels):
    self.rect.x -= pixels
    if self.rect.x < 0:
      self.rect.x = 0
  def moverParaDireita(self,pixels):
    self.rect.x += pixels
    if self.rect.x > 700:
      self.rect.x = 700