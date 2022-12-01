import pygame
pygame.init()

WIDTH, HEIGHT = 400, 400
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.SysFont("comicsans",24)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8 PUZZLE GAME")


state = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 0]
]

goalstate = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 0]
]

def text_surf(surf, txt, pos):
  pos_text = font.render(txt, True, white)
  pos_rect = pos_text.get_rect()
  pos_rect.center = pos
  surf.blit(pos_text, pos_rect)

def draw_grid(surf, state):
  for i in range(3):
    for j in range(3):
      rect = pygame.Rect(
        (j * WIDTH/3, i * HEIGHT/3), (WIDTH/3, HEIGHT/3))
      if state[i][j] != 0:
        text_surf(
          surf,
          "{}".format(state[i][j]),
          (j * WIDTH/3 + WIDTH/6, i * HEIGHT/3 + HEIGHT/6))
      pygame.draw.rect(surf, white, rect, width=2)

def recog_piece(pos):
  return(int(pos[1] / (HEIGHT/3)), int(pos[0] / (WIDTH/3)))

neigh = [
  [[(0, 1), (1, 0)], [(0, 0), (0, 2), (1, 1)], [(0, 1), (1, 2)]],
  [[(0, 0), (1, 1), (2, 0)], [(0, 1), (1, 0), (1, 2), (2, 1)], [(0, 2), (1, 1), (2, 2)]],
  [[(1, 0), (2, 1)], [(1, 1), (2, 0), (2, 2)], [(1, 2), (2, 1)]]
]

def move_to_empty(idx):
  empty_slot = None

  for slot in neigh[idx[0]][idx[1]]:
    if state[slot[0]][slot[1]] == 0:
      empty_slot = slot

  if empty_slot is None:
    return False

  state[empty_slot[0]][empty_slot[1]] = state[idx[0]][idx[1]]
  state[idx[0]][idx[1]] = 0

  return True

import random

def init_shuffle():
  for _ in range(1000):
    randclick = random.randint(0, 8)
    move_to_empty((int(randclick / 3), randclick % 3))

init_shuffle()

def goal_reached():
  for i in range(3):
    for j in range(3):
      if state[i][j] != goalstate[i][j]:
        return False
  return True

win = False
running = True
while running:
  pygame.time.delay(200)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and not win:
      pos = pygame.mouse.get_pos()
      idx = recog_piece(pos)

      move_to_empty(idx)
  
  screen.fill(black)
  draw_grid(screen, state)

  if not win and goal_reached():
    win = True
    running = False
  pygame.display.update()

pygame.quit()