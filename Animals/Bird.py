class Bird:
	def __init__(self):
		self.members=["Sparrow","Robin","Duck"]
	def printMember(self):
		print("Print members of the Birds class")
		for member in self.member:
			print("\t%s",member)
