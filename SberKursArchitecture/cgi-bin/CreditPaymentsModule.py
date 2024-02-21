import sqlite3
import time
from datetime import date


class CreditPayments:

    def __init__(self):
        conn = sqlite3.connect("mydatabase.db")
        self.cursor = conn.cursor()

    def get_timestamp(self, x):
        date_arr = x.split(".")
        d = date(int(date_arr[1]), int(date_arr[0]), 1)
        unixtime = time.mktime(d.timetuple())
        return unixtime

    def getRestOfCredit(self, id, date):
        sql = 'select sum(summ) from payment where deal_id = ? and pdate <= ?'
        self.cursor.execute(sql, [(id), (self.get_timestamp(date))])
        payed = self.cursor.fetchone()[0]
        sum = self.getSummOfCredit(id)
        return sum - payed

    def getSummOfCredit(self, id):
        sql = 'select summ from credit where id = ?'
        self.cursor.execute(sql, [(id)])
        payed = self.cursor.fetchone()[0]
        return payed
