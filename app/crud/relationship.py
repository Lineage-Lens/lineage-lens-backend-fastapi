from sqlmodel import Session

from .base import BaseRepository
from models.relationship import Relationship


class RelationshipRepository(BaseRepository[Relationship]):
    def __init__(self, session: Session):
        super().__init__(session, Relationship)