from typing import List, Tuple
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
from .strategies import Strategy, AggressiveStrategy, DefensiveStrategy


class Tournament:
    def __init__(self, matches: List[Tuple[Creature, Strategy, Creature]]) -> None:
        self.matches = matches

    def _validate_match(self, actor: Creature, strategy: Strategy) -> bool:
        if isinstance(strategy, AggressiveStrategy):
            has_transform = isinstance(actor, TransformCapability)
            is_fire = actor.creature_type == "Fire"
            return has_transform or is_fire
        if isinstance(strategy, DefensiveStrategy):
            return isinstance(actor, HealCapability)
        return True

    def start(self) -> None:
        for actor, strategy in self.matches:
            if not self._validate_match(actor, strategy):
                print("Battle error, aborting tournament...")
                return
            print(f"Tournament: {actor.name} strategy execution")
            action_output = strategy.decide_action(actor, actor)
            print(action_output)

            if isinstance(actor, TransformCapability):
                print(actor.revert())