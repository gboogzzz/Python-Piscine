

def set_analytics(alice: set, bob: set, charlie: set) -> None:
    print("=== Achievement Analytics ===")
    all_setunion = alice.union(bob, charlie)
    print(f"All unique achievements: {all_setunion}")
    print(f"Total unique achievements: {len(all_setunion)}\n")
    all_set = [alice, bob, charlie]
    common_all = alice.intersection(bob, charlie)
    print(f"Common to all players: {common_all}")
    rares = set()
    for achivement in all_setunion:
        count = 0
        for sets in all_set:
            if achivement in sets:
                count += 1
        if count == 1:
            rares.add(achivement)
    print(f"Rare achievements (1 player): {rares}\n")


def set_compare(alice: set, bob: set) -> None:
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")
    set_analytics(alice, bob, charlie)
    set_compare(alice, bob)


if __name__ == "__main__":
    main()
