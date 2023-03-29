'''
Check if the string parsing works as expected
'''
import pytest
from string_parser.string_parser import StringParser

@pytest.mark.parametrize("test_input,expected", [(pytest.string_with_spaces,
                                                  {'hello': 2, 'hey': 4, 'hi': 3}),
                                                 (pytest.string_with_comas,
                                                  {'hello': 2, 'hey': 4, 'hi': 3}),
                                                 (pytest.string_with_dots,
                                                  {'hello': 2, 'hey': 4, 'hi': 3}),
                                                 (pytest.string_with_dashes,
                                                  {'hello': 2, 'hey': 4, 'hi': 3}),
                                                 (pytest.string_with_camel_case,
                                                  {'Hello': 2, 'Hey': 4, 'Hi': 3})])
def test_count_words(test_input, expected):
    '''
    Checks if the returned dictionary contains valid word counts
    '''
    parser = StringParser(test_input)
    assert parser.count_words() == expected

@pytest.mark.parametrize("test_input,expected", [(pytest.string_with_spaces, 'hey'),
                                                 (pytest.string_with_comas, 'hey'),
                                                 (pytest.string_with_dots, 'hey'),
                                                 (pytest.string_with_dashes, 'hey'),
                                                 (pytest.string_with_camel_case, 'Hey')])
def test_most_frequent_word(test_input, expected):
    '''
    Check if the returned most frequent word is the correct one
    '''
    parser = StringParser(test_input)
    assert parser.get_most_frequent_word() == expected
