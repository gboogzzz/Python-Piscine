import sys
import os
import site


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def display_outside_venv() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    # path of the current python
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")

    print("Then run this program again.")


def display_inside_venv() -> None:
    # path of the current venv, if doestn exist returns ""
    venv_path = os.environ.get("VIRTUAL_ENV", "")
    # name of the venv
    venv_name = os.path.basename(venv_path)
    # folder where the packages are installed
    site_packages = site.getsitepackages()[0]

    print("MATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    print("Package installation path:")
    print(site_packages)


def main() -> None:
    if is_in_venv():
        display_inside_venv()
    else:
        display_outside_venv()


if __name__ == "__main__":
    main()
