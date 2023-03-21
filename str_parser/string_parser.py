class StringParser:
    def __init__(self, str1):
        self.str1 = str1

    def count_words(self):
        words = self.str1.split()
        words_quantity = {}

        for i in words:
            words_quantity[i] = words.count(i)

        return words_quantity

    def get_most_frequent_word(self):
        words_quantity = self.count_words()
        max_value = max(words_quantity.values())

        for key, value in words_quantity.items():
            if value == max_value:
                return key
