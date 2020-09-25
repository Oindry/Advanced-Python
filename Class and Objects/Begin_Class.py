class Robot:#The class name is Robot. Meaning this class is for a groups of robots. 1st alphabet of a class should be in capital
	def __init__(self, name,color,weight): # This is the "constractor". Here you can describe the attributes. 
										   # This way you donot need to do the declaration manually. The first "self" is object defination.
		self.name= name # Assigning each attribute to a variable
		self.color=color
		self.weight=weight
	def introduce_self(self):
		print("My name is "+self.name) # "self" is the "object" here and name is an attribute of that object. By Object we mean defining each robot.
#r1 & r2 are objects here. When we did .name or .color we define the attributes of that object.
r1= Robot("OT","Brown",40)
r1.introduce_self()