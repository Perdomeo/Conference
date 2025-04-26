from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.speaker import SpeakerCreate, SpeakerUpdate, SpeakerOut
from app.services import speaker_service
from app.db.database import get_db

router = APIRouter(
    prefix="/speakers",
    tags=["speakers"]
)

@router.post("/", response_model=SpeakerOut)
def create_speaker_route(speaker: SpeakerCreate, db: Session = Depends(get_db)):
    """
    Create a new speaker.
    """
    try:
        return speaker_service.register_speaker(db, speaker)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[SpeakerOut])
def list_speakers_route(db: Session = Depends(get_db)):
    """
    Retrieve all speakers.
    """
    return speaker_service.list_speakers(db)

@router.get("/{speaker_id}", response_model=SpeakerOut)
def get_speaker_route(speaker_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a speaker by its ID.
    """
    speaker = speaker_service.get_speaker(db, speaker_id)
    if not speaker:
        raise HTTPException(status_code=404, detail="Speaker not found")
    return speaker

@router.put("/{speaker_id}", response_model=SpeakerOut)
def update_speaker_route(speaker_id: int, updates: SpeakerUpdate, db: Session = Depends(get_db)):
    """
    Update an existing speaker.
    """
    updated = speaker_service.modify_speaker(db, speaker_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Speaker not found")
    return updated

@router.delete("/{speaker_id}")
def delete_speaker_route(speaker_id: int, db: Session = Depends(get_db)):
    """
    Delete a speaker by ID.
    """
    if not speaker_service.remove_speaker(db, speaker_id):
        raise HTTPException(status_code=404, detail="Speaker not found")
    return {"message": "Speaker deleted successfully"}
