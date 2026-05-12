from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power
    def accumulator() -> int:
        nonlocal total_power
        total_power += initial_power
        return total_power
    
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def factory(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return factory


def memory_vault() -> dict[str, Callable]:
    mem = {}
    def store(key: str, value: Any) -> None:
        mem[key] = value
    
    def recall(key: str) -> Any:
        return mem.get(key, "Memory not found")
    
    return {
        "store": store,
        "recall": recall
    }


def main():
    counter1 = mage_counter()
    counter2 = mage_counter()
    print(counter1())
    print(counter1())
    print(counter2())

    acc = spell_accumulator(10)
    print(acc())
    print(acc())

    fire_enchant = enchantment_factory("Fire")
    print(fire_enchant("Sword"))
    print(fire_enchant("Staff"))

    vault = memory_vault()
    vault["store"]("mana", 100)
    vault["store"]("spell", "Fireball")
    print(vault["recall"]("mana"))
    print(vault["recall"]("spell"))


if __name__ == "__main__":
    main()
    