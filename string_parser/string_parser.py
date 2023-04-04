'''
Contains methods for parsing a string of words
'''

class StringParser:
    '''
    Class for parsing a string
    '''
    def __init__(self, string_to_parse: str) -> None:
        '''
        Inits StringParser with string as an argument
        '''
        self.string_to_parse = string_to_parse

    def count_words(self) -> dict:
        '''
        Takes a string and returns a dictionary with words quantity
        '''

        words_list = []

        #Split string into words, solution #1
        # for i in self.string_to_parse:
        #     if i in [',', '.', '/', '(', ')']:
        #         pass
        #     else:
        #         words_list.append(i)
        # words_list = (''.join(words_list)).split()

        # Split string into words, solution #2
        # for i in self.string_to_parse:
        #     if i not in [',', '.', '/', '(', ')']:
        #         words_list.append(i)
        #
        # words_list = (''.join(words_list)).split()

        # Split string into words, solution #3
        # for i in self.string_to_parse:
        #     if i in [',', '.', '/', '(', ')']:
        #         continue
        #     else:
        #         words_list.append(i)
        #
        # words_list = (''.join(words_list)).split()

        # Split string into words, solution #4
        string_after_parsing = ''
        for i in self.string_to_parse:
            if i in [',', '.', '/', '(', ')']:
                continue
            else:
                string_after_parsing = string_after_parsing + i

        words_list = string_after_parsing.split()



        #Create a dictionary with words as a keys and their quantities as values
        word_quantity_dict = {}

        for i in words_list:
            word_quantity_dict[i] = words_list.count(i)

        return word_quantity_dict

    def get_most_frequent_word(self) -> str:
        '''
        Takes a string and returns the most frequent word
        '''
        word_quantity_dict = self.count_words()
        max_frequency = max(word_quantity_dict.values())

        for key, value in word_quantity_dict.items():
            if value == max_frequency:
                most_frequent_word = key

        return most_frequent_word
