# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: esafar <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 15:56:33 by esafar            #+#    #+#              #
#    Updated: 2021/11/09 16:20:26 by esafar           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

count = 1
success = 0
to_guess = random.randint(1, 99)

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")

entry = input(">> ")
if entry == "exit":
    print("Program closed.")
    print("See you later :)")
elif entry.isdigit():
    while success == 0:
        if entry.isdigit():
            if int(entry) == int(to_guess):
                print("Congratulations, you've got it!")
                success = 1
            else:
                if int(entry) < int(to_guess):
                    print("Too low!")
                    count += 1
                else:
                    print("Too high!")
                    count += 1
                entry = input(">> ")
        else:
            if entry == "exit":
                print("Program closed.")
                print("See you later :)")
                break
            else:
                print("That's not a number.")
                entry = input(">> ")
if success == 1:
    print("You won in", count, "attempts!")
