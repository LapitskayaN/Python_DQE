"""
Create a tool, which will do user generated news feed:
1.User select what data type he wants to add
2.Provide record type required data
3.Record is published on text file in special format

You need to implement:
1.News – text and city as input. Date is calculated during publishing.
2.Private ad – text and expiration date as input. Day left is calculated during publishing.
3.Your unique one with unique publish rules.

Each new record should be added to the end of file. Commit file in git for review.
"""

import datetime
import sys


def current_date():
    return datetime.datetime.now().strftime("%d/%m/%y %I:%M")


class ChooseTypeNews:
    def __init__(self):
        self.type_NewsFeed = input(f"""Enter type news you want to add - 
                      News(1), PrivateAd(2), Exchange_rate(3) or EXIT from App(4): """)


class NewsFeed:
    def __init__(self):
        self.date = current_date()
        self.text = input("Enter text of news feed: ")
        self.text_format = ''

    def write_to_file(self, filename="News2.txt"):
        with open(filename, "a") as NewsFeed_file:
            NewsFeed_file.write(self.text_format)


class News(NewsFeed):
    def __init__(self, title="News"):
        super().__init__()
        self.city = input('Enter city of news: ')
        self.title = title
        confirmation = input("Are you sure that you want to add the news? (y / n) ")
        if confirmation == "y":
            self.text_format = f"---{self.title}------------------" \
                               f"\n{self.text}" \
                               f"\n{self.date}\n\n"
            print("News was successfully added to news feed!\n")


class PrivateAd(NewsFeed):
    def __init__(self, title="PrivateAd"):
        super().__init__()
        self.title = title
        self.year = int(input("Enter year of expiration date:\n year: "))
        self.month = int(input("Enter month of expiration date:\nmonth: "))
        self.day = int(input("Enter day of expiration date:\nday: "))
        self.expiration_date = datetime.date(self.year, self.month, self.day)
        confirmation = input("Are you sure that you want to add the news? (y / n) ")
        self.len_days = self.expiration_date - datetime.date.today()
        if confirmation == "y":
            self.text_format = f"---{self.title}-------------------" \
                               f"\n{self.text}" \
                               f"\nActual until: {self.expiration_date:%d/%m/%Y}\n {self.len_days} left\n\n"
            print("Private Ad was successfully added to news feed!\n")


class Finance(NewsFeed):
    def __init__(self, title="Exchange_rate"):
        super().__init__()
        self.title = title
        currency = ""
        ex_rate = -1
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
        while ex_rate < 0:
            try:
                ex_rate = float(input("Add currency exchange rate: "))
            except ValueError:
                print("Incorrect currency choice! Try more")
        confirmation = input("Are you sure that you want to add the news? (y / n) ")
        if confirmation == "y":
            self.text_format = f'---{self.title}-------------------' \
                               f'\n{self.text}' \
                               f'\nCurrency {currency} on the date: {self.date}' \
                               f'\n1  {currency} =  {ex_rate} BYN \n\n'
            print("News was successfully added to news feed!\n")


while True:
    choose_type = ChooseTypeNews()
    if choose_type.type_NewsFeed == '1':
        News().write_to_file()
    elif choose_type.type_NewsFeed == '2':
        PrivateAd().write_to_file()
    elif choose_type.type_NewsFeed == '3':
        Finance().write_to_file()
    elif choose_type.type_NewsFeed == '4':
        sys.exit()
