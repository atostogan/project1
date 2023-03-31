'''
Check if the string parsing works as expected
'''
import pytest
from string_parser.string_parser import StringParser

@pytest.mark.parametrize("test_input,expected", [(pytest.string_with_spaces,
                                                  {'Variables': 1, 'may': 1, 'subsequently': 1,
                                                   'be': 1, 'rebound': 1, 'at': 1,
                                                   'any': 2, 'time': 1, 'to': 1,
                                                   'object': 1}),
                                                 (pytest.string_with_comas_dots,
                                                  {'It': 1, 'has': 1, 'list': 1,
                                                   'comprehensions': 1, 'and': 2,
                                                   'dictionaries': 1, 'Sets': 1, 'generator': 1,
                                                   'expressions': 1}),
                                                 (pytest.string_with_dashes,
                                                  {'Python': 1, 'is': 2, 'a': 1,
                                                   'high-level': 1, 'general-purpose': 1,
                                                   'programming': 1, 'language': 1,
                                                   'which': 1, 'beginner-oriented': 1}),
                                                 (pytest.string_quote_parentheses_new_line,
                                                  {"Python's": 1, 'development': 1, 'is': 1,
                                                   'conducted': 1, 'largely': 1, 'through': 1,
                                                   'the': 2, 'Python': 1, 'Enhancement': 1,
                                                   'Proposal': 1, 'PEP': 1, 'process': 1,
                                                   'primary': 1, 'mechanism': 1, 'for': 1,
                                                   'proposing': 1, 'major': 1, 'features': 1})])

def test_count_words(test_input, expected):
    '''
    Checks if the returned dictionary contains valid word counts
    '''
    parser = StringParser(test_input)
    assert parser.count_words() == expected

@pytest.mark.parametrize("test_input,expected", [(pytest.string_with_spaces, 'any'),
                                                 (pytest.string_with_comas_dots, 'and'),
                                                 (pytest.string_with_dashes, 'is'),
                                                 (pytest.string_quote_parentheses_new_line, 'the')])
def test_most_frequent_word(test_input, expected):
    '''
    Check if the returned most frequent word is the correct one
    '''
    parser = StringParser(test_input)
    assert parser.get_most_frequent_word() == expected
