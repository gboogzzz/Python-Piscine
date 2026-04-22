

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def age_old(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    height_day_1 = rose.height
    for i in range(1, 7):
        rose.grow()
        rose.age_old()
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{rose.height - height_day_1}cm")
