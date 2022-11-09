#!/usr/bin/env python3
# A program that prompts a user to guess a number between 1 and 10

# Import the random library
import random

def main():
    # Generate a random numbeer between 1 and 10
    randomNum = [random.randint(1, 10)]
    
    # Set loop counter
    count = 0
    maxTurns = 3
    
    print('You have 3 turns to guess the magic number.')
    
    # Enter loop                   
    while (count < maxTurns):
        # Request number from player 
        numGuess = input("Enter an integer between 1 and 10 -->")     
        if numGuess.isnumeric and numGuess > 0 and numGuess <= 10:
            print('You provided a valid guess')
        else:
            print('You provided invalid input')
            break

        # Convert guess to int
        numGuess = int(numGuess)

        # Increment turn counter                            
        count = count + 1

        if numGuess == randomNum:
            print('You guessed correctly')
            print('Show me da money!!!')
            break
        elif ((numGuess + 1) == randomNum) or ((numGuess - 1) == randomNum):
            print('You guessed: ' + str(numGuess) + '. The random number was ' + str(randomNum) + '.')
            print('You were really close. Unlucky..\n.')
        else:
            print('You guessed: ' + str(numGuess) + ' . The random number was ' + str(randomNum) + '.')
            if count != 3:
                print('Try again. You have ' + str(maxTurns - count) + 'remaining.' )
            elif count == 3:
                print('That was your last go. Bye, bye!')

main()
