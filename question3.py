a=int(input("Enter a number of any digit: "))
b=len(str(a))
i=1
t=0
while True :
    r=(a%10**i)//(10**(i-1))
    t=t+r
    if i==b:
        break
    i=i+1
print(t)