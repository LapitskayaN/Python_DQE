"""
Description Task 10
Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:
1.Different types of records require different data tables
2.New record creates new row in data table
3.Implement “no duplicate” check.
"""
import datetime
import sys
import re
import os
from Module_4_Functions_for_Module6 import normalizing_text
from Module_7_CSV import *
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from Module_10_DB_connection import DBConnection


def current_date():
    return datetime.datetime.now().strftime("%d/%m/%y %I:%M")

def write_from_file(target_of_writing="News_final.txt"):
    db = DBConnection()
    file_path = ''
    file_name = ''
    text_from_file = ''
    file_path_correct = ''
    while file_path_correct == '':
        type_folder = input(f"""Choose folder for file:-\n1 - Default folder, \n2 - Choose folder \n3 - EXIT from App
              Your choice: """)
        if type_folder == '1':
            file_path = './'
            file_name = 'News_add.txt'
            curr_dir = Path(__file__).parent
            file_path = curr_dir.joinpath(file_name)
            try:
                file = open(file_path, 'r').read()
                file_path_correct = 'yes'
            except:
                print("No such file! Try more")
        elif type_folder == '2':
            file_path_input = input(r"Enter path to file (in format D:\) ")
            file_name_input = input('Enter your file name\n')
            file_path = file_path_input + file_name_input
            try:
                file = open(file_path, 'r').read()
                file_path_correct = 'yes'
            except:
                print("Not correct file path! Try more")
        elif type_folder == '3':
            sys.exit()
        else:
            print("Incorrect choice for type_folder! Try more")
    while text_from_file == '':
        need_parsing = input(f"""Is text need parsing: - \n1 - No, \n2 - Yes  \n    Your choice: """)
        if need_parsing == '1':
            text_from_file = re.split("\\n\\n", file)
            with open(target_of_writing, "a") as file:
                for i in text_from_file:
                    file.write('\n\n' + i)
            os.remove(file_path)
            print("Text was added to News feed")
        elif need_parsing == '2':
            text_from_file = re.split("\\n", file)
            count_parsed = 0
            count_not_parsed = 0
            for element in text_from_file:
                parsed_list = element.split('---')
                if parsed_list != ['']:
                    post_code = parsed_list[0]
                    if post_code == '1':
                        text = normalizing_text(parsed_list[1])
                        city = parsed_list[2]
                        post_date = current_date()
                        q = NewsFeed().format_text('News', text, city)
                        db.insertNews(post_code, text, city, post_date)
                        count_parsed = count_parsed + 1;
                    elif post_code == '2':
                        text_private_add = normalizing_text(parsed_list[1])
                        end_date = parsed_list[2]
                        q = NewsFeed().format_text('PrivateAd', text_private_add, end_date)
                        db.insertPrivateAd(post_code, text_private_add, end_date)
                        count_parsed = count_parsed + 1;
                    elif post_code == '3':
                        currency_type = normalizing_text(parsed_list[1])
                        ex_rate = parsed_list[2]
                        q = NewsFeed().format_text('Finance', currency_type, ex_rate)
                        db.insertFinance(post_code, currency_type, ex_rate)
                        count_parsed = count_parsed + 1;
                    else:
                        q = ''
                        with open('rows_not_parsed.txt', "a") as file:
                            file.write(str(parsed_list))
                        count_not_parsed = count_not_parsed + 1;
                    with open(target_of_writing, "a") as file:
                        for i in q:
                            file.write(i)
            with open(target_of_writing, "a") as file:
                file.write('\nrows was/were  parsed ')
                file.write(str(count_parsed))
            with open( 'rows_not_parsed.txt', "a") as file:
                file.write('\nrows was/were not parsed ')
                file.write(str(count_not_parsed))
            os.remove(file_path)
            print("Parsing list was added to News feed")
        else:
            print("Incorrect choice for need_parsing! Try more")
        db.closeCursor()
        file.close()


class NewsFeed:
    def input_text(self):
        in_text = normalizing_text(input("Enter text of news_feed: "))
        return in_text

    def format_text(self, title, text_news_feed, text_additional):
        text_format = f'\n\n{title} --------------\n'
        text_format += text_news_feed + '\n' + text_additional + '\n'
        return text_format

    def conformation_adding(self):
        confirmation = input("Are you sure that you want to add the news? (y / n) ")
        return confirmation

    def write_to_file(self, publ, filename="News_final.txt"):
        with open(filename, "a") as NewsFeed_file:
            NewsFeed_file.write(publ)


class News(NewsFeed):
    def input_city(self):
        city = normalizing_text(input('Enter city of news: '))
        return city

    def publ_news(self):
        text_news_add = current_date() + ', ' + self.input_city()
        title = "News"
        publ_news = self.format_text(title, self.input_text(), text_news_add)
        if self.conformation_adding() == "y":
            self.write_to_file(publ_news)
            print("News was successfully added to news feed!\n")


class PrivateAd(NewsFeed):
    def input_exp_date(self):
        year = int(input("Enter year of expiration date:\n year: "))
        month = int(input("Enter month of expiration date:\nmonth: "))
        day = int(input("Enter day of expiration date:\nday: "))
        expiration_date = datetime.date(year, month, day)
        return expiration_date

    def publ_private_ad(self):
        title = "Private Ad"
        expiration_date = self.input_exp_date()
        len_days = expiration_date - datetime.date.today()
        text_private_ad_add = "Actual until:" + str(expiration_date) + '; ' + str(len_days) + ' left '
        publ_private_ad = self.format_text(title, self.input_text(), text_private_ad_add)
        if self.conformation_adding() == "y":
            self.write_to_file(publ_private_ad)
            print("Private Ad was successfully added to news feed!\n")


class Finance(NewsFeed):
    def input_currency(self):
        currency = ""
        while currency == '':
            choice_currency = input("Choose currency USD(1), EUR(2), RUR(3): ")
            if choice_currency == '1':
                currency = "USD"
            elif choice_currency == '2':
                currency = "EUR"
            elif choice_currency == '3':
                currency = "RUR"
            else:
                print("Incorrect currency choice! Try more")
        return currency

    def input_ex_rate(self):
        ex_rate = -1
        while ex_rate < 0:
            try:
                ex_rate = float(input("Add currency exchange rate: "))
            except ValueError:
                print("Incorrect currency exchange rate! Try more")
        return ex_rate

    def finance_deal_type(self):
        currency_type = ""
        while currency_type == '':
            finance_deal_type = input("Choose finance deal_type  1 - SELLING, 2 - BUYING, 4 - EXIT from App : ")
            if finance_deal_type == '1':
                currency_type = "SELLING"
            elif finance_deal_type == '2':
                currency_type = "BUYING"
            elif choose_type == '3':
                sys.exit()
            else:
                print("Incorrect currency choice! Try more")
        return currency_type

    def publ_finance(self):
        title = "Finance"
        text_finance_add = "Currency Ex rate " + self.input_currency() + " on the date: " + current_date() + \
                           ' is ' + str(self.input_ex_rate())
        publ_finance = self.format_text(title, self.finance_deal_type(), text_finance_add)
        if self.conformation_adding() == "y":
            self.write_to_file(publ_finance)
            print("Finance news was successfully added to news feed!\n")


class FileJson:
    @staticmethod
    def fileReadJSON(import_file_path = './News_add.json'):
        curr_dir = Path(__file__).parent
        file_path = curr_dir.joinpath(import_file_path)
        file_json = json.load(open(file_path))
        return file_json

    @staticmethod
    def fileWriteJson(output_file_path='../News_final.txt', text=''):
        f = open(output_file_path, 'a')
        f.write(text)
        f.close()
        return output_file_path

    def parseFileJson(self, src_text):
        db = DBConnection()
        for element in range(len(src_text)):
            json_dict = src_text[element]
            post_code = json_dict["post_code"]
            if post_code == '1':
                text = json_dict["post_text"]
                city = json_dict["post_city"]
                p = NewsFeed().format_text('News', text, city)
                post_date = current_date()
                db.insertNews(post_code, text, city, post_date)
            elif post_code == '2':
                text_private_add = json_dict["post_text"]
                end_date = json_dict["end_date"]
                p = NewsFeed().format_text('Private Ad', text_private_add, end_date)
                db.insertPrivateAd(post_code, text_private_add, end_date)
            elif post_code == '3':
                currency_type = json_dict["post_text"]
                ex_rate = json_dict["ex_rate"]
                p = NewsFeed().format_text('Finance', currency_type, ex_rate)
                post_date = current_date()
                db.insertFinance(post_code, currency_type, ex_rate)
            else:
                p = NewsFeed().format_text('', '', '')
            self.fileWriteJson('News_final.txt', p)
        db.closeCursor()


class FileXml:
    pass

    @staticmethod
    def fileReadXml(import_file_path='./News_add.xml'):
        curr_dir = Path(__file__).parent
        file_path = curr_dir.joinpath(import_file_path)
        xml_file = ET.parse(file_path)
        root = xml_file.getroot()
        return root

    @staticmethod
    def fileWriteTxt(outputfilepath='../result.txt', text=''):
        f = open(outputfilepath, 'a')
        f.write(text)
        f.close()
        return outputfilepath

    @staticmethod
    def parseFileXml(xml_root):
        # xml_root = FileXml.fileReadXml()
        xml_dict = {}
        list_common = []
        db = DBConnection()
        for post in xml_root:
            for element in post:
                xml_dict[element.tag] = element.text
            list_common.append(xml_dict)
            xml_dict = {}
        for some_dict in range(len(list_common)):
            current_dict = list_common[some_dict]
            post_code = current_dict["post_code"]
            if post_code == '1':
                text = current_dict["post_text"]
                city = current_dict["post_city"]
                post = NewsFeed().format_text('News', text, city)
                post_date = current_date()
                db.insertNews(post_code, text, city, post_date)
            elif post_code == '2':
                text_private_add = current_dict["post_text"]
                end_date = current_dict["end_date"]
                post = NewsFeed().format_text('Private Ad', text_private_add, end_date)
                db.insertPrivateAd(post_code, text_private_add, end_date)
            elif post_code == '3':
                currency_type = current_dict["post_text"]
                ex_rate = current_dict["ex_rate"]
                post = NewsFeed().format_text('Finance', currency_type, ex_rate)
                post_date = current_date()
                values = f"{post_code}, 'Finance', \"{currency_type}\", '{ex_rate}'"
                db.insert('Finance', values)
                db.insertFinance(post_code, currency_type, ex_rate)
            else:
                post = NewsFeed().format_text('', '', '')
            '''self.fileWriteJson('News_final.txt', p)'''
            FileXml.fileWriteTxt('News_final.txt', post)
        db.closeCursor()



def start():
    DBConnection().createTableNews()
    DBConnection().createTablePrivateAd()
    DBConnection().createTableFinance()
    while True:
        choose_input = input(f"""Choose input type for NewsFeed: - \n1 - Input, \n2 - From file txt, \n3 - From file JSON,
4 - From file XML,  \n5 - EXIT from App , \nYour choice: """)
        if choose_input == '1':
            choose_type = input(f"""Enter type news you want to add - \n1 - News, \n2 - PrivateAd, \n3 - Exchange_rate
4 - EXIT from App \n    Your choice: """)
            if choose_type == '1':
                News().publ_news()
            elif choose_type == '2':
                PrivateAd().publ_private_ad()
            elif choose_type == '3':
                Finance().publ_finance()
            elif choose_type == '4':
                sys.exit()
            if choose_type == '1' or  choose_type == '2' or  choose_type == '3':
                createCSV()
        elif choose_input == '2':
            write_from_file()
            createCSV()
        elif choose_input == '3':
            file_json = FileJson()
            file_json_read = file_json.fileReadJSON()
            file_json.parseFileJson(file_json_read)
            print("Json file was added to News feed")
            createCSV()
        elif choose_input == '4':
            file_xml_read = FileXml.fileReadXml()
            FileXml.parseFileXml(file_xml_read)
            print("XLM file was added to News feed")
            createCSV()
        elif choose_input == '5':
            sys.exit()
        else:
            print("Incorrect choice! Try more")


start()



