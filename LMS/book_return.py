from sqlalchemy_db import *

def book_return(book_name,book_id,email):

    book_issue_data = Session.query(issue_book).filter(issue_book.issuer_email == email , issue_book.book_id == book_id).first()

    available_add = available_book (bookId=book_id,book_name=book_name,bookAuthor=book_issue_data.bookAuthor,bookPrice = book_issue_data.bookPrice , typeName = book_issue_data.typeName)
    Session.add(available_add)

    issue_delete = Session.query(issue_book).filter(issue_book.book_id==book_id).first()
    Session.delete(issue_delete)

    Session.commit()
    # Session.rollback()
    time.sleep(1)
    return "book return successfully"



