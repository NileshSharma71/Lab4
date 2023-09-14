n=int(input("Enter the limit of the sequence: "))
a,b=0,1
count=0
while True:
    res=a+b
    a,b=b,res
    count+=1
    if count==n:
        break
    print(res)