from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax
import pygame, sys

class GameController(TwoPlayerGame):

  def __init__(self, players):
    self.players = players
    self.current_player = 1
    self.board = [0] * 9

  def possible_moves(self):
    return [a + 1 for a, b in enumerate(self.board) if b == 0]
  
  def make_move(self, move):
    self.board[int(move) - 1] = self.current_player
  
  def loss_condition(self):
    possible_combinations = [[1,2,3], [4,5,6], [7,8,9],
                             [1,4,7], [2,5,8], [3,6,9],
                             [1,5,9], [3,5,7]]
    
    return any([all([(self.board[i-1] == self.opponent_index)
            for i in combination]) for combination in possible_combinations])

  def is_over(self):
    return (self.possible_moves() == []) or self.loss_condition()
  
  def show(self):
    print('\n' + '\n'.join([['.', 'O', 'X'][self.board[3*j + i]]
        for i in range(3)]) for j in range(3))

  def scoring(self):
    return -100 if self.loss_condition() else 0

    
pygame.init()

board = [0] * 9
WIDTH, HEIGHT = 510, 510
MESSAGE_MARGIN = 30
white = (255, 255, 255)
black = (0, 0, 0)
turn = 1
ox_mark = ["", "O", "X"]
win_conditions = [[1,2,3],[4,5,6],[7,8,9],
                  [1,4,7],[2,5,8],[3,6,9],
                  [1,5,9],[3,5,7]]

screen = pygame.display.set_mode((WIDTH, HEIGHT + MESSAGE_MARGIN))
pygame.display.set_caption("TIC-TAC-TOE")
font = pygame.font.SysFont("comicsans",20)

def possible_moves():
  return [a + 1 for a, b in enumerate(board) if b == 0]

def loss_condition(who):
  opp = 1 if who == 2 else 2
  return any([all([(board[i-1] == opp)
          for i in combination]) for combination in win_conditions])

def is_over():
  return (possible_moves() == []) \
    or loss_condition(who=1) or loss_condition(who=2)

def calc_grid(pos):
  return (int(pos[1] / (HEIGHT/3)), int(pos[0] / WIDTH/3))

def _message_margin(txt):
  rect = pygame.Rect( (0, HEIGHT), (WIDTH, MESSAGE_MARGIN) )
  pygame.draw.rect(screen, black, rect)
  pos_text = font.reder(txt, True, white)
  pos_rect = pos_text.get_rect()
  pos_rect.center = ( WIDTH/2, HEIGHT + MESSAGE_MARGIN/2 )
  screen.blit(pos_text, pos_rect)


def draw_board(current_board):
  def _ox(txt, center):
    pos_text = font.render(txt, True, white)
    pos_rect = pos_text.get_rect()
    pos_rect.center = center
    screen.blit(pos_text, pos_rect)

    for i in range(3):
      for j in range(3):
        rect = pygame.Rect(
          (j * WIDTH/3, i * HEIGHT/3), (WIDTH/3, HEIGHT/3))
        pygame.draw.rect(screen, white, rect, width=1)
        _ox(ox_mark[board[i*3+j]])
  def loss_condition(self, who=None):
    if who is None:
      who = self.current_player
    return loss_condition(who)
  
  def is_over(self):
    return is_over()
  
  def show(self):
    print('\n' + '\n'.join([' '.join([['.', 'O', 'X'][self.board[3*j + i]]
              for i in range(3)]) for j in range(3)]))
  
  def scoring(self):
    i_lost = self.loss_condition()
    i_won = self.loss_condition(who=self.opponent_index)
    if i_lost and not i_won:
      return -100
    elif not i_lost and i_won:
      return 100
    return 0

running = True
finished = False

if __name__ == "__main__":
  gc = GameController([Human_Player(), AI_Player(Negamax(13))], turn, board)

  msg = "Player {}'s turn".format(ox_mark[gc.current_player])
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif not finished and event.type == pygame.MOUSEBUTTONDOWN:
        pos = calc_grid(pygame.mouse.get_pos())
        num = 1 + pos[0] * 3 + pos[1]

        if num in possible_moves():
          gc.play_move(num)

          if gc.current_player == 2:
            gc.play_move(gc.get_move())

          if is_over():
            finished = True
          
            if loss_condition(who=1):
              msg = "Player {} wins".format(ox_mark[2])
            elif loss_condition(who=2):
              msg = "Player {} wins".format(ox_mark[1])
            else:
              msg = "Tie"
        else:
          msg = "Player {}'s turn".format(ox_mark[gc.current_player])
    
    draw_board(board)
    _message_margin(msg)
    pygame.display.update()
    pygame.time.delay(200)

pygame.quit()
sys.exit()