from db import get_session
from crud.person import PersonRepository


session = next(get_session())
person_repository = PersonRepository(session)