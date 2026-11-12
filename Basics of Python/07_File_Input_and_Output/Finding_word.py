# Find a word.

word=input("find word:")

with open("practice.txt","r") as f:
    data=f.read()
    if word in data:
        print("found")
    else:
        print("not found")
        
    # could use
    # if(data.find(word)!=-1):
    #     print("found")
    # else:
    #     print("not found")