from .entity import Entity
import random

REACH = 10

class Dove(Entity):
    def __init__(self, id:str, pos:tuple[int,int], hunger:int):
        super().__init__(id, pos, hunger)
    
    def __str__(self):
        return "Dove"

    def do(self, foods):
        self.auto_move()
        self.check_food(foods)
        for food in self.foods:
            food.get_eaten(self)