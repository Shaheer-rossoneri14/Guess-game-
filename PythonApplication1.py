'''Guessing game on python
1.Computer generates a random number between 1 and 100
1.User guesses the number. 
2.Computer guides you to approach the answer. 
3.Count the number of trails. 
4.Restart the game. 
'''
import random  #To generate a random number
ask = 'y' 
while (ask=='y'):
    play_game = input('Press y to play and n to exit: ')

    if (play_game == 'y'):
        answer = random.randint(1, 100)
        print('Computer has thought of a number, can you guess it?')
        try_number = input('Guess a number between 1 and 100: ')
        try_number = int(try_number)
        counter = 1                 #No of guess to reach answer    

        while try_number !=answer:
            if try_number > answer:
                print('Your number is too large.')

            if try_number < answer:
                print('Your number is too small')

            try_number = int(input('Guess a number between 1 and 100: '))
            counter = counter + 1 
        print('You got it! You tried ' + str(counter) + ' times to get to the answer.')

    if (play_game== 'n'):
        print('Thank You')

