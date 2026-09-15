class Plant:
    def __init__(self, plant_name: str,
                 plant_height: float, plant_age: int) -> None:
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f"{self.plant_name}: "
              f"{self.plant_height}cm, {self.plant_age} days old")

    def age(self) -> None:
        self.plant_age += 1

    def grow(self) -> None:
        self.plant_height += 0.8
        self.plant_height = round(self.plant_height, 1)


def main() -> None:
    p = Plant("Rose", 25.0, 30)
    start_height = p.plant_height
    print("=== Garden Plant Growth ===")
    p.show()
    for i in range(1, 8):
        p.age()
        p.grow()
        print(f"=== Day {i} ===")
        p.show()
    print(f"Growth this week: {round(p.plant_height - start_height, 1)}cm")


if __name__ == "__main__":
    main()
