from services.lending import Book_service
from models.Book import Book
from models.user import User
from services.user_service import LendingServices
def run():
    bs = Book_service()
    ls = LendingServices()
book1=Book("sissoylu",1,"james")
book2=Book("asdasd",2,"james")
book3=Book("ruzgar",1,"james")
book4=Book("ruza",1,"james")

