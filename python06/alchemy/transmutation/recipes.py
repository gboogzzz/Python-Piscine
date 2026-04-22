# Import Absoluto
from alchemy.potions import strength_potion
# Import Relativo
from ..elements import create_air
# Import da Raiz
from elements import create_fire


def lead_to_gold() -> str:
    """Performs the great transmutation."""
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
            f"and '{strength_potion()}' mixed with '{create_fire()}'")
