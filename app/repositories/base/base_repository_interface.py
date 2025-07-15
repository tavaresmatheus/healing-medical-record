from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from sqlmodel import SQLModel


ModelType = TypeVar('ModelType', bound=SQLModel)

class IBaseRepository(ABC, Generic[ModelType]):

    @abstractmethod
    def create(self, model_data: ModelType) -> ModelType:
        pass

    @abstractmethod
    def get_by_id(self, model_data: ModelType) -> ModelType:
        pass

    @abstractmethod
    def get_all(self) -> List[ModelType]:
        pass

    @abstractmethod
    def update(self, database_model: ModelType, model_data: ModelType) -> ModelType:
        pass

    @abstractmethod
    def delete(self, database_model: ModelType) -> ModelType:
        pass
