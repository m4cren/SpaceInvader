from variables import *
import random
from bullet import Bullet
class Enemy:
     def __init__(self, x, y):
          self.image = pygame.transform.scale(enemy_img, (40,40))
          self.x = x
          self.y = y
          self.speed = 3
          self.direction = 1
      

     def move(self):
          self.x += self.speed * self.direction
          if self.x >= WIDTH - 40 or self.x <= 0:
               self.direction *= -1
               self.y += 40
     
     def draw(self):
          screen.blit(self.image, (self.x, self.y))

     def fire(self):
          if random.randint(1, 15) == 1:
               self.bullets.append(Bullet(self.x + 45, self.y +90, speed=5))