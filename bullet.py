from variables import *

class Bullet:
     def __init__(self, x, y, speed =-12):
          self.image = pygame.transform.scale(bullet_img, (10, 20))
          self.x = x + 20
          self.y = y
          self.speed = speed
          self.active = True

     def move(self):
          self.y += self.speed
          if self.y < 0 or self.y > HEIGHT:
               self.active = False

     def draw(self):
          screen.blit(self.image, (self.x, self.y))