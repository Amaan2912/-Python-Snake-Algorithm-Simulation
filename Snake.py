#python my_script.py
import turtle as trtl
import random
import keyboard
# setup for the snake's area, score indicator, and the snake itself
player = input("Please enter your full name? ")
wn = trtl.Screen()
tracer = trtl.Turtle()
tracer.speed(7)
tracer.pensize(4)
tracer.fillcolor("dark green")
tracer.penup()
tracer.goto(-300,-300)
tracer.setheading(315)
tracer.pendown()
tracer.begin_fill()
tracer.circle(500, 360, 4)
tracer.end_fill()
score = 0
tracer.hideturtle()
board = trtl.Turtle()
board.speed(7)
board.penup()
board.pencolor("navy blue")
board.goto(-100,420)
board.pendown()
board.write("Score: " + str(score) + " Fruit", font=("Calibri", 20, "normal"))
board.hideturtle()
observe = trtl.Turtle()
observe.speed(7)
observe.penup()
observe.goto(100,420)
observe.write("Player: " + str(player), font=("Calibri", 20, "normal"))
observe.hideturtle()
animal = trtl.Turtle()
animal.penup()
animal.pensize(5)
animal.shape("turtle")
skin = input("Please enter the color of your snake? ")
animal.fillcolor(skin)
animal.goto(-270, -50)
# setup for the fruit the snake is aimed to consume within the grass
food = trtl.Turtle()
food.speed(7)
def irrigation():
    x = random.randint(-290, 190)
    food.penup()
    food.goto(x,x)
produce = ["circle", "square", "triangle", "arrow", "turtle", "classic"]
shades = ["red", "orange", "yellow", "lime", "green", "blue", "indigo", "purple", "hot pink", "brown"]
def fruit_salad():
    food.shape(random.choice(produce))
    food.color(random.choice(shades))
fruit_choice = input("Which fruit do you want your snake to eat? ")
if fruit_choice == "apple":
    irrigation()
    food.shape("circle")
    food.color("dark red")
elif fruit_choice == "banana":
    irrigation()
    food.shape("arrow")
    food.color("yellow")
elif fruit_choice == "pineapple":
    irrigation()
    food.shape("turtle")
    food.color("golden rod")
elif fruit_choice == "grape":
    irrigation()
    food.shape("triangle")
    food.color("orchid")
elif fruit_choice == "pumpkin":
    irrigation()
    food.shape("square")
    food.color("dark orange")
elif fruit_choice == "radish":
    irrigation()
    food.shape("triangle")
    food.color("white")
elif fruit_choice == "eggplant":
    irrigation()
    food.shape("arrow")
    food.color("purple")
elif fruit_choice == "strawberry":
    irrigation()
    food.shape("triangle")
    food.color("crimson")
elif fruit_choice == "cherry":
    irrigation()
    food.shape("circle")
    food.color("maroon")
elif fruit_choice == "carrot":
    irrigation()
    food.shape("arrow")
    food.color("orange")
elif fruit_choice == "mushroom":
    irrigation()
    food.shape("circle")
    food.color("gray")
elif fruit_choice == "broccoli":
    irrigation()
    food.shape("turtle")
    food.color("green")
elif fruit_choice == "watermelon":
    irrigation()
    food.shape("arrow")
    food.color("tomato")
elif fruit_choice == "pepper":
    irrigation()
    food.shape("arrow")
    food.color("lime green")
elif fruit_choice == "kiwi":
    irrigation()
    food.shape("circle")
    food.color("olive")
elif fruit_choice == "lemon":
    irrigation()
    food.shape("turtle")
    food.color("yellow")
elif fruit_choice == "orange":
    irrigation()
    food.shape("circle")
    food.color("orange")
elif fruit_choice == "peach":
    irrigation()
    food.shape("circle")
    food.color("coral")
elif fruit_choice == "peanut":
    irrigation()
    food.shape("turtle")
    food.color("dark brown")
elif fruit_choice == "blueberry":
    irrigation()
    food.pensize(2)
    food.shape("circle")
    food.color("dark blue")
elif fruit_choice == "tomato":
    irrigation()
    food.shape("circle")
    food.color("red")
elif fruit_choice == "produce mix":
    irrigation()
    fruit_salad()
else:
    print("This food is unavailable")
    fruit_choice = input("Choose another fruit? ")
# function for how the snake will move within the grass
def snake_move():
    animal.forward(10)
# function for how the fruit will randomly locate after the snake touches the fruit
def relocate():
    irrigation()
    if fruit_choice == "produce mix":
        fruit_salad()
# function for score incrementation when the snake touches the fruit
def increase():
    global score
    score += 1
    board.clear()
    board.write("Score: " + str(score) + " Fruit", font=("Calibri", 20, "normal"))
# function used to end the game when the snake touches the garden's boundaries
def game_over():
    food.clear()
    animal.fillcolor("red")
    animal.shape("circle")
    board.clear()
    board.write("Game Over!", font=("Calibri", 20, "normal"))
    trtl.Screen().bye()
# conditonals for the snake's direction if keys a, s, d, or w are pressed
while True:
    if keyboard.is_pressed('d'):
        animal.setheading(360)
        snake_move()
    elif keyboard.is_pressed('w'):
        animal.setheading(90)
        snake_move()
    elif keyboard.is_pressed('a'):
        animal.setheading(180)
        snake_move()
    elif keyboard.is_pressed('s'):
        animal.setheading(270)
        snake_move()
# explains what happens when the snake touches the fruit
    if (abs(animal.xcor() - food.xcor()) <= 10) and (abs(animal.ycor() - food.ycor()) <= 10):
        relocate()
        increase()
    elif (abs(animal.xcor() - -300) <= 10) or (abs(animal.xcor() - 700) <= 10):
        game_over()
    elif (abs(animal.ycor() - -300) <= 10) or (abs(animal.ycor() - 700) <= 10):
        game_over()


wn = trtl.Screen()
wn.mainloop()