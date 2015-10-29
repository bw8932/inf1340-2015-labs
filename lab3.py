#!/usr/bin/env python3

""" Graded Lab #3 for Inf1340, Fall 2015 """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def days_in_month(month):
    month = month.capitalize()
    days = ""

    if month == "April" or month == "June" \
            or month == "September" or month == "November":
        days = 30
    elif month == "January" or month == "March" or month == "May" \
            or month == "July" or month == "August" or month == "October" or month == "December":
        days = 31
    elif month == "February":
        days = "28 or 29"
    else:
        raise ValueError

    return days
