from sqlalchemy import Column, Integer, String, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "User"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    role_id = Column(Integer)

    ForeignKeyConstraint(
        ['role_id'], ['Role.role_id']
    )
