'''
Check if the string parsing works as expected
'''
from string_parser.string_parser import StringParser

parser = StringParser('hi hi hi hello hello hey hey hey hey')
count_words = parser.count_words()
most_frequent_word = parser.get_most_frequent_word()

def test_count_words():
    '''
    Checks if the returned dictionary contains valid word counts
    '''
    assert count_words == {'hello': 2, 'hey': 4, 'hi': 3}

def test_most_frequent_word():
    '''
    Check if the returned most frequent word is the correct one
    '''
    assert most_frequent_word == 'hey'
