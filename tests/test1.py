from str_parser.string_parser import StringParser

parser = StringParser('hi hi hi hello hello hey hey hey hey')

print('Number of words:', parser.count_words())
print('Most frequent word is:', parser.get_most_frequent_word())