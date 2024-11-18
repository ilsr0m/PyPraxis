from abc import ABC, abstractmethod
from currency_type import *

# Interface (abstract class) defines output method
# which can be overridden by many derived classes
class ICostOutput:
    @abstractmethod
    def output(self, currency_type : ICurrencyType):
        pass

# Russian output -> roubles, kopecks
class RusCostConsoleOutput(ICostOutput):
    def output(self, currency_type : ICurrencyType):
        rus_currency = RusCurrency()
        rus_currency.__dict__ = currency_type.__dict__
        try:
            print(f'{rus_currency.roubles} р. {rus_currency.kopecks} коп.')
        except AttributeError as error: # important
            print(error)

# American output -> dollars, cents
class UsaCostConsoleOutput(ICostOutput):
    def output(self, currency_type : ICurrencyType):
        dollar_currency = DollarCurrency()
        dollar_currency.__dict__ = currency_type.__dict__
        try:
            print(f'{dollar_currency.dollars}$ {dollar_currency.cents} cents')
        except AttributeError as error: # important
            print(error)
