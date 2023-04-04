'''
Check if the string parsing works as expected
'''
import pytest
from string_parser.string_parser import StringParser

@pytest.mark.parametrize("test_input,expected", [(pytest.string_with_spaces,
                                                  pytest.string_with_spaces_parsing_result),
                                                 (pytest.string_with_comas_dots,
                                                  pytest.string_with_comas_dots_parsing_result),
                                                 (pytest.string_with_dashes,
                                                  pytest.string_with_dashes_parsing_result),
                                                 (pytest.string_parentheses_new_line,
                                                pytest.string_parentheses_new_line_parsing_result)])

def test_count_words(test_input, expected):
    '''
    Checks if the returned dictionary contains valid word counts
    '''
    parser = StringParser(test_input)
    assert parser.count_words() == expected

@pytest.mark.parametrize("test_input,expected", [(pytest.string_with_spaces, 'any'),
                                                 (pytest.string_with_comas_dots, 'and'),
                                                 (pytest.string_with_dashes, 'is'),
                                                 (pytest.string_parentheses_new_line, 'the')])
def test_most_frequent_word(test_input, expected):
    '''
    Check if the returned most frequent word is the correct one
    '''
    parser = StringParser(test_input)
    assert parser.get_most_frequent_word() == expected
