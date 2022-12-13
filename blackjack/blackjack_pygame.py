import pygame as pygame
from blackjack_deck import *
import sys
import time
pygame.init()

background_color = (0,128,0)
grey = (220,220,220)
black = (0,0,0)
green = (0, 200, 0)
red = (255,0,0)
light_slat = (119,136,153)

pygame.init()
font = pygame.font.SysFont("Arial", 20)



SUITS = ['c', 's', 'h', 'd']
RANKS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((900, 600))

flip_sound = pygame.mixer.Sound("card.wav")
def play_cardflip_sound(rep):
    pygame.mixer.Sound.play(flip_sound, loops=rep-1)

pygame.display.set_caption('BlackJack')
gameDisplay.fill(background_color)

pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 250, 700))

###text object render
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def end_text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


#game text display
def game_texts(text, x, y):
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

 
def game_finish(text, x, y, color):
    TextSurf, TextRect = end_text_objects(text, font, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def black_jack(text, x, y, color):
    TextSurf, TextRect = end_text_objects(text, font, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    
#button display
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    TextSurf, TextRect = text_objects(msg, font)
    TextRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(TextSurf, TextRect)


class Play:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()
        
    def blackjack(self):

        self.dealer.calc_hand()
        self.player.calc_hand()

        show_dealer_card = pygame.image.load('' + self.dealer.card_img[1] + '.gif').convert()
        
        if self.player.value == 21 and self.dealer.value == 21:
            gameDisplay.blit(show_dealer_card, (550, 200))
            black_jack("Both with BlackJack!", 500, 250, grey)
            time.sleep(4)
            self.play_or_exit()
        elif self.player.value == 21:
            gameDisplay.blit(show_dealer_card, (550, 200))
            black_jack("You got BlackJack!", 500, 250, green)
            time.sleep(4)
            self.play_or_exit()
        elif self.dealer.value == 21:
            gameDisplay.blit(show_dealer_card, (550, 200))
            black_jack("Dealer has BlackJack!", 500, 250, red)
            time.sleep(4)
            self.play_or_exit()
            
        self.player.value = 0
        self.dealer.value = 0

    def deal(self):
        for i in range(2):
            self.dealer.add_card(self.deck.deal())
            self.player.add_card(self.deck.deal())
        self.dealer.display_cards()
        self.player.display_cards()
        self.player_card = 1
        dealer_card = pygame.image.load('' + self.dealer.card_img[0] + '.gif').convert()
        play_cardflip_sound(1)
        dealer_card_2 = pygame.image.load('back.png').convert()
        play_cardflip_sound(1)
            
        player_card = pygame.image.load('' + self.player.card_img[0] + '.gif').convert()
        play_cardflip_sound(1)
        player_card_2 = pygame.image.load('' + self.player.card_img[1] + '.gif').convert()
        play_cardflip_sound(1)

        
        game_texts("Dealer's hand is:", 500, 150)

        gameDisplay.blit(dealer_card, (400, 200))
        gameDisplay.blit(dealer_card_2, (550, 200))

        game_texts("Your's hand is:", 500, 400)
        
        gameDisplay.blit(player_card, (300, 450))
        gameDisplay.blit(player_card_2, (410, 450))
        self.blackjack()
            
            

    def hit(self):
        self.player.add_card(self.deck.deal())
        self.blackjack()
        self.player_card += 1
        
        if self.player_card == 2:
            self.player.calc_hand()
            self.player.display_cards()
            player_card_3 = pygame.image.load('' + self.player.card_img[2] + '.gif').convert()
            play_cardflip_sound(1)
            gameDisplay.blit(player_card_3, (520, 450))

        if self.player_card == 3:
            self.player.calc_hand()
            self.player.display_cards()
            player_card_4 = pygame.image.load('' + self.player.card_img[3] + '.gif').convert()
            play_cardflip_sound(1)
            gameDisplay.blit(player_card_4, (630, 450))
                
        if self.player.value > 21:
            show_dealer_card = pygame.image.load('' + self.dealer.card_img[1] + '.gif').convert()
            play_cardflip_sound(1)
            gameDisplay.blit(show_dealer_card, (550, 200))
            game_finish("You Busted!", 500, 250, red)
            time.sleep(4)
            self.play_or_exit()
            
        self.player.value = 0

        if self.player_card > 4:
            sys.exit()
            
            
    def stand(self):
        self.dealer.add_card(self.deck.deal())
        show_dealer_card = pygame.image.load('' + self.dealer.card_img[1] + '.gif').convert()
        play_cardflip_sound(1)
        gameDisplay.blit(show_dealer_card, (550, 200))
        
        self.blackjack()
        self.dealer.calc_hand()
        self.player.calc_hand()
        print(self.dealer.value)
        if self.player.value > self.dealer.value:
            game_finish("You Won!", 500, 250, green)
            time.sleep(4)
            self.play_or_exit()
        elif self.player.value < self.dealer.value:
            game_finish("Dealer Wins!", 500, 250, red)
            time.sleep(4)
            self.play_or_exit()
        else:
            game_finish("It's a Tie!", 500, 250, grey)
            time.sleep(4)
            self.play_or_exit()
        
    
    def exit(self):
        sys.exit()
    
    def play_or_exit(self):
        game_texts("Play again press Deal!", 200, 80)
        time.sleep(3)
        self.player.value = 0
        self.dealer.value = 0
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()
        gameDisplay.fill(background_color)
        pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 250, 700))
        pygame.display.update()

        
play_blackjack = Play()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        button("Start/Reset", 30, 100, 150, 50, red, green, play_blackjack.deal)
        button("Hit", 30, 200, 150, 50, red, green, play_blackjack.hit)
        button("Stay", 30, 300, 150, 50, red, green, play_blackjack.stand)
        button("EXIT", 30, 500, 150, 50, red, green, play_blackjack.exit)
    
    pygame.display.flip()