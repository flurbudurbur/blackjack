from array import array
import random


class BlackJack:
    def __init__(self):
        self.player_score = 0
        self.cards = [self.kaarten_trekken(self)]
        self.message()
        self.compare_cards(self, self.cards)


    def message(self):
        print("Welcome to BlackJack!")
        print("Player score: ", self.player_score)

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

    @staticmethod
    def kaarten_trekken(self):
        cards = self.cards.append(random.randint(1, 11))
        return cards

    def stop_message(self):
        print("Game Over!")
        print("Player score: ", self.player_score)


if __name__ == '__main__':
    game = BlackJack()