from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#crear la ventana del juego 
screen = Screen()
screen.setup(width=600, height=600) #determina el tamaño de la ventana
screen.bgcolor("blue")
screen.title("Snake Game Valentina")
screen.tracer(0) #establece el delay en 0 

snake = Snake() #trae la clase snake y todas sus funciones 
food = Food() #trae la clase food y todas sus funciones 
scoreboard = Scoreboard() #trae la clase scoreboard y todas sus funciones

screen.listen() #la indica a la pantalla que debe aplicar las funciones que se van a llamar 
screen.onkey(snake.up, "Up") #trae las funciones up, down, left, right, a traves de las cuales se aplica o simula el movimiento en la pantalla
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09) #establece el tiempo del movimiento
    snake.move() #mueve la snake al llamar la clase

#Detecta la colision con la comida
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#Detecta la colision con la pared
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

#Detecta la colision con la cola
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()#cierra la pantalla al presionar el boton 

