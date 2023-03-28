from sqlalchemy_db import *

def bookissuelist():
    issue_info = Session.query(issue_book)
    issue_data = [{"issuerName": data.issuer_name, "issuerContactNo": data.issuer_contact, "bookName": data.book_name,
                   "bookId": data.book_id, "bookAuthor": data.bookAuthor, "bookPrice": data.bookPrice,
                   "typeName": data.typeName} for data in issue_info]

    # Session.rollback()
    time.sleep(1)

    return  issue_data