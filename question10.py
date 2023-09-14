#to solve Quadratic equation
print("Quadratic eqation ax^2+bx=c")
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))
d=(b*b)-(4*a*c)
if d<0:
    print("Roots are complex.")
if d==0:
    print("Thers is only one root and it's value is:-")
    print("%.2f"%((-b/(2*a))))
if d>0:
    print("Root 1 is ","%.2f"%((-b+(d)**(1/2))/(2*a)))
    print("Root 2 is ","%.2f"%((-b-(d)**(1/2))/(2*a)))
    