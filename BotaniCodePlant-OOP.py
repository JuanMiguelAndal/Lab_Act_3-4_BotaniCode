from abc import ABC, abstractmethod

class Plant(ABC):
    def __init__(self, plant_name: str, height: float, age: int):
        self.plant_name = plant_name
        self.height = height
        self.age = age
    
    @abstractmethod
    def grow(self) -> str:
        pass
    
    @abstractmethod
    def make_food(self) -> str:
        pass

class Flower(Plant):
    def __init__(self, plant_name: str, height: float, age: int, color: str):
        super().__init__(plant_name, height, age)
        self.color = color
    
    def grow(self) -> str:
        self.height += 0.5
        self.age += 1
        return f"{self.plant_name} has grown! New height: {self.height}cm, Age: {self.age} years"
    
    def make_food(self) -> str:
        return f"{self.plant_name} is making food through photosynthesis"

class Tree(Plant):
    def __init__(self, plant_name: str, height: float, age: int, leaf_type: str):
        super().__init__(plant_name, height, age)
        self.leaf_type = leaf_type
    
    def grow(self) -> str:
        self.height += 2.0
        self.age += 1
        return f"{self.plant_name} has grown! New height: {self.height}m, Age: {self.age} years"
    
    def make_food(self) -> str:
        return f"{self.plant_name} is making food through photosynthesis and storing it in its trunk"

class Herbs(Plant):
    def __init__(self, plant_name: str, height: float, age: int, medicinal_use: str):
        super().__init__(plant_name, height, age)
        self.medicinal_use = medicinal_use
    
    def grow(self) -> str:
        self.height += 0.3
        self.age += 1
        return f"{self.plant_name} has grown! New height: {self.height}cm, Age: {self.age} years"
    
    def make_food(self) -> str:
        return f"{self.plant_name} is making food through photosynthesis and producing medicinal compounds"

class Vines(Plant):
    def __init__(self, plant_name: str, height: float, age: int, fragrance: str):
        super().__init__(plant_name, height, age)
        self.fragrance = fragrance
    
    def grow(self) -> str:
        self.height += 1.5
        self.age += 1
        return f"{self.plant_name} has grown! New height: {self.height}m, Age: {self.age} years"
    
    def make_food(self) -> str:
        return f"{self.plant_name} is making food through photosynthesis and producing aromatic compounds"

class Poaceae(Plant):
    def __init__(self, plant_name: str, height: float, age: int, grain_type: str):
        super().__init__(plant_name, height, age)
        self.grain_type = grain_type
    
    def grow(self) -> str:
        self.height += 0.8
        self.age += 1
        return f"{self.plant_name} has grown! New height: {self.height}m, Age: {self.age} years"
    
    def make_food(self) -> str:
        return f"{self.plant_name} is making food through photosynthesis and producing {self.grain_type} grains"

if __name__ == "__main__":
    rose = Flower("Rose", 30.0, 1, "Red")
    oak = Tree("Oak", 5.0, 10, "Deciduous")
    basil = Herbs("Basil", 20.0, 1, "Sweet & Pungent")
    grape = Vines("Grape", 2.0, 3, "Sweet and Fruity")
    wheat = Poaceae("Wheat", 1.0, 1, "Cereal")
    
    print("\nTesting Flower:")
    print(rose.grow())
    print(rose.make_food())
    
    print("\nTesting Tree:")
    print(oak.grow())
    print(oak.make_food())
    
    print("\nTesting Herbs:")
    print(basil.grow())
    print(basil.make_food())
    
    print("\nTesting Vines:")
    print(grape.grow())
    print(grape.make_food())
    
    print("\nTesting Poaceae:")
    print(wheat.grow())
    print(wheat.make_food()) 