from datetime import date
from enum import Enum
from typing import List, TYPE_CHECKING

from pydantic import computed_field
from sqlmodel import Field, Relationship as R, SQLModel

from .person_relationship_link import PersonRelationshipLink
if TYPE_CHECKING:
    from .person import Person


class RelationshipType(str, Enum):
    DATING = "Dating"
    ENGAGED = "Engaged"
    MARRIED = "Married"

class Relationship(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    relationship_type: RelationshipType
    start_date: date

    people: List["Person"] = R(back_populates="_relationships", link_model=PersonRelationshipLink)
    
    @computed_field
    @property
    def people_ids(self) -> List[int]:
        return [person.id for person in self.people]