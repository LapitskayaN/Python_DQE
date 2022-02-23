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


def current_date():
    return datetime.datetime.now().strftime("%d/%m/%y %I:%M")


class NewsFeed:
    def __init__(self, type_news, text, date):
        self.type_news = type_news
        self.text = text
        self.date = date

    def __str__(self):
        return f'{self.type_news} , {self.text} , {self.date}\n'

    def write_to_file(self):
        record = self.__str__()
        with open("NewsFeed.txt", "a") as NewsFeed_file:
            NewsFeed_file.write(record)


class News(NewsFeed):
    def __init__(self, text, city, type_news='News', date=current_date()):
        super().__init__(type_news, text, date)
        self.city = city

    def __str__(self):
        return (
            f'\n---{self.type_news} -------------------'
            f'\n{self.text}'
            f'\n{self.city}, {self.date}\n\n'
        )


class PrivateAd(NewsFeed):
    def __init__(self, text, date, len_days, type_news='PrivateAd'):
        self.date = date
        super().__init__(type_news, text, date)
        self.len_days = len_days

    def __str__(self):
        return (
            f'\n---{self.type_news}-------------------'
            f'\n{self.text}'
            f'\nActual until: {self.date:%d/%m/%Y} | {self.len_days}  left\n\n'
        )


class Finance(NewsFeed):
    def __init__(self,  currency, ex_rate, text='Exchange rate National Bank RB', type_news='Finance',
                 date=current_date()):
        super().__init__(type_news, text, date)
        self.currency = currency
        self.ex_rate = ex_rate

    def __str__(self):
        return (
            f'\n---{self.type_news} -------------------'
            f'\n{self.text}'
            f'\nCurrency {self.currency} on the date: {self.date}'
            f'\n1  {self.currency} =  {self.ex_rate} BYN \n\n'
        )


def post_news():
    text = ""
    city = ""
    while text == "" or city == "":
        print("--News-----\n"
              "Please, fill the following fields:")
        text = input("Enter text news: ")
        city = input("Enter city: ")
    confirmation = input("Are you sure that you want to add the news? (y / n) ")
    if confirmation == "y":
        news = News(text, city)
        news.write_to_file()
        print("News was successfully added to news feed!")


def post_private_ad():
    text = ""
    today_date = datetime.date.today()
    year = -1
    month = -1
    day = -1
    while text == "":
        print("--Private Ad-----\n"
              "Please, fill the following fields:")
        text = input("Enter text Private Ad: ")
    while year < 2022 or year > 2050:
        try:
            year = int(input("Enter year of expiration date:\n year: "))
        except ValueError:
            print("Incorrect input year! Try more")
    while month < 0 or month > 12:
        try:
            month = int(input("Enter month of expiration date:\nmonth: "))
        except ValueError:
            print("Incorrect input month! Try more")
    while day < 0 or day > 31:
        try:
            day = int(input("Enter day of expiration date:\nday: "))
        except ValueError:
            print("Incorrect input day! Try more")
    expiration_date = datetime.date(year, month, day)
    confirmation = input("Are you sure that you want to add the news? (y / n) ")
    len_days = expiration_date - today_date
    if confirmation == "y":
        private_ad = PrivateAd(text, expiration_date, len_days)
        private_ad.write_to_file()
        print("Private Ad was successfully added to news feed!")


def post_finance_news():
    currency = ""
    ex_rate = -1
    print("--Finance_ex_rate-----\n"
          "Please, fill the following fields:")
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
        finance_news = Finance(currency, ex_rate)
        finance_news.write_to_file()
        print("News was successfully added to news feed!")


def choice_news_type():
    print("--- Welcome to news feed application! ---")
    print("Enter type news you want to add - News(1), PrivateAd(2), FinanceNews(3) or EXIT from App(4): ")


choice_news_type()
choice = input('Your choice: ')
while choice != '4':
    post = ''
    if choice == '1':
        post_news()
    elif choice == '2':
        post_private_ad()
    elif choice == '3':
        post_finance_news()
    else:
        print("Incorrect choice! Try more")
    choice_news_type()
    choice = input('Your choice: ')

