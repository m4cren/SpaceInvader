from variables import *

class Player:
     def __init__(self):
          self.image = pygame.transform.scale(player_img, (100,100))
          self.x = WIDTH//2 - 25
          self.y = HEIGHT -70
          self.speed = 5
          self.health = 50

     def move(self, direction):
          if direction == 'left' and self.x >0:
               self.x -= self.speed
          if direction == 'right' and self.x < WIDTH -50:
               self.x += self.speed
          if direction == 'up' and self.y > HEIGHT//2:
               self.y -= self.speed
          if direction == 'down' and self.y > 100:
               self.y += self.speed
          

     
     def draw(self):
          screen.blit(self.image, (self.x, self.y))
          health_text = font.render(f'Player HP: {self.health}', True, GREEN)
          screen.blit(health_text, (10, 40))

     def take_damage(self):
          self.health -= 1
