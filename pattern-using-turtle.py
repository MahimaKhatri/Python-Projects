import turtle

turtle.bgcolor("black")
turtle.pensize(1)
turtle.speed(0)

b=["red","green","yellow","white"]
for i in range (9):
   for a in b:
       turtle.color(a) 
       turtle.circle(100)
       turtle.left(10)
turtle.mainloop()