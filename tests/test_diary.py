from lib.diary import *


"""if given at empty string
it returns an empty string."""

def test_return_empty_string():
    assert make_snippet('') == ''

"""if given a string of less than five words
it returns the same string."""

def test_return_less_than_five_word_string():
    assert make_snippet("i love my cats") == "i love my cats"

"""if given a string of five words or more
returns same string with ... on the end"""

def test_return_5_word_string_with_ellipse():
    assert make_snippet('i wish i had more cats') == 'i wish i had more cats...'



"""COUNT WORD FUNCTION TESTS"""

"""if given an empty string
it returns 0"""

def test_return_length_of_empty_string():
    assert count_words('') == 0

"""if given a string length of more than 0
it returns the length of that string"""

def test_return_length_of_string():
    assert count_words('im learning tdd') == 3

"""if given a string including numbers
return the length of the string not including numbers"""

def test_return_length_of_string_without_numbers():
    assert count_words('hi! im 30 years old') == 4

