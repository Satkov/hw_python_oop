import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, some_record):
        self.records.append(some_record)

    def get_today_stats(self):
        date_today = dt.date.today()
        values_for_today = 0

        for record in self.records:
            if record.date == date_today:
                values_for_today += record.amount

        return values_for_today

    def get_week_stats(self):
        date_today = dt.date.today()
        delta_7_days = dt.timedelta(days=7)
        day_week_ago = date_today - delta_7_days
        values_for_week = 0

        for record in self.records:
            if day_week_ago < record.date <= date_today:
                values_for_week += record.amount

        return values_for_week

    def get_today_remained(self):

        something_spent_today = self.get_today_stats()
        remaining_something = self.limit - something_spent_today
        return remaining_something


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CashCalculator(Calculator):
    USD_RATE = 77.23
    EURO_RATE = 91.11
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        remaining_cash = self.get_today_remained()
        currency_list = {
            'usd': [self.USD_RATE, 'USD'], 'eur': [self.EURO_RATE, 'Euro'],
            'rub': [self.RUB_RATE, 'руб']
            }

        if remaining_cash == 0:
            return 'Денег нет, держись'

        currency_conv = round(remaining_cash / currency_list[currency][0], 2)
        
        minus_currency_conv = abs(round(remaining_cash / currency_list[currency][0], 2))

        currency_name = currency_list[currency][1]

        if remaining_cash > 0:
            return (f'На сегодня осталось'
                    f' {currency_conv}'
                    f' {currency_name}')

        if remaining_cash < 0:
            return (f'Денег нет, держись: твой долг - '
                    f'{minus_currency_conv}'
                    f' {currency_name}')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        remaining_something = self.get_today_remained()

        if remaining_something > 0:
            return (f'Сегодня можно съесть что-нибудь ещё,'
                    f' но с общей калорийностью не более'
                    f' {remaining_something} кКал')

        if remaining_something < 0:
            return 'Хватит есть!'
