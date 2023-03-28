# from sqlalchemy_db import *

def new_donner(donner_name , library_id ):

    donner_id = Session.query(Donner.donner_id).order_by(desc(Donner.donner_id)).first()[0]

    donner_add = Donner(donner_id=donner_id + 1, name=donner_name, Contact=9825, library_id=library_id)
    Session.add(donner_add)
    Session.commit()
