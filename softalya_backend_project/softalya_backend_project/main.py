from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# API Key'i .env dosyasından al
API_KEY = os.getenv("SOFTALYA_API_KEY")

# Veritabanı tablolarını oluştur
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# API Key doğrulama fonksiyonu
def verify_api_key(x_softalya_api_key: str = Header(...)):
    if x_softalya_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

# Veritabanı oturumunu almak için bağımlılık
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", dependencies=[Depends(verify_api_key)])
def read_root():
    return {"Hello": "World"}

@app.post("/users/register/", dependencies=[Depends(verify_api_key)])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/users/login/", dependencies=[Depends(verify_api_key)])
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    return crud.login_for_access_token(db=db, form_data=form_data)

@app.post("/users/address/", dependencies=[Depends(verify_api_key)])
def add_address(address: schemas.AddressCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.add_address(db=db, address=address, current_user=current_user)
