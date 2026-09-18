class Plant:
    def __init__(self, plant_name: str,
                 plant_height: float, plant_age: int) -> None:
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_age = plant_age

class Flower(Plant):
    def __init__(
        self,
        plant_name: str,
        plant_height: float,
        plant_age: int,
        color: str
    ) -> None:
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
	def __init__(
        self,
        plant_name: str,
        plant_height: float,
        plant_age: int,
        trunk_diameter: float
    ) -> None:
		self.trunk_diameter = trunk_diameter
	def produce_shade(self) -> None:
		

class Vegetable(Plant):
	def __init__(self, nutritional_value: int):
		self.nutritional_value = 0
		self.nutritional_value = nutritional_value
	def grow(self, ):

