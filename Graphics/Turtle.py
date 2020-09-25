import turtle
wn= turtle.Screen() #This creates a graphics window
alex= turtle.Turtle()
'''alex.forward(150)
alex.left(90)
alex.forward(150)
wn.exitonclick()'''
i=0
while True:
	alex.forward(150)
	alex.left(100)
	i+=1
	if i==7:
		break
wn.exitonclick() #This will make the screen stay.

	