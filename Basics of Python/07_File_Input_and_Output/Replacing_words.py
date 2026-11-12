# Replace python with java.

with open("practice.txt" ,"r") as r:
    d=r.read()
    
data=d.replace("Python","Java")
print(data)

with open("practice.txt","w")as h:
    h.write(data)
