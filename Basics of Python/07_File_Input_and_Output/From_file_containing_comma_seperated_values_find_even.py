# From a file containing comma separated numbers, find even.

with open("num.csv","r") as n:
    d=n.read()
    print(d)


# _____method to print the numbers
num=""
for i in range(len(d)):
    if(d[i]==","):
        if int(num) % 2 == 0:
            print(int(num))
        num=""
    else:
        num+=d[i]


# _____method to count the numbers
count=0 
nums=d.split(",")
for g in nums:
    if(g != '' and int(g) % 2==0):
        count+=1
print(count)
