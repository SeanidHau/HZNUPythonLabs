import turtle as t
t.setup(width = 640, height = 480) 
t.pencolor("navy") 
t.pensize(1)
for i in range(1, 6 * 3 * 10, 3) :     
    t.fd(i)     
    t.left(60)     
t.mainloop()