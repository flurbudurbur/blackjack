from array import array
from random import random


class BlackJack:
    def __init__(self):
        self.cards = array('i', [int(random()*10) for i in range(2)])
        self.compare_cards(self, cards=self.cards)

    @staticmethod
    def compare_cards(self, cards):
        bj_sum = 0
        for card in cards:
            bj_sum += card

        if bj_sum == 21:
            print("BlackJack!")
            exit()
        elif bj_sum > 21:
            print("Busted!")
            exit()
        else:
            print("You have: ", bj_sum)
            return bj_sum


if __name__ == '__main__':
    game = BlackJack()