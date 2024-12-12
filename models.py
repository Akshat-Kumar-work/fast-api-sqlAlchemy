#creating schema using sql alchemy orm

from sqlalchemy import String,Integer,Column,Boolean

from database import Base


class Person(Base):
    __tablename__='person'
    id=Column(Integer,primary_key=True)
    firstName= Column(String(40),nullable=False)
    lastName=Column(String(40),nullable=False)
    isMale=Column(Boolean)