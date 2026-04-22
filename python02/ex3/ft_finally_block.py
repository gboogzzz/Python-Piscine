

def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise ValueError("Cannot water None - invalid plant!")
            else:
                print(f"Watering {plant}")
    except ValueError as e:
        print(f"{e}")
    else:
        print("Watering completed successfully!")
    finally:
        print("Closing watering system (cleanup)\n")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Testing with error...")
    water_plants(["tomato", None])
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
