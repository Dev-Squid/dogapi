from fastapi import status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/dogs",
    tags=["dogs"]
)

@router.get("/search", response_model=list[schemas.DogResponse])
def search_dogs(db: Session = Depends(get_db), limit: int = 1, skip: int = 0):
    query = db.query(models.Dog).limit(limit)

    return query.all()

@router.get("/", response_model=list[schemas.DogResponse])
def get_dogs(db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    query = db.query(models.Dog)

    print(query)

    return query.all()

@router.get("/{id}", response_model=schemas.DogResponse)
def get_dog(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Dog).filter(models.Dog.dog_id == id)

    dog = query.first()

    if not dog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Dog with id {id} not found")
    
    if dog.user_id != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail=f"User not authorized to view dog with id {id}")

    return dog

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.DogResponse)
def create_dogs(Dog: schemas.DogRequest, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_dog = models.Dog(**Dog.model_dump())
    new_dog.user_id = current_user.user_id
    db.add(new_dog)
    db.commit()
    db.refresh(new_dog)

    return new_dog

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dog(id:int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Dog).filter(models.Dog.dog_id == id)

    dog = query.first()

    if not dog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Dog with id {id} not found")

    if dog.user_id != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail=f"User not authorized to delete dog with id {id}")
    
    query.delete(synchronize_session=False)
    db.commit()
    
    return

@router.put("/{id}", response_model=schemas.DogResponse)
def put_dog(id:int, Dog: schemas.DogRequest, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Dog).filter(models.Dog.dog_id == id)

    dog = query.first()

    if not dog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Dog with id {id} not found")
    
    if dog.user_id != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail=f"User not authorized to update dog with id {id}")

    query.update(Dog.model_dump(), synchronize_session=False)
    db.commit()

    return dog
