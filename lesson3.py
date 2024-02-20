from turtle import *

speed(20)
shape("turtle")
color("red")
width(7)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)             #end of square

      #drawing door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(150, 90)
pendown()

color("green")
begin_fill()
right(150)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
end_fill()

penup()
goto(20, 90)
pendown()

color("green")
begin_fill()
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
end_fill()        #end of the first house



begin_fill()
penup()

goto(-300, 200)
pendown()
end_fill()



left(90)     #drawing square
width(7)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

penup()            
goto(-300, 100)

forward(100)
left(90)
forward(60)

color("cyan")           #door
begin_fill()
penup()
goto(-300, 0)
forward(70)
pendown()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#roof
penup()
goto(-100, 200)
color("cyan")
begin_fill()
right(150)
pendown()
forward(200)
left(120)
forward(200)
end_fill()

color("blue")
begin_fill()
penup()        #first window
left(40)
forward(80)
left(80)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()


color("blue")
begin_fill()
right(90)        #second window
penup()
goto(-150, 120)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

            #third house
left(90)
penup()
forward(500)
right(90)
pendown()
forward(80)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(120)            #end of square

                     #door
color("orange")
penup()
goto(-520, 0)
pendown()
begin_fill()
forward(120)
left(90)
forward(60)
left(90)
forward(120)
end_fill()

#roof
penup()
goto(-450, 200)
pendown()
color("indigo")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#first window
penup()
left(40)
forward(80)
left(80)
pendown()
color("silver")
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

#second window
right(90)
penup()
forward(130)
pendown()
color("silver")
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

#end of houses
#sun

color("yellow")
penup()
goto(450, 150)
pendown()
begin_fill()

circle(100)

end_fill()


















































exitonclick()
