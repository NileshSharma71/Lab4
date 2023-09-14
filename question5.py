n=int(input("Enter: "))
if n<0:
    print("Invalid input.Enter a positive value.")
i=1
while n>0:
    i=i*n
    n=n-1

print(i)  