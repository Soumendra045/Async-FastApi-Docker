import uuid
import datetime
from sqlalchemy import Column, String, Integer, DateTime, Date
from sqlalchemy.dialects.postgresql import UUID

from src.db.database import Base


class Book(Base):
    __tablename__ = "books"

    uid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False
    )

    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    publisher = Column(String(255))
    published_date = Column(Date)
    page_count = Column(Integer)
    language = Column(String(50))

    created_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )

    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )

    def __repr__(self):
        return f"<Book {self.title}>"
