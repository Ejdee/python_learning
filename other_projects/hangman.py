import random
word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Testing code
print(f'Pssst, the solution is {word}.')

display = []
lives = 6

for letter in word:
    display += "_"

while "_" in display and lives > 0:
    guessed = False
    guess = input("Guess a letter: ").lower()
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess
            guessed = True

    if not guessed:
        print(stages[lives - 1])
        lives -= 1

    print(f"{' '.join(display)}")

    if "_" not in display:
        print("You won!")
        break

    if lives == 0:
        print("You lose!")
        print(f"The word was {word}")
        break