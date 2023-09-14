a=int(input("Enter a number of any digit: "))
b=len(str(a))
r=0
t=0
while True :
    r=a%(10)
    t=t+r
    r=r//(10**(b-1))

    b=b-1
    if b==0:
        break