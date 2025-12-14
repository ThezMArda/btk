from utils.penalties import Penalty_strategy
from utils.log import Logger
from models.user import User
from models.Book import Book
class LendingServices:
    def __init__(self,penalty_strategy:Penalty_strategy):
        self.penalty_strategy=penalty_strategy
        self.logger = Logger()

    def lend(self,user:User  ,book:Book):
        if not book.is_available==True:
            self.logger.log("kitap mevcut değil")
        
        book.is_available=False
        self.logger(f"{user.user_name} kitabi aldi basligi da {book.book_name}")
    
    def return_book(self,book:Book,days_late:int):
        book.is_available =True
        penalty = self.penalty_strategy.calculate(days_late)
        self.logger.log(f"kitap iade edildi cezasi da {penalty}")
        return penalty