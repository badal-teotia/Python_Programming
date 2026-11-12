# WAF to find line in which a word occurs.

word=input("find word:")

with open("practice.txt","r") as f:
    data=f.readlines()
    for line in data:
        if word in line:
            print(line)
            break
        else:
            print('Not found')
            