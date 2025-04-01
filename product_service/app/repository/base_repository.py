# Repositório base 

from abc import ABC, abstractmethod
from typing import List, Optional, Any

class BaseRepository(ABC):
    @abstractmethod
    def get(self, id: int) -> Optional[Any]:
        pass

    @abstractmethod
    def get_all(self) -> List[Any]:
        pass

    @abstractmethod
    def create(self, entity: Any) -> Any:
        pass

    @abstractmethod
    def update(self, id: int, entity: Any) -> Optional[Any]:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass 
