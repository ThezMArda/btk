class Logger:
    _instance = None
    def __new__(cls)  :
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self,msg: str ):
        print("[LOG]",msg)
class PricingStrategy:
    def calculate(self, base:float) ->float:...

class NoDisc(PricingStrategy):
    def calculate(self, base: float) -> float:
        return base

class StudDisc(PricingStrategy):
    def calculate(self, base: float) -> float:
        return base*0.9

class BlackFriday(PricingStrategy):
    def calculate(self, base: float) -> float:
        return base*.5

class PaymentMethod:
    def pay(self, amount:float):...

class CcPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Kredi karti ile ödeme {amount}")
class PaypalPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paypal ile ödeme {amount}")


class PaymentFactory:
    @staticmethod
    def create(method:str)->PaymentMethod:
        if method== "kart":
            return CcPayment()
        if method == "paypal":
            return PaypalPayment()
        raise ValueError("desteklenmeyen ödeme yöntemi")

def process_order(price:float ,method :str , strategy : PricingStrategy ):
    log = Logger()

    final_price=strategy.calculate(price)
    log.log(f"Hesaplanan fiyatlarin : {final_price}")

    payment=PaymentFactory.create(method)
    payment.pay(final_price)
    log.log("ödeme tamamlandi")

process_order(100,"paypal",BlackFriday())
