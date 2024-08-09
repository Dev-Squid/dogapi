from fastapi import status, HTTPException, Depends, APIRouter

from .. import models, schemas, utils
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def users(user: schemas.UserRequest, db: Session = Depends(get_db)):
    
    user.password = utils.hash_password(user.password)
    
    new_user = models.User(**user.model_dump())
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    
@router.get("/{id}", response_model=schemas.UserResponse)
def users(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with id {id} not found")
    
    return user