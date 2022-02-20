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


# parent Class NewsFeed
class NewsFeed:
    def __init__(self):
        self.text = input("Enter text of publication: ")


# it was created class News. It depends on the parent class
class News(NewsFeed):
    #  create class News , adds attributes : city, text
    def __init__(self):
        super().__init__()  # calling parent class init features
        self.city = input("Enter city: ")
        self.date = datetime.datetime.now().strftime("%d/%m/%y %I:%M")

    def __str__(self):  # formatting class output

        return (
            f'\n---News -------------------'
            f'\n{self.text}'
            f'\n{self.city}, {self.date}'
        )


# created a class for private. It depends on the parent class
class PrivateAd(NewsFeed):
    # create class PrivateAd , adds attributes : city, text
    def __init__(self):
        super().__init__()  # calling parent class init features
        self.expiration_date = datetime.date((int(input("Enter ad last date:\nyear: "))), (int(input("month: "))),
                                             (int(input("day: "))))
        self.today_date = datetime.date.today()
        # len - number days that are left
        self.len = self.expiration_date - self.today_date

    def __str__(self):  # formatting class output

        return (
            f'\n---PrivateAd -------------------'
            f'\n{self.text}'
            f'\nActual until: {self.expiration_date:%d/%m/%Y}, {self.len.days} days left'
        )


# created a class for private ad with dependence on the parent class
class Finance(NewsFeed):
    def __init__(self):
        super().__init__()
        self.currency = input("Enter currency (USD, EUR, RUR): ")
        self.ex_rate = input("Add currency exchange rate: ")
        self.date = datetime.datetime.today().strftime("%d/%m/%Y")

    def __str__(self):  # formatting class output

        return (
            f'\n---Exchange_rate -------------------'
            f'\n{self.text}'
            f'\nCurrency {self.currency} on the date: {self.date}'
            f'\n1  {self.currency} =  {self.ex_rate} BYN '
        )


# create e a function list_news() with  condition about entered data
def list_news():
    # User select what data type he wants to add
    print("--- Welcome to news feed application! ---")
    news_type = input("Enter type news you want to add - "
                      "News(1), PrivateAd(2), Exchange_rate(3) or EXIT from App(4): ")
    while news_type != '4':
        post = ''
        if news_type == '1':
            post = News()
        elif news_type == '2':
            post = PrivateAd()
        elif news_type == '3':
            post = Finance()
            # output message in case if we don't choose correct Class
        else:
            input("Incorrect choice! Try more")
        with open('NewsFeed.txt', 'a') as News_Feed:  # append to file
            print(post, file=News_Feed)
        print("------------------------")
        news_type = input("Enter type news you want to add -"
                          "News(1), PrivateAd(2), Exchange_rate(3) or EXIT from App(4): ")


list_news()
