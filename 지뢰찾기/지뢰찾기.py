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
difficulty1 = 2

clock = pygame.time.Clock()


start_image = pygame.image.load(r"images\starticon.png")
quit_image = pygame.image.load(r"images\quiticon.png")
click_start_image = pygame.image.load(r"images\clickedStartIcon.png")
click_quit_image = pygame.image.load(r"images\clickedQuitIcon.png")
easy_image = pygame.image.load(r"images\Easy.png")
normal_image = pygame.image.load(r"images\Normal.png")
hard_image = pygame.image.load(r"images\Hard.png")
click_easy_image = pygame.image.load(r"images\click_easy.png")
click_normal_image = pygame.image.load(r"images\click_normal.png")
click_hard_image = pygame.image.load(r"images\click_hard.png")
start_image = pygame.transform.scale(start_image, (240,80))
quit_image = pygame.transform.scale(quit_image, (240,80))
click_start_image = pygame.transform.scale(click_start_image, (240,80))
click_quit_image = pygame.transform.scale(click_quit_image, (240,80))
easy_image = pygame.transform.scale(easy_image, (120,40))
normal_image = pygame.transform.scale(normal_image, (120,40))
hard_image = pygame.transform.scale(hard_image, (120,40))
click_easy_image = pygame.transform.scale(click_easy_image, (120,40))
click_normal_image = pygame.transform.scale(click_normal_image, (120,40))
click_hard_image = pygame.transform.scale(click_hard_image, (120,40))
temp1_image = easy_image
temp2_image = normal_image
temp3_image = hard_image

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
        
        screen.fill(BLACK)

        start_button = Button(start_image, 100, 260, 240, 80, click_start_image, 100, 260, select_difficulty)
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
        
        screen.fill(BLACK)
        high_score_image = small_font.render("High_score : " + high_score + "sec", True, RED)
        screen.blit(high_score_image, high_score_image.get_rect(centerx= 650, centery = 20))
        map_difficulty_image = large_font.render('Map', True, WHITE)
        screen.blit(map_difficulty_image, map_difficulty_image.get_rect(centerx= 250, centery= 80))
        mine_difficulty_image = large_font.render('Mine', True, WHITE)
        screen.blit(mine_difficulty_image, mine_difficulty_image.get_rect(centerx= 550, centery= 80))
 
        map_easy_button = Button(temp1_image, 200, 150, 120, 40, click_easy_image, 200, 150, set_map_difficulty1)
        map_normal_button = Button(temp2_image, 200, 300, 120, 40, click_normal_image, 200, 300, set_map_difficulty2)
        map_hard_button = Button(temp3_image, 200, 450, 120, 40, click_hard_image, 200, 450, set_map_difficulty3)

        mine_easy_button = Button(easy_image, 500, 150, 120, 40, click_easy_image, 500, 150, set_mine_difficulty1)
        mine_normal_button = Button(normal_image, 500, 300, 120, 40, click_normal_image, 500, 300, set_mine_difficulty2)
        mine_hard_button = Button(hard_image, 500, 450, 120, 40, click_hard_image, 500, 450, set_mine_difficulty3)
        
        pygame.display.update()
        clock.tick(15)

def set_map_difficulty1():
    global difficulty1, temp1_image, temp2_image, temp3_image
    difficulty1 = 1
    temp1_image = click_easy_image
    temp2_image = normal_image
    temp3_image = hard_image

def set_map_difficulty2():
    global difficulty1, temp1_image, temp2_image, temp3_image
    difficulty1 = 2
    temp1_image = easy_image
    temp2_image = click_normal_image
    temp3_image = hard_image

def set_map_difficulty3():
    global difficulty1, temp1_image, temp2_image, temp3_image
    difficulty1 = 3
    temp1_image = easy_image
    temp2_image = normal_image
    temp3_image = click_hard_image

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
        SCREEN_WIDTH = 450
        SCREEN_HEIGHT = 450
        CELL_SIZE = 50
        COLUMN_COUNT = SCREEN_WIDTH // CELL_SIZE
        ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    elif difficulty1 == 2:
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 800
        CELL_SIZE = 50
        COLUMN_COUNT = SCREEN_WIDTH // CELL_SIZE
        ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    elif difficulty1 == 3:
        SCREEN_WIDTH = 1500
        SCREEN_HEIGHT = 800
        CELL_SIZE = 50
        COLUMN_COUNT = SCREEN_WIDTH // CELL_SIZE
        ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    global grid
    grid = [[{'mine': False, 'open': False, 'mine_count_around': 0, 'flag': False} for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
    
    if difficulty1 == 1:
        if difficulty2 == 1:
            MINE_COUNT = 10
        elif difficulty2 == 2:
            MINE_COUNT = 20
        elif difficulty2 == 3:
            MINE_COUNT = 30
    elif difficulty1 == 2:
        if difficulty2 == 1:
            MINE_COUNT = 40
        elif difficulty2 == 2:
            MINE_COUNT = 80
        elif difficulty2 == 3:
            MINE_COUNT = 120
    elif difficulty1 == 3:
        if difficulty2 == 1:
            MINE_COUNT = 99
        elif difficulty2 == 2:
            MINE_COUNT = 150
        elif difficulty2 == 3:
            MINE_COUNT = 200
    #Map_size : {9 * 9 = 81, 16 * 16 = 256, 30 * 16 = 480}
    #Map : {Mine}
    #easy: {10, 20, 30}
    #normal: {40, 80, 120}
    #hard: {99, 150, 200}
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
                pygame.quit()
                sys.exit()
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
                    mine_image = pygame.image.load(r"images\mine.png").convert()
                    mine_image = pygame.transform.scale(mine_image, (CELL_SIZE,CELL_SIZE))
                    screen.blit(mine_image, mine_image.get_rect(centerx=column_index * CELL_SIZE + CELL_SIZE // 2, centery=row_index * CELL_SIZE + CELL_SIZE // 2)) #지뢰 설치
                if not tile['open']:
                    pygame.draw.rect(screen, GRAY, pygame.Rect(column_index * CELL_SIZE, row_index * CELL_SIZE, CELL_SIZE, CELL_SIZE)) #커버
                if tile['flag']:
                    flag_image = pygame.image.load(r"images/flag.png").convert()
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
            for i in range(COLUMN_COUNT):
                column_index = i
                for j in range(ROW_COUNT):
                    row_index = j
                    tile = grid[row_index][column_index]
                    if tile['mine']:
                        mine_image = pygame.image.load(r"images\mine.png").convert()
                        mine_image = pygame.transform.scale(mine_image, (CELL_SIZE,CELL_SIZE))
                        screen.blit(mine_image, mine_image.get_rect(centerx=column_index * CELL_SIZE + CELL_SIZE // 2, centery=row_index * CELL_SIZE + CELL_SIZE // 2))
                    pygame.display.update()

            pygame.time.delay(5000)
            pygame.init()
            main_menu() 
        elif game_over == SUCCESS:
            global high_score
            end = time.time()
            current_time = end - start
            if float(high_score) > current_time:
                high_score = str(round(current_time,2))
                pygame.display.update()
            pygame.time.delay(2000)
            pygame.init()
            main_menu()
main_menu()