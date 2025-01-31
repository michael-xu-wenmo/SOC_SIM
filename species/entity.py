import random
import math


# Parent class for all entities
class Entity:
    
    def __init__(self, id:int, pos:tuple[int,int], points:int):
        self.id = id
        self.pos = pos
        self.points = points
        self.within_bounds = []
        self.alive = True
    
    def get_points(self):
        return self.points
    
    def is_alive(self):
        return self.alive

    def get_pos(self):
        return self.pos
    
    def get_id(self):
        return self.id
    
    def die(self):
        self.alive = False

    # move to new position
    def _move(self, new_pos):
        self.pos = new_pos

    # move randomly
    def _auto_move(self):
        angle = random.randint(0,360)
        radius = random.randint(0,10)
        new_x = self.pos[0] + radius * math.cos(angle)
        new_y = self.pos[1] + radius * math.sin(angle)
        self._move((new_x, new_y))
    
    # default action
    def do(self):
        self._auto_move()
        if random.randint(0,100) > 99:
            self.die()