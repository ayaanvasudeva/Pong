import pygame, sys
from pygame.locals import QUIT, K_UP, K_DOWN, K_w, K_s
import random
from pygame import mixer #music
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

y = 2
x = 0
t = 0
n = 0
direction = 'f'
player1 = 0
player2 = 0
angle = 0
test_font_1 = pygame.font.Font(None, 40)
test_font_2 = pygame.font.Font(None, 40)
owner = pygame.font.Font(None, 20)
creator = owner.render('SuperSayianCoding', True, 'Black')
sky_surface = pygame.Surface((800, 400))
sky_surface.fill('yellow')
edge_up = pygame.Surface((800, 5))
edge_up.fill('yellow')
edge_up_rec = edge_up.get_rect(midtop=(0, 0))
edge_d = pygame.Surface((800, 5))
edge_d.fill('yellow')
edge_d_rec = edge_d.get_rect(midtop=(0, 295))
goal_surface = pygame.Surface((10, 800))
goal_surface.fill('yellow')
goal_rec = goal_surface.get_rect(midbottom=(400, 300))
goal1_surface = pygame.Surface((10, 800))
goal1_surface.fill('yellow')
goal1_rec = goal1_surface.get_rect(midbottom=(0, 300))
paddle_surface = pygame.Surface((12.5, 50))
paddle_surface.fill('white')
paddle_rec = paddle_surface.get_rect(midbottom=(20, 200))
paddle1_surface = pygame.Surface((12.5, 50))
paddle1_surface.fill('white')
paddle1_rec = paddle1_surface.get_rect(midbottom=(375, 200))
ball = pygame.image.load('ball.png').convert_alpha()
ball_rec = ball.get_rect(midbottom=(200, 175))
while True:
    hit = mixer.Sound('hit.wav')
    hit.play(-1)
    t += 1
    if t >= 1000:
      n = 1
    score1 = test_font_1.render(f'{player1}', True, 'Black')
    score2 = test_font_2.render(f'{player2}', True, 'Black')
    ball_rec.x += y
    ball_rec.y += x
    if paddle_rec.colliderect(ball_rec):
      direction = 'f'
      if n == 0:
        y = 3
      else:
        y = 4
      hit = mixer.Sound('hit.wav')
      hit.play(-1)
    if paddle1_rec.colliderect(ball_rec):
      direction = 'b'
      if n == 0:
        y = -3
      else:
        y = -4
      a = random.randint(1,2)
      if a == 1:
        if n == 0:
          x = -3
        else:
          x = -4
      else:
        if n == 0:
          x = 3
        else:
          x = 4
    if ball_rec.colliderect(edge_up_rec):
      if direction == 'b':
        if n == 0:
          y = -3
        else:
          y = -4
      else:
        if n == 0:
          y = 3
        else:
          y = 4
      if n == 0:
        x = 3
      else:
        x = 4
      angle += 75
    
    if ball_rec.colliderect(edge_d_rec):
      if direction == 'b':
         if n == 0:
           y = -3
         else:
           y = -4
      else:
        if n == 0:
          y = 3
        else:
          y = 4
      if n == 0:
        x = -3
      else:
        x = -4
      angle += 75
  
    if ball_rec.colliderect(goal_rec):
      direction = 'b'
      if n == 0:
        y = -3
      else:
        y = -4
      player1 += 1
    if ball_rec.colliderect(goal1_rec):
      direction = 'f'
      if n == 0:
        y = 3
      else:
        y = 4
      player2 += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
      paddle1_rec.y -= 3
    if keys[pygame.K_DOWN]:
      paddle1_rec.y += 3
    if keys[pygame.K_w]:
      paddle_rec.y -= 3
    if keys[pygame.K_s]:
      paddle_rec.y += 3
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(goal_surface,(goal_rec))
    screen.blit(goal1_surface,(goal1_rec))
    screen.blit(edge_up, (edge_up_rec))
    screen.blit(edge_d, (edge_d_rec))
    screen.blit(creator,(125,5))
    screen.blit(paddle_surface,(paddle_rec))
    screen.blit(paddle1_surface,(paddle1_rec))
    screen.blit(pygame.transform.rotate(ball, angle),ball_rec)
    screen.blit(score1,(0,0))
    if player2 <= 9:
      screen.blit(score2,(385,0))
    else:
      screen.blit(score2,(370,0))
    pygame.display.update()
    clock.tick(60)
