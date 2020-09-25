value= "cat picture is cat picture"
i= value.rfind("picture")
print(i)
b=value.rfind("picture",0,i-1)
print(b)
location=0
while True:
	location=value.find("picture",location+1)
	if location==-1:
		break
	else:
		print(location)
