n=int(input("Enter: "))
if n<0:
    print("Enter invalid input.Enter a positive value.")
c=0
d=0
while True:
    i=int(input("Enter value : "))
    if i%n==0:
        c+=1
    if i%n!=0:
        d+=1
    if i==-999:
        break
print(f"There are {c} numbers that are divisible by {n}.")
print(f"And there are {d} numbers that are not divisible by {n}.")