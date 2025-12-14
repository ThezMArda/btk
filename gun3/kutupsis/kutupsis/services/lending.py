from models.Book import Book
from utils.log import Logger

class Book_service:
    def __init__(self):
        self.books:list[Book]=[]
        self.logger = Logger()

    def add_book(self,book:Book):
        self.books.append(book)
        self.logger.log(f"Kitap eklendi kitabin başligi :{book.book_name}")
    
    def find_book(self,title:str) ->Book |None:
        return next((b for t in self.books if b.book_name==title),None)

    


