import pygame
import sys
import random


pygame.init()
pygame.display.set_caption('game')



def main():
    # set screen, fps
    screen = pygame.display.set_mode((900, 600))
    fps = pygame.time.Clock()
    background = pygame.image.load('background.jpg')
    background = pygame.transform.scale(background, (900, 600))


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
    
    circle_x_L = False
    circle_x_R = False

    # mini
    mini_image = pygame.image.load('mini.png')
    mini_image = pygame.transform.scale(mini_image, (30,30))
    mini_x = 870
    mini_y = random.uniform(75, 475)

    # mini2
    mini_image2 = pygame.image.load('mini.png')
    mini_image2 = pygame.transform.scale(mini_image, (30,30))
    mini_x2 = 870 - 150
    mini_y2 = random.uniform(75, 475)

    # mini3
    mini_image3 = pygame.image.load('mini.png')
    mini_image3 = pygame.transform.scale(mini_image, (30,30))
    mini_x3 = 870 - 300
    mini_y3 = random.uniform(75, 475)

    # mini4
    mini_image4 = pygame.image.load('mini.png')
    mini_image4 = pygame.transform.scale(mini_image, (30,30))
    mini_x4 = 870 - 450
    mini_y4 = random.uniform(75, 475)

    # mini5
    mini_image5 = pygame.image.load('mini.png')
    mini_image5 = pygame.transform.scale(mini_image, (30,30))
    mini_x5 = 0
    mini_y5 = random.uniform(75, 475)

    # mini6
    mini_image6 = pygame.image.load('mini.png')
    mini_image6 = pygame.transform.scale(mini_image, (30,30))
    mini_x6 = 150
    mini_y6 = random.uniform(75, 475)

    # mini7
    mini_image7 = pygame.image.load('mini.png')
    mini_image7 = pygame.transform.scale(mini_image, (30,30))
    mini_x7 = 300
    mini_y7 = random.uniform(75, 475)

    # mini8
    mini_image8 = pygame.image.load('mini.png')
    mini_image8 = pygame.transform.scale(mini_image, (30,30))
    mini_x8 = 450
    mini_y8 = random.uniform(75, 475)




    while running:
        screen.fill((255, 255, 255))
        
        screen.blit(background, (0, 0))
        for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
            if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
                running = False

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
        mini_x -= 10.0
        if mini_x <= 0:
            mini_x = 870
            mini_y = random.randint(75, 475)

        # minie move2
        mini_x2 -= 10.0
        if mini_x2 <= 0:
            mini_x2 = 870
            mini_y2 = random.randint(75, 475)

        # minie move3
        mini_x3 -= 10.0
        if mini_x3 <= 0:
            mini_x3 = 870
            mini_y3 = random.randint(75, 475)

        # minie move4
        mini_x4 -= 10.0
        if mini_x4 <= 0:
            mini_x4 = 870
            mini_y4 = random.randint(75, 475)

        # minie move5
        mini_x5 += 10.0
        if mini_x5 >= 900:
            mini_x5 = 0
            mini_y5 = random.randint(75, 475)

        # minie move6
        mini_x6 += 10.0
        if mini_x6 >= 900:
            mini_x6 = 0
            mini_y6 = random.randint(75, 475)

        # minie move7
        mini_x7 += 10.0
        if mini_x7 >= 900:
            mini_x7 = 0
            mini_y7 = random.randint(75, 475)

        # minie move8
        mini_x8 += 10.0
        if mini_x8 >= 900:
            mini_x8 = 0
            mini_y8 = random.randint(75, 475)


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





        # update
        pygame.display.update()
        fps.tick(30)


if __name__ == '__main__':
    main()