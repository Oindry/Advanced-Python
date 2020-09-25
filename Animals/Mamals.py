class Mamals():
	def __init__(self):
		#create some members animals
		self.members=["Tiger","Elephant","Lion"]
	def printMember(self):
		print("Printing members of the mamals")
		for member in self.members:
			print("\t%s"%member)
