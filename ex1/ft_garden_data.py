class Plant:
    def __init__(self, plant_name: str, plant_height: int, plant_age: int) -> None:
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f"{self.plant_name}: {self.plant_height}cm, {self.plant_age} days old")


def main() -> None:
    p = Plant("Rose", 25, 30)
    p1 = Plant("Sunflower", 80, 45)
    p2 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    p.show()
    p1.show()
    p2.show()


if __name__ == "__main__":
    main()
