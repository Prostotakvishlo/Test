import turtle
turtle.shape('turtle')


def koch(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)
        turtle.right(120)
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)


def snowflake(order, size):
    for i in range(3):
        koch(order, size)
        turtle.right(120)
snowflake(4, 300)
turtle.mainloop()
