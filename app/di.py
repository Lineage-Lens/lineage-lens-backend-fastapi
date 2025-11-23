from db import get_session
from crud.person import PersonRepository
from crud.relationship import RelationshipRepository


session = next(get_session())
person_repository = PersonRepository(session)
relationship_repository = RelationshipRepository(session)