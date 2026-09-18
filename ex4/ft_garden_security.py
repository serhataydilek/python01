class Plant:
    def __init__(self, plant_name: str,
                 plant_height: float, plant_age: int) -> None:
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_age = plant_age

    def show(self) -> None:
        print(
            f"{self.plant_name}: {round(self.plant_height, 3)}cm, {self.plant_age} days old")

    def create(self) -> None:
        print(f"Plant created: ", end="")

    def set_height(self, height: float):
        if height < 0:
            print(f"{self.plant_name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.plant_height = height
            print(f"Height updated: {self.plant_height}cm")

    def set_age(self, age: int):
        if age < 0:
            print(f"{self.plant_name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.plant_age = age
            print(f"Age updated: {self.plant_age} days")
            print("\n")


def main():
    p = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    p.create()
    p.show()
    print("\n")
    p.set_height(25)
    p.set_age(30)
    p.set_height(-1)
    p.set_age(-1)
    print(f"\nCurrent state: ", end="")
    p.show()


if __name__ == "__main__":
    main()
