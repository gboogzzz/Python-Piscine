from ex0 import FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(opponents_configs):
    combatants = []
    for factory, strategy in opponents_configs:
        creature = factory.create_base()
        combatants.append((creature, strategy))

    print("*** Tournament ***")
    print(f"{len(combatants)} opponents involved")

    for i in range(len(combatants)):
        for j in range(i + 1, len(combatants)):
            c1, s1 = combatants[i]
            c2, s2 = combatants[j]

            print("* Battle *")
            print(f"{c1.name} is a {c1.creature_type} type "
                  f"Creature\nvs.\n{c2.name} is a {c2.creature_type}"
                  f" type Creature\nnow fight!")

            try:
                if not s1.is_valid(c1):
                    raise Exception(
                        f"Battle error, aborting tournament: "
                        f"Invalid Creature-strategy combination for {c1.name}"
                    )

                if not s2.is_valid(c2):
                    raise Exception(
                        f"Battle error, aborting tournament: "
                        f"Invalid Creature-strategy combination for {c2.name}"
                    )
                print(s1.act(c1, c2))
                print(s2.act(c2, c1))
            except Exception as e:
                print(f"{e}")
                return


if __name__ == "__main__":
    opponents = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
        (FlameFactory(), DefensiveStrategy())
    ]
    battle(opponents)
