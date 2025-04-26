from pydantic import BaseModel
from datetime import date

class ConferenceBase(BaseModel):
    """
    Shared attributes for conference models.
    """
    name: str
    date: date
    location: str
    description: str | None = None

class ConferenceCreate(ConferenceBase):
    """
    Schema for creating a new conference.
    """
    pass

class ConferenceUpdate(BaseModel):
    """
    Schema for updating conference data. All fields optional.
    """
    name: str | None = None
    date: date | None = None
    location: str | None = None
    description: str | None = None

class ConferenceOut(ConferenceBase):
    """
    Schema used for returning conference data in API responses.
    """
    id: int

    class Config:
        orm_mode = True
