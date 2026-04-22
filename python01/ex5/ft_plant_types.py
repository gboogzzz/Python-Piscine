

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_basicinfo(self) -> str:
        return f"{self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} (Flower): {self.get_basicinfo()},"
              f"{self.color} color")
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} (Tree): {self.get_basicinfo()},"
              f"{self.trunk_diameter} cm")
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutricional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutricional_value = nutricional_value

    def nutricional(self) -> None:
        print(f"{self.name} (Vegetable): {self.get_basicinfo()},"
              f"{self.harvest_season}")
        print(f"{self.name} is rich in {self.nutricional_value}")


if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    tulipe = Flower("Tulipe", 30, 25, "purple")
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 450, 2050, 40)
    tomato = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
    carrot = Vegetable("Carrot", 20, 20, "summer harvest", "vitamin D")
    print("=== Garden Plant Types ===\n")
    rose.bloom()
    print()
    tulipe.bloom()
    print()
    oak.produce_shade()
    print()
    pine.produce_shade()
    print()
    tomato.nutricional()
    print()
    carrot.nutricional()
