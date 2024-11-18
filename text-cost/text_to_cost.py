from cost_output import *
from cost_calculator import *

# Class "converts" text value into cost

# You can use many different currencies, implementing derived classes of
# ICurrencyType, ICostCalculator and ICostOutput and overriding its methods
class TextToCost:
    def __init__(self, text : str = '', currency : ICurrencyType = None):
        self.text = text
        self.currency = currency

    def calculate_cost(self, cost_calculator: ICostCalculator):
        if self.currency is None:
            print("Error: currency is None")
            return
        # Any derived class from ICostCalculator
        cost_calculator.calculate(self.text, self.currency)

    def output_cost(self, cost_output: ICostOutput):
        # Any derived class from ICostOutput
        cost_output.output(self.currency)
