import turtle

def main():
    # create a turtle object
    michaelangelo = turtle.Turtle()

    michaelangelo.color('red')

    # Ask the turtle to move around the canvas
    for i in range(500):
        michaelangelo.forward(50 + i)
        michaelangelo.right(108)

    turtle.exitonclick()

if __name__ == "__main__":
    main()
