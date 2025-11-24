from datetime import date

from fastapi import APIRouter
from pydantic import BaseModel

from di import person_relationship_link_repository, relationship_repository
from models.person_relationship_link import PersonRelationshipLink
from models.relationship import Relationship, RelationshipType


router = APIRouter(prefix="/relationship", tags=["relationship"])

class CreateRelationship(BaseModel):
    relationship_type: RelationshipType
    start_date: date

    people: list[int]

@router.post("")
async def create(create_relationship: CreateRelationship):
    relationship = Relationship(
        relationship_type=create_relationship.relationship_type,
        start_date=create_relationship.start_date
    )
    relationship = relationship_repository.save(relationship)

    people_rels = [
        PersonRelationshipLink(person_id=person, relationship_id=relationship.id) 
        for person in create_relationship.people
    ]
    person_relationship_link_repository.save_all(people_rels)