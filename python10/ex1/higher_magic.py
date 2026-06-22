from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} defense"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if not callable(condition):
            return "Spell fizzled"
        try:
            if condition(target, power):
                return spell(target, power)
            return "Spell fizzled"
        except Exception:
            return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        if not spells:
            return []
        return list(map(lambda spell: spell(target, power), spells))
    return sequence


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 50)
    print(f"Combined spell result: {result[0]}, {result[1]}")
    print()

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: 10, Amplified: {10 * 3}")
    print()

    print("Testing conditional caster...")

    def enough_power(target: str, power: int) -> bool:
        return power >= 50

    safe_spell = conditional_caster(enough_power, fireball)
    print(safe_spell("Goblin", 30))
    print(safe_spell("Goblin", 70))
    print()

    print("Testing spell sequence...")
    combo = spell_sequence([fireball, heal, shield])
    results = combo("Knight", 40)
    for result in results:
        print(result)
