import random


print("Welcome to the casino!")
print("")
score = 0
cards = [random.randint(1,11)]
print("Starting card:", cards[0])

while True:
    choice = input("Do you want to draw another card? (y/n): ")
    if choice == 'y':
        cards.append(random.randint(1,11))
        print("Your cards:", cards)
        score = sum(cards)
        print("Your score:", score)
        if score == 21:
            print("BlackJack!")
            break
        elif score > 21:
            print("Busted!")
            break
    else:
        print("Game Over!")
        print("Your score:", score)
        break
