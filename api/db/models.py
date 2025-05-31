from sqlalchemy import (
    Column,
    String,
    DateTime,
    Text,
    Enum,
    ForeignKey,
    Boolean,
    JSON,
    PrimaryKeyConstraint,
    ForeignKeyConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship, validates
from datetime import datetime
import uuid as uuid_lib
from utils.hash import hash_password

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid_lib.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    @validates("password")
    def validate_password(self, key, user_password):
        return hash_password(user_password)

    chat_histories = relationship("ChatHistories", back_populates="user")


class ChatHistory(Base):
    __tablename__ = 'ChatHistories'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid_lib.uuid4)
    created_at = Column(DateTime, default=datetime.utcnow)
    messages = Column(JSON, nullable=False)
    session_id = Column(UUID(as_uuid=True), ForeignKey("Users.id", ondelete="CASCADE"), nullable=False)

    user = relationship("Users", back_populates="chat_histories")