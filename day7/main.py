

# * Day 7 Python
import random
from words import word_list

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
# word_list = ['hello', 'cup', 'dog', 'stream',
#              'house', 'schedule', 'mouse', 'computer']

choosen_word = random.choice(word_list).lower()
#@ print(f'hint choosen word is {choosen_word}')
# print(f'You have 7 opportunities')
display = []

for letter in choosen_word:
    display.append('_')
    # if letter == guess:
    #     print(' Is a match')
    # else:
    #     print('Not quite right')

end_of_game = False
lifes_left = 6
while not end_of_game:
    print(f'You have {lifes_left} left')
    if ('_' in display):
        guess = input('Gues a letter that could be on the word. \n').lower()
        for p in range(len(choosen_word)):
            if (choosen_word[p] == guess):
                display[p] = guess
        print(f"{' '.join(display)}")

        if guess not in choosen_word:
            print(f'You guess the letter {guess}, that is not on the word')
            lifes_left -= 1
            print(stages[lifes_left])
            if lifes_left == 0:
                end_of_game = True
                print(f'You lost ;(')
                print(f'Word was {choosen_word}')
    else:
        end_of_game = True
        print(f'Congrats you won xD')
        print(f'Word was {choosen_word}')
