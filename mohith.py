#reverse a number
def rev(n):
    
    reversed_number=0
    while (n!=0):
          digit=n%10
          reversed_number=reversed_number*10+digit
          n=n//10
    print("reversed number: ",str(reversed_number))
try:
  n=int(input("enter the number:"))
 # rev(n)
  if(n<0):
        print("negative number")
  else:
      rev(n)
except ValueError:
    print("invalid input ")
