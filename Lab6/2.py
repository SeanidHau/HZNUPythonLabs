import turtle as t
t.setup(width = 640, height = 480) 
t.penup() 
t.goto(130, 0) 
t.pencolor("orange") 
t.pensize(10) 
t.seth(90) 
t.pendown()
for i in range(130, -30, -40) :     
    t.circle(i)     
t.mainloop()