def fib(n): #We want the fibonacchi series up to n
	n=int(n)
	List=[0,1]
	result=[]

	i=0
	while n-2>i:
		List.append(List[i]+List[i+1])
		i+=1
	print(List)