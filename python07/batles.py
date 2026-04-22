from ex0 import FlameFactory, AquaFactory


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    base_fire = flame_factory.create_base()
    evolved_fire = flame_factory.create_evolved()

    base_water = aqua_factory.create_base()
    evolved_water = aqua_factory.create_evolved()

    print(base_fire.describe())
    print(base_fire.attack())

    print(evolved_fire.describe())
    print(evolved_fire.attack())

    print(base_water.describe())
    print(base_water.attack())

    print(evolved_water.describe())
    print(evolved_water.attack())


if __name__ == "__main__":
    main()
