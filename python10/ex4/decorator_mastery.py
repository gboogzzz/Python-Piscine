from functools import wraps
from collections.abc import Callable
import time


from functools import wraps
from collections.abc import Callable
import time


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Spell completed in {end - start:.3f} seconds")

        return result

    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):

            power = args[1] if len(args) > 1 else args[0]

            if power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(1, max_attempts + 1):

                try:
                    return func(*args, **kwargs)

                except Exception:

                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    else:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts"
                        )

        return wrapper

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3
            and all(char.isalpha() or char.isspace() for char in name)
        )

    @power_validator(10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return (
            f"Successfully cast {spell_name} "
            f"with {power} power"
        )


@spell_timer
def fireball():
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def unstable_spell():
    raise Exception("Failed spell")


if __name__ == "__main__":

    print("Testing spell timer...")
    result = fireball()
    print("Result:", result)

    print("\nTesting retrying spell...")
    print(unstable_spell())

    print("\nTesting MageGuild...")

    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("12"))

    guild = MageGuild()

    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Lightning"))