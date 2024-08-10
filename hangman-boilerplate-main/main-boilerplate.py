from hangman_words import word_list
from hangman_art import stages, logo
import random

#choose a random word out of the list of words

#get the length of the word into a variable


#change game-end = False and lives = 6
game_end = True
lives = 6

#print logo

#choose an empty list and populate it with '_' for all the chars in the word


#start the game by using while loop and game_end variable
while(not game_end):
    #ask for a guess and convert it to lowercase
    guess = input("Guess a letter: ").lower()

    #if guess is in display, print a message affirming the right guess
    

    #for all the chars in chosen_word, check if it equal to guess and if it is then put that char in display list.
    

    #if guess not in chosen word then print a message stating wrong guess and deduct one life.
    

    # if lives become 0, game_end = True and the message that you lost, the word was this {}
    

    #print the display string with one space between
    

    #if "_" not in dsiplay, then game_end = True and message goes you win.
    

    #print stages of hangman indexed via lives
    
