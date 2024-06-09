import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red','green','orange','cyan','pink','black','purple','brown','yellow','blue']
def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers= int(racers)
        else:
            print("input is not neumeric..Try again !!")
            continue
        if 2 <= racers <= 10:
             return racers
        else:
            print("Opps not in range if 2-10 try again !!")

def race(colors):
    turtles = create_turtle(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y =racer.pos()
            if y >=HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtle(colors):
    turtles = []
    spacingx= WIDTH // (len(colors) + 1)
    for i , color in enumerate(colors):
        racer= turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Drag Race !!")

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors=COLORS[:racers]
winner=race(colors)

print(winner)





# racer= turtle.Turtle()
# racer.speed(1)
# racer.pen()
# racer.shape('turtle')
# racer.color('red')
# racer.forward(100)
# racer.left(90)
# racer.forward(100)
# racer.right(90)
# racer.backward(100)
# time.sleep(5)