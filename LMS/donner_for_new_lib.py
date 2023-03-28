from sqlalchemy_db import *

def new_donner_lib(donner_name , library_name ):

    donner_id = Session.query(Donner.donner_id).order_by(desc(Donner.donner_id)).first()[0]

    library_id = Session.query(Library.id).order_by(desc(Library.id)).first()[0]

    donner_add = Donner(donner_id=donner_id + 1, name=donner_name, Contact=9825, library_id=library_id + 1)

    library_add = Library(library_name=library_name)

    Session.add_all([library_add ,donner_add])

    Session.commit()






