class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 prize_points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points


class GardenManager:
    total_gardens: int = 0

    class GardenStats:
        def calculate_score(self, plants) -> int:
            score = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower) is True:
                    score += (plant.age + plant.height + plant.prize_points)
                elif isinstance(plant, Plant) is True:
                    score += (plant.age + plant.height)
            return score

        def plant_type_count(self, plants) -> dict:
            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in plants:
                if isinstance(plant, PrizeFlower) is True:
                    counts["prize"] += 1
                elif isinstance(plant, FloweringPlant) is True:
                    counts["flowering"] += 1
                elif isinstance(plant, Plant) is True:
                    counts["regular"] += 1
            return counts

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.total_growth = 0
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant) -> None:
        print(f"Added {plant.name} to {self.owner}'s garden")
        self.plants.append(plant)

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            print(f"{plant.name} grew 1cm")
            plant.grow()
            self.total_growth += 1

    def get_report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower) is True:
                print(f"-{plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers (blooming), "
                      f"Prize points: {plant.prize_points}")
            elif isinstance(plant, FloweringPlant) is True:
                print(f"-{plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers (blooming)")
            elif isinstance(plant, Plant) is True:
                print(f"-{plant.name}: {plant.height}cm")
        print()
        print(f"Plants added: {len(self.plants)}, "
              f"Total growth: {self.total_growth}cm")
        plant_list = self.stats.plant_type_count(self.plants)
        print(
                f"Plant types: {plant_list['regular']} regular, "
                f"{plant_list['flowering']} flowering, "
                f"{plant_list['prize']} prize flowers"
        )

    @classmethod
    def create_garden_network(cls, owners: list) -> list:
        network = []
        for owner in owners:
            network.append(cls(owner))
        return network

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    owners = ["Alice", "Bob"]
    gardens = []
    gardens = GardenManager.create_garden_network(owners)
    oak_tree = Plant("Oak Tree", 100, 150)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)
    print()
    pine_tree = Plant("Pine Tree", 90, 130)
    tulipe = FloweringPlant("Tulipe", 25, 20, "purple")
    rosemary = PrizeFlower("Rosemary", 35, 46, "green", 15)
    alice_plants = [oak_tree, rose, sunflower]
    bob_plants = [pine_tree, tulipe, rosemary]
    for plant in alice_plants:
        gardens[0].add_plant(plant)
    print()
    gardens[0].grow_all()
    print()
    gardens[0].get_report()
    print()
    for plant in bob_plants:
        gardens[1].add_plant(plant)
    print()
    gardens[1].grow_all()
    print()
    gardens[1].get_report()
    print()
    if GardenManager.validate_height(15) is True:
        print("Height validation test: True")
    print(f"Garden scores - Alice: "
          f"{gardens[0].stats.calculate_score(gardens[0].plants)}, "
          f"Bob: {gardens[1].stats.calculate_score(gardens[1].plants)}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")
