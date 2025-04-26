from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.speaker import Speaker
from app.schemas.speaker import SpeakerCreate, SpeakerUpdate
from app.repositories import speaker_repository

def register_speaker(db: Session, speaker_data: SpeakerCreate) -> Speaker:
    """
    Registers a new speaker in the system.

    Args:
        db (Session): SQLAlchemy session.
        speaker_data (SpeakerCreate): Input data for the new speaker.

    Returns:
        Speaker: The created speaker.

    Raises:
        ValueError: If a speaker with the same email already exists.
    """
    existing_speakers = speaker_repository.get_all_speakers(db)
    for spk in existing_speakers:
        if spk.email == speaker_data.email:
            raise ValueError("Speaker with this email already exists.")

    new_speaker = Speaker(**speaker_data.dict())
    return speaker_repository.create_speaker(db, new_speaker)

def get_speaker(db: Session, speaker_id: int) -> Optional[Speaker]:
    """
    Retrieves a speaker by its ID.

    Args:
        db (Session): SQLAlchemy session.
        speaker_id (int): The unique ID of the speaker.

    Returns:
        Optional[Speaker]: The found speaker or None.
    """
    return speaker_repository.get_speaker_by_id(db, speaker_id)

def list_speakers(db: Session) -> List[Speaker]:
    """
    Retrieves all speakers from the database.

    Args:
        db (Session): SQLAlchemy session.

    Returns:
        List[Speaker]: List of all speakers.
    """
    return speaker_repository.get_all_speakers(db)

def modify_speaker(db: Session, speaker_id: int, updates: SpeakerUpdate) -> Optional[Speaker]:
    """
    Updates an existing speaker with new data.

    Args:
        db (Session): SQLAlchemy session.
        speaker_id (int): The ID of the speaker to update.
        updates (SpeakerUpdate): The updated fields.

    Returns:
        Optional[Speaker]: The updated speaker or None if not found.
    """
    return speaker_repository.update_speaker(db, speaker_id, updates.dict(exclude_unset=True))

def remove_speaker(db: Session, speaker_id: int) -> bool:
    """
    Deletes a speaker from the system.

    Args:
        db (Session): SQLAlchemy session.
        speaker_id (int): The ID of the speaker to delete.

    Returns:
        bool: True if deleted, False if not found.
    """
    return speaker_repository.delete_speaker(db, speaker_id)
