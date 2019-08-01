import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.speed(50)
    for j in range(36):
        for i in range(4):
            brad.forward(200)
            brad.right(90)
        brad.right(10)
    window.exitonclick()

draw_square()