import sys
import importlib.util
import importlib.metadata


def check_dependencies() -> bool:
    packages = {
        'pandas': (
            'Data manipulation ready',
            'pip install pandas'
        ),
        'numpy': (
            'Numerical computation ready',
            'pip install numpy'
        ),
        'matplotlib': (
            'Visualization ready',
            'pip install matplotlib'
        ),
    }

    all_ok = True

    for name, (description, install_cmd) in packages.items():
        # check if you have the package returns None if u havent
        check = importlib.util.find_spec(name)

        if check:
            # returns an version of an package
            version = importlib.metadata.version(name)
            print(f"[OK]  {name} ({version}) - {description}")
        else:
            print(f"[MISSING] {name} - not installed. Run: {install_cmd}")
            all_ok = False

    return all_ok


def show_package_comparison() -> None:
    print("\n--- Dependency Management Comparison ---")
    print("pip  → requirements.txt (manual, no lock file, no venv)")
    print("       install: pip install -r requirements.txt")
    print("Poetry → pyproject.toml (auto lock file, auto venv)")
    print("         install: poetry install")
    print("         run:     poetry run python loading.py")
    print("----------------------------------------\n")


def generate_matrix_data() -> dict:
    import numpy  # type: ignore
    import pandas  # type: ignore

    # 1000 random nbrs
    time = numpy.linspace(0, 100, 1000)

    # 1000 points spaced between (0, 100)
    signal = numpy.random.randn(1000)

    # 100 random nbrs between 0 and 1
    noise = numpy.random.uniform(0, 1, 1000)

    # create DataFrame with numpy
    return pandas.DataFrame({
        'time': time,
        'signal': signal,
        'noise': noise
    })


def analyze_data(df) -> None:
    print(f"Processing {len(df)} data points...")

    mean = df['signal'].mean()  # media
    std = df['signal'].std()  # standart deviation

    print(mean, std)


def generate_visualizations(df) -> None:
    import matplotlib.pyplot  # type: ignore

    fig, ax = matplotlib.pyplot.subplots()

    ax.plot(df['time'], df['signal'])
    ax.set_title('Matrix Data Analysis')
    ax.set_xlabel('Time')
    ax.set_ylabel('Signal')

    matplotlib.pyplot.savefig('matrix_analysis.png')  # saves file
    matplotlib.pyplot.close()

    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...")

    if not check_dependencies():
        sys.exit(1)

    show_package_comparison()

    print("Analyzing Matrix data...")

    df = generate_matrix_data()

    analyze_data(df)

    print("Generating visualization...")

    generate_visualizations(df)

    print("Analysis complete!")


if __name__ == "__main__":
    main()
