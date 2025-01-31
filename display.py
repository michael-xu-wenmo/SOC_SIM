import turtle
import time
from species.entity import Entity

class Vdisplay:

    def __init__(self, width: int, height: int, entities: list[Entity]):
        self.width = width
        self.height = height
        self.entities = entities

        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.title("Soc Sim")
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setpos(-width/2, -height/2)
    
    def render(self):
        self.screen.tracer(0)
        self.turtle.clear()
        for entity in self.entities:
            self.turtle.setpos(entity.get_pos())
            if entity.is_alive():
                self.turtle.dot(5, "blue")
            else:
                self.turtle.dot(5, "red")
            self.turtle.write(entity.get_id())
        self.screen.update()
        time.sleep(0.1)

class Cdisplay:
    
    def __init__(self, entities: list[Entity]):
        self.entities = entities
    
    def print_round(self, round_num: int, alive_count):
        print(f"Round {round_num}  Population: {alive_count}")
        print(f"{'ID':<5}|{'PosX':^15}|{'PosY':^15}|{'Points':<6}")
        print("-"*50)
        for entity in self.entities:
            print(f"{entity.get_id():>5}|{round(entity.get_pos()[0],10):>15}|{round(entity.get_pos()[1],10):>15}|{entity.get_points():>6}")
        print()