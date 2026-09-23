from fastapi import FASTAPI ,  Depends
from sqlalchemy.orm import Session 
import models 
import schemas

from database import engine , get_db
models.Base.metadata.create_all(bind=engine)

app = FASTAPI(title="FinLedger API")

@app.post("/accounts/",response_model=schemas.AccountResponse)
def create_account(account:schemas.AccountCreate, db:Session = Depends(get_db)):


    new_account = models.Account(owner_name = account.owner_name , balance =0)
    db.add(new_account)
    db.commit()

    db.refresh(new_account)

    return new_account