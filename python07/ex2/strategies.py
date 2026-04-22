from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class Strategy(ABC):
    @abstractmethod
    def decide_action(self, actor: Creature, opponent: Creature) -> str:
        pass


class AggressiveStrategy(Strategy):
    def decide_action(self, actor: Creature, opponent: Creature) -> str:
        if isinstance(actor, TransformCapability):
            return f"{actor.transform()}\n{actor.attack()}"
        return f"{actor.attack()}"


class DefensiveStrategy(Strategy):
    def decide_action(self, actor: Creature, opponent: Creature) -> str:
        if isinstance(actor, HealCapability):
            return f"{actor.attack()}\n{actor.heal()}"
        return f"{actor.attack()}"


class CowardStrategy(Strategy):
    def decide_action(self, actor: Creature, opponent: Creature) -> str:
        return f"{actor.name} tries to hide!"
