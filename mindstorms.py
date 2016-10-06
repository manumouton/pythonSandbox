import turtle


def main():
    window = turtle.Screen()
    window.bgcolor("red")

    my_turtle = turtle.Turtle()
    my_turtle.shape("turtle")
    my_turtle.color("blue")
    my_turtle.speed(2)
    draw_square(my_turtle, 100)

    window.exitonclick()


def draw_square(my_turtle, size):
    for i in range(1,5):
        my_turtle.forward(size)
        my_turtle.right(90)

main()