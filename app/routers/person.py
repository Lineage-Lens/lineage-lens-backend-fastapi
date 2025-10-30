from fastapi import APIRouter

from di import person_repository
from models.person import Person


router = APIRouter(prefix="/person", tags=["person"])

@router.get("/")
async def read():
    return person_repository.find_all()

@router.post("/")
async def create(person: Person):
    return person_repository.save(person)