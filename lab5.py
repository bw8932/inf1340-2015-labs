#!/usr/bin/env python3

""" GUI for Name that Shape """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from name_that_shape import *
import Tkinter
import tkMessageBox

"""
   Create a GUI for the Name That Shape program
   See name_shape_gui.png for specification
   Use the name_that_shape.py to perform computations
   For inputs that raise an error, pop up a modal dialog box
   For inputs that produce a shape name, display the string in the window
"""


class NameThatShapeGUI:

    def __init__(self):

        # Create a main window
        self.main_window = Tkinter.Tk()

        Tkinter.mainloop()


# Instantiating the object
ntsg = NameThatShapeGUI()
