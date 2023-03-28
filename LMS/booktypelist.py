from sqlalchemy_db import *

def booktypelist():

    book_type_info = Session.query(Book_Type)
    book_type_data = [{"bookTypeId": data.typeId, "bookTypeName": data.typeName} for data in book_type_info]

    # Session.rollback()
    time.sleep(1)

    return book_type_data