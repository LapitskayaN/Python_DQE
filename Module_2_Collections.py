# Module is imported in order to use randint and choice for random generation
import random as r
# Module is imported in order to get lowercase letters using proper method
import string
'''
TASK1
create a list of random number of dicts (from 2 to 10)
dicts random numbers of keys should be letter,
dicts values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
'''
# Initialization of list
dict_list = []
# Method returns lowercase letters
letters = string.ascii_lowercase
# number of created dictionary's returns a random number between the given range 2 and 10
dict_number = r.randint(2, 10)
# Loop is used in order to fill list with random number of dictionaries
for i in range(dict_number):
    '''
    Generator is used in order to create dictionary.
    r.choice(letters) is responsible for key generation, r.randint(0, 100) - for value generation.
    Number of key: value pairs inside dictionary is variable and determined by dict_number
    '''
    random_dict = {r.choice(letters): r.randint(0, 100) for j in range(dict_number)}
    # generated dictionary is added into list with method 'append'
    dict_list.append(random_dict)
# Result output
print('\nTask1\n List with created dicts "dict_list:"', dict_list)

'''
TASK2 
get previously generated list of dicts and create one common dict:
if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}'''

# create new result dict result_dict
result_dict = {}
# create new dict with repeated letters (keys) and number of dict with max value (value)
repeated_letters = {}
# go through the dicts in list and add to result_dict unique keys and their values
# if key is already in result_dict for this key compare the current value with the value in result_dict
# if condition is true give the max value for this key in result_dict
# and define in what dict is this key and add to the dictionary 'repeated_letters' pair key-dict number
# at first, we will find dict with all letters from dict_list (keys) and max values (value)'
for i in dict_list:
    # items() returns a list containing a tuple for each key value pair
    for key, values in i.items():
        # print(key, values in i.items())
        # if letter is unique in dict_list
        if key not in result_dict:
            # get() returns the value of the specified key
            result_dict[key] = i.get(key)
        # if letter is NOT unique in dict_list
        else:
            # if condition is true give the max value for this key in result_dict
            if i[key] > result_dict[key]:
                result_dict[key] = i[key]
                # fill dict 'repeated_letters' with repeated_letters and № of dict with max value
                # we add 1 because the index of first dict is 0
                repeated_letters[key] = dict_list.index(i) + 1
                # print(result_dict, repeated_letters)
            else:
                n = key
                m = result_dict[key]
                # print(n,m)
                for j in dict_list:
                    for k, v in j.items():
                        if k == n and v == m:
                            repeated_letters[key] = dict_list.index(j) + 1
                            # print(result_dict, repeated_letters)

print('\nTask2\n dict with all keys and max values "result_dict":', result_dict)
print(' dict with repeated letters and number of dict with max value (value) "repeated_letters"', repeated_letters)

# transform result_dict checking if key from the result_dict is in the dict "repeated_letters"
for key in list(result_dict):
    if key in repeated_letters:
        # pop() method removes the element with the specified key
        result_dict[key + f'_{repeated_letters[key]}'] = result_dict.pop(key)
print('\nFINAL dict - result_dict :', result_dict)
