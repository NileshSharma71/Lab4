k=input("Enter a string: ")
index=0
specialch=0
capitalch=0
smallch=0
while True:
    if "A"<(k[index])<"Z":
        capitalch+=1
    elif "a"<k[index]<"z":
        smallch+=1
    else:
        specialch+=1
    index+=1
    if index==len(k):
        break
print("Capital letter in string: ",capitalch)
print("Small letter in string: ",smallch)
print("Special letter in string: ",specialch)