from abc import ABC
class Sell(ABC):
    def __init__(self,price_per_meter,discountble,convertable, *args, **kwargs):
        self.price_per_meter =price_per_meter
        self.discountble=discountble
        self.convertable=convertable
        super().__init__(*args, **kwargs)

        def show_price(self):
            print(f"{self.price_per_meter}\t discount: {self.discountable}\t convert: {self.convertable} ")


class Rent(BaseClass):
    def __init__(self,initial_price,monthly_price,convertable,discountble, *args, **kwargs):
        self.initial_price=initial_price
        self.monthly_price=monthly_price
        self.convertable=convertable
        self.discountble=discountble
        super().__init__(*args, **kwargs)

