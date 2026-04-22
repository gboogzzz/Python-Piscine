import sys


if __name__ == "__main__":
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
    elif len(sys.argv) > 1:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        for argv in range(1, len(sys.argv)):
            print(f"Argument {argv}: {sys.argv[argv]}")
        print(f"Total arguments: {len(sys.argv)}")
