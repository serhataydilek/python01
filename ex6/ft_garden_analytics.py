class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def grow(self) -> None:
            self._grow_calls += 1

        def age(self) -> None:
            self._age_calls += 1

        def show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(self, plant_name: str,
                 plant_height: float, plant_age: int) -> None:
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_age = plant_age
        self._statistics = self.Statistics()

    @staticmethod
    def is_year_old(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self, amount: float) -> None:
        self.plant_height += amount
        self._statistics.grow()

    def age(self, days: int) -> None:
        self.plant_age += days
        self._statistics.age()

    def show(self) -> None:
        self._statistics.show()
        print(f"{self.plant_name}: {self.plant_height}cm, "
              f"{self.plant_age} days old")

    def display_statistics(self) -> None:
        self._statistics.display()


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
        self._shade_calls = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(f"Tree {self.plant_name} now produces a shade of "
              f"{self.plant_height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def display_statistics(self) -> None:
        super().display_statistics()
        print(f"{self._shade_calls} shade")


class Seed(Flower):
    def __init__(self, plant_name: str, plant_height: float,
                 plant_age: int, color: str) -> None:
        super().__init__(plant_name, plant_height, plant_age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.plant_name}]")
    plant.display_statistics()


def main() -> None:
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    anonymous = Plant.create_anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_year_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_year_old(400)}")
    print("=== Flower")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_statistics(rose)
    print("=== Tree")
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)
    print("=== Anonymous")
    anonymous.show()
    display_statistics(anonymous)


if __name__ == "__main__":
    main()
