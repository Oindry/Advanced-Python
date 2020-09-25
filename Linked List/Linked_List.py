class node:
	def __init__ (self, data,next):
	 	self.data=data
	 	self.next= next
	def set_data(self,data):
		self.data=data
	def get_data(self):
		return self.data
	def set_node(self,next):
		self.next=next
	def get_node(self):
		return self.next
class linked_list:
	def __init__(self,start=None):
		self.start= start
		self.size=0
	def get_size(self):
		return self.size
	def add(self,data):
		new_node=node(data,self.start)
		if (self.start==None):
			self.start=new_node
		#self.size+=1:
		else:
			temp=self.start
			while temp!=None:
				temp=temp.next
			temp= new_node
	def display(self):
		Create_list= []
		cur=self.start
		while cur!=None:
			Create_list+=[cur.data]
			cur=cur.next
		print(Create_list)
	'''def remove(self,data):
		rem_data=self.start
		prev_node=None
		Create_list= []
		if rem_data.get_data() == data:
				if prev_node:
					prev_node.set_node(rem_data.get_node())
					Create_list-=[cur.data]
				else:
					self.head= rem_data
					self.size-=1
		else:
				prev_node=rem_data
				rem_data=rem_data.get_node()
		return self.display'''

My_List= linked_list()
My_List.add(2)
My_List.add(3)
My_List.add(4)
#My_List.remove(2)
My_List.display()

