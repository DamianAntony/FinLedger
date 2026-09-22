from pydantic import BaseModel


class AccountCreate(BaseModel):
    owner_name:str

class TransactionCreate(BaseModel):
    account_id:int
    amount:int

class AccountResponse(BaseModel):
    id :int 
    owner_name:str
    balance:int 


    class Config:
        from_attributes = True
