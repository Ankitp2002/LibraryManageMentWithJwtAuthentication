from sqlalchemy_db import *

def create_new_type(book_type):

    type_add = Book_Type(typeName=book_type)

    Session.add(type_add)
    Session.commit()

    type_data = Session.query(Book_Type)
    tota_type = [(data.typeName,data.typeId) for data in type_data]

    return {"typeData" : tota_type}
