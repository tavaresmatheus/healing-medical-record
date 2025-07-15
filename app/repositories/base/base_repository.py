from typing import Generic, List

from fastapi import HTTPException
from sqlmodel import Session, select
from sqlalchemy.exc import SQLAlchemyError

from .base_repository_interface import IBaseRepository, ModelType

class BaseRepository(Generic[ModelType], IBaseRepository[ModelType]):
    def __init__(self, model: type[ModelType], session: Session):
        self.model = model
        self.session = session

    def create(self, model_data: ModelType) -> ModelType:
        try:
            self.session.add(model_data)
            self.session.commit()
            self.session.refresh(model_data)
            return model_data
        except SQLAlchemyError as e:
            self.session.rollback()
            raise HTTPException(status_code=500, detail=e._message())

    def get_by_id(self, id: str) -> ModelType | None:
        model = self.session.get(self.model, id)
        return model

    def get_all(self) -> List[ModelType]:
        model_list = self.session.exec(select(self.model)).scalars().all()
        return model_list

    def update(self, database_model: ModelType, model_data: ModelType) -> ModelType:
        try:
            model_data_to_update = model_data.model_dump(exclude_unset=True)

            for key, value in model_data_to_update.items():
                setattr(database_model, key, value)

            self.session.add(database_model)
            self.session.commit()
            self.session.refresh(database_model)
        except SQLAlchemyError as e:
            self.session.rollback()
            raise HTTPException(status_code=500, detail=e._message())

    def delete(self, database_model: ModelType) -> None:
        try:
            self.session.delete(database_model)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise HTTPException(status_code=500, detail=e._message())
