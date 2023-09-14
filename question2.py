x=int(input("Enter value of x: "))
y=int(input("Enter value of y: "))
n=int(input("Enter value of n: "))
i=x+1

while True:
    if i%n==0:
        print(i)
    i=i+1

    if i>=y:
        break