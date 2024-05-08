import turtle
h = 3 ** 0.5 / 2 * 200
turtle.setup(width = 640, height = 480) 
turtle.penup() 
turtle.goto(-h / 2, -h / 3) 
turtle.pencolor("blue") 
turtle.pensize(10) 
turtle.pendown()
for i in range(3) :     
    turtle.seth(i * 120)     
    turtle.fd(200)
turtle.mainloop()