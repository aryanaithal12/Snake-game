import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor('black')
my_screen.title('MY SNAKE GAME')
my_screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
# to detect user response
my_screen.listen()
my_screen.onkey((lambda: snake.up()), "w")
my_screen.onkey((lambda: snake.down()), "s")
my_screen.onkey((lambda: snake.left()), "a")
my_screen.onkey((lambda: snake.right()), "d")

my_screen.onkey((lambda: snake.up()), "Up")
my_screen.onkey((lambda: snake.down()), "Down")
my_screen.onkey((lambda: snake.left()), "Left")
my_screen.onkey((lambda: snake.right()), "Right")

game_is_running = True
while game_is_running:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    score.write_score()
    if food.distance(snake.head) < 15:
        score.clear_score()
        food.refresh(snakebody=snake.body)
        snake.add()
        score.update_score()
    if snake.check():
        game_is_running = False
        score.game_over()
    if snake.check_self_col():
        game_is_running = False
        score.game_over()
my_screen.exitonclick()
