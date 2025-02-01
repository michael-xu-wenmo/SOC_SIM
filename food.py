
class Food:
    def __init__(self,pos:tuple[int,int],nutri:int):
        self.pos = pos
        self.eaters = []
        self.nutri = nutri

    def get_pos(self):
        return self.pos
    
    def get_eaters(self):
        return self.eaters
    
    def get_eaten(self, eater):
        self.eaters.append(eater)
    
    def provide_nutri(self):
        for eater in self.eaters:
            eater.receive_nutri(self.nutri/len(self.eaters))