from typing import Optional, List

from sqlmodel import Field, Relationship, SQLModel


class Person(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str

    father_id: int | None = Field(default=None, foreign_key="person.id")
    mother_id: int | None = Field(default=None, foreign_key="person.id")

    father: Optional["Person"] = Relationship(
        back_populates="children_as_father",
        sa_relationship_kwargs={
            "remote_side": "Person.id",
            "foreign_keys": "[Person.father_id]",
        },
    )

    mother: Optional["Person"] = Relationship(
        back_populates="children_as_mother",
        sa_relationship_kwargs={
            "remote_side": "Person.id",
            "foreign_keys": "[Person.mother_id]",
        },
    )

    children_as_father: List["Person"] = Relationship(
        back_populates="father",
        sa_relationship_kwargs={"foreign_keys": "[Person.father_id]"},
    )

    children_as_mother: List["Person"] = Relationship(
        back_populates="mother",
        sa_relationship_kwargs={"foreign_keys": "[Person.mother_id]"},
    )