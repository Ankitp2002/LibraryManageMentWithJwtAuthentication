from sqlalchemy_db import *

def booklist():

    book_info = Session.query(Book)
    book_data = [{"bookId" : data.bookId , "bookName" : data.bookName,"bookAuthor" : data.bookAuthor,"bookPrice" : data.bookPrice , "typeName":data.book_type_Name,"donorId" : data.donorId , "libraryName" : data.libName } for data in book_info]

    # Session.rollback()
    time.sleep(1)

    return book_data