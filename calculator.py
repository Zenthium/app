#! /usr/bin/env python3

import math

#Basic four function calculator. Not much just yet, might add more functionality.

choice = 0


def addition(numOne, numTwo):
    result = float(numOne) + float(numTwo)
    return result


def subtraction(numOne, numTwo):
    result = float(numOne) - float(numTwo)
    return result


def multiplication(numOne, numTwo):
    result = float(numOne) * float(numTwo)
    return result


def division(numOne,numTwo):
    result = float(numOne)/float(numTwo)
    return result

def exponents(numOne, power):
    if int(power) == 0:
        return 1
    elif int(power) == 0:
        return numOne
    else:
        try:
            return math.pow(int(numOne), int(power))
        except OverflowError:
            return 'That number too large! Overflow error!'
def factorial(numOne):
    if int(numOne) == 0:
        return 1;
    else:
        return int(numOne) * factorial(int(numOne) - 1)


print("Welcome to my python project!\n" + \
      "This is a calculator.\n" + \
      "Select which function you would like to do\n" + \
      "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n" + \
      "5. Exponents\n6. Factorials\n7. Exit")

while int(choice) != 7 and int(choice) < 7:
    choice = input("Which function would you like to do? ")
    if int(choice) == 1:
        num1 = input("Enter your first number. ")
        num2 = input("Enter your second number. ")
        print("The answer is " + str(addition(num1,num2)))
    elif int(choice) == 2:
        num1 = input("Enter your first number. ")
        num2 = input("Enter your second number. ")
        print("The answer is " + str(subtraction(num1,num2)))
    elif int(choice) == 3:
        num1 = input("Enter your first number. ")
        num2 = input("Enter your second number. ")
        print("The answer is " + str(multiplication(num1,num2)))
    elif int(choice) == 4:
        num1 = input("Enter your first number. ")
        num2 = input("Enter your second number. ")
        print("The answer is " + str(division(num1,num2)))
    elif int(choice) == 5:
        num1 = input("Enter your number. ")
        power = input("What power would you like to raise that number to? ")
        print("The answer is " + str(exponents(num1, power)))
    elif int(choice) == 6:
        num1 = input("What number would you like to factorial? ")
        print("The answer is " + str(factorial(num1)))
print("Shutting down...")
