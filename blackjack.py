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

def printCards(hand, hidden):
    printHand = ''
    
    if hidden == True:
        printHand = '?\t'
        print(printHand)
    
    for card in hand:
        printHand = card.suitValue + card.value + '\t'
        print(printHand)


def Game(cardDeck):
    playerHand = []
    dealerHand = []
    playerHandValue = 0
    dealerHandValue = 0
    winner = False

    while winner != True:
        handIteration = 0
        clearScreen()
        while True:
            while len(playerHand) < 2 and len(dealerHand) < 2:
                
                card = random.choice(cardDeck)
                playerHand.append(card)
                playerHandValue += card.cardValue
                cardDeck.remove(card)
                print('PLAYER HAND: ' + str(playerHandValue))
                printCards(playerHand, False)
                time.sleep(1)
                
                card = random.choice(cardDeck)
                dealerHand.append(card)
                dealerHandValue += card.cardValue
                cardDeck.remove(card)
                print('DEALER HAND: ?')
                time.sleep(1)
                
                if len(dealerHand) == 1:
                    printCards(dealerHand[:-1], True)
                elif len(playerHand) == 2 and len(dealerHand) == 2:
                    printCards(dealerHand[:-1], True)
                    break
                else:
                    printCards(dealerHand, False)
                    
                time.sleep(1)
                clearScreen()

            if playerHandValue == 21:
                print("Player Wins!")
                winner = True
                break
            elif dealerHandValue == 21:
                print("Dealer Wins!")
                print('DEALER HAND: ' + str(dealerHandValue))
                printCards(dealerHand, False)
                winner = True
                break

            action = input("Hit(H) or Stay(S): ")
            if action == 'H':
                card = random.choice(cardDeck)
                playerHand.append(card)
                playerHandValue += card.cardValue
                cardDeck.remove(card)
                if playerHandValue > 21:
                    while handIteration != len(playerHand):
                        if playerHand[handIteration].cardValue == 11:
                            playerHand[handIteration].cardValue = 1
                            playerHandValue -= 11
                            playerHandValue += playerHand[handIteration].cardValue
                        handIteration += 1
                    if playerHandValue > 21:
                        print('PLAYER HAND: ' + str(playerHandValue))
                        printCards(playerHand, False)
                        time.sleep(1)
                        print('DEALER HAND: ' + str(dealerHandValue))
                        printCards(dealerHand, False)
                        time.sleep(1)
                        print("Dealer Wins!")
                        winner = True
                        break
                    else:
                        print('PLAYER HAND: ' + str(playerHandValue))
                        printCards(playerHand, False)
                        continue
                print('PLAYER HAND: ' + str(playerHandValue))
                printCards(playerHand, False)
                time.sleep(1)
                continue
            elif action == 'S':
                print('PLAYER HAND: ' + str(playerHandValue))
                printCards(playerHand, False)
                time.sleep(1)
                print('DEALER HAND: ' + str(dealerHandValue))
                printCards(dealerHand, False)
                time.sleep(1)
                while dealerHandValue < 17:
                    card = random.choice(cardDeck)
                    dealerHand.append(card)
                    dealerHandValue += card.cardValue
                    cardDeck.remove(card)
                    print('PLAYER HAND: ' + str(playerHandValue))
                    printCards(playerHand, False)
                    time.sleep(1)
                    print('DEALER HAND: ' + str(dealerHandValue))
                    printCards(dealerHand, False)
                    time.sleep(1)
                    if dealerHandValue < 21:
                        continue
                    elif dealerHandValue > 21:
                        if dealerHandValue > 21:
                            while handIteration != len(dealerHand):
                                if dealerHand[handIteration].cardValue == 11:
                                    dealerHand[handIteration].cardValue = 1
                                    dealerHandValue -= 11
                                    dealerHandValue += dealerHand[handIteration].cardValue
                                handIteration += 1
                            if dealerHandValue > 21:
                                print("Player Wins!")
                                winner = True
                                break  
                if dealerHandValue > playerHandValue and dealerHandValue <= 21:
                        print("Dealer Wins!")
                        winner = True
                        break         
                elif playerHandValue > dealerHandValue and playerHandValue <= 21:
                        print("Player Wins!")
                        winner = True
                        break     
                elif playerHandValue == dealerHandValue:
                        print("Dealer Wins!")
                        winner = True
                        break         
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
