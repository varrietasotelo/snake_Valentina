from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)] #determina la poscion inicial
MOVE_DISTANCE = 20 #determina cuantos puntos se va a mover el objeto 
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake: #se crea la clase snake que permitira utilizar las funciones en main

    def __init__(self): 
        self.segments = []
        self.create_snake() #crea el objeto snake
        self.head = self.segments[0]

    def create_snake(self): 
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position): #convierte los cuadrados en un objeto
        new_segment = Turtle("square") #determina la forma
        new_segment.color("#FBFACD") #determina el color de la snake
        new_segment.penup() #mano alzada - evita que veamos el trazo del movimiento
        new_segment.goto(position)
        self.segments.append(new_segment) #convierte los cuadrados en un solo objeto

    def extend(self):

        self.add_segment(self.segments[-1].position())

    def move(self): #permite el movimiento del objeto 
        for seg_num in range(len(self.segments)- 1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self): #determina el movimiento hacia arriba 
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self): #determina el movimiento hacia abajo 
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self): #determina el movimiento hacia izquierda 
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self): #determina el movimiento hacia derecha
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
