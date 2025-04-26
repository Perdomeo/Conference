from pydantic import BaseModel, EmailStr

class SpeakerBase(BaseModel):
    """
    Shared attributes for speaker models.
    """
    name: str
    specialty: str
    email: EmailStr
    conference_id: int

class SpeakerCreate(SpeakerBase):
    """
    Schema for creating a new speaker.
    """
    pass

class SpeakerUpdate(BaseModel):
    """
    Schema for updating speaker data. All fields optional.
    """
    name: str | None = None
    specialty: str | None = None
    email: EmailStr | None = None
    conference_id: int | None = None

class SpeakerOut(SpeakerBase):
    """
    Schema used for returning speaker data in API responses.
    """
    id: int

    class Config:
        orm_mode = True
