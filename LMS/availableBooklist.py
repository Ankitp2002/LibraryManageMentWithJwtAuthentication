from sqlalchemy_db import *

def availableInfo():
    available_info = Session.query(available_book)
    available_data = [
        {"bookId": data.bookId, "bookName": data.book_name, "bookAuthor": data.bookAuthor, "bookPrice": data.bookPrice,
         "typeName": data.typeName, "libraryName": data.libName} for data in available_info]

    # Session.rollback()
    time.sleep(1)

    return  available_data

