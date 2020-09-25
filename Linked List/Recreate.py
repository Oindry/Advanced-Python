class node:
	def __init__ (self, data, node = None):
	 	self.data=data
	 	self.node=node
	def set_data(self,data):
		self.data=data
	def get_data(self):
		return self.data
	def set_node(self,node):
		self.node=node
	def get_node(self):
		return self.node
class linked_list:
	def __init__(self,head=None):
		self.head= head
		self.size=0
	def get_size(self):
		return self.size
	def add(self,data):
		new_node=node(data,self.head)
		self.head=new_node
		self.size+=1
	def display(self):
		List=[]
		cur= self.head
		while cur!=None:
			List+=[cur.data]
			cur=cur.node
		print(List)

My_List= linked_list()
My_List.add(3)
My_List.add(4)
My_List.add(2)
My_List.display()