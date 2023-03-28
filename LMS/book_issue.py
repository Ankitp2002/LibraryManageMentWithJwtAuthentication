from sqlalchemy_db import *

def book_issue(book_name,book_id,user_name,issuer_email,issuer_contact):

    book_available_data = Session.query(available_book).filter(available_book.book_name == book_name , available_book.bookId).first()

    if int(book_id) == book_available_data.bookId :

        issue_add = issue_book(issuer_name=user_name,issuer_contact=issuer_contact,issuer_email = issuer_email,book_name=book_name,book_id=int(book_id) , bookAuthor=book_available_data.bookAuthor,bookPrice=book_available_data.bookPrice,typeName=book_available_data.typeName)

        Session.add(issue_add)

        available_delete = Session.query (available_book).filter(available_book.bookId ==book_id).first()

        Session.delete(available_delete)

        Session.commit()
        # Session.rollback()
        time.sleep(1)
        return "book issue successfully"

    else:
        return "enter valid data...."

