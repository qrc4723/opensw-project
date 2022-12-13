import pygame
from pygame.locals import *
import random
import math

# pygame 초기화
pygame.init()
# 화면
size = [1525, 800]
screen = pygame.display.set_mode(size)
FPS = 30
done = False
clock = pygame.time.Clock()
# 캐릭터 좌표
x = 400
y = 580
# 행동 상태
run, last = True, True
jump, slide, right, left, doing = False, False, False, False, False
# 목숨
life = 100
# 점수
score = 0
# 걸음수
walk_cnt = 0
# 최고 점수
best_score = 0

# 점프 리스트
Rjump_list = [pygame.image.load('Rmotion\Jump(1).png'), pygame.image.load('Rmotion\Jump(1).png'), pygame.image.load('Rmotion\Jump(2).png'), pygame.image.load('Rmotion\Jump(2).png'), pygame.image.load(
    'Rmotion\Jump(3).png'), pygame.image.load('Rmotion\Jump(3).png'), pygame.image.load('Rmotion\Jump(4).png'), pygame.image.load('Rmotion\Jump(4).png'), pygame.image.load('Rmotion\Jump(5).png'), pygame.image.load('Rmotion\Jump(5).png')]
Ljump_list = [pygame.image.load('Lmotion\Jump(1).png'), pygame.image.load('Lmotion\Jump(1).png'), pygame.image.load('Lmotion\Jump(2).png'), pygame.image.load('Lmotion\Jump(2).png'), pygame.image.load(
    'Lmotion\Jump(3).png'), pygame.image.load('Lmotion\Jump(3).png'), pygame.image.load('Lmotion\Jump(4).png'), pygame.image.load('Lmotion\Jump(4).png'), pygame.image.load('Lmotion\Jump(5).png'), pygame.image.load('Lmotion\Jump(5).png')]
# 슬라이딩 리스트
Rslide_list = [pygame.image.load('Rmotion\Slide(1).png'), pygame.image.load('Rmotion\Slide(1).png'), pygame.image.load('Rmotion\Slide(2).png'), pygame.image.load(
    'Rmotion\Slide(2).png'), pygame.image.load('Rmotion\Slide(3).png'), pygame.image.load('Rmotion\Slide(3).png'), pygame.image.load('Rmotion\Slide(4).png'), pygame.image.load('Rmotion\Slide(4).png')]
Lslide_list = [pygame.image.load('Lmotion\Slide(1).png'), pygame.image.load('Lmotion\Slide(1).png'), pygame.image.load('Lmotion\Slide(2).png'), pygame.image.load(
    'Lmotion\Slide(2).png'), pygame.image.load('Lmotion\Slide(3).png'), pygame.image.load('Lmotion\Slide(3).png'), pygame.image.load('Lmotion\Slide(4).png'), pygame.image.load('Lmotion\Slide(4).png')]
# 달리기 리스트
Rrun_list = [pygame.image.load('Rmotion\Run(1).png'), pygame.image.load('Rmotion\Run(2).png'), pygame.image.load('Rmotion\Run(3).png'), pygame.image.load('Rmotion\Run(4).png'), pygame.image.load('Rmotion\Run(5).png'),
             pygame.image.load('Rmotion\Run(6).png'), pygame.image.load('Rmotion\Run(7).png'), pygame.image.load('Rmotion\Run(8).png'), pygame.image.load('Rmotion\Run(9).png'), pygame.image.load('Rmotion\Run(10).png')]
Lrun_list = [pygame.image.load('Lmotion\Run(1).png'), pygame.image.load('Lmotion\Run(2).png'), pygame.image.load('Lmotion\Run(3).png'), pygame.image.load('Lmotion\Run(4).png'), pygame.image.load('Lmotion\Run(5).png'),
             pygame.image.load('Lmotion\Run(6).png'), pygame.image.load('Lmotion\Run(7).png'), pygame.image.load('Lmotion\Run(8).png'), pygame.image.load('Lmotion\Run(9).png'), pygame.image.load('Lmotion\Run(10).png')]

# 가만히 있는 모습
Ridle = [pygame.image.load('Rmotion\Idle(1).png'), pygame.image.load('Rmotion\Idle(2).png'), pygame.image.load('Rmotion\Idle(3).png'), pygame.image.load('Rmotion\Idle(4).png'), pygame.image.load(
    'Rmotion\Idle(5).png'), pygame.image.load('Rmotion\Idle(6).png'), pygame.image.load('Rmotion\Idle(7).png'), pygame.image.load('Rmotion\Idle(8).png'), pygame.image.load('Rmotion\Idle(9).png'), pygame.image.load('Rmotion\Idle(10).png')]
Lidle = [pygame.image.load('Lmotion\Idle(1).png'), pygame.image.load('Lmotion\Idle(2).png'), pygame.image.load('Lmotion\Idle(3).png'), pygame.image.load('Lmotion\Idle(4).png'), pygame.image.load(
    'Lmotion\Idle(5).png'), pygame.image.load('Lmotion\Idle(6).png'), pygame.image.load('Lmotion\Idle(7).png'), pygame.image.load('Lmotion\Idle(8).png'), pygame.image.load('Lmotion\Idle(9).png'), pygame.image.load('Lmotion\Idle(10).png')]
# 배경화면
BackGround = pygame.image.load('BackGournd.jpg')
# 장애물
RBlot = [pygame.image.load('huddle\motion\Bolt\Bolt1.png'), pygame.image.load('huddle\motion\Bolt\Bolt2.png'), pygame.image.load(
    'huddle\motion\Bolt\Bolt3.png'), pygame.image.load('huddle\motion\Bolt\Bolt4.png')]
LBlot = [pygame.image.load('huddle\motion\LBlot\Bolt1.png'), pygame.image.load('huddle\motion\LBlot\Bolt2.png'), pygame.image.load(
    'huddle\motion\LBlot\Bolt3.png'), pygame.image.load('huddle\motion\LBlot\Bolt4.png')]
# 폰트
font = pygame.font.SysFont("Score", 50, True, True)
# 게임오버
game_over = False
gameover = pygame.image.load('game_over.png')


class huddle:
    def __init__(self, way, xy, type):
        self.way = random.randint(0, 1)
        self.xy = [way * 1500, random.randint(650, 650)]
        self.type = 0
        self.speed = 5

    def check(self):
        if self.xy[0] > 1525 or self.xy[0] < 0 or self.xy[1] > 800 or self.xy[0] < 0:
            self.random_point()

    def random_point(self):
        self.type = random.randint(0, 1)
        self.way = random.randint(0, 1)
        self.xy = [self.way * 1500, random.randint(580, 700)]

    def move(self):
        if self.way == 0:
            self.xy[0] += self.speed
            self.check()
        else:
            self.xy[0] -= self.speed
            self.check()


def setting():
    global done, walk_cnt, jump, slide, run, x, y, right, left, last, doing, score, RBlot, life, game_over, a, b, c, d, e, f, g, h, i, j, huddles, using,best_score
    game_over = False
    life = 1000
    # 캐릭터 좌표
    x = 400
    y = 580
    # 행동 상태
    run, last = True, True
    jump, slide, right, left, doing = False, False, False, False, False
    # 목숨
    life = 100
    # 점수
    score = 0
    # 걸음수
    walk_cnt = 0
    # 게임오버
    game_over = False
    # 장애물
    a = huddle(0, [0, 0], 0)
    b = huddle(0, [0, 0], 0)
    c = huddle(0, [0, 0], 0)
    d = huddle(0, [0, 0], 0)
    e = huddle(0, [0, 0], 0)
    f = huddle(0, [0, 0], 0)
    g = huddle(0, [0, 0], 0)
    h = huddle(0, [0, 0], 0)
    i = huddle(0, [0, 0], 0)
    j = huddle(0, [0, 0], 0)

    huddles = [a, b, c, d, e, f, g, h, i, j]
    using = []


# 장애물들
a = huddle(0, [0, 0], 0)
b = huddle(0, [0, 0], 0)
c = huddle(0, [0, 0], 0)
d = huddle(0, [0, 0], 0)
e = huddle(0, [0, 0], 0)
f = huddle(0, [0, 0], 0)
g = huddle(0, [0, 0], 0)
h = huddle(0, [0, 0], 0)
i = huddle(0, [0, 0], 0)
j = huddle(0, [0, 0], 0)

huddles = [a, b, c, d, e, f, g, h, i, j]
using = []


def rungame():
    global done, walk_cnt, jump, slide, run, x, y, right, left, last, doing, score, RBlot, life, game_over, a, b, c, d, e, f, g, h, i, j, huddles, using, best_score

    while not done:
        clock.tick(FPS)
        screen.blit(BackGround, (0, 0))
        text = font.render("Score: " + str(score), True, (255, 255, 255))
        health_point = font.render("HP: " + str(life), True, (255, 255, 255))
        screen.blit(text, (10, 10))
        # screen.blit(health_point,(1350,10))
        screen.blit(health_point, (1350, 10))

        # 장애물
        if huddles != [] and score % 50 == 0:
            using.append(huddles.pop())

        for i in using:
            if i.way == 0:
                screen.blit(LBlot[score % 4], (i.xy[0], i.xy[1]))
                i.move()
            else:
                screen.blit(RBlot[score % 4], (i.xy[0], i.xy[1]))
                i.move()

        for z in using:
            h = z.xy
            distance = int(math.sqrt((h[0] - (x+75))**2 + (h[1] - (y+100))**2))
            if distance <= 30:
                life -= 10
            print([x, y], h)

        # 이벤트 잡아네기
        for event in pygame.event.get():
            # X를 눌러서 종료하기
            if event.type == pygame.QUIT:
                done = True
            if event.type == KEYDOWN:
                if event.key == pygame.K_UP and not doing:
                    jump = True
                    walk_cnt = 0
                    doing = True
                if event.key == pygame.K_SPACE and not doing:
                    jump = True
                    walk_cnt = 0
                    doing = True
                if event.key == pygame.K_DOWN and not doing:
                    slide = True
                    walk_cnt = 0
                    doing = True
                if event.key == pygame.K_RIGHT:
                    right = True
                    left = False
                if event.key == pygame.K_LEFT:
                    left = True
                    right = False
            if event.type == KEYUP:
                if event.key == pygame.K_RIGHT:
                    right = False
                    last = True
                if event.key == pygame.K_LEFT:
                    left = False
                    last = False

        if right:
            x += 10
        if left:
            x -= 10

        if not left and not right and not jump and not slide:
            if last:
                screen.blit(Ridle[walk_cnt % 10], (x, y))
            else:
                screen.blit(Lidle[walk_cnt % 10], (x, y))

        if not jump and not slide and (left or right):
            if right:
                screen.blit(Rrun_list[walk_cnt % 10], (x, y))
            else:
                screen.blit(Lrun_list[walk_cnt % 10], (x, y))

        if jump:
            if walk_cnt < 6:
                y -= 25
                if right:
                    x += 10
                    screen.blit(Rjump_list[walk_cnt], (x, y))
                elif left:
                    x -= 10
                    screen.blit(Ljump_list[walk_cnt], (x, y))
                else:
                    if last:
                        x += 10
                        screen.blit(Rjump_list[walk_cnt], (x, y))
                    else:
                        x -= 10
                        screen.blit(Ljump_list[walk_cnt], (x, y))

            elif walk_cnt < 8:
                y += 25
                if right:
                    x += 10
                    screen.blit(Rjump_list[walk_cnt], (x, y))
                elif left:
                    x -= 10
                    screen.blit(Ljump_list[walk_cnt], (x, y))
                else:
                    if last:
                        x += 10
                        screen.blit(Rjump_list[walk_cnt], (x, y))
                    else:
                        x -= 10
                        screen.blit(Ljump_list[walk_cnt], (x, y))

            elif walk_cnt < 10:
                y += 50
                if right:
                    x += 10
                    screen.blit(Rjump_list[walk_cnt], (x, y))
                elif left:
                    x -= 10
                    screen.blit(Ljump_list[walk_cnt], (x, y))
                else:
                    if last:
                        x += 10
                        screen.blit(Rjump_list[walk_cnt], (x, y))
                    else:
                        x -= 10
                        screen.blit(Ljump_list[walk_cnt], (x, y))

            else:
                jump = False
                walk_cnt = 0
                doing = False

        if slide:
            if walk_cnt < 8:
                if right:
                    x += 15
                    screen.blit(Rslide_list[walk_cnt], (x, y))
                elif left:
                    x -= 15
                    screen.blit(Lslide_list[walk_cnt], (x, y))
                else:
                    if last:
                        x += 15
                        screen.blit(Rslide_list[walk_cnt], (x, y))
                    else:
                        x -= 15
                        screen.blit(Lslide_list[walk_cnt], (x, y))
            else:
                slide = False
                walk_cnt = 0
                doing = False

        score += 1
        walk_cnt += 1
        if life <= 0:
            game_over = True
        pygame.display.update()

        if game_over:
            if score > best_score:
                best_score = score
            while game_over:
                screen.blit(BackGround, (0, 0))
                screen.blit(gameover, (550, 0))
                game_over_msg = font.render(
                    "PRESS 'SPACE' to continue.", True, (255, 255, 255))
                best_score_msg = font.render(
                    "BEST SCORE : " + str(best_score), True, (255, 255, 255))
                screen.blit(game_over_msg, (480, 400))
                screen.blit(best_score_msg, (550, 500))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            setting()
        

rungame()
pygame.quit()
