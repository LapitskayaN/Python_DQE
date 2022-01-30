import random as r # Module is imported in order to use randint and choice for random generation
import string # Module is imported in order to get lowercase letters using proper method
import re # Module for usage of regular expressions
'''
Сreate a list of random number of dicts (from 2 to 10)
dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
'''
dict_list = [] # Initialization of list
letters = string.ascii_lowercase    # Method returns lowercase letters
for i in range(r.randint(2, 10)):   # Loop is used in order to fill list with random number of dictionaries
    '''
    Generator is used in order to create dictionary.
    r.choice(letters) is responsible for key generation, r.randint(0, 100) - for value generation.
    Number of key: value pairs inside dictionary is variable and determined by r.randint(2, 10)
    '''
    random_dict = {r.choice(letters): r.randint(0, 100) for i in range(r.randint(2, 10))}
    '''Generated dictionary is added into list'''
    dict_list.append(random_dict)
print(dict_list) # Result output
