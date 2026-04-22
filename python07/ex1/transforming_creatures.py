from ex0.creature import Creature
from .capabilities import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")

    def attack(self) -> str:
        if self._is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self._is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self._is_transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        if self._is_transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self._is_transformed = True
        return f"{self.name} morphs into  a dragonic battle form!"

    def revert(self) -> str:
        self._is_transformed = False
        return f"{self.name} stabilizes its form."
