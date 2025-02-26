from variables import *
from bullet import Bullet
import random
class MasterEnemy:
     def __init__(self):
          self.image = pygame.transform.scale(master_enemy_img, (100, 100))
          self.x = WIDTH // 2 -50
          self.y = 50
          self.speed = 7
          self.health = 50
          self.direction = 1
          self.bullets = []

     def move(self, direction):
          # self.x += self.speed * self.direction
          # if self.x >= WIDTH - 120 or self. x <= 0:
          #      self.direction *= -1
          if direction == 'left' and self.x >0:
               self.x -= self.speed
          if direction == 'right' and self.x < WIDTH -50:
               self.x += self.speed
          if direction == 'up' and self.y >0:
               self.y -= self.speed
          if direction == 'down' and self.y < WIDTH -50:
               self.y += self.speed


     def fire(self):
          if random.randint(1, 3) == 1:
               self.bullets.append(Bullet(self.x + 45, self.y +90, speed=15))

     def draw(self):
          screen.blit(self.image, (self.x, self.y))
          health_text = font.render(f"Boss HP: {self.health}", True, RED)
          screen.blit(health_text, (WIDTH - 220, 10))
     
     def take_damage(self):
          self.health -= 1
