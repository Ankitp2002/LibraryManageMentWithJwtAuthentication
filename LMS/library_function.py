from sqlalchemy_db import *

def library_new_create(library_name):
    lib_last_id = Session.query(Library.libId).order_by(desc(Library.libId)).first()[0] + 1

    add_lib = Library(libraryName=library_name)

    Session.add(add_lib)

    Session.commit()

    return "Suceessfully Add Library"
