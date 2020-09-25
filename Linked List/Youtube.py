class node:
	def __init__(self,data):
		self.data=data
		self.next= None
class LinkedList:
	def __init__(self):
		self.start=None
	def viewList(self):
		temp=self.start
		while temp!=None:
			print(temp.data)
			temp=temp.next
	def insertLast(self,value):
		newNode=node(value)
		if(self.start==None):
			self.start=newNode
		else:
			temp=self.start
			while temp.next!=None:
				tem=temp.next
			temp.next=newNode
		
MyList= LinkedList()
MyList.insertLast(3)
MyList.insertLast(4)
MyList.viewList()

