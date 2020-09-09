# ********************************
# Author: Doug Smyka
# Application: rockpaperscissors
# Date Created: 9.9.20
# Date Revised: 9.9.20
# ********************************

import random  # allows random choice

user_guess = ''  # variable for players guess
choices = ['rock', 'paper', 'scissors']  # list of guesses to choose from
alt_choices = ['r', 'p', 's']  # provides user with optional entries
computer_guess = random.choice(choices)  # computer picks random choice
num_ties = 0  # tracks number of ties
num_wins = 0  # tracks number of wins
num_losses = 0  # tracks number of losses
user_response = ''  # string for user input

# welcomes user to program
name = input('Welcome to the Rock, Paper, Scissors application, what is your' +
             'name?\n')  # asks for users name
print('Nice to meet you ' + name + ', let\'s play!')

# engages user to play rock paper scissors
while True:
    # queries user for rock, paper, scissors
    user_guess = input('Ready or not! Rock, Paper, Scissors!\n').lower()
    # checks to see if input from user is part of list choices\alt_choices
    if user_guess in choices or alt_choices:
        # where the application determines the outcome of user versus computer
        if user_guess == computer_guess:
            num_ties += 1
            print('It\'s a tie! you both picked '
                  + str(user_guess) + '!')
        elif user_guess == 'rock' or 'r':
            if computer_guess == 'scissors':
                num_wins += 1
                print('Rock beats scissors! You win!')
            else:
                num_losses += 1
                print('Paper beats rock, you lose')
        elif user_guess == 'paper' or 'p':
            if computer_guess == 'rock':
                num_wins += 1
                print('Paper beats rock! You Win!')
            else:
                num_losses += 1
                print('Scissors beats paper, you lose')
        elif user_guess == 'scissors' or 's':
            if computer_guess == 'paper':
                num_wins += 1
                print('Scissors beats paper, you win!')
            else:
                num_losses += 1
                print('Rock beats scissors, you lose')
    else:
        # displays users invalid response
        print('So you picked ' + str(user_guess) + '?')
    # next line asks user if they want to play again
    user_response = input('Would you like to play again?\n').lower()
    if user_response == 'y' or user_response == 'yes':
            continue
    else:
        # Thanks user for playing, gives statistics, ends program
        print('Thank you for playing ' + str(name) +
              ' your stats are as follows:')
        print('Wins: ' + str(num_wins) + ' Losses:' + str(num_losses) +
              ' Ties: ' + str(num_ties) + '!')
        break