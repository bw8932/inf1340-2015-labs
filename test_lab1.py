#!/usr/bin/env python3

""" Test Suite for Graded Lab #1 for Inf1340, Fall 2015 """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

import mock
from lab1 import vowel_or_consonant


def test_vowel_or_consonant(capsys):

    vowels = list("aeiou")
    for letter in vowels:
        with mock.patch("__builtin__.raw_input", return_value=letter):
            vowel_or_consonant()
            (out, err) = capsys.readouterr()
            assert out == "vowel\n"

    with mock.patch("__builtin__.raw_input", return_value="y"):
        vowel_or_consonant()
        (out, err) = capsys.readouterr()
        assert out == "sometimes a vowel, sometimes a consonant\n"

    consonants = list("bcdfghjklmnpqrstvwxz")
    for letter in consonants:
        with mock.patch("__builtin__.raw_input", return_value=letter):
            vowel_or_consonant()
            (out, err) = capsys.readouterr()
            assert out == "consonant\n"