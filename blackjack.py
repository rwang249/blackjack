#!/usr/bin/env python3

import random
import os
import time

class Card:
    def __init__(self, suitValue, value, cardValue):
        self.suitValue = suitValue
        self.value = value
        self.cardValue = cardValue

def clearScreen():
    os.system('clear')

def printCards(hand): 
    cardCount = 1
    count = 0
    length = 3
    top = ''
    middle = [''] * length
    suitMiddle = ''
    emptyMiddle = ''
    bottom = ''
    
    for card in hand:
        cards = range(1, length)
        #cards = 0
        index = 0
        
        #print top section
        while len(top) < (10 * cardCount):
            if len(top) == (10 * cardCount - 1):
                top += '\t'
            else:
                top += '-'

        #print middle section
        suitMiddle += '|' + card.suitValue + card.value + '\t|\t'
        middle[0] = suitMiddle
        middle[0] += '\n'
        index += 1
        
        emptyMiddle += '|' + '  ' + '\t|\t'
        
        for n in cards:
            if n == 1:
                middle[n] = emptyMiddle
                middle[n] += '\n'
            elif n == (length - 1):
                middle[n] += emptyMiddle
            elif n == length:
                break
            else:
                middle[n] += emptyMiddle
                middle[n] += '\n'
              
        # #print bottom section
        while len(bottom) < (10 * cardCount):
            if len(bottom) == (10 * cardCount - 1):
                bottom += '\t'
            else:
                bottom += '-'    

        
        print(top)
        print(''.join(middle))
        print(bottom)
        cardCount += 1
        time.sleep(1)


def Game(cardDeck):
    playerHand = []
    dealerHand = []
    playerHandValue = 0
    dealerHandValue = 0
    winner = False

    while winner != True:
        clearScreen()

        while len(playerHand) < 2 and len(dealerHand) < 2:
            card = random.choice(cardDeck)
            playerHand.append(card)
            playerHandValue += card.cardValue
            cardDeck.remove(card)
            
            card = random.choice(cardDeck)
            dealerHand.append(card)
            dealerHandValue += card.cardValue
            cardDeck.remove(card)

        while True:
            print('PLAYER HAND')
            printCards(playerHand)
            print('#################################################')
            print('DEALER HAND')
            printCards(dealerHand)

            if playerHandValue == 21:
                print("Player Wins!")
                winner = True
                break
            elif dealerHandValue == 21:
                print("Dealer Wins!")
                winner = True
                break

            if playerHandValue > 21:
                print("Player Loses!")
                winner = True
                break
            elif dealerHandValue > 21:
                print("Player Wins!")
                winner = True
                break

            action = input("Hit(H) or Stay(S): ")
            if action == 'H':
                card = random.choice(cardDeck)
                playerHand.append(card)
                playerHandValue += card.cardValues[values]
                cardDeck.remove(card)
                continue
            elif action == 'S':
                if dealerHandValue < 17:
                    card = random.choice(cardDeck)
                    dealerHand.append(card)
                    dealerHandValue += card.cardValues[values]
                    cardDeck.remove(card)
                    continue
#                else:

            else:
                print("Not a valid selection!")
                continue
            





suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
suitValues = {"Diamonds":"\u2666", "Hearts":"\u2665", "Clubs":"\u2663", "Spades":"\u2660"}
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
cardValues = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}
cardDeck = []


if __name__ == "__main__":
    for suit in suits:
        for card in values:
            cardDeck.append(Card(suitValues[suit], card, cardValues[card]))

    Game(cardDeck)
