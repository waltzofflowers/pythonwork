import random

stages = [
    '''
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
=========
''', '''
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

''', '''
  +---+
      |
      |
      |
      |
      |
=========
'''
]

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []

for letter in chosen_word:
    display.append("_")

life = 7

while "_" in display:
    guess = input("Guess a letter: ").lower()

    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = str(guess)

    if guess not in chosen_word:
        print(f"\n{guess} was wrong you just lost life.")
        life = life - 1
    display_str = "".join(display)

    print(stages[life])
    print(display_str)
    print(life)

    if life == 0:
        print("You lose")
        break
    elif "_" not in display:
        print("You win")
        break
