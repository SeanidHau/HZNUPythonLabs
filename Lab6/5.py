import turtle
def koch(t, order, size) :
    if order == 0 :
        t.fd(size)
    else :
        for i in [60, -120, 60, 0] :
            koch(t, order - 1, size / 3)
            t.right(i)  

order = int(input()) 
flake = turtle.Turtle() 
flake.penup() 
flake.goto(-150, -90) 
flake.pendown()
for _ in range(3) :
    koch(flake, order, 300)
    flake.left(120)
turtle.mainloop()