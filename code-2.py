# Write a Python program that accept a list of integers and check the length and the fifth element.
# Return true if the length of the list is 8 and fifth element occurs thrice in the said list

l = []
while True:
    # loop to create list
    a = input("enter number : ")
    if a.isnumeric():
        l.append(int(a))

    else:
        break

if len(l) == 8:
    if l.count(l[4]) == 3:
        print("True")
    else:
        print("False")
else:
    print("False")