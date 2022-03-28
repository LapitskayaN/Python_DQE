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


def choose_type_news_feed():
    type_news_feed = input(f"""Enter type news you want to add - \n1 - News, \n2 - PrivateAd, \n3 - Exchange_rate or 
4 - EXIT from App \n    Your choice: """)
    return type_news_feed


class NewsFeed:
    def input_text(self):
        in_text = input("Enter text of news_feed: ")
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
        city = input('Enter city of news: ')
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
    choose_type = choose_type_news_feed()
    if choose_type == '1':
        News().publ_news()
    elif choose_type == '2':
        PrivateAd().publ_private_ad()
    elif choose_type == '3':
        Finance().publ_finance()
    elif choose_type == '4':
        sys.exit()
