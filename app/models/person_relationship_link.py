from sqlmodel import Field, SQLModel


class PersonRelationshipLink(SQLModel, table=True):
    person_id: int | None = Field(default=None, foreign_key="person.id", primary_key=True)
    relationship_id: int | None = Field(default=None, foreign_key="relationship.id", primary_key=True)