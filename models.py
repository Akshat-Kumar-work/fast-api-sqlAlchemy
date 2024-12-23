#creating schema using sql alchemy orm

from sqlalchemy import String,Integer,Column,Boolean

from database import Base


#inheriting base to Person class 
# Inheriting from base ensure that person class is recognized by sql-alchemy
class Person(Base):
    __tablename__='person'
    id=Column(Integer,primary_key=True,autoincrement=True)
    firstName= Column(String(40),nullable=False)
    lastName=Column(String(40),nullable=False)
    isMale=Column(Boolean)
    password=Column(String)
    mobileNumber = Column(String(15))