import turtle
turtle.shape('turtle')


def levi(order,size):
    if order == 0:
        turtle.forward(size)
    else:
       turtle.left(45)
       levi(order-1,size/2)
       turtle.right(90)
       levi(order-1,size/2)
       turtle.left(45)
levi(3,300)
turtle.mainloop()
