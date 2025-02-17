############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import logo
import random

print(logo.logo_blackjack)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_starting_cards():
    drawn_cards = []
    for i in range(2):
        number = random.choice(cards)
        drawn_cards.insert(i, number)
    return drawn_cards


def draw_another_card():
    draw_card = random.choice(cards)
    if draw_card == cards[0]:
        choose = int(input(f"You get {draw_card} - you have a choice to count it as 1 (1) or 11 (11)"))
        if choose == 1:
            user_cards.insert(len(user_cards), choose)
        else:
            user_cards.insert(len(user_cards), 11)
    else:
        user_cards.insert(len(user_cards), draw_card)

    return draw_card


def draw_computer_card():
    if total_computer < 17:
        draw_card = random.choice(cards)
        if draw_card == cards[0]:
            if total_computer + 11 <= 21:
                computer_cards.insert(len(computer_cards), cards[0])
            else:
                computer_cards.insert(len(computer_cards), 1)
        else:
            computer_cards.insert(len(computer_cards), draw_card)
    else:
        draw_card = 0

    return draw_card


user_cards = draw_starting_cards()
computer_cards = draw_starting_cards()

total_user = sum(user_cards)
total_computer = sum(computer_cards)

print(f"    Your cards are {user_cards} total of {total_user}")

draw = ''

while draw != 'n' and total_user < 21 and total_computer < 21:
    print(f"    The computer's first card is {computer_cards[0]}")
    draw = input("Do you want to draw 'y'? Or pass 'n'?: ")
    drawn_card_computer = draw_computer_card()
    total_computer = sum(computer_cards)
    if draw == 'y':
        drawn_card_user = draw_another_card()
        total_user = sum(user_cards)
    else:
        break

    print(f"    Your cards now are {user_cards} so the new total is {total_user}")

    if total_computer > 21 or total_user > 21:
        break

if total_computer == 21:
    print(f"You lose! computer has a BLACKJACK with cards {computer_cards}")
elif total_user == 21:
    if total_user == total_computer:
        print("Draw, you both have a BLACKJACK")
    else:
        print(f"You win, you have a BLACKJACK, computer had {computer_cards}")
elif total_computer > 21:
    print(f"You win, computer crossed 21 with cards {computer_cards}.")
elif total_user > 21:
    print(f"You lose, you crossed 21 with cards {user_cards}. Computer had {computer_cards} so far.")
else:
    if total_user > total_computer:
        print(f"You win with total of {total_user}, computer had total of {total_computer} with cards {computer_cards}")
    elif total_computer > total_user:
        print(f"You lose, computer had total of {total_computer} with cards {computer_cards}")
    else:
        print("It's a tie!")
