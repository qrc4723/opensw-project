import pygame 
import random
import sys
import time

pygame.init() 

high_score = '10000'
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
large_font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("지뢰찾기  High_score : " + high_score + "sec")

clock = pygame.time.Clock()


start_image = pygame.image.load("C:\coding\python\학교\오픈소스 SW\images\starticon.png")
quit_image = pygame.image.load("C:\coding\python\학교\오픈소스 SW\images\quiticon.png")
click_start_image = pygame.image.load("C:\coding\python\학교\오픈소스 SW\images\clickedStartIcon.png")
click_quit_image = pygame.image.load("C:\coding\python\학교\오픈소스 SW\images\clickedQuitIcon.png")
start_image = pygame.transform.scale(start_image, (240,80))
quit_image = pygame.transform.scale(quit_image, (240,80))
click_start_image = pygame.transform.scale(click_start_image, (240,80))
click_quit_image = pygame.transform.scale(click_quit_image, (240,80))
start_image1 = pygame.transform.scale(start_image, (120,40))
quit_image1 = pygame.transform.scale(quit_image, (120,40))
click_start_image1 = pygame.transform.scale(click_start_image, (120,40))
click_quit_image1 = pygame.transform.scale(click_quit_image, (120,40))

class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            screen.blit(img_in, (x,y))

def quit_game():
    pygame.quit()
    sys.exit()

def main_menu():
    menu = True
    screen = pygame.display.set_mode((800, 600))
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(WHITE)

        start_button = Button(start_image,100,260,240,80,click_start_image,100,260,select_difficulty)
        quit_button = Button(quit_image, 400, 260, 240, 80, click_quit_image, 400, 260, quit_game)
        pygame.display.update()
        clock.tick(15)

def select_difficulty():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(WHITE)

        map_easy_button = Button(start_image1,200,150,120,40,click_start_image1,200,150,set_map_difficulty1)
        map_normal_button = Button(quit_image1, 200, 300, 120, 40, click_quit_image1, 200, 300, set_map_difficulty2)
        map_hard_button = Button(quit_image1, 200, 450, 120, 40, click_quit_image1, 200, 450, set_map_difficulty3)

        mine_easy_button = Button(start_image1,400,150,120,40,click_start_image1,400,150,set_mine_difficulty1)
        mine_normal_button = Button(quit_image1, 400, 300, 120, 40, click_quit_image1, 400, 300, set_mine_difficulty2)
        mine_hard_button = Button(quit_image1, 400, 450, 120, 40, click_quit_image1, 400, 450, set_mine_difficulty3)
        
        pygame.display.update()
        clock.tick(15)

def set_map_difficulty1():
    global difficulty1
    difficulty1 = 1

def set_map_difficulty2():
    global difficulty1
    difficulty1 = 2

def set_map_difficulty3():
    global difficulty1
    difficulty1 = 3

def set_mine_difficulty1():
    global difficulty2
    difficulty2 = 1
    runGame()

def set_mine_difficulty2():
    global difficulty2
    difficulty2 = 2
    runGame()

def set_mine_difficulty3():
    global difficulty2
    difficulty2 = 3
    runGame()

def in_bound(column_index, row_index):
    if (0 <= column_index < COLUMN_COUNT and 0 <= row_index < ROW_COUNT):
        return True
    else:
        return False

def open_tile(column_index, row_index): 
    if not in_bound(column_index, row_index):
        return

    tile = grid[row_index][column_index]
    if not tile['open']:
        tile['open'] = True
    else:    
        return

    if tile['mine']:
        return

    mine_count_around = get_mine_count_around(column_index, row_index)
    if mine_count_around > 0:
        tile['mine_count_around'] = mine_count_around
    else:
        for dc, dr in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            column_index_around, row_index_around = (column_index + dc, row_index + dr)
            open_tile(column_index_around, row_index_around)

def get_mine_count_around(column_index, row_index):
    count = 0

    for dc, dr in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        column_index_around, row_index_around = (column_index + dc, row_index + dr)
        if in_bound(column_index_around, row_index_around) and grid[row_index_around][column_index_around]['mine']:
            count += 1
    return count

def runGame():
    start = time.time()
    SUCCESS = 1
    FAILURE = 2
    game_over = 0
    global column_index, COLUMN_COUNT, row_index, ROW_COUNT
    if difficulty1 == 1:
        SCREEN_WIDTH = 400
        SCREEN_HEIGHT = 600
        CELL_SIZE = 50
        COLUMN_COUNT = SCREEN_WIDTH // CELL_SIZE
        ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    elif difficulty1 == 2:
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        CELL_SIZE = 50
        COLUMN_COUNT = SCREEN_WIDTH // CELL_SIZE
        ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    elif difficulty1 == 3:
        SCREEN_WIDTH = 1600
        SCREEN_HEIGHT = 600
        CELL_SIZE = 50
        COLUMN_COUNT = SCREEN_WIDTH // CELL_SIZE
        ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    global grid
    grid = [[{'mine': False, 'open': False, 'mine_count_around': 0, 'flag': False} for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
    MINE_COUNT = 15 * difficulty1 * difficulty2
    for _ in range(MINE_COUNT):
        while True:
            column_index = random.randint(0, COLUMN_COUNT - 1)
            row_index = random.randint(0, ROW_COUNT - 1)
            tile = grid[row_index][column_index]
            if not tile['mine']:
                tile['mine'] = True 
                break

    while True: 
        clock.tick(30) 
        screen.fill(BLACK) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                column_index = event.pos[0] // CELL_SIZE
                row_index = event.pos[1] // CELL_SIZE
                if event.button == 1:
                    if in_bound(column_index, row_index):
                        tile = grid[row_index][column_index]
                        if tile['mine']:
                            tile['open'] = True
                            game_over = FAILURE
                        else:
                            open_tile(column_index, row_index)
                elif event.button == 3:
                    if in_bound(column_index, row_index):
                        tile = grid[row_index][column_index]
                        if not tile['flag']:
                            tile['flag'] = True
                        else:
                            tile['flag'] = False

                        success = True
                        for row_index in range(ROW_COUNT):
                            for column_index in range(COLUMN_COUNT):
                                tile = grid[row_index][column_index]
                                if tile['mine'] and not tile['flag']:
                                    success = False
                                    break
                        if success:
                            game_over = SUCCESS

        for column_index in range(COLUMN_COUNT):
            for row_index in range(ROW_COUNT):
                tile = grid[row_index][column_index]
                if tile['mine_count_around']:
                    mine_count_around_image = small_font.render('{}'.format(tile['mine_count_around']), True, YELLOW)
                    screen.blit(mine_count_around_image, mine_count_around_image.get_rect(centerx=column_index * CELL_SIZE + CELL_SIZE // 2, centery=row_index * CELL_SIZE + CELL_SIZE // 2))
                if tile['mine']:
                    mine_image = pygame.image.load("C:\coding\python\학교\오픈소스 SW\images\mine.png").convert()
                    mine_image = pygame.transform.scale(mine_image, (CELL_SIZE,CELL_SIZE))
                    screen.blit(mine_image, mine_image.get_rect(centerx=column_index * CELL_SIZE + CELL_SIZE // 2, centery=row_index * CELL_SIZE + CELL_SIZE // 2)) #지뢰 설치
                if not tile['open']:
                    pygame.draw.rect(screen, GRAY, pygame.Rect(column_index * CELL_SIZE, row_index * CELL_SIZE, CELL_SIZE, CELL_SIZE)) #커버
                if tile['flag']:
                    flag_image = pygame.image.load("C:\coding\python\학교\오픈소스 SW\images/flag.png").convert()
                    flag_image = pygame.transform.scale(flag_image, (CELL_SIZE,CELL_SIZE))
                    screen.blit(flag_image, (column_index * CELL_SIZE, row_index * CELL_SIZE))
                pygame.draw.rect(screen, WHITE, pygame.Rect(column_index * CELL_SIZE, row_index * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

        if game_over > 0:
            if game_over == SUCCESS:
                success_image = large_font.render('Success', True, RED)
                screen.blit(success_image, success_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))
            elif game_over == FAILURE:
                failure_image = large_font.render('Failure', True, RED)
                screen.blit(failure_image, failure_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))
                

        pygame.display.update() 
        if game_over == FAILURE:
            pygame.time.delay(2000)
            pygame.init()
            main_menu()
        elif game_over == SUCCESS:
            global high_score
            end = time.time()
            current_time = end - start
            if float(high_score) > current_time:
                high_score = str(current_time)
                pygame.display.set_caption("지뢰찾기  High_score : " + high_score + "sec")
                pygame.display.update()
            pygame.time.delay(2000)
            pygame.init()
            main_menu()
main_menu()