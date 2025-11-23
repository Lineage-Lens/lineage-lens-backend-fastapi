from db import get_session
from crud.person import PersonRepository
from crud.person_relationship_link import PersonRelationshipLinkRepository
from crud.relationship import RelationshipRepository


session = next(get_session())
person_repository = PersonRepository(session)
person_relationship_link_repository = PersonRelationshipLinkRepository(session)
relationship_repository = RelationshipRepository(session)