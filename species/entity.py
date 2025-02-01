import random
import math
from food import Food
from abc import ABC, abstractmethod


# Parent class for all entities
class Entity(ABC):
    
    def __init__(self, id:str, pos:tuple[int,int],hunger:int):
        self.id = id
        self.pos = pos
        self.hunger = hunger
        self.foods = []
        self.alive = True
    
    def is_alive(self):
        return self.alive

    def get_pos(self):
        return self.pos
    
    def get_id(self):
        return self.id
    
    def die(self):
        self.alive = False

    def reset_hunger(self):
        self.hunger = 0

    def get_hunger(self):
        return self.hunger

    def receive_nutri(self, nutri):
        self.hunger += nutri

    # move to new position
    def move(self, new_pos):
        self.pos = new_pos

    # move randomly
    def auto_move(self):
        angle = random.randint(0,360)
        radius = random.randint(0,10)
        new_x = self.pos[0] + radius * math.cos(angle)
        new_y = self.pos[1] + radius * math.sin(angle)
        self.move((new_x, new_y))
    
    def metabolism(self):

        # Die
        if self.hunger == 0:
            return 0
        
        elif self.hunger < 1:
            return int(random.random() <= self.hunger)
        
        elif self.hunger == 1:
            return 1
        
        elif self.hunger < 2:
            return int(random.random()+1 <= self.hunger) + 1
        
        else:
            self.hunger = 0
            return 2
    
    def check_food(self, foods:list[Food]):
        for food in foods:
            if (((food.get_pos()[1] - self.pos[1])**2) + ((food.get_pos()[0] - self.pos[0])**2))**0.5 <= 10:
                self.foods.append(food)

    # default action
    @abstractmethod
    def do(self, foods):
        pass