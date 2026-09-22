
from sqlalchemy import Column, Integer , String , ForeignKey
from sqlalchemy.orm import relationship 
from database import Base

class Account(Base):
    __tablename__="accounts"

    id = Column(Integer , primary_key=True , index =True)
    owner_name = Column(String , nullable =False)


    balance = Column(Integer , default=0)

    transactions = relationship("Transaction" , back_populates="account")

class Transactions(Base):
    __tablename__="transactions"

    id = Column(Integer , primary_key=True , index =True)
    account_id = Column(Integer , ForeignKey("accounts.id"), nullable=False)
    amount = Column(Integer , nullable=False)

    account = relationship("Account" , back_populates="transactions"    )