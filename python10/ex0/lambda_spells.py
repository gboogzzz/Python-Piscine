def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_list = sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)
    return sorted_list


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_mages = list(filter(lambda mage: mage["power"] >= min_power, mages))
    return filtered_mages


def spell_transformer(spells: list[str]) -> list[str]:
    transformed_spells = list(map(lambda spell: f"* {spell} *", spells))
    return transformed_spells


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(
        mages,
        key=lambda mage: mage["power"]
    )["power"]
    min_power = min(
        mages,
        key=lambda mage: mage["power"]
    )["power"]
    avg_power = round(
        sum(mage["power"] for mage in mages) / len(mages),
        2
    )
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":

    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "magic"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Shadow Ring", "power": 70, "type": "artifact"}
    ]
    mages = [
        {"name": "Aldor", "power": 90, "element": "fire"},
        {"name": "Lyra", "power": 45, "element": "water"},
        {"name": "Zeph", "power": 75, "element": "air"}
    ]
    spells = ["fireball", "heal", "shield"]
    print("Testing artifact sorter...")
    print(artifact_sorter(artifacts))
    print()
    print("Testing power filter...")
    print(power_filter(mages, 70))
    print()
    print("Testing spell transformer...")
    print(spell_transformer(spells))
    print()
    print("Testing mage stats...")
    print(mage_stats(mages))
