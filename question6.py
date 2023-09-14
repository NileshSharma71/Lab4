jk=int(input("Enter a positive integer: "))
kk=jk
r=0
while True:
    r1=jk%10
    r=(r*10)+r1
    jk=jk//10
    if jk==0:
        break
print(r)
if kk==r:
    print("The no. is Palindrome.")
else:
    print("The no. is not Palindrome.")