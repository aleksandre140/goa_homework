from turtle import*

#we want to paint house


#steep 1: draw e square
begin_fill()
color("blue")

width(4)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing e door

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
goto(200,200)
pendown()


exitonclick()