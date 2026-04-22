import alchemy  # noqa: F401
from alchemy.transmutation.recipes import lead_to_gold


def main() -> None:
    """
    Testa a transmutação acedendo ao sub-pacote enquanto
    o pacote principal também está importado no namespace.
    """
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    # Nota: isto requer que transmutation esteja importado
    # no alchemy/__init__.py ou acedido via caminho completo.
    try:
        # Chamada da função importada especificamente
        result = lead_to_gold()
        print(f"Testing lead to gold: {result}")
    except ImportError as e:
        print(f"Import Error: {e}")


if __name__ == "__main__":
    main()
