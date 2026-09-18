class Plant:
    def __init__(self, plant_name: str,
                 plant_height: float, plant_age: int) -> None:
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_age = plant_age

    def show(self) -> None:
        print(
            f"{self.plant_name}: {round(self.plant_height, 3)}cm, "
            f"{self.plant_age} days old")

    def create(self) -> None:
        print("Created: ", end="")


def main() -> None:
    p = Plant("Rose", 25.0, 30)
    p1 = Plant("Oak", 200.0, 365)
    p2 = Plant("Cactus", 5.0, 90)
    p3 = Plant("Sunflower", 80.0, 45)
    p4 = Plant("Fern", 15.0, 120)
    print("=== Plant Factory Output ===")
    p.create()
    p.show()
    p1.create()
    p1.show()
    p2.create()
    p2.show()
    p3.create()
    p3.show()
    p4.create()
    p4.show()


if __name__ == "__main__":
    main()
