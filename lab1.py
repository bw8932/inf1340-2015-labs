#!/usr/bin/env python3

""" Graded Lab #1 for Inf1340, Fall 2015 """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def vowel_or_consonant():
    letter = raw_input("Enter letter:")
    if letter == "a" or letter == "i" or letter == "e" or letter == "o" or letter == "u":
        print ("vowel")
    elif letter == ("y"):
        print ("sometimes a vowel, sometimes a consonant")
    else:
        print ("consonant")

    """
    Exercise: Vowel or Consonant
    Reads a letter of the alphabet from the user. (You can assume that it's
    lowercase.) If the user enters a, e, i, o or u then your program should
    display "vowel". If the user enters y then your program should display
    "sometimes a vowel, sometimes a consonant". Otherwise your program should
    display a message indicating that the letter is a "consonant".
    """

# comment out for test to work vowel_or_consonant()
