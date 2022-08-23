"""
Description
Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:
1.Different types of records require different data tables
2.New record creates new row in data table
3.Implement “no duplicate” check.
"""
import sqlite3


class DBConnection:
    def __init__(self, database_name='Module_10.db'):
        with sqlite3.connect(database_name) as self.connection:
            self.cur = self.connection.cursor()

    def createTableNews(self):
        self.cur.execute(
            'create table if not exists News (post_code integer, post_name text, post_text text, post_city text, post_date text)')

    def createTablePrivateAd(self):
        self.cur.execute(
            'create table if not exists PrivateAd (post_code integer, post_name text, post_text text, end_date text)')

    def createTableFinance(self):
        self.cur.execute(
            'create table if not exists Finance (post_code integer, post_name text, post_text text, ex_rate text)')

    def select(self, table, columns):
        return self.cur.execute(f'select {columns} from {table}').fetchall()

    def insert(self, table, values):
        self.cur.execute(f"insert into {table} values ({values})")
        print(f"Inserted into {table}")
        self.connection.commit()

    def checkNewsDuplicates(self, post_code, post_text, post_city):
        return self.cur.execute(f'select count(*) from News as N where N.post_code = {post_code} '
                                f'and N.post_text = \'{post_text}\' '
                                f'and N.post_city = \'{post_city}\'').fetchall()[0][0]

    def checkPrivateAdDuplicates(self, post_code, post_text, end_date):
        return self.cur.execute(f'select count(*) from PrivateAd where post_code = {post_code} '
                                f'and post_text = \'{post_text}\''
                                f'and end_date = \'{end_date}\'').fetchall()[0][0]

    def checkFinanceDuplicates(self, post_code, post_text, ex_rate):
        return self.cur.execute(f'select count(*) from Finance where post_code = {post_code} '
                                f'and post_text = \'{post_text}\' '
                                f'and ex_rate = \'{ex_rate}\'').fetchall()[0][0]

    def insertNews(self, post_code, post_text, post_city, post_date):
        print(self.checkNewsDuplicates(post_code, post_text, post_city))
        if self.checkNewsDuplicates(post_code, post_text, post_city) >= 1:
            print(f'Record {post_code}, {post_text}, {post_city} already exists')
        else:
            self.cur.execute(f"insert into News values ({post_code}, 'News', \'{post_text}\', \'{post_city}\', \'{post_date}\')")
            print(f"Inserted into News")
            self.connection.commit()

    def insertPrivateAd(self, post_code, post_text, end_date):
        if self.checkPrivateAdDuplicates(post_code, post_text, end_date) >= 1:
            print(f'Record {post_code}, {post_text}, {end_date} already exists')
        else:
            self.cur.execute(f"insert into PrivateAd values ({post_code}, 'PrivateAd', \'{post_text}\', \'{end_date}\')")
            print(f"Inserted into PrivateAd")
            self.connection.commit()

    def insertFinance(self, post_code, post_text, ex_rate):
        if self.checkFinanceDuplicates(post_code, post_text, ex_rate) >= 1:
            print(f'Record {post_code}, {post_text}, {ex_rate} already exists')
        else:
            self.cur.execute(
                f"insert into Finance values ({post_code}, 'Finance', \'{post_text}\', \'{ex_rate}\')")
            print(f"Inserted into Finance")
            self.connection.commit()

    def closeCursor(self):
        self.cur.close()


dbcon = DBConnection()
print(dbcon.select('News', '*'))
print(dbcon.select('PrivateAd', '*'))
print(dbcon.select('Finance', '*'))

