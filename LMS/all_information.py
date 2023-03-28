# from sqlalchemy_db import *
#
# def information():
#
#     book_info = Session.query(Book)
#     book_data = [{"bookId" : data.bookId , "bookName" : data.bookName,"bookAuthor" : data.bookAuthor,"bookPrice" : data.bookPrice , "typeName":data.book_type_Name,"donorId" : data.donorId , "libraryName" : data.libName } for data in book_info]
#
#     Session.rollback()
#     time.sleep(2)
#
#     book_type_info = Session.query(Book_Type)
#     book_type_data = [{"bookTypeId" : data.typeId, "bookTypeName" : data.typeName} for data in book_type_info]
#
#     Session.rollback()
#     time.sleep(2)
#
#     #
#     # lib_info = Session.query(Library)
#     # lib_data = [{"libraryId " : data.libId, "libraryName " : data.libraryName } for data in lib_info]
#
#
#     # signup_info = Session.query(Signup)
#     # signup_data = [{"donorId " : data.id, "donorName " : data.name ,"donerContactNo. " : data.contact} for data in donner_info]
#
#     available_info = Session.query(available_book)
#     available_data = [{"bookId" : data.bookId , "bookName" : data.book_name,"bookAuthor" : data.bookAuthor,"bookPrice" : data.bookPrice , "typeName":data.typeName, "libraryName" : data.libName } for data in available_info]
#
#     Session.rollback()
#     time.sleep(2)
#
#     issue_info = Session.query(issue_book)
#     issue_data = [{ "issuerName" : data.issuer_name , "issuerContactNo" : data.issuer_contact , "bookName" : data.book_name , "bookId" : data.book_id ,"bookAuthor" : data.bookAuthor,"bookPrice" : data.bookPrice , "typeName":data.typeName} for data in issue_info]
#
#     Session.rollback()
#     time.sleep(2)
#
#     return (["bookTypeInformation : ",book_type_data],
#            ["book  Information : ",book_data],
#             ["availableBookInformation : ",available_data],["issueBookInformation :",issue_data])
#
