#!/usr/bin/env python3

""" Name that Shape module for use with Lab 5, Inf1340, Fall 2015 """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


"""
Instructions: Add a function to to get input from the user and used that
function in name_that_shape()

The function should prompt the user for input until an integer value is
entered.

"""

def name_that_shape(sides):
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs | Expected Outputs
    -------------------------
      < 3  | Error
      3    | triangle
      4    | quadrilateral
      5    | pentagon
      6    | hexagon
      7    | heptagon
      8    | octagon
      9    | nonagon
      10   | decagon
      > 10 | Error

    Errors: ValueError when input is a string or float

    """
    sides = str(sides)
    if sides.isdigit() or sides[0] is "-" and sides[1:].isdigit():
        sides = int(sides)
    else:
        return None

    if sides == 3:
        return ("triangle")
    elif sides == 4:
        return ("quadrilateral")
    elif sides == 5:
        return("pentagon")
    elif sides == 6:
        return("hexagon")
    elif sides == 7:
        return("heptagon")
    elif sides == 8:
        return("octagon")
    elif sides == 9:
        return("nonagon")
    elif sides == 10:
        return("decagon")
    else:
        return None
