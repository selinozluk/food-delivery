from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

# Şifreyi basit bir şekilde "hash"lemek için örnek fonksiyon
def fake_hash_password(password: str):
    return "fakehashed" + password

# Kullanıcıyı doğrulamak için fonksiyon
def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not fake_hash_password(password) == user.hashed_password:
        return False
    return user

# Kullanıcı oluşturma fonksiyonu
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = fake_hash_password(user.password)  # Şifreyi hash'lemen gerekiyor
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# E-posta adresi ile kullanıcıyı bulma fonksiyonu
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Adres oluşturma fonksiyonu
def create_address(db: Session, address: schemas.AddressCreate, current_user: models.User):
    db_address = models.Address(**address.dict(), owner_id=current_user.id)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

# Giriş işlemi için fonksiyon
def login_for_access_token(db: Session, form_data: OAuth2PasswordRequestForm):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    # Token oluşturma işlemleri burada yapılmalı
    return {"access_token": user.email, "token_type": "bearer"}
