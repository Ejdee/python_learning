from game_data import data
import logo
import random

print(logo.logo_higherlower)


# print(data[0]['follower_count'])

# function to pick random guy
def pick_random():
    number = random.randint(0, len(data) - 1)
    return data[number]


def compare_followers(man_a, man_b):
    if man_a['follower_count'] > man_b['follower_count']:
        return man_a
    else:
        return man_b


def new_round(guy_a, guy_b):
    guy_a = guy_b
    guy_b = pick_random()

    return guy_a, guy_b


people_a = pick_random()
people_b = pick_random()
score = 0

while True:
    print(f"Compare A: {people_a['name']}, {people_a['description']} from {people_a['country']}")
    print(logo.vs)
    print(f"Compare B: {people_b['name']}, {people_b['description']} from {people_b['country']}")

    guess = input("Who has more followers on instagram? Type 'A' or 'B' or 'Q' to quit: ")

    if guess == 'Q':
        break

    if guess != 'A' and guess != 'B':
        print("Please enter a valid input")
        continue

    more_followers = compare_followers(people_a, people_b)

    if (more_followers == people_a and guess == 'A') or (more_followers == people_b and guess == 'B'):
        score += 1
        print(f"That's correct! Your current score is {score}.")
    else:
        print(f"That's not right. Your final score is {score}.")
        break

    people_a, people_b = new_round(people_a, people_b)



