from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import String, Integer, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="My FastAPI application")

# Database setup
db_name = "users.db"
connect_args = {"check_same_thread": False}

engine = create_engine(f"sqlite:///{db_name}", connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    role = Column(String, nullable=False)

Base.metadata.create_all(engine)

# Pydantic models (API Models)
class UserCreate(BaseModel):
    name:str
    email:str
    role:str

class UserResponse(BaseModel):
    id:int
    name:str
    email:str
    role:str

    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

get_db()

# Endpoints
@app.get("/")
def root():
    return {
        "message": "root endpoint"
    }

# Get user
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
    return user

# Create user
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db:Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Update user
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user:UserCreate, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User does not exist!!")
    for field, value in user.dict().items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user

# Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id:int, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User does not exist!!")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted"}


# Get all users
@app.get("/users/", response_model=List[UserResponse])
def get_all_users(db:Session = Depends(get_db)):
    return db.query(User).all()