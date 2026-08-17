from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ModuleRequest:
    action: str
    payload: dict[str, Any]


@dataclass(frozen=True)
class ModuleResponse:
    success: bool
    data: Any = None
    error: str | None = None


class I34Module(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def handle(self, request: ModuleRequest) -> ModuleResponse:
        raise NotImplementedError

    @abstractmethod
    def health(self) -> bool:
        raise NotImplementedError
