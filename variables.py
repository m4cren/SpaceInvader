import pygame
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GREY = (48, 48, 48)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
player_img = pygame.image.load('Images/character.png')

enemy_img = pygame.image.load('Images/small_monster.png')

bullet_img = pygame.image.load('Images/bullet.png')

master_enemy_img = pygame.image.load('Images/boss.png')




