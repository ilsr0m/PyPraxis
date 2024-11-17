from enum import Enum
from abc import ABC, abstractmethod

# Abstract class IBmiOutput provides different output ways
class IBmiOutput:
    def __init__(self):
        pass
    # abstract method for implementing different output ways
    @abstractmethod
    def output_estimate(self, bmi_estimate : Enum):
        pass

# Derived class of IBmiOutput implementing console output way to show BMI estimates
class BmiConsoleOutput(IBmiOutput):
    # Console output way method
    def output_estimate(self, bmi_estimate : Enum):
        if bmi_estimate is  BmiType.UNDERWEIGHT:
            print("Недостаточная масса")
        elif bmi_estimate is BmiType.OVERWEIGHT:
            print("Избыточная масса")
        else: print("Оптимальная масса")

# Enum type keeps bmi estimate IDs
class BmiType(Enum):
    NORMAL_WEIGHT   = 0
    UNDERWEIGHT     = 1
    OVERWEIGHT      = 2

# Bmi class implementing bmi formula and set estimates
# Weight in KGs
# Height in meters
class Bmi:
    def __init__(self, weight : float, height : float):
        self._height = height
        self._weight = weight
        self._bmi = self._weight / (self._height ** 2) # formula
        self._bmi_estimate = self.__estimate()

    # Private estimate method
    def __estimate(self):
        if self._bmi < 18.5:
            return BmiType.UNDERWEIGHT
        if self._bmi > 25:
            return BmiType.OVERWEIGHT
        return BmiType.NORMAL_WEIGHT

    # Output based on class IBMIOutput
    def output_estimate(self, bmi_output : IBmiOutput):
        bmi_output.output_estimate(self._bmi_estimate)
        pass

if __name__ == '__main__':
    weight = float(input())
    height = float(input())
    Bmi(weight, height).output_estimate(BmiConsoleOutput())

