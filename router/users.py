from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_user
from typing import List
from auth.oauth2 import get_current_user

router = APIRouter(prefix='/user',tags=['user'])

# Create User
@router.post('/',response_model=UserDisplay)
def create_user(request: UserBase, db: Session= Depends(get_db)):
    return db_user.create_user(db,request)

# Read All User
@router.get('/',response_model=List[UserDisplay],)
def get_all_user(db: Session = Depends(get_db),current_user: UserBase = Depends(get_current_user)):
    return db_user.get_all_users(db)


# Read one user
@router.get('/{id}',response_model=UserDisplay)
def get_user(id: int, db: Session= Depends(get_db),current_user: UserBase = Depends(get_current_user)):
    return db_user.get_user(db,id)


# Update User
@router.post('/{id}/update')
def update_user(request: UserBase,id: int, db: Session = Depends(get_db),current_user: UserBase = Depends(get_current_user)):
    return db_user.update_user(db,id,request)


# Delete User
@router.get('/delete/{id}')
def delete_user(id: int, db: Session = Depends(get_db),current_user: UserBase = Depends(get_current_user)):
    return db_user.delete_user(db,id)