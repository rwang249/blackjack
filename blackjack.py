#!/usr/bin/env python3

import random
import os

class Card:
    def __init__(self, suit, suitvalue, value, cardValue):
        self.suits = suit
        self.suitValue = suitValue
        self.value = value
        self.cardValue = cardValue

def clearScreen():
    system('clear')

def printCards(hand):
    for card in hand:
        top += '---------------   ' 
        print(top)

        middle += '|' +  hand.value + hand.suiteValue + '\n|\n|\n|\n'             '|\n|\n|\n|\n   '
        print(middle)

        bottom += '---------------   '
        print(bottom)

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
            playerHandValue += card.cardValues[values]
            cardDeck.remove(card)
            
            card = random.choice(cardDeck)
            dealerHand.append(card)
            dealerHandValue += card.cardValues[values]
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
            elif action = 'S':
                if dealerHandValue < 17:
                    card = random.choice(cardDeck)
                    dealerHand.append(card)
                    dealerHandValue += card.cardValues[values]
                    cardDeck.remove(card)
                    continue
                else:

            else:
                print("Not a valid selection!")
                continue
            





suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
suitValues = ["Diamonds":"\u2666", "Hearts":"\u2665", "Clubs":"\u2663", "Spades":"\u2660"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
cardValues = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}
cardDeck = []


if __name__ == "__main__":
    for suit in suits:
        for card in values:
            deck.append(Card(suit, suitValues[suit], card, cardValues[values]))
    
    Game(cardDeck)