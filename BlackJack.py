
import random


class BlackJack:
    def __init__(self):
        self.start()


    def message(self):
        print("\nWelcome to BlackJack, the most fun and interactive game! Get ready for an exciting game of chance and strategy, \nspecifically made for you, Jos, our teacher and benevolent overlord.")

    @staticmethod
    def compare_cards(self, cards):
        bj_sum = 0
        for card in cards:
            bj_sum += card

        if bj_sum == 21:
            bidding = input("BlackJack! You have reached a total score of 21, and thus you have won the game!\nYou're amazing and you win our never-ending loyalty and approval.\nWhat is thy bidding, our master?\n")
            print("thx!")
            self.retry()
        elif bj_sum > 21:
            print("Busted! You have reached a higher score than what is allowed. You have lost the game.")
            self.retry()

        else:
            user_input = input(f"\nYour current score is {bj_sum}. Do you want to draw another card? (y/n): ")
            if user_input == "y":
                self.kaarten_trekken(self)
            elif user_input == "n":
                self.stop_message(bj_sum)
                exit()
            else:
                print("Please enter (y/n)")

            self.compare_cards(self, self.cards)
            return bj_sum

    @staticmethod
    def kaarten_trekken(self):
        cards = self.cards.append(random.randint(1, 11))
        return cards

    def stop_message(self, score):
        print("\nOh no, the game is over!")
        print("Your score is: ", score)



    def start(self):
      self.cards = []
      self.cards.append(random.randint(1, 11))
      self.message()
      self.compare_cards(self, self.cards)

    def retry(self):
        try_again = input(
            "Care to try again? (y/n) ")
        if try_again == "y":
            self.start()
        elif try_again == "n":
            exit("Thank you for playing! See you in the future!")
        else:
            print("Oh no! You've accidentally typed something other than y or n. Try again!")
            self.retry()
if __name__ == '__main__':
    game = BlackJack()