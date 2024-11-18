from text_to_cost import *

if __name__ == '__main__':
    # just a list of some texts to calculate the cost of it
    texts = ['Привет, как дела?!', 'Hello, I am greeting you!',
             'Do you speak Guarani?', 'Go, go, go',
             'Ananas', 'Безделье - это игрушка дьявола, есть жи']

    # calculate one by one
    for text in texts:
        print(text)
        # fist of all, roubles - russian version
        text_rus_cost = TextToCost(text, RusCurrency())
        text_rus_cost.calculate_cost(RoubleCostCalculator())
        text_rus_cost.output_cost(RusCostConsoleOutput())

        # next, dollars - the USA version
        text_usa_cost = TextToCost(text, DollarCurrency())
        text_usa_cost.calculate_cost(DollarCostCalculator())
        text_usa_cost.output_cost(UsaCostConsoleOutput())

        print()
        del text_rus_cost
        del text_usa_cost

    pass