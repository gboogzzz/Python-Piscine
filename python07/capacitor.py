from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def main() -> None:

    print("Testing Creature with healing capability")
    h_factory = HealingCreatureFactory()

    print("base:")
    b_heal = h_factory.create_base()
    print(b_heal.describe())
    print(b_heal.attack())

    if isinstance(b_heal, HealCapability):
        print(b_heal.heal())

    print("evolved:")
    e_heal = h_factory.create_evolved()
    print(e_heal.describe())
    print(e_heal.attack())

    if isinstance(e_heal, HealCapability):
        print(e_heal.heal())

    print("\nTesting Creature with transform capability")
    t_factory = TransformCreatureFactory()

    print("base:")
    b_trans = t_factory.create_base()
    print(b_trans.describe())
    print(b_trans.attack())

    if isinstance(b_trans, TransformCapability):
        print(b_trans.transform())
        print(b_trans.attack())
        print(b_trans.revert())

    print("evolved:")
    e_trans = t_factory.create_evolved()
    print(e_trans.describe())
    print(e_trans.attack())

    if isinstance(e_trans, TransformCapability):
        print(e_trans.transform())
        print(e_trans.attack())
        print(e_trans.revert())


if __name__ == "__main__":
    main()
