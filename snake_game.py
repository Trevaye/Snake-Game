import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Screen setup
wn = turtle.Screen()
wn.title("Snake Game by @Trevaye Morris")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) 

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)

segments = []

# Functions
def go_up():
    if head.direction != "down":  
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

def update_score():
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        print("Game Over!")
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Reset score
        if score > high_score:
            high_score = score
        score = 0
        update_score()

        # Clear the snake body
        for segment in segments:
            segment.goto(1000, 1000)  # Move off-screen
        segments.clear()

    # Checking for collision with the food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        # Update score
        score += 10
        if score > high_score:
            high_score = score
        update_score()

    # Move end first
    for index in range(len(segments) - 1, 0, -1):
        segments[index].goto(segments[index - 1].xcor(), segments[index - 1].ycor())

    # Move segment zero to head position
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check for self-collision
    for segment in segments:
        if segment.distance(head) < 20:
            print("Game Over!")
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Reset score
            if score > high_score:
                high_score = score
            score = 0
            update_score()

            # Clear the snake body
            for segment in segments:
                segment.goto(1000, 1000)  # Move off-screen
            segments.clear()

    time.sleep(delay)

wn.mainloop()
