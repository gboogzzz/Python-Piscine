from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(
        self,
        name: str,
        creature_type: str,
        *args,
        **kwargs
    ) -> None:

        self.name = name
        self.creature_type = creature_type

        super().__init__(*args, **kwargs)

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (
            f"{self.name} is a "
            f"{self.creature_type} type Creature"
        )
