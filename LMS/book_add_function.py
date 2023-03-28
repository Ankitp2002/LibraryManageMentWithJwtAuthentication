import time

from sqlalchemy_db import *

def book_add_function(bookTypeName, book_name ,donor_id,bookAuthor,bookPrice):

    data_add = Book(bookName=book_name,book_type_Name=bookTypeName , donorId = donor_id , libName = "Ahmedabad" ,bookAuthor=bookAuthor,bookPrice=bookPrice)

    Session.add(data_add)

    available_id = Session.query(Book.bookId).order_by(desc(Book.bookId)).first()[0]

    available_add = available_book(bookId =available_id, book_name=book_name,typeName=bookTypeName , libName = "Ahmedabad" ,bookAuthor=bookAuthor,bookPrice=bookPrice)

    Session.add(available_add)

    Session.commit()

    Session.rollback()
    time.sleep(1)

    book_data  =  Session.query(Book)

    book_list = [(data.bookName,data.book_type_Name,data.bookId) for data in book_data]


    return {"bookData" : book_list}

# book_add_function(1,"parth",1)