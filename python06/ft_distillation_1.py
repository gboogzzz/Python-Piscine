import alchemy


def main() -> None:
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    # 'heal' é o alias definido em alchemy/__init__.py
    print(f"Testing heal alias: {alchemy.heal()}")


if __name__ == "__main__":
    main()
