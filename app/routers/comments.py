from fastapi import status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.CommentResponse)
def create_comment(
    comment: schemas.CommentRequest, 
    db: Session = Depends(get_db), 
    current_user: schemas.UserResponse = Depends(oauth2.get_current_user)):
    dog = db.query(models.Dog).filter(models.Dog.dog_id == comment.dog_id).first()

    if not dog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Dog with id {comment.dog_id} not found")
    
    new_comment = models.Comment(**comment.model_dump())
    new_comment.user_id = current_user.user_id

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment
    
