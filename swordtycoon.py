import pygame 
import random
from random import choice
import time
pygame.init() 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

background = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\background.jpg")
background1 = pygame.image.load(r"C:\Users\user\Desktop\opensw\image\background1.png")

Lv1sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv1sword.png")
Lv2sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv2sword.png")
Lv3sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv3sword.png")
Lv4sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv4sword.png")
Lv5sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv5sword.png")
Lv6sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv6sword.png")
Lv7sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv7sword.png")
Lv8sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv8sword.png")
Lv9sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv9sword.png")
Lv10sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv10sword.png")
Lv11sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv11sword.png")
Lv12sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv12sword.png")
Lv13sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv13sword.png")
Lv14sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv14sword.png")
Lv15sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv15sword.png")
Lv16sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv16sword.png")
Lv17sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv17sword.png")
Lv18sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv18sword.png")
Lv19sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv19sword.png")
Lv20sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv20sword.png")
Lv21sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv21sword.png")
Lv22sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv22sword.png")
Lv23sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv23sword.png")
Lv24sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv24sword.png")
Lv25sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv25sword.png")
Lv26sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv26sword.png")
Lv27sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv27sword.png")
Lv28sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv28sword.png")
Lv29sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv29sword.png")
Lv30sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv30sword.png")
Lv31sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv31sword.png")
Lv32sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv32sword.png")
Lv33sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv33sword.png")
Lv34sword = pygame.image.load(r"C:\Users\User\Desktop\opensw\image\Lv34sword.png")

Lv1monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv1monster.png")
Lv2monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv2monster.png")
Lv3monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv3monster.png")
Lv4monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv4monster.png")
Lv5monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv5monster.png")
Lv6monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv6monster.png")
Lv7monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv7monster.png")
Lv8monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv8monster.png")
Lv9monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv9monster.png")
Lv10monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv10monster.png")
Lv11monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv11monster.png")
Lv12monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv12monster.png")
Lv13monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv13monster.png")
Lv14monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv14monster.png")
Lv15monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv15monster.png")
Lv16monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv16monster.png")
Lv17monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv17monster.png")
Lv18monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv18monster.png")
Lv19monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv19monster.png")
Lv20monster = pygame.image.load(r"C:\Users\User\Desktop\opensw\monster\Lv20monster.png")

health = 10

monster_counter = 0

count = 0

my_hp = 100

monster_hp = 100

my_attack = 10 

monster_attack = 10

attack_type = ''

win_count = False

health_count = 1

sword_list = [Lv1sword, Lv2sword, Lv3sword, Lv4sword, Lv5sword, 
              Lv6sword, Lv7sword, Lv8sword, Lv9sword, Lv10sword,
              Lv11sword, Lv12sword, Lv13sword, Lv14sword, Lv15sword, 
              Lv16sword, Lv17sword, Lv18sword, Lv19sword, Lv20sword,
              Lv21sword, Lv22sword, Lv23sword, Lv24sword, Lv25sword,
              Lv26sword, Lv27sword, Lv28sword, Lv29sword, Lv30sword, 
              Lv31sword, Lv32sword, Lv33sword, Lv34sword]

monster_list = [Lv1monster, Lv2monster, Lv3monster, Lv4monster, Lv5monster, Lv6monster, Lv7monster, Lv8monster, Lv9monster, Lv10monster, 
                Lv11monster, Lv12monster,Lv13monster, Lv14monster, Lv15monster, Lv16monster, Lv17monster, Lv18monster, Lv19monster, Lv20monster]

pro_list = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2 ]

large_font = pygame.font.SysFont('malgungothic', 72)
small_font = pygame.font.SysFont('malgungothic', 20)

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
money =  10

breaksys = False

class Object:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power
        
    def attack(self, target):
        target.hp = target.hp - self.power
        print(f"{self.name}이 공격했습니다!")
            
class Player(Object):
    def magic(self, target):
        target.hp = target.hp - 50 * self.power
        
class Monster(Object):
    def heal(self):
        self.hp = self.hp + 5
        print(f"{self.name}이 힐했습니다!")
    def stand(self):
        print(f"{self.name}이 대기했습니다!")
        

monster = Monster(f"{monster_list[monster_counter]}", monster_hp, monster_attack)
monsters = [monster]
magic_count = 2
player = Player("player", my_hp, my_attack)
players = [player]


def draw_money():
    score_text = small_font.render('골드 {}'.format(money), True, WHITE)
    health_text = small_font.render('최대 체력 {}'.format(my_hp), True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(health_text, (10, 40 ))

def draw_health():
    score_text = small_font.render('골드 {}'.format(money), True, WHITE)
    my_hp_text = small_font.render('내 hp {}'.format(player.hp), True, BLACK)
    monster_hp_text = small_font.render('몬스터 hp {}'.format(monster.hp), True, BLACK)
    magic_count_text = small_font.render('스킬 횟수 {}'.format(magic_count), True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(my_hp_text, (10, 40))
    screen.blit(monster_hp_text, (10, 70))
    screen.blit(magic_count_text, (10, 100))

def draw_win():
    win_text = large_font.render('승리', True, BLACK)
    screen.blit(win_text, (screen_width/2 - 50, screen_height/2 - 50))    
    
def pro(n):
    a = random.randint(1,100)
    if a <= n:
        return True
    else:
        return False

class InhenceBtn:
    def __init__(self, text, width, height, pos):
        self.pressed = False
        # 버튼의 top 
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'
        # 버튼의 text
        self.text_surf = small_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 10)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()
        
    def check_click(self):
        global money
        global count, player, players
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):   
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    if count < 33 and money > 0:
                        if pro(pro_list[count]) == True:
                            sword_list[count].set_alpha(0)
                            sword_list[count+1].set_alpha(255)
                            money = money - 10
                            count = count + 1
                            my_attack = 10 + 5 * (count + 1)
                            del players[players.index(player)]
                            player = Player("player", my_hp, my_attack)
                            players = [player]
                            print(my_attack)
                            print('click')
                            self.pressed = False
                        else:
                            sword_list[count].set_alpha(0)
                            sword_list[0].set_alpha(255)
                            count = 0
                            my_attack = 10 + 5 * (count + 1)
                            del players[players.index(player)]
                            player = Player("player", my_hp, my_attack)
                            players = [player]
                            self.pressed = False
                    else:
                        self.pressed = False
                        
class BattleBtn:
    def __init__(self, text, width, height, pos):
        self.pressed = False
        # 버튼의 top 
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'
        # 버튼의 text
        self.text_surf = small_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 10)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):   
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    print('click')
                    runGame1()
                    monster_list[monster_counter].set_alpha(255)
                    monster_list[monster_counter-1].set_alpha(0)
                    self.pressed = False
                    
class SellBtn:
    def __init__(self, text, width, height, pos):
        self.pressed = False
        # 버튼의 top 
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'
        # 버튼의 text
        self.text_surf = small_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 10)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()
        
    def check_click(self):
        global money
        global count, players, player
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    sword_list[count].set_alpha(0)
                    sword_list[0].set_alpha(255)
                    money = money + (count * 10)
                    count = 0
                    my_attack = 10 + 5* (count + 1)
                    del players[players.index(player)]
                    player = Player("player", my_hp, my_attack)
                    players = [player]
                    print('click')
                    self.pressed = False
                    
class InhenceHealthBtn:
    def __init__(self, text, width, height, pos):
        self.pressed = False
        # 버튼의 top 
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'
        # 버튼의 text
        self.text_surf = small_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 10)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()
        
    def check_click(self):
        global money
        global health_count, my_hp, health
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):   
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    my_hp = my_hp + health
                    money -= 5 * health_count
                    health_count += 1
                    self.pressed = False
                                     
class homeBtn:
    def __init__(self, text, width, height, pos):
        self.pressed = False
        # 버튼의 top 
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'
        # 버튼의 text
        self.text_surf = small_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 10)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()
        
    def check_click(self):
        global breaksys
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    print('click')
                    breaksys = True
                    player.hp = my_hp
                    monster.hp = monster_hp
                    self.pressed = False

class Battle:
    def __init__(self, text, width, height, pos):
        self.pressed = False
        # 버튼의 top 
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'
        # 버튼의 text
        self.text_surf = small_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 10)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()
        
    def check_click(self):
        global my_hp, monster_attack, monster_hp, my_attack
        global magic_count
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    attack_type = 10
                    m = monsters[0]
                    if m in monsters:
                        if attack_type >= 0:
                            player.attack(m)
                            print("공격")
                        elif magic_count > 0 and attack_type < 0:            
                            player.magic(m)
                            magic_count -= 1
                            print("마법")
                        elif magic_count <= 0 and attack_type < 0:
                            while "마법공격":
                                print("더이상 마법공격을 할 수 없습니다.")
                                    
                    for m in monsters:
                        choice = random.randrange(0,3)
                        if choice == 0:
                            m.attack(player)
                        elif choice == 1:
                            m.heal()               
                        else:
                            m.stand()

                    self.pressed = False

class MagicBattle:
    def __init__(self, text, width, height, pos):
        self.pressed = False
        # 버튼의 top 
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'
        # 버튼의 text
        self.text_surf = small_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 10)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()
        
    def check_click(self):
        global my_hp, monster_attack, monster_hp, my_attack
        global magic_count
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    attack_type = -10
                    m = monsters[0]
                    if m in monsters:
                        if attack_type >= 0:
                            player.attack(m)
                            print("공격")
                        elif magic_count > 0 and attack_type < 0:            
                            player.magic(m)
                            magic_count -= 1
                            print("마법")
                        elif magic_count <= 0 and attack_type < 0:
                            while "마법공격":
                                print("더이상 마법공격을 할 수 없습니다.")
                                    
                    for m in monsters:
                        choice = random.randrange(0,3)
                        if choice == 0:
                            m.attack(player)
                        elif choice == 1:
                            m.heal()               
                        else:
                            m.stand()
    
                    self.pressed = False
    
def runGame():
    button1 = InhenceBtn('강화하기', 200, 40, (1050, 50))
    button2 = BattleBtn('전투하기', 200, 40, (1050, 110))
    button3 = SellBtn('판매하기', 200, 40, (1050, 170))
    button4 = InhenceHealthBtn('최대체력증가', 200, 40, (1050, 230))
    for j in range(1, 34):
        sword_list[j].set_alpha(0)
    while True:
        screen.fill((0, 0, 255))
        screen.blit(background, (0, 0))
        for i in range(34):
            screen.blit(sword_list[i], (screen_width/2 -100, screen_height/2 - 100))
        event = pygame.event.poll() #이벤트 처리
        if event.type == pygame.QUIT:
            exit()
        draw_money()
        button1.draw()
        button2.draw()
        button3.draw()
        button4.draw()
        pygame.display.update() #모든 화면 그리기 업데이트
        clock.tick(60)
        
def runGame1():
    global breaksys, win_count, monster_counter, monster, monsters, money
    
    button1 = homeBtn('나가기', 200, 40, (1050, 50))
    button2 = Battle('공격하기', 200, 40, (1050, 110))
    button3 = MagicBattle('스킬쓰기', 200, 40, (1050, 170))
    
    for i in range(monster_counter + 1, 20):
        monster_list[i].set_alpha(0)
           
    while True:
        screen.fill((0, 0, 255))
        screen.blit(background1, (0, 0))     
        event = pygame.event.poll() #이벤트 처리
        for i in range(monster_counter, 20):
            screen.blit(monster_list[i], (screen_width/2 -150, screen_height/2 - 150))
        
        draw_health()
        if event.type == pygame.QUIT:
            exit()
            
        if breaksys == True:
            breaksys = False
            break
        
        if monster.hp <= 0:
            player.hp = my_hp
            monster_hp = 100 + 5 * (monster_counter + 4)
            monster_attack = 10 + 5* (monster_counter + 4)
            monster_counter = monster_counter + 1
            money += 5 * (monster_counter + 2)
            del monsters[monsters.index(monster)]
            monster = Monster(f"{monster_list[monster_counter]}", monster_hp, monster_attack)
            monsters = [monster]
            print('승리')
            print(monster.hp)
            print(monster_attack)
            break
        
        if player.hp <= 0:
            player.hp = my_hp
            monster.hp = monster_hp
            monster_counter = monster_counter + 1
            print('패배')
            break
            
        
        if monster_counter >= 20:
            draw_win()
            exit()
        
        button1.draw()
        button2.draw()
        button3.draw()
 
        pygame.display.update() #모든 화면 그리기 업데이트
        clock.tick(60)

runGame()
pygame.quit()
