rno=int(input("enter roll no : "))
sname=input("enter student name : ")
s1=int(input("enter mark of subject 1 : "))
s2=int(input("enter mark of subject 2 : "))
s3=int(input("enter mark of subject 3 : "))

total=s1+s2+s3
per=total/3

print("roll no: ",rno)
print("name : ",sname)
print("total : ",total)
print("percentage : ",per)

if per>=70:
    print("grade A")
elif per>=60:
    print("grade B")
elif per>=50:
    print("grade C")
elif per>=40:
    print("grade D")
else:
    print("fail")
