import pygame
import math
import random


pygame.init()
pygame.display.set_caption('game')



def main():
    # set screen, fps
    screen = pygame.display.set_mode((900, 600))
    fps = pygame.time.Clock()
    background = pygame.image.load('background.jpg')
    background = pygame.transform.scale(background, (900, 600))


    #game over
    game = pygame.image.load('gameover.png')
    game = pygame.transform.scale(game, (900, 600))




    # circle, edge
    circle_image = pygame.image.load('circle.png')
    circle_image = pygame.transform.scale(circle_image, (40,40))
    edge_image = pygame.image.load('edge.png')
    edge_image = pygame.transform.scale(edge_image, (750,500))

    circle_x = 425
    circle_y = 320


    edge_x = 80
    edge_y = 45
    
    up = False
    down = True
    running = True
    game_over = False
    space = True
    
    circle_x_L = False
    circle_x_R = False

    end = True

    # mini
    mini_image = pygame.image.load('mini.png')
    mini_image = pygame.transform.scale(mini_image, (30,30))
    mini_x = 870
    mini_y = 30
    


    # mini2
    mini_image2 = pygame.image.load('mini.png')
    mini_image2 = pygame.transform.scale(mini_image, (30,30))
    mini_x2 = 870 - 150
    mini_y2 = 30
    


    # mini3
    mini_image3 = pygame.image.load('mini.png')
    mini_image3 = pygame.transform.scale(mini_image, (30,30))
    mini_x3 = 870 - 300
    mini_y3 = 30



    # mini4
    mini_image4 = pygame.image.load('mini.png')
    mini_image4 = pygame.transform.scale(mini_image, (30,30))
    mini_x4 = 870 - 450
    mini_y4 = 30



    # mini5
    mini_image5 = pygame.image.load('mini.png')
    mini_image5 = pygame.transform.scale(mini_image, (30,30))
    mini_x5 = 0
    mini_y5 = 540



    # mini6
    mini_image6 = pygame.image.load('mini.png')
    mini_image6 = pygame.transform.scale(mini_image, (30,30))
    mini_x6 = 150
    mini_y6 = 540



    # mini7
    mini_image7 = pygame.image.load('mini.png')
    mini_image7 = pygame.transform.scale(mini_image, (30,30))
    mini_x7 = 300 
    mini_y7 = 540



    # mini8
    mini_image8 = pygame.image.load('mini.png')
    mini_image8 = pygame.transform.scale(mini_image, (30,30))
    mini_x8 = 450
    mini_y8 = 540


# Font 정의
    game_font = pygame.font.Font(None, 40)
    start_ticks = pygame.time.get_ticks() # 시작 시간 정의




    while end:
        
        circle_x = 425
        circle_y = 320

        mini_x = 870
        mini_y = 30

        mini_x2 = 870 - 150
        mini_y2 = 30

        mini_x3 = 870 - 300
        mini_y3 = 30

        mini_x4 = 870 - 450
        mini_y4 = 30

        mini_x5 = 0
        mini_y5 = 540

        mini_x6 = 150
        mini_y6 = 540

        mini_x7 = 300 
        mini_y7 = 540

        mini_x8 = 450
        mini_y8 = 540

        up = False
        down = True
        running = True
        game_over = False
        space = True
        
        circle_x_L = False
        circle_x_R = False

        start_ticks = pygame.time.get_ticks() # 시작 시간 정의


        while running:
            screen.fill((255, 255, 255))
            
            screen.blit(background, (0, 0))
            for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
                if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
                    end = False

                if event.type == pygame.KEYDOWN: #키보드의 키가 눌러졌을 경우
                    if event.key == pygame.K_LEFT: #왼쪽 방향키가 눌렸을 때
                        circle_x_L = True
                    elif event.key == pygame.K_RIGHT: #오른쪽 방향키가 눌렸을 때
                        circle_x_R = True
                        
                        
                if event.type == pygame.KEYUP: #키보드의 키가 눌러졌을 경우
                    if event.key == pygame.K_LEFT: #왼쪽 방향키가 눌렸을 때
                        circle_x_L = False
                    elif event.key == pygame.K_RIGHT: #오른쪽 방향키가 눌렸을 때
                        circle_x_R = False
                        
                        
            # circle move
            if up:
                circle_y -= 8.0
            elif not up and down:
                circle_y += 8.0


            if circle_y <= 80:
                up = False
                down = True

            if circle_y >= 470:
                up = True
                down = False


            if circle_x_L:
                circle_x -= 8
                
            if circle_x_R:
                circle_x += 8


            if circle_x <= 120:
                circle_x = 120
                
            if circle_x >= 755:
                circle_x = 755



            # minie move
            if (pygame.time.get_ticks() - start_ticks) / 1000  <= 10.0:
                mini_x -= 5.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 10.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 20.0:
                mini_x -= 6.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 20.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 30.0:
                mini_x -= 7.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 30.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 40.0:
                mini_x -= 8.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 40.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 50.0:
                mini_x -= 9.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 50.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 60.0:
                mini_x -= 10.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 60.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 70.0:
                mini_x -= 11.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 70.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 80.0:
                mini_x -= 12.0
            else:
                mini_x -= 13.0

            if mini_x <= 0:
                mini_x = 870
                mini_y = random.randint(80, 470)

            # minie move2
            if (pygame.time.get_ticks() - start_ticks) / 1000  <= 10.0:
                mini_x2 -= 5.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 10.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 20.0:
                mini_x2 -= 6.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 20.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 30.0:
                mini_x2 -= 7.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 30.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 40.0:
                mini_x2 -= 8.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 40.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 50.0:
                mini_x2 -= 9.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 50.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 60.0:
                mini_x2 -= 10.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 60.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 70.0:
                mini_x2 -= 11.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 70.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 80.0:
                mini_x2 -= 12.0
            else:
                mini_x -= 13.0

            if mini_x2 <= 0:
                mini_x2 = 870
                mini_y2 = random.randint(80, 470)

            # minie move3
            if (pygame.time.get_ticks() - start_ticks) / 1000  <= 10.0:
                mini_x3 -= 5.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 10.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 20.0:
                mini_x3 -= 6.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 20.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 30.0:
                mini_x3 -= 7.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 30.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 40.0:
                mini_x3 -= 8.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 40.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 50.0:
                mini_x3 -= 9.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 50.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 60.0:
                mini_x3 -= 10.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 60.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 70.0:
                mini_x3 -= 11.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 70.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 80.0:
                mini_x3 -= 12.0
            else:
                mini_x3 -= 13.0

            if mini_x3 <= 0:
                mini_x3 = 870
                mini_y3 = random.randint(80, 470)

            # minie move4
            if (pygame.time.get_ticks() - start_ticks) / 1000  <= 10.0:
                mini_x4 -= 5.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 10.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 20.0:
                mini_x4 -= 6.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 20.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 30.0:
                mini_x4 -= 7.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 30.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 40.0:
                mini_x4 -= 8.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 40.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 50.0:
                mini_x4 -= 9.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 50.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 60.0:
                mini_x4 -= 10.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 60.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 70.0:
                mini_x4 -= 11.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 70.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 80.0:
                mini_x4 -= 12.0
            else:
                mini_x4 -= 13.0

            if mini_x4 <= 0:
                mini_x4 = 870
                mini_y4 = random.randint(80, 470)

            # minie move5
            if (pygame.time.get_ticks() - start_ticks) / 1000  <= 10.0:
                mini_x5 += 5.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 10.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 20.0:
                mini_x5 += 6.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 20.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 30.0:
                mini_x5 += 7.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 30.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 40.0:
                mini_x5 += 8.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 40.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 50.0:
                mini_x5 += 9.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 50.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 60.0:
                mini_x5 += 10.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 60.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 70.0:
                mini_x5 += 11.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 70.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 80.0:
                mini_x5 += 12.0
            else:
                mini_x5 += 13.0

            if mini_x5 >= 900:
                mini_x5 = 0
                mini_y5 = random.randint(80, 470)

            # minie move6
            if (pygame.time.get_ticks() - start_ticks) / 1000  <= 10.0:
                mini_x6 += 5.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 10.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 20.0:
                mini_x6 += 6.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 20.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 30.0:
                mini_x6 += 7.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 30.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 40.0:
                mini_x6 += 8.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 40.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 50.0:
                mini_x6 += 9.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 50.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 60.0:
                mini_x6 += 10.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 60.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 70.0:
                mini_x6 += 11.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 70.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 80.0:
                mini_x6 += 12.0
            else:
                mini_x6 += 13.0

            if mini_x6 >= 900:
                mini_x6 = 0
                mini_y6 = random.randint(80, 470)

            # minie move7
            if (pygame.time.get_ticks() - start_ticks) / 1000  <= 10.0:
                mini_x7 += 5.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 10.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 20.0:
                mini_x7 += 6.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 20.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 30.0:
                mini_x7 += 7.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 30.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 40.0:
                mini_x7 += 8.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 40.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 50.0:
                mini_x7 += 9.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 50.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 60.0:
                mini_x7 += 10.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 60.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 70.0:
                mini_x7 += 11.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 70.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 80.0:
                mini_x7 += 12.0
            else:
                mini_x7 += 13.0

            if mini_x7 >= 900:
                mini_x7 = 0
                mini_y7 = random.randint(80, 470)

            # minie move8
            if (pygame.time.get_ticks() - start_ticks) / 1000  <= 10.0:
                mini_x8 += 5.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 10.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 20.0:
                mini_x8 += 6.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 20.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 30.0:
                mini_x8 += 7.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 30.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 40.0:
                mini_x8 += 8.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 40.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 50.0:
                mini_x8 += 9.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 50.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 60.0:
                mini_x8 += 10.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 60.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 70.0:
                mini_x8 += 11.0
            elif (pygame.time.get_ticks() - start_ticks) / 1000  > 70.0 and (pygame.time.get_ticks() - start_ticks) / 1000  <= 80.0:
                mini_x8 += 12.0
            else:
                mini_x8 += 13.0

            if mini_x8 >= 900:
                mini_x8 = 0
                mini_y8 = random.randint(80, 470)


            # draw mini
            screen.blit(mini_image, (mini_x, mini_y))

            # draw mini2
            screen.blit(mini_image2, (mini_x2, mini_y2))

            # draw mini3
            screen.blit(mini_image3, (mini_x3, mini_y3))

            # draw mini4
            screen.blit(mini_image4, (mini_x4, mini_y4))

            # draw mini5
            screen.blit(mini_image5, (mini_x5, mini_y5))

            # draw mini6
            screen.blit(mini_image6, (mini_x6, mini_y6))

            # draw mini7
            screen.blit(mini_image7, (mini_x7, mini_y7))

            # draw mini8
            screen.blit(mini_image8, (mini_x8, mini_y8))



            # draw circle, edge
            screen.blit(circle_image, (circle_x, circle_y))
            screen.blit(edge_image, (edge_x, edge_y))


            # 충돌
            if math.sqrt((circle_x-mini_x+5)*(circle_x-mini_x+5) + (circle_y-mini_y+5)*(circle_y-mini_y+5)) <= 35:
                running = False
                game_over = True
                up = False
                down = False

            if math.sqrt((circle_x-mini_x2+5)*(circle_x-mini_x2+5) + (circle_y-mini_y2+5)*(circle_y-mini_y2+5)) <= 35:
                running = False
                game_over = True
                up = False
                down = False

            if math.sqrt((circle_x-mini_x3+5)*(circle_x-mini_x3+5) + (circle_y-mini_y3+5)*(circle_y-mini_y3+5)) <= 35:
                running = False
                game_over = True
                up = False
                down = False

            if math.sqrt((circle_x-mini_x4+5)*(circle_x-mini_x4+5) + (circle_y-mini_y4+5)*(circle_y-mini_y4+5)) <= 35:
                running = False
                game_over = True
                up = False
                down = False

            if math.sqrt((circle_x-mini_x5+5)*(circle_x-mini_x5+5) + (circle_y-mini_y5+5)*(circle_y-mini_y5+5)) <= 35:
                running = False
                game_over = True
                up = False
                down = False

            if math.sqrt((circle_x-mini_x6+5)*(circle_x-mini_x6+5) + (circle_y-mini_y6+5)*(circle_y-mini_y6+5)) <= 35:
                running = False
                game_over = True
                up = False
                down = False

            if math.sqrt((circle_x-mini_x7+5)*(circle_x-mini_x7+5) + (circle_y-mini_y7+5)*(circle_y-mini_y7+5)) <= 35:
                running = False
                game_over = True
                up = False
                down = False

            if math.sqrt((circle_x-mini_x8+5)*(circle_x-mini_x8+5) + (circle_y-mini_y8+5)*(circle_y-mini_y8+5)) <= 35:
                running = False
                game_over = True
                up = False
                down = False



            # 타이머 집어 넣기
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간(ms)을 1000으로 나눠 초 단위로 표시

            timer = game_font.render(str(elapsed_time), True, (255,255,255)) # 출력할 글자, True, 글자 색상
            screen.blit(timer, (10,10)) # 화면에 타이머가 그려지는 위치


            # update
            pygame.display.update()
            fps.tick(30)



        if game_over:
            while space:
                screen.blit(game, (0, 0))
                pygame.display.update()

                for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
                    if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
                        space = False
                        end = False
                    if event.type == pygame.KEYDOWN: #키보드의 키가 눌러졌을 경우
                        if event.key == pygame.K_SPACE: #스페이스가 눌렸을 때
                            
                            space = False 
                            running = True

if __name__ == '__main__':
    main()
