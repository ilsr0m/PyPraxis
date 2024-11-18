from abc import ABC, abstractmethod
from currency_type import *

class ICostCalculator:
    @abstractmethod
    def calculate(self, text : str, currency_type : ICurrencyType):
        return currency_type

# rouble calculation
class RoubleCostCalculator(ICostCalculator):
    def calculate(self, text : str, currency_type : ICurrencyType):
        rus_currency = RusCurrency()
        rus_currency.__dict__ = currency_type.__dict__
        try:
            raw_kopecks = len(text) * 60
            rus_currency.kopecks = raw_kopecks % 100
            rus_currency.roubles = int(rus_currency.kop_to_rub(raw_kopecks))
        except AttributeError as error:
            print(error)
        currency_type.__dict__ = rus_currency.__dict__
        return currency_type

# dollar calculation
class DollarCostCalculator(ICostCalculator):
    def calculate(self, text : str, currency_type : DollarCurrency):
        dollar_currency = DollarCurrency()
        dollar_currency.__dict__ = currency_type.__dict__
        try:
            raw_cents = len(text) * 2
            dollar_currency.cents = raw_cents % 100
            dollar_currency.dollars = int(dollar_currency.cent_to_dollar(raw_cents))
        except AttributeError as error:
            print(error)
        currency_type.__dict__ = dollar_currency.__dict__
        return currency_type
