#checking input prime or not
jk=int(input("Enter: "))
if jk<0:
    print("Invalid input. Enter a positive value.")
if jk==0 or jk==1:
    print("The no. is neither prime nor composite.")
else:
    k=2
    while True:
        if jk%k==0:
            print("The number is not prime.")
            break
        elif jk%k!=0:
            print("The number is prime.")
            break
        k=k+1
        if k==jk:
            break
    