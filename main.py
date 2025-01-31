from display import Vdisplay, Cdisplay
from species.fool import Fool

ENTITY_NUM = 100

def main():
    # Create entities
    entities = [Fool(i, (0,0), 10) for i in range(ENTITY_NUM)]

    # Create displays
    vdisplay = Vdisplay(800, 600, entities) # type: ignore
    cdisplay = Cdisplay(entities) # type: ignore

    # Start simulation
    round_num = 0
    while len(entities) > 0:
        # Render entities
        vdisplay.render()

        # Remove Corpses
        for entity in entities:
            if not entity.is_alive():
                entities.remove(entity)
                del entity

        # Do entity actions
        for entity in entities:
            entity.do()

        # Print round info
        cdisplay.print_round(round_num, len(entities))
        round_num += 1

    print("Simulation ended")
    vdisplay.screen.mainloop()

if __name__ == "__main__":
    main()
    print("done")