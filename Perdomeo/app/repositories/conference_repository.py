from sqlalchemy.orm import Session
from app.models.conference import Conference
from typing import List, Optional

def create_conference(db: Session, conference: Conference) -> Conference:
    """
    Adds a new conference to the database.

    Args:
        db (Session): SQLAlchemy session object.
        conference (Conference): The conference instance to insert.

    Returns:
        Conference: The newly created conference.
    """
    db.add(conference)
    db.commit()
    db.refresh(conference)
    return conference

def get_conference_by_id(db: Session, conference_id: int) -> Optional[Conference]:
    """
    Retrieves a conference by its unique ID.

    Args:
        db (Session): SQLAlchemy session object.
        conference_id (int): The ID of the conference to retrieve.

    Returns:
        Optional[Conference]: The conference if found, else None.
    """
    return db.query(Conference).filter(Conference.id == conference_id).first()

def get_all_conferences(db: Session) -> List[Conference]:
    """
    Retrieves all conferences from the database.

    Args:
        db (Session): SQLAlchemy session object.

    Returns:
        List[Conference]: A list of all conferences.
    """
    return db.query(Conference).all()

def update_conference(db: Session, conference_id: int, updates: dict) -> Optional[Conference]:
    """
    Updates an existing conference.

    Args:
        db (Session): SQLAlchemy session object.
        conference_id (int): ID of the conference to update.
        updates (dict): Fields to be updated.

    Returns:
        Optional[Conference]: The updated conference, or None if not found.
    """
    conference = get_conference_by_id(db, conference_id)
    if not conference:
        return None

    for key, value in updates.items():
        setattr(conference, key, value)

    db.commit()
    db.refresh(conference)
    return conference

def delete_conference(db: Session, conference_id: int) -> bool:
    """
    Deletes a conference by ID.

    Args:
        db (Session): SQLAlchemy session object.
        conference_id (int): ID of the conference to delete.

    Returns:
        bool: True if deleted, False otherwise.
    """
    conference = get_conference_by_id(db, conference_id)
    if not conference:
        return False

    db.delete(conference)
    db.commit()
    return True
