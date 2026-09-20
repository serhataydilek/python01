class Plant:
    def __init__(self, plant_name: str,
                 plant_height: float, plant_age: int) -> None:
        self.plant_name = plant_name
        self._height = 0.0
        self._age = 0
        if plant_height < 0:
            print(f"{self.plant_name}: Error, height can't be negative")
        else:
            self._height = plant_height
        if plant_age < 0:
            print(f"{self.plant_name}: Error, age can't be negative")
        else:
            self._age = plant_age

    def show(self) -> None:
        print(
            f"{self.plant_name}: {round(self.get_height(), 3)}cm"
            f", {self.get_age()} days old"
        )

    def create(self) -> None:
        print("Plant created: ", end="")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.plant_name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self.get_height()}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.plant_name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self.get_age()} days")
            print()

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


def main() -> None:
    p = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    p.create()
    p.show()
    print()
    p.set_height(25)
    p.set_age(30)
    p.set_height(-1)
    p.set_age(-1)
    print("\nCurrent state: ", end="")
    p.show()


if __name__ == "__main__":
    main()
