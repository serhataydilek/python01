class Plant:
    def __init__(self, plant_name: str,
                 plant_height: float, plant_age: int) -> None:
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f"{self.plant_name}: {round(self.plant_height, 3)}cm, "
              f"{self.plant_age} days old")

    def grow(self, amount: float) -> None:
        self.plant_height += amount

    def age(self, days: int) -> None:
        self.plant_age += days


class Flower(Plant):
    def __init__(self, plant_name: str, plant_height: float,
                 plant_age: int, color: str) -> None:
        super().__init__(plant_name, plant_height, plant_age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._is_blooming:
            print(f"{self.plant_name} is blooming beautifully!")
        else:
            print(f"{self.plant_name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, plant_name: str, plant_height: float,
                 plant_age: int, trunk_diameter: float) -> None:
        super().__init__(plant_name, plant_height, plant_age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.plant_name} now produces a shade of "
              f"{self.plant_height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, plant_name: str, plant_height: float,
                 plant_age: int, harvest_season: str) -> None:
        super().__init__(plant_name, plant_height, plant_age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def grow(self, amount: float = 2.1) -> None:
        super().grow(amount)
        self.nutritional_value += 0.5

    def age(self, days: int) -> None:
        super().age(days)
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value:g}")


def main() -> None:
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age(1)
    tomato.show()


if __name__ == "__main__":
    main()
