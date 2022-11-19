import datetime
import math

rates = {'THB': 1.61, 'TRY': 2.61, 'RUB': 1}


class Rec:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        try:
            if datetime.datetime.strptime(date, '%Y-%m-%d'):
                self.date = datetime.datetime.strptime(date, '%Y-%m-%d').date()

        except:
            self.date = datetime.date.today()

    def __repr__(self):
        return f"{self.amount} - {self.comment} - {self.date}"  # records выводился в виде объекта, repr позволил
        # выдать строковое представление


class Calc:

    def __init__(self, limit, date):
        self.limit = limit
        self.date = date
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stat(self):
        res = 0
        for record in self.records:
            if record.date == datetime.date.today():
                res += record.amount
        return res

    def last_sevendays_stat(self):
        sum = 0
        onlyseven = 0
        for record in self.records:
            if onlyseven < 7:
                onlyseven += 1
                sum += record.amount
            elif onlyseven >= 7:
                break
        return sum

    def curr_date_count(self):
        amount_summ_of_current_date = 0

        for record in self.records:
            if str(record.date) == str(self.date):
                amount_summ_of_current_date += record.amount

        return amount_summ_of_current_date


class CashCL(Calc):

    def __init__(self, currency, limit, date):
        super().__init__(limit, date)
        self.currency = currency

    def get_today_cash_remained(self):
        sum_for_limit = 0
        for record in self.records:
            if datetime.date.today() == record.date:
                sum_for_limit += record.amount

        if self.limit > sum_for_limit:
            for key, value in rates.items():
                if self.currency == key:
                    return f'На сегодня осталось {math.floor(self.limit - (sum_for_limit / value))} {key}'


class CaloriesCL(Calc):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        return str(f'Ваш лимит по калориям на сегодня - {self.limit - self.get_today_stat()} ккалл.')


user = CashCL('THB', 1000, '2022-11-15')
user.add_record(Rec(30, 'Заправка Лукоил', '2022-10-21'))
user.add_record(Rec(300, 'Поездака в Нижний Новгород', ''))
user.add_record(Rec(300, 'Поездака в Кисловодск', '2022-10-20'))
user.add_record(Rec(10, 'Покупка хлеба', '2022-10-19'))

print(user.get_today_stat())


