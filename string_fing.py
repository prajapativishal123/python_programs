s=input("enter string : ")

uc=0
lc=0
sp=0
al=0
nm=0
for i in s:
    if i.isupper():
        uc=uc+1
    elif i.islower():
        lc=lc+1
    elif i.isspace():
        sp=sp+1
    if i.isapha():
        al=al+1
    elif i.isnumeric():
        nm=nm+1

    print("uppercase : ",uc)
    print("lowercase : ",lc)
    
