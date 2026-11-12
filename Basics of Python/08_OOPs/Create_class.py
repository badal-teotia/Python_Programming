#  Create class. And calculate average of 3 subject marks.


class Student:
    S_Name="Badal"
    def __init__(self,Sub, Marks):
        self.S=Sub
        self.m=Marks
        
sub1=input("1st subject:")
m1=float(input("Its marks:"))

sub2=input("2nd subject:")
m2=float(input("Its marks:"))

sub3=input("3rd subject:")
m3=float(input("Its marks:"))

S1=Student(sub1,m1)
print("Marks in ",S1.S,"is",S1.m)

S2=Student(sub2,m2)
print("Marks in ",S2.S,"is",S2.m)

S3=Student(sub3,m3)
print("Marks in ",S3.S,"is",S3.m)

print("So, Badal's average marks are",(m1+m2+m3)/3)
