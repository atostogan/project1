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

        list_of_punctuation_marks = [' ', ',', '.', '-']
        words = []
        punctuation_mark_count = 0

        #Check if list contains punctuation marks. If so, split string at punctuation mark
        for i in list_of_punctuation_marks:
            if self.str1.find(i) != -1:
                words = self.str1.split(i)
                punctuation_mark_count += 1

        #Check if punctuation marks were found. If not, try to split string at uppercase letters
        if punctuation_mark_count == 0:
            for i in range(len(self.str1)):
                if self.str1[i].isupper() and i != 0:
                    words.append(',' + self.str1[i])
                else:
                    words.append(self.str1[i])
            words = (''.join(words)).split(',')

        #Create a dictionary with words as a keys and their quantities as values
        words_quantity = {}

        for i in words:
            words_quantity[i] = words.count(i)

        return words_quantity

    def get_most_frequent_word(self) -> str:
        '''
        Takes a string and returns the most frequent word
        '''
        words_quantity = self.count_words()
        max_frequency = max(words_quantity.values())

        for key, value in words_quantity.items():
            if value == max_frequency:
                most_frequent_word = key

        return most_frequent_word
