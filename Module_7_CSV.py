"""
Calculate number of words and letters from previous Homeworks 5/6 output test file.
Create two csv:
1.word-count (all words are preprocessed in lowercase)
2.letter, cout_all, count_uppercase, percentage (add header, spacecharacters are not included)
CSVs should be recreated each time new record added.
"""
import re
import csv
from pathlib import Path

file_name='News_final.txt'
file_csv1 = '../Python_DQE_Lapitskaya/task07_01.csv'
file_csv2 = '../Python_DQE_Lapitskaya/task07_02.csv'

def fileRead(file_name='News_final.txt'):
    curr_dir = Path(__file__).parent
    file_path = curr_dir.joinpath(file_name)
    file = open(file_path, 'r')
    src_text = file.read()
    file.close()
    return src_text


def list_of_words(text=fileRead()):
    temp_list_of_words = re.findall(r'\w+', text)
    list_of_words = [item for item in temp_list_of_words if item.isalpha()]
    return list_of_words


def list_of_letters(text=fileRead()):
    char_list = [char for char in text]
    return [item for item in char_list if item.isalpha()]


def list_of_lower_letters(text=fileRead()):
    char_list = [char for char in text.lower()]
    return [item for item in char_list if item.isalpha()]


def wordsInLower(list_of_words=list_of_words()):
    words_lower_list = []
    for word in list_of_words:
        words_lower = str(word).lower()
        words_lower_list.append(words_lower)
    return words_lower_list


def countElements(word_list=wordsInLower()):
    word_count_dict = {}
    for i in range(len(word_list)):
        word = word_list[i]
        if word in word_count_dict.keys():
            word_count_dict[word] = word_count_dict.get(word) + 1
        else:
            word_count_dict[word] = 1
    return word_count_dict


def upperLowerLettersDict(letters_dict=countElements(list_of_letters())):
    upper_dict = {}
    lower_dict = {}
    for key, value in letters_dict.items():
        if key.isupper():
            upper_dict[key] = value
        else:
            lower_dict[key] = value
    return upper_dict, lower_dict


def totalLettersCount(letters=list_of_letters()):
    return len(letters)


def csvFile1(count_words=None, wordsInLower = wordsInLower()):
    if count_words is None:
        count_words = countElements(wordsInLower)
    with open(file_csv1, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter='-')
        for key, value in count_words.items():
            writer.writerow([key, value])


def csvFile2(total=totalLettersCount(), upper=upperLowerLettersDict()[0],
                       count_all_letter=countElements(list_of_lower_letters())):
    with open(file_csv2, 'w', newline='') as csv_file:
        header = ['letter', 'count_all', 'count_uppercase', 'percentage']
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        for key, value in count_all_letter.items():
            percent = round(value / total * 100, 2)
            upper_count = upper.get(key.upper())
            if upper_count is None:
                upper_count = 0
            writer.writerow(
                {'letter': key, 'count_all': value, 'count_uppercase': upper_count, 'percentage': str(percent) + '%'})
            # print(key, value, upper_count, str(percent)+'%')

'''
print(list_of_words())
print(list_of_letters())
print(upperLowerLettersDict()[0])
print(upperLowerLettersDict()[1])
print(totalLettersCount())
'''

