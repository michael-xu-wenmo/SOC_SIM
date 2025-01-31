from species.entity import Entity

class Fool(Entity):
    def __init__(self, id:int, pos:tuple[int,int], points:int):
        super().__init__(id, pos, points)