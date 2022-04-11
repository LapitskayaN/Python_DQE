"""
Expand previous Homework 5 with additional class, which allow to provide records by text file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
4.Apply case normalization functionality form Homework 3/4
"""
import datetime
import sys
import re
import os
from Module_4_Functions_for_Module6 import normalizing_text


def current_date():
    return datetime.datetime.now().strftime("%d/%m/%y %I:%M")


def choose_type_input():
    type_input = input(f"""Choose input type: - \n1 - Input, \n2 - From file, \n3 - EXIT from App \nYour choice: """)
    return type_input


def choose_type_news_feed():
    type_news_feed = input(f"""Enter type news you want to add - \n1 - News, \n2 - PrivateAd, \n3 - Exchange_rate or 
4 - EXIT from App \n    Your choice: """)
    return type_news_feed


def write_from_file(target_of_writing="News3.txt"):
    type_folder = input(f"""Folder for file: - \n1 - Default folder, \n2 - Choose folder   \n    Your choice: """)
    file_path = ''
    file_name = ''
    if type_folder == '1':
        file_path = f"""D:\DQE\Python\Python_DQE\DOP"""
        file_name = f"""News_add.txt"""
    elif type_folder == '2':
        file_path = input(r"Enter path to file (in format D:\) ")
        file_name = input('Enter your file name\n')
    file_path = os.path.join(file_path, file_name)
    file = open(file_path, 'r').read()
    text_from_file = re.split("\\n\\n", file)
    with open(target_of_writing, "a") as file:
        for i in text_from_file:
            file.write(i + '\n\n')
    os.remove(file_path)


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

    def write_to_file(self, publ, filename="News3.txt"):
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
            finance_deal_type = input("Choose finance deal_type SELLING(1), BUYING(2): ")
            if finance_deal_type == '1':
                currency_type = "SELLING"
            elif finance_deal_type == '2':
                currency_type = "BUYING"
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


while True:
    choose_input = choose_type_input()
    if choose_input == '1':
        choose_type = choose_type_news_feed()
        if choose_type == '1':
            News().publ_news()
        elif choose_type == '2':
            PrivateAd().publ_private_ad()
        elif choose_type == '3':
            Finance().publ_finance()
        elif choose_type == '4':
            sys.exit()
    if choose_input == '2':
        write_from_file()
    elif choose_input == '3':
        sys.exit()


