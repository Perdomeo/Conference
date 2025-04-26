from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.conference import ConferenceCreate, ConferenceUpdate, ConferenceOut
from app.services import conference_service
from app.db.database import get_db

router = APIRouter(
    prefix="/conferences",
    tags=["conferences"]
)

@router.post("/", response_model=ConferenceOut)
def create_conference_route(conference: ConferenceCreate, db: Session = Depends(get_db)):
    """
    Create a new conference.
    """
    try:
        return conference_service.register_conference(db, conference)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[ConferenceOut])
def list_conferences_route(db: Session = Depends(get_db)):
    """
    Retrieve all conferences.
    """
    return conference_service.list_conferences(db)

@router.get("/{conference_id}", response_model=ConferenceOut)
def get_conference_route(conference_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a conference by its ID.
    """
    conference = conference_service.get_conference(db, conference_id)
    if not conference:
        raise HTTPException(status_code=404, detail="Conference not found")
    return conference

@router.put("/{conference_id}", response_model=ConferenceOut)
def update_conference_route(conference_id: int, updates: ConferenceUpdate, db: Session = Depends(get_db)):
    """
    Update an existing conference.
    """
    updated = conference_service.modify_conference(db, conference_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Conference not found")
    return updated

@router.delete("/{conference_id}")
def delete_conference_route(conference_id: int, db: Session = Depends(get_db)):
    """
    Delete a conference by ID.
    """
    if not conference_service.remove_conference(db, conference_id):
        raise HTTPException(status_code=404, detail="Conference not found")
    return {"message": "Conference deleted successfully"}
