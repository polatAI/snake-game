import turtle
import time
import random

game_screen = turtle.Screen()
game_screen.title("Snake Game")
game_screen.setup(width=1400, height=800)
game_screen.bgcolor("orange")
game_screen.tracer(0)

snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.color("black")
snake_head.shape("circle")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = 'stop'

snake_speed = 0.15
food = turtle.Turtle()
food.speed(0)
food.color('blue')
food.shape('circle')
food.penup()
food.goto(0, 100)
food.shapesize(0.80, 0.80)

tail = []
score = 0
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color('white')
scoreboard.shape('square')
scoreboard.penup()
scoreboard.goto(0, 350)
scoreboard.hideturtle()
scoreboard.write("Score: {}".format(score), align='center', font=('Courier', 30, 'normal'))

def move():
    if snake_head.direction == 'up':
        y = snake_head.ycor()
        snake_head.sety(y + 10)
    if snake_head.direction == 'down':
        y = snake_head.ycor()
        snake_head.sety(y - 10)
    if snake_head.direction == 'right':
        x = snake_head.xcor()
        snake_head.setx(x + 10)
    if snake_head.direction == 'left':
        x = snake_head.xcor()
        snake_head.setx(x - 10)

def go_up():
    if snake_head.direction != 'down':
        snake_head.direction = 'up'

def go_down():
    if snake_head.direction != 'up':
        snake_head.direction = 'down'

def go_right():
    if snake_head.direction != 'left':
        snake_head.direction = 'right'

def go_left():
    if snake_head.direction != 'right':
        snake_head.direction = 'left'

game_screen.listen()
game_screen.onkey(go_up, 'Up')
game_screen.onkey(go_down, 'Down')
game_screen.onkey(go_left, 'Left')
game_screen.onkey(go_right, 'Right')

def reset():
    global score, snake_speed
    time.sleep(1)
    snake_head.goto(0, 0)
    snake_head.direction = 'stop'

    for i in tail:
        i.goto(5000, 5000)

    tail.clear()
    score = 0
    scoreboard.clear()
    scoreboard.write("Score: {}".format(score), align='center', font=('Courier', 30, 'normal'))

    snake_speed = 0.15

while True:
    game_screen.update()

    if snake_head.xcor() > 750 or snake_head.xcor() < -750 or snake_head.ycor() > 380 or snake_head.ycor() < -375:
        reset()

    if snake_head.distance(food) < 20:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        food.goto(x, y)

        score += 10
        scoreboard.clear()
        scoreboard.write("Score: {}".format(score), align='center', font=('Courier', 30, 'normal'))

        snake_speed -= 0.01

        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape('circle')
        new_tail.color("black")
        new_tail.penup()
        tail.append(new_tail)

    for i in range(len(tail) - 1, 0, -1):
        x = tail[i-1].xcor()
        y = tail[i-1].ycor()
        tail[i].goto(x, y)

    if len(tail) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        tail[0].goto(x, y)

    move()
    time.sleep(snake_speed)
