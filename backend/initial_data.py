import logging

from core.db import SessionLocal
from settings import settings
from user.services import crud_user
from user.schemas import UserCreate


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()

    _user = crud_user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not _user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True
        )
        _user = crud_user.create(db, obj_in=user_in)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
