from typing import Generic, Type, TypeVar

from sqlmodel import Session, SQLModel, select


T = TypeVar("T", bound=SQLModel)

class BaseRepository(Generic[T]):
    def __init__(self, session: Session, model_class: Type[T]):
        self._session = session
        self._model_class = model_class
    
    def find_all(self) -> list[T]:
        return self._session.exec(select(self._model_class)).all()
    
    def save(self, obj: T) -> T:
        self._session.add(obj)
        self._session.commit()
        self._session.refresh(obj)
        return obj