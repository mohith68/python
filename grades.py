def marks(n):
    total=a+b+c
    avg=(total)/3
print("average= ",avg)
name=input("enter name")
a=int(input("enter a marks"))
b=int(input("enter b marks"))
c=int(input("enter c marks"))
if(avg>=90):
    print("grade a")
elif(avg>=80):
    print("garde b")
elif(avg>=70):
    print("grade c")
elif(avg>=60):
    print("grade d")
elif(avg>=50):
    print("grade e")
else:
    print("fail")
marks(n)
