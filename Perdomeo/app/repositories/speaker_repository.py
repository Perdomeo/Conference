from sqlalchemy.orm import Session
from app.models.speaker import Speaker
from typing import List, Optional

def create_speaker(db: Session, speaker: Speaker) -> Speaker:
    """
    Adds a new speaker to the database.

    Args:
        db (Session): SQLAlchemy session object.
        speaker (Speaker): The speaker instance to insert.

    Returns:
        Speaker: The newly created speaker.
    """
    db.add(speaker)
    db.commit()
    db.refresh(speaker)
    return speaker

def get_speaker_by_id(db: Session, speaker_id: int) -> Optional[Speaker]:
    """
    Retrieves a speaker by its unique ID.

    Args:
        db (Session): SQLAlchemy session object.
        speaker_id (int): The ID of the speaker to retrieve.

    Returns:
        Optional[Speaker]: The speaker if found, else None.
    """
    return db.query(Speaker).filter(Speaker.id == speaker_id).first()

def get_all_speakers(db: Session) -> List[Speaker]:
    """
    Retrieves all speakers from the database.

    Args:
        db (Session): SQLAlchemy session object.

    Returns:
        List[Speaker]: A list of all speakers.
    """
    return db.query(Speaker).all()

def update_speaker(db: Session, speaker_id: int, updates: dict) -> Optional[Speaker]:
    """
    Updates an existing speaker.

    Args:
        db (Session): SQLAlchemy session object.
        speaker_id (int): ID of the speaker to update.
        updates (dict): Fields to be updated.

    Returns:
        Optional[Speaker]: The updated speaker, or None if not found.
    """
    speaker = get_speaker_by_id(db, speaker_id)
    if not speaker:
        return None

    for key, value in updates.items():
        setattr(speaker, key, value)

    db.commit()
    db.refresh(speaker)
    return speaker

def delete_speaker(db: Session, speaker_id: int) -> bool:
    """
    Deletes a speaker by ID.

    Args:
        db (Session): SQLAlchemy session object.
        speaker_id (int): ID of the speaker to delete.

    Returns:
        bool: True if deleted, False otherwise.
    """
    speaker = get_speaker_by_id(db, speaker_id)
    if not speaker:
        return False

    db.delete(speaker)
    db.commit()
    return True
