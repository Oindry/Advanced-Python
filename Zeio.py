fname= r("Enter the file name : ")
fh = open (r'fname',"r")
print(fh.name)
x = fh.read()
print(x.upper())