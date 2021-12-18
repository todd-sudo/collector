from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship

from ..core.base_class import Base


class User(Base):
    """Модель пользователя"""
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
