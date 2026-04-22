

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager():
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant_name: str) -> None:
        try:
            if plant_name:
                self.plants.append(plant_name)
                print(f"Added {plant_name} successfully")
            else:
                raise PlantError("Plant name cannot be empty!")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        print("Opening watering system")
        for plant in self.plants:
            print(f"Watering {plant} - success")
        print("Closing watering system (cleanup)")

    def check_health(self, plant_name: str, water_level: int,
                     sunlight: int) -> None:
        try:
            if water_level > 10:
                raise WaterError(f"Water level {water_level} "
                                 "is too high (max 10)")
            print(f"{plant_name}: healthy (water: "
                  f"{water_level}, sun: {sunlight})")
        except WaterError as e:
            print(f"Error checking {plant_name}: {e}")


def test_garden_manager() -> None:
    print("=== Garden Management System ===\n")
    manager = GardenManager()
    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")
    print()
    print("Watering plants...")
    manager.water_plants()
    print()
    print("Checking plant health...")
    manager.check_health("tomato", 5, 8)
    manager.check_health("lettuce", 15, 6)
    print()
    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_manager()
