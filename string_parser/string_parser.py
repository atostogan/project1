'''
Contains methods for parsing a string of words
'''

class StringParser:
    '''
    Class for parsing a string
    '''
    def __init__(self, str1: str) -> None:
        '''
        Inits StringParser with string as an argument
        '''
        self.str1 = str1

    def count_words(self) -> dict:
        '''
        Takes a string and returns a dictionary with words quantity
        '''
        words = self.str1.split()
        words_quantity = {}

        for i in words:
            words_quantity[i] = words.count(i)

        return words_quantity

    def get_most_frequent_word(self) -> str:
        '''
        Takes a string and returns the most frequent word
        '''
        words_quantity = self.count_words()
        max_value = max(words_quantity.values())

        for key, value in words_quantity.items():
            if value == max_value:
                max_key = key

        return max_key
