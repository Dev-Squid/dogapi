from fastapi import status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2, database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/votes",
    tags=["votes"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.VoteResponse)
def vote(
    vote: schemas.VoteRequest, 
    db: Session = Depends(database.get_db), 
    current_user: schemas.UserResponse = Depends(oauth2.get_current_user)):

    comment = db.query(models.Comment).filter(models.Comment.comment_id == vote.comment_id).first()

    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Comment with id {vote.comment_id} not found")
    
    if comment.user_id == current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"User cannot vote on their own comment")
    
    if(db.query(models.Vote).filter(models.Vote.comment_id == vote.comment_id, models.Vote.user_id == current_user.user_id).first()):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"User has already voted on this comment")
    
    new_vote = models.Vote(**vote.model_dump())
    new_vote.user_id = current_user.user_id
    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)

    return new_vote