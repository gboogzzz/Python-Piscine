from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str = "itself") -> str:
        pass


class TransformCapability(ABC):

    def __init__(self, *args, **kwargs) -> None:

        self._is_transformed: bool = False

        super().__init__(*args, **kwargs)

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
