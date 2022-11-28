import sys
import pygame
from pygame.locals import *
#pygame 초기화 
pygame.init()
#화면
RGB = (153,255,153)
size = [1525,800]
screen = pygame.display.set_mode(size)
FPS = 30
done = False
clock = pygame.time.Clock()
#캐릭터 좌표
x = 10
y = 580
#행동 상태
jump = False
slide = False
run = True
right = False
left = False
last = True # True 면 오른쪽
doing = False
#목숨
life = 100
#점수
score = 0
#걸음수
walk_cnt = 0
#점프 리스트
Rjump_list = [pygame.image.load('Rmotion\Jump(1).png'),pygame.image.load('Rmotion\Jump(1).png'),pygame.image.load('Rmotion\Jump(2).png'),pygame.image.load('Rmotion\Jump(2).png'),pygame.image.load('Rmotion\Jump(3).png'),pygame.image.load('Rmotion\Jump(3).png'),pygame.image.load('Rmotion\Jump(4).png'),pygame.image.load('Rmotion\Jump(4).png'),pygame.image.load('Rmotion\Jump(5).png'),pygame.image.load('Rmotion\Jump(5).png')]
Ljump_list = [pygame.image.load('Lmotion\Jump(1).png'),pygame.image.load('Lmotion\Jump(1).png'),pygame.image.load('Lmotion\Jump(2).png'),pygame.image.load('Lmotion\Jump(2).png'),pygame.image.load('Lmotion\Jump(3).png'),pygame.image.load('Lmotion\Jump(3).png'),pygame.image.load('Lmotion\Jump(4).png'),pygame.image.load('Lmotion\Jump(4).png'),pygame.image.load('Lmotion\Jump(5).png'),pygame.image.load('Lmotion\Jump(5).png')]
#슬라이딩 리스트
Rslide_list = [pygame.image.load('Rmotion\Slide(1).png'),pygame.image.load('Rmotion\Slide(1).png'),pygame.image.load('Rmotion\Slide(2).png'),pygame.image.load('Rmotion\Slide(2).png'),pygame.image.load('Rmotion\Slide(3).png'),pygame.image.load('Rmotion\Slide(3).png'),pygame.image.load('Rmotion\Slide(4).png'),pygame.image.load('Rmotion\Slide(4).png')]
Lslide_list = [pygame.image.load('Lmotion\Slide(1).png'),pygame.image.load('Lmotion\Slide(1).png'),pygame.image.load('Lmotion\Slide(2).png'),pygame.image.load('Lmotion\Slide(2).png'),pygame.image.load('Lmotion\Slide(3).png'),pygame.image.load('Lmotion\Slide(3).png'),pygame.image.load('Lmotion\Slide(4).png'),pygame.image.load('Lmotion\Slide(4).png')]
#달리기 리스트
Rrun_list = [pygame.image.load('Rmotion\Run(1).png'),pygame.image.load('Rmotion\Run(2).png'),pygame.image.load('Rmotion\Run(3).png'),pygame.image.load('Rmotion\Run(4).png'),pygame.image.load('Rmotion\Run(5).png'),
pygame.image.load('Rmotion\Run(6).png'),pygame.image.load('Rmotion\Run(7).png'),pygame.image.load('Rmotion\Run(8).png'),pygame.image.load('Rmotion\Run(9).png'),pygame.image.load('Rmotion\Run(10).png')]
Lrun_list = [pygame.image.load('Lmotion\Run(1).png'),pygame.image.load('Lmotion\Run(2).png'),pygame.image.load('Lmotion\Run(3).png'),pygame.image.load('Lmotion\Run(4).png'),pygame.image.load('Lmotion\Run(5).png'),
pygame.image.load('Lmotion\Run(6).png'),pygame.image.load('Lmotion\Run(7).png'),pygame.image.load('Lmotion\Run(8).png'),pygame.image.load('Lmotion\Run(9).png'),pygame.image.load('Lmotion\Run(10).png')]

#가만히 있는 모습
Ridle = [pygame.image.load('Rmotion\Idle(1).png'),pygame.image.load('Rmotion\Idle(2).png'),pygame.image.load('Rmotion\Idle(3).png'),pygame.image.load('Rmotion\Idle(4).png')
,pygame.image.load('Rmotion\Idle(5).png'),pygame.image.load('Rmotion\Idle(6).png'),pygame.image.load('Rmotion\Idle(7).png'),pygame.image.load('Rmotion\Idle(8).png'),pygame.image.load('Rmotion\Idle(9).png'),pygame.image.load('Rmotion\Idle(10).png')]
Lidle = [pygame.image.load('Lmotion\Idle(1).png'),pygame.image.load('Lmotion\Idle(2).png'),pygame.image.load('Lmotion\Idle(3).png'),pygame.image.load('Lmotion\Idle(4).png')
,pygame.image.load('Lmotion\Idle(5).png'),pygame.image.load('Lmotion\Idle(6).png'),pygame.image.load('Lmotion\Idle(7).png'),pygame.image.load('Lmotion\Idle(8).png'),pygame.image.load('Lmotion\Idle(9).png'),pygame.image.load('Lmotion\Idle(10).png')]
#배경화면
BackGround = pygame.image.load('BackGournd.jpg')

font = pygame.font.SysFont("Score",50,True, True)



def rungame():
    global done, walk_cnt, jump, slide, run, x, y,right, left, last, doing, score
    while not done:
        clock.tick(FPS)
        screen.blit(BackGround,(0,0))
        text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(text,(10,10))
        #이벤트 잡아네기
        for event in pygame.event.get():
            # X를 눌러서 종료하기
            if event.type == pygame.QUIT:
                done=True
            if event.type == KEYDOWN:
                if event.key == pygame.K_UP and not doing:
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
            x += 20
        if left:
            x -= 20
            
        if not left and not right and not jump and not slide:
            if last:
                screen.blit(Ridle[walk_cnt % 10],(x,y))
            else:
                screen.blit(Lidle[walk_cnt % 10],(x,y))

        if not jump and not slide and (left or right):
            if right : 
                screen.blit(Rrun_list[walk_cnt % 10],(x,y))
            else:
                screen.blit(Lrun_list[walk_cnt % 10],(x,y))


        if jump:
            if walk_cnt < 6:
                y -= 25
                if right:
                    screen.blit(Rjump_list[walk_cnt],(x,y))
                elif left:
                    screen.blit(Ljump_list[walk_cnt],(x,y))
                else:
                    if last:
                        screen.blit(Rjump_list[walk_cnt],(x,y))
                    else:
                        screen.blit(Ljump_list[walk_cnt],(x,y))

            elif walk_cnt < 8:
                y += 25
                if right:
                    screen.blit(Rjump_list[walk_cnt],(x,y))
                elif left:
                    screen.blit(Ljump_list[walk_cnt],(x,y))
                else:
                    if last:
                        screen.blit(Rjump_list[walk_cnt],(x,y))
                    else:
                        screen.blit(Ljump_list[walk_cnt],(x,y))

            elif walk_cnt < 10:
                y += 50
                if right:
                    screen.blit(Rjump_list[walk_cnt],(x,y))
                elif left:
                    screen.blit(Ljump_list[walk_cnt],(x,y))
                else:
                    if last:
                        screen.blit(Rjump_list[walk_cnt],(x,y))
                    else:
                        screen.blit(Ljump_list[walk_cnt],(x,y))

            else:
                jump = False
                walk_cnt = 0
                doing = False

        if slide:
            if walk_cnt < 8:
                if right:
                    screen.blit(Rslide_list[walk_cnt],(x,y))
                elif left:
                    screen.blit(Lslide_list[walk_cnt],(x,y))
                else:
                    if last:
                        screen.blit(Rslide_list[walk_cnt],(x,y))
                    else:
                        screen.blit(Lslide_list[walk_cnt],(x,y))
            else:
                slide = False
                walk_cnt = 0
                doing = False
        
        score += 1
        walk_cnt += 1
        pygame.display.update()

rungame()
pygame.quit()

