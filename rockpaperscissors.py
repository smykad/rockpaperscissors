# Doug Smyka
#

import random  # allows random choice

user_guess = ''  # variable for players guess
choices = ['rock', 'paper', 'scissors']  # list of guesses to choose from
computer_guess = random.choice(choices)
num_ties = 0  # tracks number of ties
num_wins = 0  # tracks number of wins
num_losses = 0  # tracks number of losses
user_response = ''
play = True

print('Welcome to the Rock, Paper, Scissors application, what is your name?')
name = input()  #asks for users name
print('Nice to meet you ' + name + ', let\'s play!')  # engages user to play rock paper scissors

while True:
    print('Ready or not! Rock, Paper, Scissors!')
    user_guess = input() #queries user for rock, paper, scissors
    user_guess = user_guess.lower() #converts the string to a lower case response
    if user_guess in choices:   #checks to see if input from line 15 is valid
        if user_guess == computer_guess:    #checks to see if both users picked the same
            num_ties += 1
            print('It\'s a tie! you both picked ' + str(user_guess) + '!')  #displays tie and what choice they made
        elif user_guess == 'rock':
            if computer_guess == 'scissors':
                num_wins += 1
                print('Rock beats scissors! You win!')
            else:
                num_losses += 1
                print('Paper beats rock, you lose')
        elif user_guess == 'paper':
            if computer_guess == 'rock':
                num_wins += 1
                print('Paper beats rock! You Win!')
            else:
                num_losses += 1
                print('Scissors beats paper, you lose')
        elif user_guess == 'scissors':
            if computer_guess == 'paper':
                num_wins += 1
                print('Scissors beats paper, you win!')
            else:
                num_losses += 1
                print('Rock beats scissors, you lose')
    else:
        print('So you picked ' + str(user_guess) + '?')
    print('Would you like to play again?')
    user_response = input()
    user_response = user_response.lower()
    if user_response == 'y' or user_response == 'yes':
            continue
    else:
        print('Thank you for playing ' + str(name) + ' your stats are as followed:')
        print('Wins: ' + str(num_wins) + ' Losses:' + str(num_losses) + 'Ties: ' + str(num_ties) + '!')
        break
