import pytest

pytest.string_with_spaces = 'Variables may subsequently be rebound at any time to any object'
pytest.string_with_comas_dots = 'It has list comprehensions, and dictionaries. Sets, and generator expressions'
pytest.string_with_dashes = 'Python is a high-level, general-purpose programming language which is beginner-oriented'
pytest.string_parentheses_new_line = ("Python's development is conducted largely through the Python Enhancement" 
                                    "\nProposal (PEP) process, the primary mechanism for proposing major features")

pytest.string_with_spaces_parsing_result = {'Variables': 1, 'may': 1, 'subsequently': 1, 'be': 1,
                                            'rebound': 1, 'at': 1, 'any': 2, 'time': 1, 'to': 1, 'object': 1}
pytest.string_with_comas_dots_parsing_result = {'It': 1, 'has': 1, 'list': 1, 'comprehensions': 1, 'and': 2,
                                                'dictionaries': 1, 'Sets': 1, 'generator': 1, 'expressions': 1}
pytest.string_with_dashes_parsing_result = {'Python': 1, 'is': 2, 'a': 1, 'high-level': 1, 'general-purpose': 1,
                                            'programming': 1, 'language': 1, 'which': 1, 'beginner-oriented': 1}
pytest.string_parentheses_new_line_parsing_result =  {"Python's": 1, 'development': 1, 'is': 1,
                                                            'conducted': 1, 'largely': 1, 'through': 1,
                                                            'the': 2, 'Python': 1, 'Enhancement': 1,
                                                            'Proposal': 1, 'PEP': 1, 'process': 1,
                                                            'primary': 1, 'mechanism': 1, 'for': 1,
                                                            'proposing': 1, 'major': 1, 'features': 1}