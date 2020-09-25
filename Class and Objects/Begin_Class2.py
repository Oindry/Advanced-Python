class Robot:
	#The class name is Robot. Meaning this class is for a groups of robots
	def introduce_self(self):		   # "self" is the object here and name is an attribute of that object.
		print("My name is "+self.name) #  By Object we mean defining each robot.
									   #  we need to put the object in paranthesis while stating function 									   
#r1 & r2 are objects here. When we did .name or .color we define the attributes of that object.
r1= Robot()
r1.name ="Tom" 
r1.color ="red"
r1.weight= 30

r2 = Robot()
r2.name = "Jerry"
r2.color= "Blue"
r2.weight= 40

r1.introduce_self()
r2.introduce_self()