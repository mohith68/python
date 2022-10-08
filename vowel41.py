def vowel(s):
    count=0
    s=s.lower()
    for i in s:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            count+=1
    if count==0:
        print("no vowels")
    else:
        print("vowels=",count)
s=input("enter string")
vowel(s)    
    
