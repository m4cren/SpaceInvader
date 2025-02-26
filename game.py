from variables import *
from player import Player
from enemy import Enemy
import random
from masterEnemy import MasterEnemy
from bullet import Bullet

class SpaceInvader:
     def __init__(self):
          self.player = Player()
          self.enemies = [Enemy(random.randint(50, WIDTH-50), random.randint(50, 200)) for _ in range(5)]
          self.bullets = []
          self.enemy_count = 0
          self.master_enemy = MasterEnemy()
          self.running = True

     def run(self):
          while self.running:
               screen.fill(GREY)
               self.handle_events()
               self.update()
               self.draw()

               if self.master_enemy and self.master_enemy.health <= 0:
                    self.display_message("You Win", f"Total Points: {self.enemy_count}")
                    self.running = False

               if self.player.health <= 0:
                    self.display_message("Game Over", f"Total Points")
                    self.running(False)

               pygame.display.update()
               clock.tick(30)

     def handle_events(self):
          keys = pygame.key.get_pressed()

          if keys[pygame.K_LEFT]:
               self.player.move('left')
          
          if keys[pygame.K_RIGHT]:
               self.player.move('right')
          
          if keys[pygame.K_UP]:
               self.player.move('up')
          if keys[pygame.K_DOWN]:
               self.player.move('down')

          if keys[pygame.K_a]:
               self.master_enemy.move('left')
          
          if keys[pygame.K_d]:
               self.master_enemy.move('right')
          
          if keys[pygame.K_w]:
               self.master_enemy.move('up')
          if keys[pygame.K_s]:
               self.master_enemy.move('down')

          if keys[pygame.K_RALT]:
               if random.randint(1, 5) == 2:
                    
                    self.bullets.append(Bullet(self.player.x, self.player.y))

          if keys[pygame.K_LALT]:
               self.master_enemy.fire()
          
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    self.running = False

     def update(self):

          
             

          for bullet in self.bullets:
               bullet.move()

          self.bullets = [b for b in self.bullets if b.active]

          for bullet in self.bullets:
               for enemy in self.enemies:
                    if enemy.x < bullet.x < enemy.x + 40 and enemy.y < bullet.y < enemy.y + 40:
                         self.enemies.remove(enemy)
                         self.bullets.remove(bullet)
          
                   
                         break
          
          # if self.enemy_count >= 30:
          #      if not self.master_enemy:
          #           self.master_enemy = MasterEnemy()

          #      self.master_enemy.move()
          #      self.master_enemy.fire()

               for bullet in self.master_enemy.bullets:
                    bullet.move()

                    # if bullet.x < self.player.x + 50 and bullet.x + 10 > self.player.x and bullet.y > self.player.y:
                    if self.player.x < bullet.x < self.player.x + 50 and self.player.y < bullet.y < self.player.y + 10:
                         self.player.take_damage()
                         self.master_enemy.bullets.remove(bullet)
                    
               
               for bullet in self.bullets:
                    if self.master_enemy.x < bullet.x < self.master_enemy.x + 100 and self.master_enemy.y < bullet.y < self.master_enemy.y + 100:
                         self.master_enemy.take_damage()
                         self.bullets.remove(bullet)


     def draw(self):
          self.player.draw()



          for bullet in self.bullets:
               bullet.draw()

          if self.master_enemy:
               self.master_enemy.draw()

               for bullet in self.master_enemy.bullets:
                    bullet.draw()

          score_text = font.render(f'Enemies Defeated: {self.enemy_count}', True, WHITE)
          screen.blit(score_text, (10, 10))


     def display_message(self, message, subtext):
          screen.fill(BLACK)
          text = font.render(message, True, WHITE)
          subtext = font.render(subtext, True, WHITE)
          screen.blit(text, (WIDTH//2-100, HEIGHT//2-20))
          screen.blit(subtext, (WIDTH//2-100, HEIGHT//2+20))
          pygame.display.update()
          pygame.time.delay(3000)

