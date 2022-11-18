from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

#Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()


'''

#crear el contenedor del juego
#creacion de un objeto tipo ventana
screen = Screen()

screen.setup(width=600, height=600) #determina el tamaño de la pantalla
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #establece delay 0 

snake = Snake ()
#food = Food()
#scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "UP")
screen.onkey(snake.down, "DOWN")
screen.onkey(snake.left, "LEFT")
screen.onkey(snake.right, "RIGHT")

#Animar o simular el movimiento
game_is_on = True


while game_is_on:
    screen.update() #mejora la visualizacion
    time.sleep(0.1) #determina el tiempo que tomara el movimiento
    Snake.move()




#crea el objeto y se va de inmediato, necesito algo que controle la salida del objeto
screen.exitonclick()
'''