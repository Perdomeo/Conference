from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.db.database import Base

class Conference(Base):
    """
    Represents a conference entity.

    Attributes:
        id (int): Unique identifier for the conference.
        name (str): Name of the conference.
        date (date): Date when the conference takes place.
        location (str): Location where the conference is held.
        description (str | None): Additional description about the conference.
    """
    __tablename__ = "conferences"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String, nullable=True)

    speakers = relationship("Speaker", back_populates="conference")
