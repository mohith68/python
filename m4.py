#a=int(input("enter value of a"))
start=int(input())
end=int(input())
for n in range(start,end+1):
    sum=0
    for i in range(1,n):
        if (n%i==0):
         sum+=i
    if(sum==n):
           print(n)
