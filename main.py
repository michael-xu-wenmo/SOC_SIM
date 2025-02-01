from display import Vdisplay, Cdisplay
import species
from food import Food

ENTITY_NUM = 100

def init_entities(type):
    entities = []
    for row in range(-10,10):
        for column in range(-10,10):
            entities.append(getattr(species, type)(str(row*column),(column,row),0))
    return entities

def init_foods():
    foods = []
    for row in range(-10,10):
        for column in range(-100,100):
            foods.append(Food((column,row),2))
    return foods

def main():
    # Create entities
    entities = init_entities('Dove')
    foods = init_foods()

    # Create displays
    vdisplay = Vdisplay(800, 600, entities) # type: ignore
    cdisplay = Cdisplay(entities) # type: ignore

    # Start simulation
    round_num = 0
    while len(entities) > 0:
        # Render entities
        vdisplay.render()

        # Remove Corpses
        n = 0
        while n < len(entities):
            if not entities[n].is_alive():
                entities.pop(n)
            else:
                n += 1

        # Do entity actions
        for entity in entities:
            entity.do(foods)
        
        # Food gives nutri
        n = 0
        while n < len(foods):
            if len(foods[n].eaters) > 0:
                foods[n].provide_nutri()
                foods.pop(n)
            else:
                n += 1

        cdisplay.print_round(round_num, len(entities))

        # Metabolism
        new_entities = []
        for entity in entities:
            state = entity.metabolism()
            if state == 0:
                entity.die()
            elif state == 1:
                entity.reset_hunger()
            else:
                new_id = entity.get_id()
                new_entities.append(getattr(species, str(entity))(new_id,entity.get_pos(),0))

        entities += new_entities
        
        round_num += 1

    print("Simulation ended")
    vdisplay.screen.mainloop()

if __name__ == "__main__":
    main()
    print("done")