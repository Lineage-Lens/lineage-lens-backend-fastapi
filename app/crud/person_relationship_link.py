from sqlmodel import Session

from .base import BaseRepository
from models.person_relationship_link import PersonRelationshipLink


class PersonRelationshipLinkRepository(BaseRepository[PersonRelationshipLink]):
    def __init__(self, session: Session):
        super().__init__(session, PersonRelationshipLink)