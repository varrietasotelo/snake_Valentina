from turtle import Turtle
ALIGNMENT = "center" #indica que la alineacion sera centrada
FONT = ("Courier", 24, "normal") #indica la fuente de los letreros

class Scoreboard(Turtle): #crea la clase para luego llamarla en main

    def __init__(self): #determina las caracteristicas fisicas del conteo de puntos
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self): #letrero de score por donde se indica la puntuacion del juego 
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self): #letrero de game over que indica cuando se ha terminado la partida
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):  #Ppermite que el conteo suba de uno en uno 
        self.score += 1
        self.clear()
        self.update_scoreboard()
