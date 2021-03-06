# module for usage of regular expressions
import re

# copy text to variable
text = """homEwork:
tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Task 1 - calculate number of whitespace characters in this Text
# use regular expression to count whitespaces
# '\s' Matches Unicode whitespace characters (which includes [ \t\n\r\f\v])
white_spaces = re.findall(r'\s', text)
print(f'Task1\nCount of whitespaces in the text: {len(white_spaces)}')
# print('White_spaces:', white_spaces)

'''
# Check Task1 :
# S - Matches any character which is not a whitespace character
S = re.findall(r'\S', text)
# print('length', len(S), S)
check = len(text) - len(S)
print(len(white_spaces) == check)
'''

# Task 2 - normalize the text from letter cases point of view
# use regexp to multiple conditions of split
# [.]\s* - to find sentence after '.'
# \n -to find 'red' rows (after word "Homework:" in first sentence) [:]\n
normalize_text = ""
# I use regexp to multiple conditions of split
# print(re.split(r'([.]\s*|\n)', text))
for i in re.split(r'([.!?]\s*|\n)', text):
    normalize_text += i.capitalize()
print(f'\nTask 2 \n Text with normal word case is:\n{normalize_text}')


# Task 3 - create one more sentence with last words of each existing sentence
last_words = re.findall(r"\w+(?=[.!?])", normalize_text)
print(f'\nTask 3\n Last words of all sentence: {last_words}')
new_sentence = ' '.join(last_words)
added_sentence = new_sentence.capitalize()
print(f' Added sentence to our text: {added_sentence}')


# Task 4  - add new sentence to the end of the paragraph (after "end of this paragraph")
place_to_past = 'end of this paragraph'
# I create list of text splits
list_of_text = re.split(r'(^|[.!?]\s*)', normalize_text)
text_with_new_sentence = ""

# I create a loop that finds a paragraph which needs to add the sentence
# Use enumerate() to get a counter in a loop
for index, i in enumerate(list_of_text):
    if place_to_past in i.lower():
        list_of_text[index] = i + list_of_text[index+1][0] + ' ' + added_sentence + '. '
        list_of_text[index + 1] = list_of_text[index+1][1:]
        # fix 'Fix“iz”'
        text_with_new_sentence = ''.join(list_of_text).replace('x“', 'x “')
    else:
        text_with_new_sentence = ''.join(list_of_text).replace('x“', 'x “')
print(f'\nTask 4 \nThis is text with new sentence:\n{text_with_new_sentence}')


# Task 5 - fix“iZ” with correct “is”
final_text = text_with_new_sentence.replace(' iz ', ' is ')
print(f'\nTask 5 \nFinal text is: \n{final_text} ')


# Task 6
final_white_spaces = re.findall(r'\s', final_text)
print(f'Task6\nCount of whitespaces in final text: {len(final_white_spaces)}')
