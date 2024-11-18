class ICurrencyType:
    pass

class RusCurrency(ICurrencyType):
    roubles : int
    kopecks : int
    # from roubles to kopecks and vise versa
    @staticmethod
    def rub_to_kop(rub : float):
        return float(rub * 100)
    @staticmethod
    def kop_to_rub(kop : int):
        return float(kop / 100)

class DollarCurrency(ICurrencyType):
    dollars : int
    cents : int
    # from dollars to cents and vise versa
    @staticmethod
    def dollar_to_cent(dollar : float):
        return float(dollar * 100)
    @staticmethod
    def cent_to_dollar(cents : int):
        return float(cents / 100)

