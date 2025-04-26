from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Speaker(Base):
    """
    Represents a speaker entity assigned to a conference.

    Attributes:
        id (int): Unique identifier for the speaker.
        name (str): Name of the speaker.
        specialty (str): Area of expertise of the speaker.
        email (str): Contact email of the speaker.
        conference_id (int): ID of the related conference.
    """
    __tablename__ = "speakers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    email = Column(String, nullable=False)
    conference_id = Column(Integer, ForeignKey("conferences.id"), nullable=False)

    conference = relationship("Conference", back_populates="speakers")
