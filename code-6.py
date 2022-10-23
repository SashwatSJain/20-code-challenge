# Write a Python program to check a given list of integers where the sum of the first i integers is i. 

def listsum(lst):
    sum = 0
    for i in range(len(lst)):
        sum+=lst[i]
    return(sum)

l = []
while True:
    # loop to create list
    a = input("enter number : ")
    if a.isnumeric():
        l.append(int(a))

    else:
        break

if len(l) == listsum(l):
    print("pass")
else:
    print("Fail")