from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, actor: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, actor: Creature, opponent: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, actor: Creature) -> bool:
        return True

    def act(self, actor: Creature, opponent: Creature) -> str:
        return actor.attack()


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, actor: Creature) -> bool:
        return isinstance(actor, TransformCapability)

    def act(self, actor: Creature, opponent: Creature) -> str:

        if not isinstance(actor, TransformCapability):
            raise Exception(
                f"Invalid Creature '{actor.name}' "
                "for AggressiveStrategy"
            )

        return (
            f"{actor.transform()}\n"
            f"{actor.attack()}\n"
            f"{actor.revert()}"
        )


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, actor: Creature) -> bool:
        return isinstance(actor, HealCapability)

    def act(self, actor: Creature, opponent: Creature) -> str:

        if not isinstance(actor, HealCapability):
            raise Exception(
                f"Invalid Creature '{actor.name}' "
                "for DefensiveStrategy"
            )

        return (
            f"{actor.attack()}\n"
            f"{actor.heal()}"
        )
