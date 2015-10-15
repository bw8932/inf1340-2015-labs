#!/usr/bin/env python

""" Module to test exercise2.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

import pytest
import mock
from lab2 import name_that_shape


def test_accepted_inputs(capsys):
    """
    Inputs that are the range 3-10 inclusive
    """

    with mock.patch("__builtin__.raw_input", return_value="3"):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out == "triangle\n"

    with mock.patch("__builtin__.raw_input", return_value="4"):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out == "quadrilateral\n"

    with mock.patch("__builtin__.raw_input", return_value="5"):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out == "pentagon\n"

    with mock.patch("__builtin__.raw_input", return_value="6"):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out == "hexagon\n"

    with mock.patch("__builtin__.raw_input", return_value="7"):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out == "heptagon\n"

    with mock.patch("__builtin__.raw_input", return_value="8"):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out == "octagon\n"

    with mock.patch("__builtin__.raw_input", return_value="9"):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out == "nonagon\n"

    with mock.patch("__builtin__.raw_input", return_value="10"):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out == "decagon\n"


def test_integers_outside_range(capsys):
    """
    Integers that are outside the 3-10 range
    """

    with mock.patch("__builtin__.raw_input", return_value="1"):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out == "Error\n"

    with mock.patch("__builtin__.raw_input", return_value="2"):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out == "Error\n"

    with mock.patch("__builtin__.raw_input", return_value="11"):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out == "Error\n"

    with mock.patch("__builtin__.raw_input", return_value="-3"):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out == "Error\n"

    with mock.patch("__builtin__.raw_input", return_value="-9"):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out == "Error\n"



def test_strings_inputs(capsys):
    """
    String inputs
    """

    with mock.patch("__builtin__.raw_input", side_effect=["string", "3"]):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out.endswith("triangle\n")


def test_float_inputs(capsys):
    """
    Float inputs
    """

    with mock.patch("__builtin__.raw_input", side_effect=["2.5", "4"]):
        name_that_shape()
        out, err = capsys.readouterr()
        assert out.endswith("quadrilateral\n")
