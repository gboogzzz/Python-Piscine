def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    # Esta importação causa o crash circular entre dark_spellbook
    #  e dark_validator
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(dark_spell_record("Darkness", "bats, arsenic"))


if __name__ == "__main__":
    main()
