# Write a Python program to check the nth-1 string is a proper substring of nth string in a given list of strings.

l = []
a = " "
while a!="":
    # loop to create list
    a = input("Value to insert into list : ")   
    if a != "":
        l.append(a)



if l[len(l)-2] in l[len(l)-1]:
    print("True")

else:
    print("False")