import random as r
import string
import re
'''
Refactor homeworks from module 2 and 3 using functional approach with decomposition.
'''


# TASK 1
# Refactor homeworks from module 2
# function for creating list with dicts
def create_list_with_dicts(min_count=2, max_count=10, max_value=100):
    dict_list = []
    letters = string.ascii_lowercase
    dict_number = r.randint(min_count, max_count)
    for i in range(dict_number):
        random_dict = {r.choice(letters): r.randint(0,  max_value) for _ in range(dict_number)}
        dict_list.append(random_dict)
    print(f'List with created dicts "dict_list:" {dict_list}')
    return dict_list


# function for creating one dict based on list of dicts
def create_new_dict(dict_list):
    result_dict = {}
    repeated_letters = {}
    for i in dict_list:
        for key, values in i.items():
            if key not in result_dict:
                result_dict[key] = i.get(key)
            else:
                if i[key] > result_dict[key]:
                    result_dict[key] = i[key]
                    repeated_letters[key] = dict_list.index(i) + 1
                else:
                    for j in dict_list:
                        for k, v in j.items():
                            if k == key and v == result_dict[key]:
                                repeated_letters[key] = dict_list.index(j) + 1
    for key in list(result_dict):
        if key in repeated_letters:
            result_dict[key + f'_{repeated_letters[key]}'] = result_dict.pop(key)
    print('\nFINAL dict - result_dict :', result_dict)
    return result_dict


print('\nTASK1\n')
# create_list_with_dicts(min_count=2, max_count=10, max_value=100):
basic_list_with_dicts = create_list_with_dicts(2, 4, 50)
create_new_dict(basic_list_with_dicts)


# TASK 2
# Refactor homeworks from module 3
# function for counting whitespaces in text
def count_of_whitespaces_in_text(input_text=''):
    if input_text == '':
        input_text = input("Enter text: ")
    else:
        pass
    white_spaces = re.findall(r'\s', input_text)
    print(f'\nCount of whitespaces in the text: {len(white_spaces)}')
    return white_spaces


# function for text normalizing
def normalizing_text(text_for_normalizing=''):
    if text_for_normalizing == '':
        text_for_normalizing = input('Enter text for normalizing: ')
    else:
        pass
    normalize_text = ""
    for i in re.split(r'([.!?]\s*|\n)', str(text_for_normalizing)):
        normalize_text += i.capitalize()
    print(f'\nText with normal word case is:\n{normalize_text}')
    return normalize_text


# function for finding last words from all text
def find_last_words(normalize_text=''):
    if normalize_text == '':
        print("There is no string value for normalization")
    else:
        last_words = re.findall(r"\w+(?=[.!?])", normalize_text)
        print(f'\nLast words of all sentence: {last_words}')
        new_sentence = ' '.join(last_words)
        added_sentence = new_sentence.capitalize()
        print(f'Added sentence to our text: {added_sentence}')
        return added_sentence


# function adding new sentence
def add_sentence_to_text(text_for_input='', place_to_past_sentence='', added_sentence=''):
    if text_for_input == '':
        print("There is no text to add sentence")
    else:
        list_of_text = re.split(r'(^|[.!?]\s*)', text_for_input)
        text_with_new_sentence = ""
        for index, i in enumerate(list_of_text):
            if place_to_past_sentence in i.lower():
                list_of_text[index] = i + list_of_text[index + 1][0] + ' ' + added_sentence + '. '
                list_of_text[index + 1] = list_of_text[index + 1][1:]
                text_with_new_sentence = ''.join(list_of_text).replace('x“', 'x “')
            else:
                text_with_new_sentence = ''.join(list_of_text).replace('x“', 'x “')
        print(f'\nThis is text with new sentence:\n{text_with_new_sentence}')
        return text_with_new_sentence


# function for fixing "iz"
def fixing_iz(text_with_new_sentence):
    if text_with_new_sentence == '':
        print("Enter string value for fixing IZ")
    else:
        final_text = text_with_new_sentence.replace(' iz ', ' is ')
        print(f'\nFinal text is: \n{final_text} ')
        return final_text


text = """homEwork:
tHis iz your homeWork, copy these Text to variable! 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph!

	it iZ misspeLLing here? fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE! 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
place_to_past = 'end of this paragraph'


print('\n\nTASK2')
count_of_whitespaces_begin = count_of_whitespaces_in_text(str(text))
my_normalized_text = normalizing_text(str(text))
my_added_sentence = find_last_words(my_normalized_text)
my_text_with_new_sentence = add_sentence_to_text(my_normalized_text, str(place_to_past), my_added_sentence)
my_final_text = fixing_iz(my_text_with_new_sentence)
count_of_whitespaces_end = count_of_whitespaces_in_text(my_final_text)
