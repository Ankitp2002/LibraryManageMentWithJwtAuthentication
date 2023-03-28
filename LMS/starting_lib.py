# from sqlalchemy_db import *

def start_lib(donner_name , library_name , book_type , book_name):

    donner_add = Donner( donner_id = 1 , name = donner_name , Contact = 9825 , library_id = 1 )
    Session.add(donner_add)

    lib_add = Library (library_name = library_name)
    Session.add(lib_add)

    book_type_add = Book_Type ( name = book_type, lib_id = 1 )
    Session.add(book_type_add)

    book_add = Book ( book_name = book_name ,book_type_id = 1  )
    Session.add(book_add)

    available_add = available_book ( book_name =book_name , book_id= 1 )
    Session.add(available_add)
    # Session.commit()

    return "sucessfull create starter kit"

# start_lib()