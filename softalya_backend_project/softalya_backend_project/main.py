from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Veritabanı oturumunu almak için bağımlılık
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/users/register/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/users/login/")
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    return crud.login_for_access_token(db=db, form_data=form_data)

@app.post("/users/address/")
def add_address(address: schemas.AddressCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.add_address(db=db, address=address, current_user=current_user)
