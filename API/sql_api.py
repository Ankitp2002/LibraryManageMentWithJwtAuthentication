from sqlalchemy_db import Signup,Book
from sqlalchemy_db import Session as sa
import time

def all_db_data():
    try:
        queary = sa.query(Signup,Book)\
                       .select_from(Book)\
                       .join(Signup ,Signup.id == Book.donorId)

        result = queary.all()

        final = []

        for row in result:
            user = row[0]
            book = row[1]

            final.append({"donorName": user.name, "libraryName": book.libName,
                  "bookType": book.book_type_Name,
                 "bookName": book.bookName})

        sa.rollback()
        time.sleep(1)

        return final

    except :

        all_db_data()



