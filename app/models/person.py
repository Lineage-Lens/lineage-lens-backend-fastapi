from datetime import date
from enum import Enum
from typing import Optional, List, TYPE_CHECKING

from pydantic import computed_field
from sqlmodel import Field, Relationship as R, SQLModel

from .person_relationship_link import PersonRelationshipLink
if TYPE_CHECKING:
    from .relationship import Relationship


class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"

class Person(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    birth_date: date
    gender: Gender

    father_id: int | None = Field(default=None, foreign_key="person.id")
    mother_id: int | None = Field(default=None, foreign_key="person.id")

    father: Optional["Person"] = R(
        back_populates="children_as_father",
        sa_relationship_kwargs={
            "remote_side": "Person.id",
            "foreign_keys": "[Person.father_id]",
        },
    )

    mother: Optional["Person"] = R(
        back_populates="children_as_mother",
        sa_relationship_kwargs={
            "remote_side": "Person.id",
            "foreign_keys": "[Person.mother_id]",
        },
    )

    children_as_father: List["Person"] = R(
        back_populates="father",
        sa_relationship_kwargs={"foreign_keys": "[Person.father_id]"},
    )

    children_as_mother: List["Person"] = R(
        back_populates="mother",
        sa_relationship_kwargs={"foreign_keys": "[Person.mother_id]"},
    )

    @property
    def children(self) -> List["Person"]:
        return (self.children_as_father or []) + (self.children_as_mother or [])

    @computed_field
    @property
    def children_ids(self) -> List[int]:
        return [child.id for child in self.children]
    
    _relationships: List["Relationship"] = R(back_populates="people", link_model=PersonRelationshipLink)
    
    @computed_field
    @property
    def relationships(self) -> List["Relationship"]:
        return self._relationships