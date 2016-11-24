import turtle
turtle.shape('turtle')


def mink(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        mink(order-1, size/4)
        turtle.left(90)
        mink(order-1, size/4)
        turtle.right(90)
        mink(order-1, size/4)
        turtle.right(90)
        mink(order-1, size/4)
        mink(order-1, size/4)
        turtle.left(90)
        mink(order-1, size/4)
        turtle.left(90)
        mink(order-1, size/4)
        turtle.right(90)
        mink(order-1, size/4)
mink(2, 300)
turtle.mainloop()


