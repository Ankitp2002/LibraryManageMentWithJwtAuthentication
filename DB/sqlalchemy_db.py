from sqlalchemy import create_engine,Integer,String,ForeignKey,Column,MetaData,desc,BIGINT
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import OperationalError,IllegalStateChangeError,ResourceClosedError,ProgrammingError,PendingRollbackError,InvalidRequestError
from sqlalchemy_utils import EmailType
import time

Base = declarative_base()

engin = create_engine("mysql://root:ashu@localhost:3306/alchemy_test?autocommit-1")
Session = sessionmaker(bind=engin)
Session = Session()

try:

    class Book_Type(Base):
        __tablename__='book_type'

        typeId = Column(Integer, primary_key=True)
        typeName = Column(String(50))

    class Book(Base):

        __tablename__='book'

        bookId = Column(Integer, primary_key=True )
        bookName=Column(String(220))
        bookAuthor = Column(String(220))
        bookPrice = Column(String(220))
        book_type_Name = Column(String(220))
        donorId = Column(Integer)
        libName = Column(String(220) , default= "Ahmedabad")
        # libId = Column(Integer)

    class available_book(Base):
        __tablename__='available'

        bookId = Column(Integer,primary_key=True , autoincrement=False)
        book_name = Column(String(220))
        bookAuthor = Column(String(220))
        bookPrice = Column(String(220))
        typeName = Column(String(220))
        libName = Column(String(220), default="Ahmedabad")




    class issue_book(Base):

        __tablename__='issue_book'

        issuer_name = Column(String(220))
        issuer_contact = Column(Integer)
        issuer_email = Column(EmailType)
        book_name = Column(String(220))
        bookAuthor = Column(String(220))
        bookPrice = Column(String(220))
        typeName = Column(String(220))
        book_id = Column(Integer,primary_key=True , autoincrement=False)

    class   Signup(Base):

        __tablename__ = 'signupUser'

        id = Column (Integer , primary_key=True)
        name = Column (String(220))
        contact = Column (BIGINT)
        email = Column(EmailType)
        password = Column (String(220))

    # =====================execute table

    Base.metadata.create_all(engin)

except OperationalError or IllegalStateChangeError or ResourceClosedError or ProgrammingError or PendingRollbackError or InvalidRequestError :
    
    Session.rollback()
    time.sleep(2)
    Session.close()
    engin.dispose()
    engin.connect()
    engin = create_engine("mysql://root:ashu@localhost:3306/alchemy_test", pool_pre_ping=True)
    Session = sessionmaker(bind=engin)
    Session = Session()
    time.sleep(1)

#
# finally:
#     # close the session
#     Session.rollback()
#     time.sleep(1)
    # Session.close()
















# Session.rollback()
# Session.close()
# engin.dispose()
# engine.connect()
# engin = create_engine("mysql://root:ashu@localhost:3306/alchemy_test?autocommit=1")
# Session = sessionmaker(bind=engin)
# Session = Session()