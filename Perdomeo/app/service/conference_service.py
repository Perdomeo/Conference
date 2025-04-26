from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.conference import Conference
from app.schemas.conference import ConferenceCreate, ConferenceUpdate
from app.repositories import conference_repository

def register_conference(db: Session, conference_data: ConferenceCreate) -> Conference:
    """
    Registers a new conference in the system.

    Args:
        db (Session): SQLAlchemy session.
        conference_data (ConferenceCreate): Input data for the new conference.

    Returns:
        Conference: The created conference.

    Raises:
        ValueError: If a conference with the same name and date already exists.
    """
    existing_conferences = conference_repository.get_all_conferences(db)
    for conf in existing_conferences:
        if conf.name == conference_data.name and conf.date == conference_data.date:
            raise ValueError("Conference with this name and date already exists.")

    new_conference = Conference(**conference_data.dict())
    return conference_repository.create_conference(db, new_conference)

def get_conference(db: Session, conference_id: int) -> Optional[Conference]:
    """
    Retrieves a conference by its ID.

    Args:
        db (Session): SQLAlchemy session.
        conference_id (int): The unique ID of the conference.

    Returns:
        Optional[Conference]: The found conference or None.
    """
    return conference_repository.get_conference_by_id(db, conference_id)

def list_conferences(db: Session) -> List[Conference]:
    """
    Retrieves all conferences from the database.

    Args:
        db (Session): SQLAlchemy session.

    Returns:
        List[Conference]: List of all conferences.
    """
    return conference_repository.get_all_conferences(db)

def modify_conference(db: Session, conference_id: int, updates: ConferenceUpdate) -> Optional[Conference]:
    """
    Updates an existing conference with new data.

    Args:
        db (Session): SQLAlchemy session.
        conference_id (int): The ID of the conference to update.
        updates (ConferenceUpdate): The updated fields.

    Returns:
        Optional[Conference]: The updated conference or None if not found.
    """
    return conference_repository.update_conference(db, conference_id, updates.dict(exclude_unset=True))

def remove_conference(db: Session, conference_id: int) -> bool:
    """
    Deletes a conference from the system.

    Args:
        db (Session): SQLAlchemy session.
        conference_id (int): The ID of the conference to delete.

    Returns:
        bool: True if deleted, False if not found.
    """
    return conference_repository.delete_conference(db, conference_id)
