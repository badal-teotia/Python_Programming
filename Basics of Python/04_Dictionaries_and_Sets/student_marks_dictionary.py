# Create empty dictionary and add subject values

marks = {}

x = int(input("Enter physics marks: "))
marks.update({"Physics": x})

y = int(input("Enter maths marks: "))
marks.update({"Maths": y})

z = int(input("Enter computer marks: "))
marks.update({"Computer": z})

print(marks)
