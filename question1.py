n=int(input("Enter: "))
ij=1
while True:
    k=n*ij
    print(f"{n}x{ij}={k}")
    ij=ij+1
    if ij==20:
        break