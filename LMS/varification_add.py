from sqlalchemy_library_system import *
from starting_lib import *
from create_donner import *
from book_add_function import *
from book_type_function import *

def new_library(donner_name , library_name , book_type , book_name):

    donner_available_data = Session.query(Donner)

    id_donner=[id_data.id for id_data in donner_available_data]

    if id_donner != []:

        total_donner = [(donner_data.name, donner_data.donner_id) for donner_data in donner_available_data]
        total_donner_name = [donner_data.name for donner_data in donner_available_data]
        donner_name = input("enter donner name")

        print("total donner", set(total_donner))

        if donner_name in total_donner_name:

            donner_id = int(input("enter your id :"))

            if (donner_name,donner_id) in total_donner:

                print("lib")

                library_available_data = Session.query(Library)

                total_library=[(library_data.library_name,library_data.id) for library_data in library_available_data]

                print("available library",total_library)

                library_name = input("enter library name :")
                library_id = int(input("enter library id :"))

                if (library_name,library_id) in total_library:
                    print("next to check type nd add")

                    book_available_type = Session.query(Book_Type)
                    total_book_type=[(type_data.name,type_data.id) for type_data in book_available_type]

                    print("book type and there id",total_book_type)

                    book_type = input("enter book type name :")
                    book_id = int(input("enter book id"))

                    if (book_type,book_id) in total_book_type:

                        print("book add")
                        return book_add_function(donner_id , library_id , book_type_id , book_name)

                    else:

                        print("new type create")
                        return create_new_type(donner_id , library_id , book_type)

                else:

                    print("new lib")
                    # ======================= donner id donner name
                    return library_new_create(donner_name,donner_id)

            else:

                print("new donner")
                return new_donner()

        else:

            print("new donner")
            # ==========================under prosse library naem ., library id donner name
            return new_donner()

    else:

        print("strating")
        return start_lib(donner_name , library_name , book_type , book_name)

