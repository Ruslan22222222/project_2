from art import logo
import os

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n ")) 
nr_symbols = int(input(f"How many symbols would you like?\n "))
nr_numbers = int(input(f"How many numbers would you like?\n "))


password_on = True


while password_on:
    print(logo)
    password_list = []

    for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))

    for char in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)

    for char in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    

    print(f"Your password is {password}")

    if input("Do u want to generate again? Type 'y' or 'n': ") == "y":
        os.system('clear')
    else:
        break




















