#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

PROVINCIAL_ST = .05
FEDERAL_ST = .025


def prov_tax(purchase):
    prov_tax_value = purchase * PROVINCIAL_ST
    #print ("Provincial tax: {0:.2f}".format(prov_tax_value))
    return prov_tax_value

def fed_tax(purchase):
    fed_tax_value = purchase * FEDERAL_ST
   # print ("Federal tax: {0:.2f}".format(fed_tax_value))
    return fed_tax_value

def bill_of_sale(purchase):

    provincial_tax = prov_tax(purchase)
    federal_tax = fed_tax(purchase)
    total_tax = federal_tax + provincial_tax
    total_sale = purchase + total_tax

    with open("costs.txt", 'w') as output_file:
        output_file.write("Federal Tax: {0:.2f}".format(federal_tax))
        output_file.write("\n Provincial Tax: {0:.2f}".format(provincial_tax))
        output_file.write("\n Total Tax: {0:.2f}".format(total_tax))
        output_file.write("\n Total Sale: {0:.2f}".format(total_sale))

bill_of_sale(100)

