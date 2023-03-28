from sqlalchemy import create_engine , Column,Integer , BIGINT ,String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import EmailType

Base = declarative_base()

engin = create_engine("mysql://root:ashu@localhost:3306/jwtAuth")

Session = sessionmaker(bind=engin)

Session = Session()

try:
    class Signup(Base):

        __tablename__ = 'signupUser'

        id = Column (Integer , primary_key=True)
        name = Column (String(220))
        contact = Column (BIGINT)
        email = Column(EmailType)
        password = Column (String(220))

    Base.metadata.create_all(engin)

    Session.close()
except:

    Session.rollback()
    Session.close()
    engin.dispose()
    engine.connect()
    engin = create_engine("mysql://root:ashu@localhost:3306/jwtAuth")
    Session = sessionmaker(bind=engin)
    Session = Session()
    time.sleep(1)

finally:

    Session.close()