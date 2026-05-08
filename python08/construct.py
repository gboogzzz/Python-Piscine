import sys
import os
import site


def is_in_venv() -> bool:
    # venv activate when the premiss is truth
    return sys.prefix != sys.base.prefix


def display_outside_venv() -> None:
    print("MATRIX STATUS: You're still plugged in")
    # path of the actual python installed
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("python -m venv matrix_env")  # create venv
    print("source matrix_env/bin/activate  # Unix")  # activate venv


def display_inside_venv() -> None:
    # return the path to venv if active
    venv_path = os.environ.get('VIRTUAL_ENV')
    # extract the name of the folder
    venv_name = os.path.basename(venv_path)
    # paths list of the packages installed
    site_packages = site.getsitepackages()[0]
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print("SUCCESS: You're in an isolated environment!")
    print(f"Package installation path: {site_packages}")


def main() -> None:
    if is_in_venv():
        display_inside_venv()
    else:
        display_outside_venv


if __name__ == "__main__":
    main()
