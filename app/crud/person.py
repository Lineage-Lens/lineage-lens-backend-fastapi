from sqlmodel import Session

from .base import BaseRepository
from models.person import Person


class PersonRepository(BaseRepository[Person]):
    def __init__(self, session: Session):
        super().__init__(session, Person)