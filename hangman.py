# Copyright (c) 2025 Thomas Duggan and Devin Reardon
# This work is licensed under CC BY-SA 4.0


from random import *
from time import sleep
import matplotlib.pyplot as plt
from engi1020.arduino.api import *


def find_positions(letter, word):
    """Returns a list of positions where the letter appears in the word.

    Parameters
    ----------
    letter : str
        A single character string representing the guessed letter.
    word : str
        A string representing the chosen word in which to find occurrences of the letter.

    Returns
    -------
    list of int
        A list of positions (indices) where the letter appears in the word.
    """


HANGMAN_PICS = [
'''
   +---+
   O   |
       |
       |
      ===''',
'''
   +---+
   O   |
   |   |
       |
      ===''',
'''
   +---+
   O   |
  /|   |
       |
      ===''',
'''
   +---+
   O   |
  /|\  |
       |
      ===''',
'''
   +---+
   O   |
  /|\  |
  /    |
      ===''',
'''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

words = [['python', 'java', 'ruby', 'html', 'css'],
         ['hangman', 'programming', 'computer', 'science'],
         ['openai', 'challenge', 'algorithm', 'datastructure']]   

History_n = []
History_s = []

def find_positions(letter, word):

    rep = -1	# “repeats”
    loc = 0		# “location”
    stop = False
    
    if len(letter) > 1:
        loc = -1
        stop = True
        
    if stop == False:
        for i in range(len(word)):
            rep += 1
            if letter in word[i]:
                loc += rep
    return loc

name = "null"
guesses = 6
guess_bank = []
failed = False
name_history = []
score_history = []

while True:
    
    digital_write(4,False)
    
    if name == "null" or failed == True:
        name = input("Enter your name: ")
        difficulty = input("Choose a difficuly level (easy, medium, hard): ")
        word_spaces = []
        spaces_filled = False
        guesses = 6
        guess_bank = []
        failed = False
        name_history += [name]
    
    if difficulty == "easy" and spaces_filled == False:
        word_temp = (words[0])
        word = choice(word_temp)
        
        for spaces in range(len(word)):
            word_spaces += ["_"]
            spaces_filled = True
            
    if difficulty == "medium" and spaces_filled == False:
        word_temp = (words[1])
        word = choice(word_temp)
        
        for spaces in range(len(word)):
            word_spaces += ["_"]
            spaces_filled = True
            
    if difficulty == "hard" and spaces_filled == False:
        word_temp = (words[2])
        word = choice(word_temp)
        
        for spaces in range(len(word)):
            word_spaces += ["_"]
            spaces_filled = True
            
    print(word_spaces)
    
    
    guess = input("Guess a letter: ")
    guess_bank += [guess]
    
    #print(guess_bank) # testing only
    #print(guess)
    
    find_positions(guess, word)
    
    location = []
    for i in range(len(word)):
        if word[i] == guess:
            location += [i]
          
    for repeats in range(len(location)):
        if location != []: 
            word_spaces[location[repeats]] = word[location[repeats]]
            print("Correct!")
            digital_write(4,True)
            sleep(1)
            
    guessed_times = 0
    
    # print(guessed_times) # For testing only
            
    for x in range(len(guess_bank)):
        if guess in guess_bank[x]:
            guessed_times += 1
            
    # print(guessed_times) # For testing only
            
    
    if location == [] and guessed_times <= 1:
        print("Try again!")
        guesses -= 1
            
    if location == [] and guessed_times > 1:
        print("You guessed that letter already, Try again!")
        
    print("Guesses Remaining: ",guesses)
    
    print(word_spaces)
    
    hangman_thing = 5-guesses
    if 5-guesses == -1:
        hangman_thing = 0
    
    
    print(HANGMAN_PICS[hangman_thing])
    
    if word == "".join(word_spaces):
        failed = True
        print("Congratulations")
        print("Hold button to continue")
        score_history += [guesses]
        sleep(4)
        if digital_read(6) == False:
            break
    
    if guesses == 0:
        failed = True
        print("Game Over! The word was; ",word)
        print("Hold button to continue")
        score_history += [guesses]
        sleep(4)
        if digital_read(6) == False:
            break
        
plt.bar(name_history, score_history)
plt.show()
        