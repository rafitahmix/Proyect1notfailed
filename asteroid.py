import pygame, random


class Asteroid(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.size = (10,20)
    self.image = pygame.image.load("asteroid.png")
    self.image = pygame.transform.smoothscale(self.image, self.size)
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.speed = pygame.math.Vector2(0,0)
    self.speed = rotate_ip(random.randint(0, 360))
def update(self):
  screen_info = pygame.display.Info()
  self.rect.move(self.speed)
  
