from dataclasses import dataclass
@dataclass
class Book:
    
    book_name :str
    book_id:int
    book_writer:str
    is_available:bool=True