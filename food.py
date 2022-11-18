from turtle import Turtle
import random #permite que la comida aparezca de forma aleatoria 

class Food(Turtle):

    def __init__(self): #determina las caracteristicas del objeto comida 
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) 
        self.color("#7F669D")
        self.speed("fastest")
        self.refresh()

    def refresh(self): #aplica los siguientes comandos cada que se refresque la comida, esto sera determinado en el main, en el cual se le indico que cuando colisione la serpiente con comida aplicara refresh 
        random_x = random.randint(-280, 280) #la comida aparecera de forma aleatoria en cualquier parte de las corrdenadas descritas- quiere decir toda la pantalla
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
