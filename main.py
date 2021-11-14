import random
import pygame
import time

snake_speed = 10

win_x = 500
win_y = 400

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('Simple Snake Game')
game_window = pygame.display.set_mode((win_x, win_y))

fps = pygame.time.Clock()

snake_position = [40, 80]

snake_body = [[40, 80], [30, 80], [20, 80], [10, 80]]

fruit_position = [random.randrange(1, (win_x//10))*10, random.randrange(1, (win_y//10))*10]

fruit_spawn = True

direction = "RIGHT"
change_to = direction

score = 0

def show_score(choice, color, font, size):
 score_font = pygame.font.SysFont(font, size)
 score_surface = score_font.render("Score: " + str(score), True, color)
 score_rect = score_surface.get_rect()
 game_window.blit(score_surface, score_rect)

def game_over():
 my_font = pygame.font.SysFont('times new roman', 50)

 game_over_surface = my_font.render("Your Score is: " + str(score), True, RED)

 game_over_rect = game_over_surface.get_rect()
 game_over_rect.midtop = (win_x/2, win_y/2)

 game_window.blit(game_over_surface, game_over_rect)

 pygame.display.flip()

 time.sleep(2)

 pygame.quit()

while True:

 for event in pygame.event.get():
  if event.type == pygame.KEYDOWN:
   if event.key == pygame.K_UP:
    change_to = "UP"
   if event.key == pygame.K_DOWN:
    change_to = "DOWN"
   if event.key == pygame.K_LEFT:
    change_to = "LEFT"
   if event.key == pygame.K_RIGHT:
    change_to = 'RIGHT'

 if change_to == "UP" and direction != "DOWN":
  direction = 'UP'

 if change_to == 'DOWN' and direction != "UP":
  direction = "DOWN"

 if change_to == "LEFT" and direction != 'RIGHT':
  direction = "LEFT"

 if change_to == 'RIGHT' and direction != "LEFT":
  direction = 'RIGHT'

 if direction == "UP":
  snake_position[1] -= 10
 if direction == 'DOWN':
  snake_position[1] += 10
 if direction == 'RIGHT':
  snake_position[0] += 10
 if direction == "LEFT":
  snake_position[0] -= 10

 snake_body.insert(0, list(snake_position))
 if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
  score += 10
  fruit_spawn = False
 else:
  snake_body.pop()

 if not fruit_spawn:
  fruit_position = [random.randrange(1, (win_x//10))*10, random.randrange(1, (win_y//10))*10]

 fruit_spawn = True

 game_window.fill(BLACK)

 for pos in snake_body:
  pygame.draw.rect(game_window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

 pygame.draw.rect(game_window, WHITE, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

 if snake_position[0] < 0 or snake_position[0] > win_x -10:
  game_over()

 if snake_position[1] < 0 or snake_position[1] > win_y-10:
  game_over()

 for block in snake_body[1:]:
  if snake_position[0] == block[0] and snake_position[1] == block[1]:
   game_over()

 show_score(1, WHITE, 'times new roman', 20)

 pygame.display.update()

 fps.tick(snake_speed)
